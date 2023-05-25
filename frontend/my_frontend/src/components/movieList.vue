<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-lg-3 col-xl-2 movie" v-for="movie in movieList" :key="movie.id">
          <hr>
          <div class="profile-card-2"><img @click="clickMovie" :id="movie.id" :src="movie.poster" class="img img-responsive">
          </div>
        </div>
      </div>
    </div>
    <div class="empty">.</div>

  </div>
</template>

<script>
export default {
  name: 'movieList',
  data(){
    return {

    }
  },
  methods:{
    clickMovie(event){
      const params = {
        region: this.$store.state.state, 
        movie_pk: event.target.id
      }
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

.empty{
  background-color: rgb(0, 0, 0);
  opacity: 0%;
  height: 100px;
}
</style>