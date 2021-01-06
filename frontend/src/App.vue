<template>
  <div id="app" >
    <b-navbar toggleable="lg" variant="light" type="light" class="justify-content-between">
      <b-navbar-brand><router-link to="/">Brand</router-link></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>

          <b-nav-item to="/inventorymenu">Inventory</b-nav-item>
          <b-nav-item to="/transfermenu" >Transfer</b-nav-item>
          <b-nav-item to="/ordermenu">Order</b-nav-item>
          <b-nav-item to="/customermenu">Customer</b-nav-item>
          <b-nav-item to="/about">About</b-nav-item>
          <b-nav-item to="/admin">Admin</b-nav-item>
        </b-navbar-nav>
      </b-collapse>

      <b-navbar-nav class="ml-auto">
<!--        RIGHT SIDE ITEMS    -->
      </b-navbar-nav>

    </b-navbar>

    <router-view/>

  </div>
</template>

<script>

</script>

<style>


</style>
