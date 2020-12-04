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
        <b-container class="resultscontainer">
        <!-- CONTENT for RESULTS  -->
        <b-table
            hover
            bordered
            responsive="sm"
            :items="search_results"
            :per-page="perPage"
            :current-page="currentPage"
            :fields="this.fieldSelection()"
            @row-clicked="info"
            :key="modalKey">
        </b-table>
        </b-container>

        <!--  MODAL   -->
        <b-modal :id="modalInfo.id" :title="modalInfo.title" ok-only @hide="resetModal()" ref="modal" data-target="myModal" rel="preload">
          <template> <!-- assume search by ID-->
            <div>
              <div>Select Size: </div>
              <b-form-select v-model="dropDownSelected" :options="options"></b-form-select>
            </div>
            <div style="margin-top: 20px">Item Information: </div>
            <div id="info" class="modalinfo">
              <div>Item Name: {{this.chosenItem.item_name}}</div>
              <div>Item Size: {{this.chosenItem.item_size}}</div>
              <div>Item SKU: {{this.chosenItem.item_sku}}</div>
            </div>
            <div style="margin-top: 20px">Item Availability: </div>
            <div id="availability" class="modalinfo">
              <div>VAN: 1</div>
              <div>EDM: 2</div>
              <div>CAL: 0</div>
              <div>TOR: 1</div>
            </div>
          </template>
        </b-modal>
        <!--  END MODAL  -->
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
      perPage: 7,
      search_term: '',
      fields: '',
      idFields: [{
        key: 'itemid_brand',
        label: 'Brand',
      }, {
        key: 'item_id',
        label: 'Style ID'
      }],
      nameFields: [{
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
      brandFields: [{
        key: 'itemid_brand',
        label: 'Brand'
      }],
      emptySearchAlert: false,
      search_results: [],
      search_options: [
        {text: 'Brand', value: 'brand'},
        {text: 'Name', value: 'name'},
      ],
      resultsByID: [],
      picked: '',
      modalInfo:{
        id: 'modal-info',
        title: '',
        content: '',
      },
      listOptions: [],
      dropDownSelected: '',
      chosenItem: '',
      options: [],
      computedModal: {},
      modalShow: false,
      modalKey: 0,
    }
  },
  mounted() {
  },
  methods: {
    forceRerender() {
      this.modalKey += 1
      console.log(this.modalKey)
    },
    resultSelection(term) {
      this.resetAll()
      this.reset() //calls reset() which resets data field to empty everytime search is committed
      if(this.picked === 'brand') {
        console.log('search by BRAND')
        this.searchByBrand(term)
      } else if(this.picked === 'name'){
        console.log('search by NAME')
        this.searchByName(term)
      } else {
        console.log('generic SEARCH')
        this.getSearch(term)
      }
    },
    searchByBrand(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Brand/?search='+term
        }).then(response => {
          if (response.data.length === 0) {
            this.emptySearchAlert = true
          }
          this.search_results = response.data;

        })
      }
    },
    searchByName(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term
        }).then(response => {
          if (response.data) {
            console.log('search by name data: ' + response.data)
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
    getSearch(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/ItemID/?search='+term
        }).then(response =>{
          if(response.data){
            console.log('GET SEARCH: ' + response.data);
            this.search_results = response.data

            if (this.search_results.length === 0) {
              console.log('getSearch RESPONSE EMPTY');
              console.log('Commence search by sku')
              this.searchSKU(term)
            }
            // else {
            //  this.idRequest(term);
            // }
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
            console.log('ERROR IN GET SEARCH', error.message);
          }
        })
      }
    },
    searchSKU(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term
        }).then(response =>{
          console.log('SEARCH SKU')
          this.search_results = response.data
          if (this.search_results.length === 0) {
            console.log('SEARCH SKU EMPTY')
            this.emptySearchAlert = true
          }else{
            this.fields = this.nameFields
          }
        })
      }
    },
    async idRequest(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term
        }).then(response =>{
          console.log('idRequest Data: '+response.data);
          if(response.data){
            this.listOptions = response.data
            this.optionListCreate(this.listOptions)
          }
          if (this.listOptions.length === 0) {
            console.log('LIST OF ITEMS EMPTY: idRequest')
          }
        }).catch((error) => {
          if (error.response) {
            console.log('RESPONSE ERROR');
            console.log(error.response.data)
            console.log(error.response.status);
            console.log(error.response.headers);
          }else if (error.request) {
            console.log('REQUEST ERROR for idRequest', error.request);
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
      if(this.picked === 'brand'){
        return this.brandFields
      }else if(this.picked === 'name'){
        return this.nameFields
      }else{
        return this.idFields
      }
    },
    resetRadio() {
      console.log('resetRadio')
      this.resetModal()
      this.modalKey += 1
      this.search_results.length = 0
      console.log(this.search_results)
      this.picked = ''
    },
    resetModal() {
      console.log('reset modal called')
      this.modalInfo.title = ''
      this.modalInfo.content = ''
      this.listOptions.length = 0
      this.options.length = 0
      this.dropDownSelected = ''
      this.modalKey = 0
    },
    info(item, index) {
      this.$root.$emit('bv::show::modal', this.modalInfo.id)
      console.log("Item: "+item + "index: " + index)
      this.modalInfo.title = ''
      // this.modalInfo.content = JSON.stringify(item, null, 2)
      this.modalInfo.content = item
      //$('#myModal').on()
      this.idRequest(item.item_id)
    },
    resetAll() {
      this.fields = ''
      this.reset();
      this.resetModal();
      console.log('PAGE RESET')
    },
    optionListCreate(list) {
      for (var i = 0; i <= list.length; i++) {
        this.options[i] = {
          text: this.listOptions[i].item_size,
          value: this.listOptions[i].item_sku
        }
      }
    },
  },
  computed: {
    rows(){
      return this.search_results.length
    },
  },
  watch: {
    dropDownSelected: function () {
      for (var i = 0; i <= this.listOptions.length; i++){
        if(this.listOptions[i].item_sku === this.dropDownSelected){
          this.chosenItem = this.listOptions[i]
        }
      }
    },
    // search_term: function () {
    //   this.reset()
    //   this.resetAll()
    // }
    // picked: function () {
    //   this.fields = ''
    //   this.search_results = ''
    // }
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

.modalinfo {
  border: 2px solid;
  margin-top: 5px;
}
</style>