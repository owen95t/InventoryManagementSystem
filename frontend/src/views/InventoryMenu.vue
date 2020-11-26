<template>
  <div class="inventorymenu" @keydown.esc="resetAll()">
    <h1 class="text-center">Inventory Menu</h1>
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
          <b-form-input type="submit" v-model="search_term" v-on:keyup.enter="resultSelection(search_term)" placeholder="Search..."></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="resultSelection(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <h3>RADIO SELECTION: {{picked}}</h3>
        <h3>TERM: {{search_term}}</h3>
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
        <b-container class="resultscontainer">
        <!-- CONTENT for RESULTS  -->
        <b-table
            hover
            striped
            bordered
            responsive="sm"
            selectable
            :items="search_results"
            :per-page="perPage"
            :current-page="currentPage"
            :fields="this.fieldSelection()"
            @row-clicked="infoTest">
<!--          <template #cell(action)="row">-->
<!--            <b-button @click="info(row.item, row.index, $event.target)">>-->
<!--              Info-->
<!--            </b-button>-->
<!--          </template>-->
        </b-table>
        </b-container>

<!--        MODAL -->
        <b-modal :id="modalInfo.id" :title="modalInfo.title" ok-only @hide="resetModal()">
          <pre>{{modalInfo.content}}</pre>
        </b-modal>
      </b-container>
    </div>

  </div>

</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: 'InventoryMenu',
  data() {
    return{
      currentPage: 1,
      perPage: 5,
      search_term: '',
      fields: [{
        key: 'item_brand',
        label: 'Brand',
        sortable: true
      }, {
        key: 'item_id',
        label: 'Style ID',
      }, {
        key: 'item_name',
        label: 'Name'
      }, {
        key: 'item_color_code',
        label: 'Color Code'
      }, {
        key: 'item_size',
        label: 'Size',
      }, {
        key: 'item_category',
        label: 'Category'
      }, {
        key: 'item_price',
        label: 'Price'
      }, {
        key: 'item_current_price',
        label: 'Current Price'
      }, {
        key: 'item_sku',
        label: 'SKU'
      }, {
        key: 'item_quantity',
        label: 'Total Quantity'
      }],
      emptySearchAlert: false,
      search_results: [],
      search_options: [
        {text: 'Brand', value: 'brand'},
        {text: 'SKU', value: 'sku'},
        {text: 'Name', value: 'name'},
        {text: 'ID', value: 'id'}
      ],
      resultsByID: [],
      picked: '',
      idFields: [{
        key: 'itemid_brand.brand_name',
        label: 'Brand'
      }, {
        key: 'item_id',
        label: 'Item ID'
      }],
      idBrands: [{
        key: 'brand_name',
        label: 'Brand'
      }, {
        key: 'supplier_name',
        label: 'Supplier'
      }, {
        key: 'url',
        label: 'Link'
      }],
      modalInfo:{
        id: 'modal-info',
        title: '',
        content: '',
      }
    }
  },
  mounted() {
  },
  methods: {
    toggleDetails(row){
      row._showDetails = !row._showDetails
    },
    //v:on method here
    resultSelection(term) {
      this.reset() //calls reset() which resets data field to empty everytime search is commited
      if(this.picked === 'id'){
        this.searchByID(term)
      }else if(this.picked === 'brand'){
        this.searchByBrand(term)
      }else if(this.picked === 'sku'){
        this.searchBySKU(term)
      }else if (this.picked === 'name') {
        this.searchByName(term);
      } else {
        this.getSearch(term)
      }
    },
    searchByID(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/ItemID/?search='+term
        }).then(response =>{
          if(response.data){
            console.log('ID SEARCH')
            this.resultsByID = response.data
            console.log(response.data)
          }
        })
      }
    },
    searchByBrand(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Brand/?search='+term
        }).then(response => {
          if (response.data) {
            this.search_results = response.data
          }
          if (this.search_results.length === 0) {
            console.log('RESPONSE EMPTY')
            this.emptySearchAlert = true

          }
        }).catch((error) => {
          if (error.response) {
            console.log('RESPONSE ERROR');
            console.log(error.response.data)
            console.log(error.response.status);
            console.log(error.response.headers);
          }else if (error.request) {
            console.log('REQUEST ERROR', error.request);
          } else {
            console.log('ERROR IN GET ITEMS', error.message);
          }
        })
      }
    },
    searchBySKU(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term //incomplete
        }).then(response => {
          if (response.data) {
            this.search_results = response.data
          }
        })
      }
    },
    searchByName(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term //incomplete
        }).then(response => {
          if (response.data) {
            this.search_results = response.data
          }
        })
      }
    },
    getSearch(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term
        }).then(response =>{
          console.log(response.data);
          if(response.data){
            this.search_results = response.data
          }
          if (this.search_results.length === 0) {
            console.log('RESPONSE EMPTY')
            this.emptySearchAlert = true

          }
        }).catch((error) => {
          if (error.response) {
            console.log('RESPONSE ERROR');
            console.log(error.response.data)
            console.log(error.response.status);
            console.log(error.response.headers);
          }else if (error.request) {
            console.log('REQUEST ERROR', error.request);
          } else {
            console.log('ERROR IN GET ITEMS', error.message);
          }
        })
      }
    },
    reset() {
      this.search_results.length = 0
      this.emptySearchAlert = false
    },
    fieldSelection() {
      if(this.picked === 'id'){
        return this.idFields
      }else if(this.picked === 'brand'){
        return this.idBrands
      }else if(this.picked === 'sku'){
        return this.fields
      }else if(this.picked === 'name'){
        return this.fields
      }else{
        return this.fields
      }
    },
    resetRadio() {
      this.picked = ""
    },
    resetModal() {
      this.modalInfo.title = ''
      this.modalInfo.content = ''
    },
    info(item, index, button) {
      this.modalInfo.title = ''
      this.modalInfo.content = JSON.stringify(item, null, 2)
      this.$root.$emit('bv::show::modal', this.modalInfo.id, button)
    },
    resetAll() {
      this.reset();
      this.resetRadio();
      this.resetModal();
      console.log('PAGE RESET')
    },
    infoTest(item, index) {
      console.log("Item: "+item.item_name + " index: " + index)
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


.resultscontainer {
  /*border: 3px seagreen solid;*/
  /*border-radius: 10px;*/
  margin-top: 5px;
  /*visibility: collapse;*/
}
</style>