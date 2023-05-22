<template>
  <div>
    <div class="main">
      <div>
        poster
      </div>
      <div>
        <h3>{{movie.movie_title}}</h3>
        <div>
          <div>
            상세 정보
          </div>
          <div>
            촬영장소
          </div>
        </div>
      </div>
    </div>
    <div class="detail">
      prompt
    </div>
    <div class="cast">
      cast
    </div>
    <div class="review">
      review
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
  data(){
    return {
      movie: this.$store.state.movie
    }
  }

}
</script>

<style>

</style>