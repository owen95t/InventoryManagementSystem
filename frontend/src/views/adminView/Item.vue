<template>
  <div>
    <b-form>

    </b-form>
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

    }
  }
}
</script>

<style scoped>

</style>