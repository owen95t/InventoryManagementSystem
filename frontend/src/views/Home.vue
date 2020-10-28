<template>
  <div class="home">

    <b-navbar variant="light" type="light" class="justify-content-between">
      <b-navbar-brand>Inventory Management System</b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input class="form-control mr-sm-2" placeholder="Search..." v-model="search_term"></b-form-input>
          <b-button variant="outline-success my-2 my-sm-2" type="submit" v-on:click="getSearch(search_term)">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
    <h1 class="title text-center">RETAIL INVENTORY MANAGEMENT</h1>

    <div>
      <b-container>
        <b-table striped bordered ></b-table>
      </b-container>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: 'Home',
  data() {
    return{
      products: [],
      product: '',
      search_term: '',
      error_msg: '',
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    getList(){
      axios({
        method: 'get',
        url: '',
        auth: {
          username: 'owen_t',
          password: '2391559Ong'
        }
      }).then(response => this.products = response.data)
    },
    getSearch(term){
      if (this.search_term !== '' || this.search_term !== null) {
        axios({
          method: 'get',
          url: '' + term,
          auth: {
            username: 'owen_t',
            password: '2391559Ong'
          }
        }).then(response => {
          console.log('INITIAL LOGGED DATA: ', response.data)
          if (response.data) {
            this.products = response.data
          }
          if (this.products.length === 0) {
            console.log('EMPTY DATA');
            this.error_msg = "No results found. Please try again"
          }
        })
          .catch((error) => {
            if (error.response) {
              console.log('RESPONSE ERROR');
              console.log('ERROR DATA'+error.response.data);
              console.log('ERROR STATUS'+error.response.status);
              console.log('ERROR HEADERS' + error.response.headers)
            }else if (error.request) {
              console.log('REQUEST ERROR');
              console.log(error.request);
            }else{
              console.log('ERROR somewhere', error.message);
            }
          })
      }
    }

  },
  // watch: {
  //   search_term(value) {
  //     this.getSearch(value)
  //   }
  // }
}
</script>
