<template>
  <div class="customermenu">
    <h1 class="text-center">Customer Menu</h1>
    <!--    Search Bar + Alert    -->
    <div style="padding-bottom: 25px">
      <b-container>
        <b-input-group>
          <b-form-input type="submit" v-model="search_term" v-on:keyup.enter="searchHandler(search_term)" placeholder="Search by phone number or email. Default is phone number"></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="searchHandler(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <b-alert :show="emptySearchAlert" fade variant="danger">
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
          :items="search_results"
          :per-page="perPage"
          :current-page="currentPage"
          :fields="this.fields"
          @row-clicked="info">
        </b-table>
      </b-container>

      <b-modal :id="modalInfo.id" :title="modalInfo.title" ok-only @hide="resetModal()" ref="modal" data-target="myModal" rel="preload">
        <template>
          {{this.modalInfo.title="Customer Information"}}
          <div style="margin-bottom: 10px"></div>
<!--          <pre>{{this.modalInfo.content}}</pre>-->
          <div>Customer Name: {{this.modalInfo.content.first_name + " " + this.modalInfo.content.last_name}}</div>
          <div>Customer ID: {{ this.modalInfo.content.customer_id }}</div>
          <div>Customer Phone Number: {{this.modalInfo.content.phone_number}}</div>
          <div>Customer Email: {{this.modalInfo.content.email? this.modalInfo.content.email:"None"}}</div>
        </template>
      </b-modal>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
name: "CustomerMenu",
  data() {
    return{
      currentPage: 1,
      perPage: 5,
      picked: '',
      search_options: '',
      search_term: '',
      search_results: {},
      emptySearchAlert: false,
      modalInfo: {
        title: '',
        id: 'modal-info',
        content: ''
      },
      fields: [{
        key: 'first_name',
        label: 'First name'
      }, {
        key: 'last_name',
        label: 'Last name'
      }, {
        key: 'phone_number',
        label: 'Phone number'
      }, {
        key: 'email',
        label: 'Email'
      }],
      order_history: '',

    }
  },
  methods: {
    searchHandler(term) {
      this.resetAll()
      this.getSearch(term)
      console.log('test')
    },
    getAll() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/Customer/'
      }).then(response => {
        if (response.data) {
          this.search_results = response.data
        }
      })
    },
    getSearch(term) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/Customer/?search='+term
      }).then(response => {
        if (response.data) {
          if (response.data.length === 0) {
            this.emptySearchAlert = true
          }
          this.search_results = response.data;
        }
      })
    },
    getModalSearch() {

    },
    info(item) {
      this.modalInfo.content = item
      this.$root.$emit('bv::show::modal', this.modalInfo.id)
    },
    resetRadio() {
      this.picked = ''
    },
    resetAll() {
      this.search_results.length = 0
      this.emptySearchAlert = false
      this.resetRadio()
      this.resetModal()
    },
    resetModal() {
      // this.modalInfo.title = ''
      // this.modalInfo.content = ''
      this.listOptions = ''
      this.dropDownSelected = ''
    },
  },
  computed: {
    rows() {
      return this.search_results.length
    }
  },
  mounted() {
    this.getAll()
  }
}
</script>

<style scoped>

</style>