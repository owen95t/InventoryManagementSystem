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
          <b-form-input type="submit" v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search..."></b-form-input>
          <b-input-group-append><b-button variant="outline-success" type="submit" v-on:click="getSearch(search_term)">Search</b-button></b-input-group-append>
        </b-input-group>
        <b-alert :show="emptySearchAlert" fade variant="danger">
          <h4>Query Returned No Results. Please Try Again</h4>
        </b-alert>
      </b-container>
<!--      <h3>{{search_term}}</h3>-->
<!--      <b-container class="resultscontainer">-->
<!--        &lt;!&ndash; CONTENT for RESULTS  &ndash;&gt;-->
<!--        <b-table hover striped bordered responsive="sm" :items="items" :fields="fields">-->
<!--        </b-table>-->
<!--      </b-container>-->

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
            :items="items"
            :per-page="perPage"
            :current-page="currentPage"
            :fields="fields"
            @row-clicked="toggleDetails">
          <template #cell(show_details)="row">
            <b-button size="sm" @click="row.toggleDetails" class="mr-2">
              {{row.detailsShowing? 'Hide' : 'Show'}} Details
            </b-button>
          </template>
        </b-table>
        </b-container>
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
    toggleDetails(row){
      row._showDetails = !row._showDetails
    },
    getSearch(term) {
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/Item/?search='+term
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
  },
  computed: {
    rows() {
      return this.items.length
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