<template>
<div>
  <div class="scroll-to-top" @click.prevent="scrollToTop">
    <font-awesome-icon
      :icon="['fas', 'circle-up']"
      style="color: #ffffff; font-size: 50px; cursor: pointer;"
    />
  </div>
    <nav class="navbar navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <img src="../assets/movie_icon.png" alt="">
        <router-link class="big-link " @click.native="resetMovieList" to="/home">C<font-awesome-icon :icon="['fas', 'map-pin']" />neMap</router-link>
        <button @click="profile" class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <font-awesome-icon :icon="['fas', 'user']" size="xl" style="color: #ffffff;" />
          <!-- <span class="navbar-toggler-icon"></span> -->
        </button>
        <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">Profile Page</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <div class="profile">
              <!-- 프로필!!! -->
              <!-- <img src="../assets/profile.jpg" class="profile-img" alt="Profile Image"><br> -->
              <img :src="getImageUrl" alt="Uploaded Image">
              <br><br>
              <!-- 업로두 -->
            <label for="file-upload" class="file-upload">
              Change Profile
              <input class="inputfile"  id="file-upload" type="file" style="display: none;" @change="handleFileUpload">
            </label>
            <br>
              <br><br>
              <h3 class="profile-username">Hello, {{this.$store.state.username}}</h3>
              <button style="position: fixed; bottom: 50px; right: 150px;" @click="logout" type="button" class="btn btn-outline-danger btn-sm">LogOut</button>
            </div>
         </div>
        </div>
      </div>
    </nav>
  <div>
    <div class="d-flex justify-content-center detail text-white" ref="detail">
      <div class="movie-detail-view">
        <div class="capa row">
          <!-- <div class="col-1"></div> -->
          <div class="main mb-4 col-4 justify-content-center">
            <movieSticky/>
          </div>
          <div class="mb-4 col-6" ref="movie-detail">
            <movieDetail/>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import movieSticky from '../components/movieSticky.vue'
import movieDetail from '../components/movieDetail.vue'

export default {
  name: 'MovieDetailView',
  data(){
    return {
      movie: this.$store.state.movie,
      getImageUrl:null,
    }
  },
  methods:{
    profile(){
      this.getImageUrl = this.$store.state.profile
    },
    handleFileUpload(e) {
      const file = e.target.files[0];

      const formData = new FormData()
      formData.append('profile_url', file)
      // console.log(formData)
      const token = this.$store.state.token
      const config = {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Token ${token}`
          }
      };
      const username = this.$store.state.username
      axios.post(`http://127.0.0.1:8000/accounts/profile/${username}/`, formData, config)
        .then(() => {
          console.log('File uploaded successfully.');
          axios({
            method:'get',
            url: `http://127.0.0.1:8000/accounts/getprofile/${username}/`
          })
          .then(res=>{
            console.log('got profile url')
            const profile = res.data.profile
            this.getImageUrl =  'http://127.0.0.1:8000' + profile
            this.$store.commit('SAVE_PROFILE', profile)
          })
        })
      },
    logout(){
        this.$store.dispatch('logout')
      },
    resetMovieList(){
      this.$store.dispatch('resetMovieList')
    },
    // scroll up
    scrollToTop() {
      this.$refs["movie-detail"].scrollIntoView({behavior: 'smooth'})
    },
    
  },
  components:{
    movieSticky,
    movieDetail,
  },
  computed:{

  },
  created(){
    const params = {
        region: this.$route.params.region, 
        movie_pk: this.$route.params.movie_pk
      }
    this.$store.dispatch('getDetailMovie', params)
    this.$store.dispatch('getProfile')
  },
  mounted(){
    this.$refs['movie-detail'].scrollIntoView()
  }
}
</script>

<style>
.file-upload {
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 5px 13px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  font-size: 13px;
}


.file-upload input[type="file"] {
  display: none;
}

.scroll-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 999;
}

.big-link {
  font-size: 2em; 
  text-decoration: none; 
}

.profile {
  text-align: center;
  margin-bottom: 20px;
}

.profile-img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.profile-username {
  font-size: 24px;
  color: white;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
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
  width: 1500px;
  background-color: rgb(0, 0, 0);
  opacity: 90%;
}
.plot{
  overflow: auto;
}

.profile-content .profile-items {
    border: 3px solid #fff;
    padding: 40px;
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