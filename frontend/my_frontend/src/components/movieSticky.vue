<template>
  <div class="position-fixed mt-5 ">
    <div class="">
      <div class="profile-card-2"><img :src="movie.poster" class="img img-responsive"></div>
    </div>
    <div class="">
      <div class="">
        <div class="mt-5 text-start ">
          <p>
            <span class="genre">장르 : </span>
            <span v-for="genre in movie.genres" :key="genre.genre">{{genre.genre}}&nbsp;</span>
          </p>
          <p>개봉일 : {{releaseDate}}</p>
          <p>런타임 : {{movie.runtime}}분</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'movieSticky',
  computed:{
    movie(){
      return this.$store.state.movie
    },
    releaseDate(){
      const release_date = this.$store.state.movie.release_date
      return release_date.slice(0, 4)+'-'+release_date.slice(4,6)+'-'+release_date.slice(6,8)
    }
  }

}
</script>

<style>
.genre{
  max-width: 280px;
}
</style>