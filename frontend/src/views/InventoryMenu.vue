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
          <b-form-input v-model="search_term" v-on:keyup.enter="resultSelection(search_term)" placeholder="Search..."></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="resultSelection(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <b-alert :show="emptySearchAlert" fade variant="danger" style="margin-top: 10px">
          <h4>Query Returned No Results. Please Try Again</h4>
        </b-alert>
      </b-container>
      <b-container>
        <b-row>
          <b-col></b-col>
          <b-col>
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
          </b-col>
          <b-col>
            <span>
              <b-form-select v-model="perPage" :options="perPageOptions" class="justify-content-center" style="margin-top: 15px"></b-form-select>
            </span>
          </b-col>
        </b-row>
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
          <template v-if="this.picked==''"> <!-- assume search by ID-->
            {{this.modalInfo.title='Info and Availabilities'}}
            <div class="text-center">
              <b-spinner variant="primary" label="Spinning" v-if="loading"></b-spinner>
            </div>
            <div>
              <div>Select Size: </div>
              <b-form-select v-model="dropDownSelected" :options="options"></b-form-select>
            </div>
            <div style="margin-top: 20px">Item Information: </div>
            <div id="info" class="modalinfo">
              <div>Item Name: {{this.chosenItem.item_name}}</div>
              <div>Item Size: {{ this.chosenItem.item_size}}</div>
              <div>Item SKU: {{this.chosenItem.item_sku}}</div>
            </div>
            <div style="margin-top: 20px">Item Availability: </div>
            <div id="availability" class="modalinfo">
              <div>VAN: </div>
              <div>EDM: </div>
              <div>CAL: </div>
              <div>TOR: </div>
            </div>
          </template>

          <template v-if="this.picked=='name'">
            {{this.modalInfo.title='Availabilities'}}
            <div>Availability By Location: </div>
            <div id="infoName" class="modalinfo">
              <div>EDM: </div>
              <div>VAN: </div>
              <div>CAL: </div>
              <div>TOR: </div>
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
      perPage: 5,
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
      fake_options: [{
        text: '7',
        value: '7'
      }, {
        text: '8',
        value: '8'
      }, {
        text: '9',
        value: '9'
      }, {
        text: '10',
        value: '10'
      }, {
        text: '11',
        value: '11'
      }, {
        text: '12',
        value: '12'
      }],
      loading: true,
      perPageOptions: [{
        value: 5,
        text: "5"
      }, {
        value: 10,
        text: "10"
      }, {
        value: 15,
        text: "15"
      }, {
        value: 20,
        text: "20"
      }, {
        value: "all",
        text: "All"
      }]
    }
  },
  mounted() {
  },
  methods: {
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
          }else if (error.request) {
            console.log('REQUEST ERROR', error.request);
          } else {
            console.log('ERROR IN GET ITEMS', error.message);
          }
        })
      }
    },
    async getSearch(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        await axios({
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
          }
        }).catch((error) => {
          if (error.response) {
            console.log('RESPONSE ERROR');
            console.log(error.response.data)
            console.log(error.response.status);
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
    async idReq(term) {
      console.log("idReq Called")
      try {
        await axios.get('http://127.0.0.1:8000/Item/?search=' + term).then((response) => {
          if (response.data) {
            // console.log("idReq response data: " + response.data)
            this.listOptions = response.data
            this.optionListCreate(this.listOptions)
            this.loading = false
          }
        }).catch((er) => {
          console.log("idReq ERROR: " + er)
          console.log("idReq ERROR STATUS: " + er.status)
        })
      } catch (ex){
        console.log("idReq error ex: " + ex)
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
      this.chosenItem = ''
      this.loading = true;
    },
    info(item) {
      this.modalInfo.content = item
      try {
        if(item.item_id.length > 0){
          this.idReq(item.item_id);
        }
      } catch (e){
        console.log(e)
      } finally {
        this.$root.$emit('bv::show::modal', this.modalInfo.id)
      }

      //console.log("Item: " + item + "index: " + index)
      console.log("Item: " + item)
      this.modalInfo.title = ''
    },
    resetAll() {
      this.fields = ''
      this.reset();
      this.resetModal();
      console.log('PAGE RESET')
    },
    optionListCreate(list) {
      for (let i = 0; i < list.length; i++) {
        this.options.push({
          text: list[i].item_size,
          value: list[i].item_sku
        })
      }
    },
  },
  computed: {
    rows(){
      return this.search_results.length
    },
  },
  watch: {
    dropDownSelected() {
      console.log('DDS: ' + this.dropDownSelected)
      try {
        for (let i = 0; i <= this.options.length; i++){
          if(this.options[i].value === this.dropDownSelected){
            this.chosenItem = this.listOptions[i]
          }
        }
      } catch (e){
        console.log(e)
        console.log(e.response.data)
      }

    },
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