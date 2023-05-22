<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-4" v-for="movie in movieList" :key="movie.id">
          <hr>
          <div class="profile-card-2"><img :src="movie.movie.poster" class="img img-responsive">
            <div class="profile-name">JOHN DOE</div>
            <div class="profile-username">@johndoesurname</div>
            <div class="profile-icons"><a href="#"><i class="fa fa-facebook"></i></a><a href="#"><i class="fa fa-twitter"></i></a><a href="#"><i class="fa fa-linkedin"></i></a></div>
          </div>
        </div>
      </div>
    </div>
    <div v-for="movie in movieList" :key="movie.id">{{movie.movie.movie_title}}</div>
  </div>
</template>

<script>
export default {
  name: 'movieList',
  data(){
    return {

    }
  },
  computed: {
    movieList(){
      return this.$store.state['movieList']
    }
  }
  
}
</script>

<style>

</style>