<template>
  <div class="position-fixed mt-5 ">
    <div class="">
      <div class="profile-card-2"><img :src="movie.poster" class="img img-responsive"></div>
    </div>
    <div class="">
      <div class="">
        <div class="">
          상세 정보
          <p>genre</p>
          <p>release_date</p>
          <p>runtime</p>
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

</style>