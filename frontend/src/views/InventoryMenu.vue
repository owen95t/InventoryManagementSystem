<template>
  <div class="inventorymenu">
    <h1 class="text-center">Inventory Menu</h1>
    <!--    Search Bar + Alert    -->
    <div style="padding-bottom: 25px">
      <b-container>
        <b-input-group>
          <b-input-group-prepend>
            <b-dropdown text="Filter">
              <b-form-group>
                <b-radio-group :options="search_options" style="padding: 3px"></b-radio-group>
              </b-form-group>
            </b-dropdown>
          </b-input-group-prepend>
          <b-form-input type="submit" class="" v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search..."></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="getSearch(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <b-alert :show="emptySearchAlert" fade variant="danger">
          <h4>Query Returned No Results. Please Try Again</h4>
        </b-alert>
      </b-container>
      <b-container class="resultscontainer">
        <!-- CONTENT for RESULTS  -->
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
      search_term: '',
      <!-- TODO: import config instead of typing out all of this -->
      config: [{
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
        key: 'item_description',
        label: 'Description',
      }, {
        key: 'item_color',
        label: 'Color'
      }, {
        key: 'item_color_code',
        label: 'Color Code'
      }, {
        key: 'item_season',
        label: 'Season'
      }, {
        key: 'item_date',
        label: 'Date'
      }, {
        key: 'item_category',
        label: 'Category'
      }, {
        key: 'item_subcategory',
        label: 'Subcategory'
      }, {
        key: 'item_price',
        label: 'Price'
      }, {
        key: 'item_current_price',
        label: 'Current Price'
      }, {
        key: 'item_on_sale',
        label: 'On Sale'
      }, {
        key: 'item_sku',
        label: 'SKU'
      }, {
        key: 'item_size',
        label: 'Size',
      }, {
        key: 'item_quantity',
        label: 'Total Quantity'
      }],
      emptySearchAlert: false,
      items: [],
      search_options: [
        {text: 'Brand'},
        {text: 'SKU'},
        {text: 'Name'},
      ],
    }
  },
  mounted() {

  },
  methods: {
    getSearch() {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/'
        }).then(response =>{
          console.log(response.data);
          if(response.data){
            this.emptySearchAlert = false;
            this.items = response.data
          }
          if (this.items.length === 0) {
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
    }
  }
}
</script>

<style scoped>


.resultscontainer {
  border: 3px seagreen solid;
  border-radius: 10px;
  margin-top: 10px;
  visibility: collapse;
}
</style>