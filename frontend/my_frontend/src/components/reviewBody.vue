<template>
  <div class="mt-5">
    <div class="row">
      <h3 class="col-2 text-center">리뷰</h3>
      <button type="button" class="btn btn-review col-2" data-bs-toggle="modal" data-bs-target="#review-create-modal">리뷰 작성</button>
    </div>
    <hr>
    <div>
      <reviewList :reviews="reviews"/>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import reviewList from '@/components/reviewList.vue'

export default {
  name: 'reviewBody',
  data(){
    return {
      value: 0,
      content: '',
    }
  },
  computed:{
    reviews(){
      return this.$store.state.reviews
    }
  },
  components:{
    reviewList
  },
  props:{
    movie_pk: String
  },
  created(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/commentlist/`
    }).then(res => {
      this.$store.commit('getMovieReviews', res.data)
    })
  },
  methods:{
  }
}
</script>

<style>
.btn-review{
  border: 1px solid;
  color: white;
  text-align: center;
}
</style>