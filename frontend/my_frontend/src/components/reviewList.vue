<template>
  <div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'reviewList',
  props:{
    movie_pk: String
  },
  created(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/commentlist/`
    }).then(res => {
      console.log(res)
    })
  }

}
</script>

<style>

</style>