<template>
  <div class="ordermenu">
    <h1 class="text-center">Order Menu</h1>
    <b-container>
      <b-input-group>
        <b-input-group-prepend>
          <b-dropdown text="Filter">
            <b-form-group>
              <b-form-radio-group :options="search_options" style="padding: 3px" v-model="picked"></b-form-radio-group>
            </b-form-group>
            <b-button v-on:click="resetRadio()">Clear</b-button>
          </b-dropdown>
        </b-input-group-prepend>
        <b-form-input type="submit" v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search..."></b-form-input>
        <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="getSearch(search_term)">Search</b-button></b-input-group-append>
      </b-input-group>
      <b-alert :show="emptySearchAlert" fade variant="danger" style="margin-top: 10px">
        <h4>Query Returned No Results. Please Try Again</h4>
      </b-alert>
    </b-container>
    <b-container>
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
          class="justify-content-center"
          style="margin-top: 15px"
          first-text="First"
          last-text="Last">
        </b-pagination>
        <b-table
          hover
          bordered
          responsive="sm"
          :items="formattedRows"
          :per-page="perPage"
          :current-page="currentPage"
          :fields="this.fields"
          @row-clicked="info">
        </b-table>
      </b-container>
    <pre>{{dataTest}}</pre>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
name: "OrderMenu",
  data() {
    return{
      currentPage: 1,
      perPage: 5,
      search_options: '',
      picked: '',
      search_term: '',
      search_results: '',
      emptySearchAlert: false,
      fields: [{
        key: 'order_id',
        label: 'Order ID'
      }, {
        key: 'order_date',
        label: 'Order Date'
      }, {
        key: 'customer',
        label: 'Customer name'
      }, {
        key: 'order_fulfilled',
        label: 'Fulfilled Status'
      }, {
        key: 'order_paid',
        label: 'Paid Status'
      }],
    }
  },
  methods: {
    getAll() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/Order'
      }).then(response => {
        if (response.data) {
          this.search_results = response.data
        }
      })
    },
    getSearch(term) {
      this.resetAll()
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/Order/?search=' + term
      }).then(response => {
        if (response.data) {
          this.search_results = response.data
        }
        if (response.data.length === 0) {
          this.emptySearchAlert = true
        }
      })

    },
    getModalSearch() {

    },
    info() {

    },
    getVariant(status1, status2) {
      if (status1=='Yes' && status2=='Yes') {
        return 'success'
      }else if (status1=='No' && status2=='Yes') {
        return 'warning'
      }else if (status1=='No' && status2=='No') {
        return 'danger'
      }
    },
    resetRadio() {
      this.picked = ''
    },
    resetAll() {
      this.resetRadio()
      this.emptySearchAlert = false
      this.search_results = ''
    }
  },
  computed: {
    rows() {
      return this.search_results.length
    },
    formattedRows() {
      if(!this.search_results) [];
      return this.search_results.map(item => {
        item._rowVariant = this.getVariant(item.order_fulfilled, item.order_paid)
        return item
      })
    }
  },
  mounted() {
    this.getAll()
  }
}
</script>

<style scoped>

</style>