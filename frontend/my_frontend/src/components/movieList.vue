<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-3 col-lg-2 movie" v-for="movie in movieList" :key="movie.id">
          <hr>
          <div class="profile-card-2"><img @click="clickMovie" :src="movie.poster" class="img img-responsive">
          </div>
        </div>
      </div>
    </div>
    <div v-for="movie in movieList" :key="movie.id">{{movie.movie_title}}</div>
  </div>
</template>

<script>
export default {
  name: 'movieList',
  data(){
    return {

    }
  },
  props:{
    region: String
  },
  methods:{
    clickMovie(event){
      const params = {
        region: this.region, 
        movie_pk: event.target.id
      }
      this.$store.dispatch('getDetailMovie', params)
      this.$router.push({name: 'movie', params})
    }

  },
  computed: {
    movieList(){
      return this.$store.state.movieList
    }
  }
  
}
</script>

<style>
.movie:hover img{
  /* transform: rotateY(180deg); */
  filter: grayscale(100%);
  transform: rotate(5deg) scale(1.1, 1.1);

}
</style>