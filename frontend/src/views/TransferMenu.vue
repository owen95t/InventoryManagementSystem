<template>
  <div class="transfermenu">
    <h1 class="text-center">Transfer Menu</h1>
<!--    Search Bar + Alert    -->
    <div>
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
          <b-form-input v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search by Transfer ID"></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="getSearch(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <b-alert :show="emptySearchAlert" fade variant="danger" style="margin-top: 10px">
          <h4>Query Returned No Results. Please Try Again</h4>
        </b-alert>
      </b-container>
    </div>
<!--    Table     -->
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
          <template v-slot:row-details="row">
            {{row}}
            <div>Hello</div>
          </template>
        </b-table>
      </b-container>
<!--    MODAL     -->
    <b-modal :id="modalInfo.id" :title="modalInfo.title" ok-only @hide="resetModal()" ref="modal" data-target="myModal" rel="preload">
      <template>
        {{this.modalInfo.title="Transfer Information"}}
        <div style="margin-bottom: 10px"></div>
<!--        <pre>{{this.modalInfo.content}}</pre>-->
        <div>Transfer ID: {{this.modalInfo.content.transfer_id}}</div>
        <div>Transfer From: {{this.modalInfo.content.location_from}}</div>
        <div style="margin-bottom: 10px">Transfer To: {{this.modalInfo.content.location_to}}</div>

        <div>Transfer created on: {{this.modalInfo.content.date_created}}</div>
        <div>Transfer completed: {{this.modalInfo.content.complete_status}}</div>

        <div></div>

      </template>
    </b-modal>
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
      initial_data: '',
      search_term: '',
      emptySearchAlert: false,
      picked: '',
      search_options: '',
      search_results: '',
      modalTable: '',
      modalInfo: {
        id: 'model-info',
        title: '',
        content: ''
      },
      fields: [{
        key: 'transfer_id',
        label: 'Transfer ID'
      }, {
        key: 'location_to',
        label: 'To'
      }, {
        key: 'location_from',
        label: 'From'
      }, {
        key: 'date_created',
        label: 'Created on'
      }, {
        key: 'date_completed',
        label: 'Completed on'
      }],
      testData: '',
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
        url: 'http://127.0.0.1:8000/Transfer/'
      }).then(response => {
        if (response.data) {
          console.log('initial: ' + response.data);
          this.search_results = response.data
          this.testData = this.formattedItems()
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
          url: 'http://127.0.0.1:8000/Transfer/?search='+term
        }).then(response => {
          if (response.data) {
            console.log('RESPONSE: '+response.data)
            this.search_results = response.data
            this.search_results = this.formattedItems()
            if (this.search_results.length === 0) {
              this.emptySearchAlert = true
            }else if (this.search_results.length !== 0) {
              this.emptySearchAlert = false
            }
          }
        }).catch((error) => {
          if (error.response) {
            console.log('getSEARCH ERROR')
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

    },
    info(item) {
      this.modalInfo.content = item
      //TODO : implement proper transfer modal
      this.$root.$emit('bv::show::modal', this.modalInfo.id)
    },
    getVariant(status) {
      if (status==='Yes') {
        return 'success'
      }
      if (status){
        return 'danger'
      }
    },
  },
  mounted() {
    this.getAllTransfers()
  },
  computed: {
    rows() {
      return this.search_results.length
    },
    formattedItems() {
      if(!this.search_results) [];
      return this.search_results.map(item => {
        item._rowVariant = this.getVariant(item.complete_status)
        return item
      })
    }
  }
}
</script>

<style>

</style>