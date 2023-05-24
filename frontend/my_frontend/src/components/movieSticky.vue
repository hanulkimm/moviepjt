<template>
  <div class="position-fixed mt-5 ">
    <div class="">
      <div class="profile-card-2"><img :src="movie.poster" class="img img-responsive"></div>
    </div>
    <div class="">
      <div class="">
        <div class="mt-5 text-start ">
          <p class="genre">장르 : 액션 로맨스 무협 공포</p>
          <p>개봉일 : 2023-05-24</p>
          <p>런타임 : 180분</p>
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
    }
  }

}
</script>

<style>
.genre{
  max-width: 280px;
}
</style>