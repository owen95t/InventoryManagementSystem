<template>
  <div class="home">

    <b-navbar variant="light" type="light" class="justify-content-between">
      <b-navbar-brand>Inventory Management System</b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input class="form-control mr-sm-2" placeholder="Search..."></b-form-input>
          <b-button variant="outline-success my-2 my-sm-2" type="submit">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
    <h1 class="title text-center">RETAIL INVENTORY MANAGEMENT</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export default {
  name: 'Home',
}
</script>
