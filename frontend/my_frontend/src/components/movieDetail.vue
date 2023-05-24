<template>
  <div class="mt-5 text-start">
    <h3>{{movie.movie_title}}</h3>
    <div class="">
      <p>촬영 장소</p>
      <p v-for="location in movie.location_details" :key="location.place">{{location.place}}</p>
    </div>
    <div class="d-flex align-items-center justify-content-center">
      <video 
        :src="movie.teaser"
        controls
        autoplay
        muted
        width=100%
        id="frame"></video>
    </div>
    <div class="">
      <div class="detail">
        <h3>줄거리</h3>
        <div class="plot">
          {{movie.plot}}
        </div>
      </div>
    </div>
    <div class="mt-5 cast profile-holder">
      <h3>Cast</h3>
      <div class="profile-content">
        <div class="profile-items">
          <div v-for="actor in movie.actors" class="profile-card-2" :key="actor.actor_name">
            <img v-if="actor.profile_path" :src="actor.profile_path" class="img img-responsive rounded mx-auto d-block">
            <img v-else src="@/assets/blankprofile.png" class="img img-responsive rounded mx-auto d-block" width=120px>
            <p>{{actor.actor_name}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="review">
      <reviewList :movie_pk="$route.params.movie_pk"/>
    </div>
  </div>
</template>

<script>
import reviewList from '../components/reviewList.vue'

export default {
  name: 'movieDetail',
  data(){
    return {
    }
  },
  computed: {
    movie(){
      return this.$store.state.movie
    }
  },
  components:{
    reviewList
  }

}
</script>

<style>
.plot{
  text-indent: 10px;
}
</style>