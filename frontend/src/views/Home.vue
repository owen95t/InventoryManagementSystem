<template>
  <div class="home">
    <h1 class="title text-center">RETAIL INVENTORY MANAGEMENT</h1>


    <h2 class="text-center">Welcome!</h2>
    <div>
      <b-container>
        <b-table striped bordered responsive="sm" ></b-table>
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
          url: 'http://127.0.0.1/...' + term,
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
              console.log('ERROR DATA',error.response.data);
              console.log('ERROR STATUS',error.response.status);
              console.log('ERROR HEADERS',error.response.headers);
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
