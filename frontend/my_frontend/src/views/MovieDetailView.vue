<template>
  <div class="d-flex justify-content-center detail text-white">
    <div class="movie-detail-view">
      <div class="capa row">
        <div class="col-1"></div>
        <div class="main mb-4 col-4">
          <movieSticky/>
        </div>
        <div class="mb-4 col-6">
          <movieDetail/>
        </div>

      </div>
      
    </div>
  </div>
</template>

<script>
import movieSticky from '../components/movieSticky.vue'
import movieDetail from '../components/movieDetail.vue'

export default {
  name: 'MovieDetailView',
  data(){
    return {
    }
  },
  components:{
    movieSticky,
    movieDetail
  },
  computed:{
    movie(){
      return this.$store.state.movie
    }
  }
}
</script>

<style>
.detail{
  margin-top: 100px;
}

*{
  box-sizing: border-box;
}
.main{
  height: 50vh;
}
.movie-detail-view{
  max-width: 1000px;
  background-color: rgb(0, 0, 0);
  opacity: 90%;
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