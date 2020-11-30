<template>
  <div class="transfermenu">
    <h1 class="text-center">Transfer Menu</h1>
<!--    Search Bar + Alert    -->
    <div style="padding-bottom: 25px">
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
        <b-alert :show="emptySearchAlert" fade variant="danger">
          <h4>Query Returned No Results. Please Try Again</h4>
        </b-alert>
      </b-container>
    </div>
<!--    Table     -->
<!--    MODAL     -->
  </div>
</template>

<script>

import axios from 'axios';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: 'TransferMenu',
  data() {
    return {
      currentPage: 1,
      perPage: 5,
      fields: [], //for TABLE
      initial_data: '',
      search_term: '',
      emptySearchAlert: false,
      picked: '',
      search_options: '',
      search_results: '',
      modalTable: '',

    }
  },
  methods: {
    resetAll() {
      this.emptySearchAlert = false
      this.search_results.length = 0
    },
    getAllTransfers(){
      axios({
        method: 'get',
        url: ''//TODO enter transfer URL for getAllTransfer
      }).then(response => {
        if (response.data) {
          console.log('initial: ' + response.data);
          this.initial_data = response.data
        }
      }).catch((error) => {
        if (error.response) {
          console.log('INITIAL REQUEST ERROR')
          console.log(error.response)
        }
      });
    },
    getSearch(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: ''+term//TODO enter transfer URL for getSearch (Transfer)
        }).then(response => {
          if (response.data) {
            console.log('RESPONSE: '+response.data)
            this.search_results = response.data
            if (this.search_results.length === 0) {
              this.emptySearchAlert = true
            }
          }
        }).catch((error) => {
          if (error.response) {
            console.log('SEARCH ERROR')
            console.log(error.response)
            console.log(error.response.data)
          }
        })
      }
    },
    resetRadio() {
      this.picked = ''
    },
    resetModal() {

    },
    getModalSearch() {

    }
  },
  mounted() {
    this.getAllTransfers()
  }
}
</script>

<style>

</style>