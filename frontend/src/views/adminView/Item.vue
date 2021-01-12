<template>
  <div class="item">
    <h1 class="text-center">Edit Page</h1>

    <h3 class="text-center">Choose from options below:</h3>

    <b-container>
      <div id="buttonRows">
        <b-button-group class="align-content-center">


        <b-button variant="outline-primary">Add/Bulk Add</b-button>
        <b-button variant="outline-primary">Edit/Bulk Edit</b-button>
          </b-button-group>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Item",
  data() {
    return{
      formatted: {},
    }
  },
  methods: {
    async postItem(data) {
      try {
        await axios.post('', data).then(response => {
          if (response) {
            console.log(response)
            console.log(response.status)
          }
        }).catch(e => {
          if (e) {
            console.log("POST ERROR"+e.status)
          }
        })
      } catch (er){
        console.log("postItem error: " + er)
      }
    },
    formatData() {

    },
    opened() {
      console.log("Item Edit Page")
    }
  },
  mounted() {
    this.opened()
  }
}
</script>

<style scoped>

#buttonRows {
}

</style>