<template>
  <div class="navbar">
    <b-navbar variant="light" type="light" class="justify-content-between">
      <b-navbar-brand><router-link to="/">Is This Nestle?</router-link></b-navbar-brand>
      <b-nav-item><router-link to="/about">Inventory</router-link></b-nav-item>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input class="form-control mr-sm-2" v-model="search_term" placeholder="Search..."></b-form-input>
          <b-button variant="outline-success my-2 my-sm-2" type="submit" v-on:click="getSearch(search_term)">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
name: "topnavbar"
}
</script>

<style scoped>

</style>