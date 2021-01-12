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
        <b-form-input v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search..."></b-form-input>
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
    <b-modal :id="modalInfo.id" :title="modalInfo.title" ok-only >
      <template>
        <div>NAME: {{modalInfo.content.customer}}</div>
        <div>ORDER ID: {{modalInfo.content.order_id}}</div>
        <div>Order Items: </div>
<!--        <b-table v-for="item in modal_search" :key="item.order_item" :fields="modalFields"></b-table>-->
        <b-list-group v-for="item in modal_search" :key="item.order_item">
          {{item.order_item}}

        </b-list-group>
      </template>
    </b-modal>
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
      search_options: [{
        text: 'Test1',
        value: 'Test1'
      }, {
        text: 'Test2',
        value: 'Test2'
      }],
      picked: '',
      search_term: '',
      search_results: '',
      modal_search: '',
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
      modalInfo: {
        id: 'modal-info',
        title: '',
        content: '',
      },
      modalFields: [{
        key: 'order',
        label:'Order'
      },{
        key: 'order_item',
        label: 'Item'
      }]
    }
  },
  methods: {
    // getAll() {
    //   axios({
    //     method: 'get',
    //     url: 'http://127.0.0.1:8000/Order/'
    //   }).then(response => {
    //     if (response.data) {
    //       this.search_results = response.data
    //       this.search_results = this.formattedRows()
    //     }
    //   })
    // },
    async getAll() {
      try {
        await axios.get('http://127.0.0.1:8000/Order/').then((response) => {
          if (response.data) {
            this.search_results = response.data
            this.search_results = this.formattedRows()
          }
        }).catch(er => {
          console.log("getAll Axios ERR: " + er)
        })
      } catch (e){
        console.log("Error at getAll after Axios: " + e)
      }
    },
    async getSearch(term) {
      this.resetAll()
      try{
        axios.get('http://127.0.0.1:8000/Order/?search=' + term).then(response => {
          if (response.data) {
            this.search_results = response.data
            this.search_results = this.formattedRows
          } else if (response.data.length === 0) {
            this.emptySearchAlert = true
          }
        }).catch(error => {
          console.log('getSearch ORDERMENU error: ' + error.status)

        })
      }catch (e){
        console.log("Error Status: " + e.response.status);
      }
    },
    async getModalSearch(term) {
      try {
        await axios.get('http://127.0.0.1:8000/OrderItem/?search=' + term).then(response => {
          if (response.data) {
            console.log('modal search: ' + response.data)
            this.modal_search = response.data
          }
        }).catch(er => {
          console.log("getModalSearch Axios error: " + er)
        });
      } catch (e){
        console.log("getModalSearch error after axios: " + e)
      }
    },
    async info(item) {
      try {
        await this.getModalSearch(item.order_id).catch(error => {
          console.log("order menu modal info error: " + error)
        });
      } catch (e){
        console.log("info error: " + e)
      } finally {
        this.$root.$emit('bv::show::modal', this.modalInfo.id)
      }

      console.log(item)
      this.modalInfo.content = item
      this.modalInfo.title = item.customer
      this.$root.$emit('bv::show::modal', this.modalInfo.id)
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
    resetModal() {
      this.modalInfo.id = 'modal-info';
      this.modalInfo.content = '';
      this.modalInfo.title = ''
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