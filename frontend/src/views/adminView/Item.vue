<template>
  <div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Item",
  data() {
    return{

    }
  },
  methods: {
    async postItem() {
      try {
        await axios.post()
      } catch (er){
        console.log("postItem error: " + er)
      }
    }
  }
}
</script>

<style scoped>

</style>