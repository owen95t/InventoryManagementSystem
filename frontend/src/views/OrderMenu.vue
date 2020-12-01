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
          :items="search_results"
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
        key: 'customer.first_name' + 'customer.last_name',
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
    getSearch() {
      if(this.search_results.length===0){
        this.emptySearchAlert = true
      }

    },
    getModalSearch() {

    },
    info() {

    },
    resetRadio() {
      this.picked = ''
    }
  },
  computed: {
    rows() {
      return this.search_results.length
    }
  }
}
</script>

<style scoped>

</style>