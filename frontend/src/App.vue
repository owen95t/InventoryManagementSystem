<template>
  <div id="app" >
    <b-navbar toggleable="lg" variant="light" type="light" class="justify-content-between">
      <b-navbar-brand><router-link to="/">Brand</router-link></b-navbar-brand>
      <b-collapse class="nav-collapse" is-nav>
        <b-nav-item><router-link to="/about">Route 1</router-link></b-nav-item>
        <b-nav-item><router-link to="/inventorymenu">Inventory</router-link> </b-nav-item>
        <b-nav-item><router-link to="/transfermenu">Transfers</router-link> </b-nav-item>
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
