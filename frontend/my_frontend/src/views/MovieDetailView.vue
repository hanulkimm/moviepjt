<template>
  <div class="d-flex justify-content-center">
    <div class="movie-detail-view">
      <div class="main row custom-border mb-4">
        <div class="col-4">
          <div class="profile-card-2"><img :src="movie.poster" class="img img-responsive"></div>
        </div>
        <div class="col-7">
          <h3>{{movie.movie_title}}</h3>
          <div class="row">
            <div class="col-5 custom-border">
              상세 정보
              <p>genre</p>
              <p>release_date</p>
              <p>runtime</p>
            </div>
            <div class="col-2"></div>
            <div class="col-5 custom-border">
              <p>촬영 장소</p>
              <p v-for="location in movie.location_details" :key="location.place">{{location.place}}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="row mb-4">
        <div class="col-4 custom-border d-flex align-items-center justify-content-center">
          <iframe 
            src="https://www.kmdb.or.kr/trailer/play/MK037733_P02.mp4" 
            frameborder="0"
            id="frame"></iframe>
        </div>
        <div class="col-8">
          <div class="detail custom-border plot">
            {{movie.plot}}
          </div>
        </div>
      </div>
      <div class="cast profile-holder">
        <div class="profile-content">
          <div class="profile-items">
            <div v-for="actor in movie.actors" class="profile-card-2" :key="actor.actor_name">
              <img :src="actor.profile_path" class="img img-responsive rounded mx-auto d-block">
              <p>{{actor.actor_name}}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="review">
        <reviewList :movie_pk="$route.params.movie_pk"/>
      </div>
    </div>
  </div>
</template>

<script>
import reviewList from '../components/reviewList.vue'

export default {
  name: 'MovieDetailView',
  data(){
    return {
    }
  },
  components:{
    reviewList
  },
  computed:{
    movie(){
      return this.$store.state.movie
    }
  }
}
</script>

<style>
*{
  box-sizing: border-box;
}
.custom-border{
  border: 3px solid #fff;
  padding: 20px;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  text-align: left;
  -webkit-transition: all 0.4s ease;
  transition: all 0.4s ease;
  height: 30vh;
}
.main{
  height: 50vh;
}
.movie-detail-view{
  max-width: 1000px;
}
.plot{
  overflow: auto;
}
.profile-content .profile-items {
    border: 3px solid #fff;
    padding: 20px;
    display: flex;
    min-width: 540px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    text-align: left;
    -webkit-transition: all 0.4s ease;
    transition: all 0.4s ease;
    height: 30vh;
    overflow: auto;
}

.profile-items .img{
  height: 80%;
  padding-right: 5px;
}

.profile-items p{
  font-size: 15px;
  color: white;
  text-align: center;
}
</style>