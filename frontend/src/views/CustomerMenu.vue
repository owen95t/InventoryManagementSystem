<template>
  <div class="customermenu">
    <h1 class="text-center">Customer Menu</h1>
    <!--    Search Bar + Alert    -->
    <div style="padding-bottom: 25px">
      <b-container>
        <b-input-group>
          <b-form-input type="submit" v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search by phone number or email"></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="getSearch(search_term)">Search</b-button></b-input-group-append>
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
    </div>
  </div>
</template>

<script>
export default {
name: "CustomerMenu",
  data() {
    return{
      currentPage: 1,
      perPage: 5,
      picked: '',
      search_options: '',
      search_term: '',
      search_results: '',
      emptySearchAlert: false,
      fields: [{
        key: 'first_name',
        label: 'First name'
      }, {
        key: 'last_name',
        label: 'Last name'
      }, {
        key: 'phone_number',
        label: 'Phone number'
      }],
      order_history: ''
    }
  },
  methods: {
    getSearch(term) {
      return term
    },
    getModalSearch() {

    },
    info(item, index) {
      console.log(item + index)
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