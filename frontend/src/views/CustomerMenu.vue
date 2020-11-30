<template>
  <div class="customermenu">
    <h1 class="text-center">Customer Menu</h1>
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
      <b-alert :show="emptySearchAlert" fade variant="danger">
        <h4>Query Returned No Results. Please Try Again</h4>
      </b-alert>
    </b-container>
  </div>
</template>

<script>
export default {
name: "CustomerMenu",
  data() {
    return{
      picked: '',
      search_options: '',
      search_term: '',
      emptySearchAlert: false,
    }
  },
  methods: {
    getSearch() {

    },
    getModalSearch() {

    },
  }
}
</script>

<style scoped>

</style>