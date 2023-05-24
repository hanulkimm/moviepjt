<template>
<div>
  <nav class="navbar navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <img src="../assets/movie_icon.png" alt="">
        <router-link class="big-link" @click.native="resetMovieList" to="/home">CineMap</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <font-awesome-icon :icon="['fas', 'user']" size="xl" style="color: #ffffff;" />
        </button>
        <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">Profile Page</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <div class="profile">
              <!-- <i class="fa-solid fa-user fa-2xl"></i>
              <i class="fa-regular fa-user fa-2xl" style="color: #ffffff;"></i> -->
              <img src="../assets/profile.jpg" class="profile-img" alt="Profile Image"><br>
              <button>upload profile image </button>
              <br><br>
              <h3 class="profile-username">Hello, {{this.$store.state.username}}</h3>
              <button @click="logout" type="button" class="btn btn-outline-danger btn-sm">LogOut</button>
            </div>
         </div>
        </div>
      </div>
    </nav>
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
</div>
</template>

<script>
import movieSticky from '../components/movieSticky.vue'
import movieDetail from '../components/movieDetail.vue'

export default {
  name: 'MovieDetailView',
  data(){
    return {
      movie: this.$store.state.movie
    }
  },
  methods:{
    logout(){
        this.$store.dispatch('logout')
      },
    resetMovieList(){
      this.$store.dispatch('resetMovieList')
    }
  },
  components:{
    movieSticky,
    movieDetail
  },
  computed:{

  },
  created(){
    const params = {
        region: this.$route.params.region, 
        movie_pk: this.$route.params.movie_pk
      }
    console.log(params)
    this.$store.dispatch('getDetailMovie', params)
  }
}
</script>

<style>
.big-link {
  font-size: 2em; 
  text-decoration: none; 
}

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