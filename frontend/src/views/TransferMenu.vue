<template>
  <div class="transfermenu">
    <h1 class="text-center">Transfer Menu</h1>
<!--    Search Bar + Alert    -->
    <div style="padding-bottom: 25px">
      <b-container>
        <b-form-input type="submit" class="mt-2" v-model="search_term" v-on:keyup.enter="getSearch(search_term)" placeholder="Search..."></b-form-input>
        <span><b-button variant="outline-success my-2 my-sm-2" type="submit" v-on:click="getSearch(search_term)">Search</b-button></span>
        <b-alert :show="emptySearchAlert" fade variant="danger">Query Returned No Results. Please Try Again</b-alert>
      </b-container>
    </div>
<!--    Table     -->
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
      search_term: '',
      emptySearchAlert: false,
      isEditing: false,
    }
  },
  methods: {
    getTransfers(){

    },
    getSearch() {

    },

  }
}
</script>

<style>

</style>