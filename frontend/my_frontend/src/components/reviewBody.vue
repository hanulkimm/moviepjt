<template>
  <div class="mt-5">
    <h3>리뷰</h3>
    <hr>
    <div>
      <reviewList :reviews="reviews"/>
    </div>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#review-create-modal">리뷰 작성</button>
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
      reviews: []
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
      this.reviews = res.data
    })
  },
  methods:{
    createReview(){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/comments/`,
        data: {
          content: this.content,
          rate: this.value,
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      }).then(res => {
        console.log(res)
      }).then(() => {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/api/v1/movies/${this.movie_pk}/commentlist/`
        }).then(res => {
          this.reviews = res.data
          console.log(res.data)
        })
      }).catch(err => {
        console.log(err)
      })
    },

  }
}
</script>

<style>

</style>