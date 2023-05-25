<template>
  <div class="mt-5 text-start" ref="detail">
    <div class="empty"></div>
    <h3>{{movie.movie_title}}</h3>
    <div class="mt-5">
      <div class="mb-3">
        <h4>촬영 장소</h4>
        <hr>
      </div>
      <p v-for="(a,i) in showReviewCnt" :key="i">- {{movie.location_details[i].place}}</p>
      <button v-if="reviewCnt > 3" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        더보기
      </button>
    </div>
    <div class="align-items-center justify-content-center mt-5">
      <div>
        <h4>티저 영상</h4>
        <hr>
      </div>
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
        <hr>
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
      <reviewBody :movie_pk="$route.params.movie_pk"/>
    </div>
    <div class="empty"></div>
  </div>
</template>

<script>
import reviewBody from './reviewBody.vue'

export default {
  name: 'movieDetail',
  data(){
    return {
    }
  },
  computed: {
    movie(){
      return this.$store.state.movie
    },
    reviewCnt(){
      return this.movie.location_details_count
    },
    showReviewCnt(){
      return this.reviewCnt > 3 ? 3:this.reviewCnt
    }
  },
  components:{
    reviewBody
  },
  methods:{
  },
  mounted(){
    this.$refs['detail'].scrollIntoView({ behavior: "smooth"})
  }
}
</script>

<style>
.plot{
  text-indent: 10px;
}

.empty{
  background-color: rgb(0, 0, 0);
  opacity: 0%;
  height: 100px;

}
</style>