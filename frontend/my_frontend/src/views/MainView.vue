<template>
  <div id="main" ref="main-top">
    <div class="position-fixed top-btn" @click="goToTop">
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
              <h3 class="profile-username">Hello, {{this.$store.state.nickname}}님</h3>
              <button style="position: fixed; bottom: 50px; right: 150px;" @click="logout" type="button" class="btn btn-outline-danger btn-sm">LogOut</button>
            </div>
         </div>
        </div>
      </div>
    </nav>
    <div class="home">
      <div class="position-relative top">
        <h3 class="movie-list text-center">{{state}} {{city}}</h3>
      </div>
      <div class="d-flex justify-content-center">
        <div class="map-space">
          <router-view @select-city="selectCity" @unselect-city="unselectCity" @get-movie-list="getMovieList"/>
        </div>
        <div>
          <div class="form-body">
            <div class="row">
              <div class="form-holder">
                <div class="form-content">
                  <div class="form-items">
                    <h3>로케이션 촬영 장소로 영화 추천 받기</h3>
                    <br>
                    <p>지도를 눌러서 빈칸을 채워주세요!</p>

                    <form class="requires-validation" novalidate @submit.prevent="getMovieList">
                      <div class="col-md-12">
                        <input v-model="state" class="form-control" type="text" name="name" placeholder="행정구역" disabled required>
                      </div>
                      <br>
                      <div class="col-md-12">
                        <select class="form-select mt-3" required v-model="city">
                          <option selected disabled value="">{{selectedCity}}</option>
                          <option v-for="city in cityList" :value="city.title" :key="city.title">{{city.title}}</option>
                        </select>
                        <p></p>
                      </div>
                        
                      <div class="form-button mt-3">
                        <button id="submit" type="submit" class="btn btn-primary" :class="{active:state!=='행정구역을 선택해주세요', disabled:state==='행정구역을 선택해주세요'}">영화 추천 받기</button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="justify-content-center" ref="movie-list">
      <h3 class="text-center"><strong>{{message}}</strong></h3>
      <div></div>
      <movieList/>
    </div>
  </div>
</template>

<script>
import movieList from '@/components/movieList.vue'
import axios from 'axios'

export default {
  name: 'MainView',
  components:{
    movieList,
  },
  data(){
    return {
      city: '',
      scrollto: this.$refs["movie-list"],
      imageFile: null,
      getImageUrl : null,
    }
  },
  methods: {
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
      this.$store.commit('unselectCity')
      this.city = ''
      this.$store.dispatch('resetMovieList')
      this.$refs["main-top"].scrollIntoView({ behavior: "smooth"})
    },
    getMovieList(){
      const payload = {
        state: this.state,
        city: this.city,
        scrollto: this.$refs["movie-list"],
        scrollToTop: this.$refs["main-top"]
      }
      this.$store.dispatch('getMovieList', payload)
    },
    selectCity(city){
      this.city = city
    },
    unselectCity(){
      this.city = this.seletedCity != '' ? this.selectedCity:''
    },
    goToTop(){
      this.$refs["main-top"].scrollIntoView({ behavior: "smooth"})
    }
  },
  computed: {
    cityList(){
      return this.$store.state.regions[this.state]
    },
    state(){
      return this.$store.state.state
    },
    message(){
      return this.$store.state.message
    },
    selectedCity(){
      return this.$store.state.selectedCity
    },
  },
  created(){
    this.$store.commit('unselectCity')
    this.city = ''
    this.$store.dispatch('getProfile')
    
  },
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
.top{
  top: 150px;
}
.big-link {
  font-size: 3em; 
  color:#6891b4;
  /* text-decoration: none;  */
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

nav a.router-link-exact-active {
  color: #42b983;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700;900&display=swap');

*, body {
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    -moz-osx-font-smoothing: grayscale;
}

.top-btn{
  bottom: 30px;
  right: 30px;
  z-index: 999;
}

.movie-list {
    color: #fff;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 5px;
}

.map-space{
  margin-top: 210px;
}

.form-holder {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      min-height: 100vh;
}

.form-holder .form-content {
    position: relative;
    text-align: center;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;
    -webkit-justify-content: center;
    justify-content: center;
    -webkit-align-items: center;
    align-items: center;
    padding: 60px;
}

.form-content .form-items {
    border: 3px solid #fff;
    padding: 40px;
    display: inline-block;
    width: 100%;
    min-width: 540px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
    text-align: left;
    -webkit-transition: all 0.4s ease;
    transition: all 0.4s ease;
    height: 50vh;
    max-width: 300px;
    background-color: rgb(0, 0, 0);
    opacity: 90%;
}

.form-content h3 {
    color: #fff;
    text-align: left;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 5px;
}

.form-content h3.form-title {
    margin-bottom: 30px;
}

.form-content p {
    color: #fff;
    text-align: left;
    font-size: 17px;
    font-weight: 300;
    line-height: 20px;
    margin-bottom: 30px;
}


.form-content label, .was-validated .form-check-input:invalid~.form-check-label, .was-validated .form-check-input:valid~.form-check-label{
    color: #fff;
}

.form-content input[type=text], .form-content select {
    width: 100%;
    padding: 15px 20px;
    text-align: left;
    border: 0;
    outline: 0;
    border-radius: 6px;
    background-color: #fff;
    font-size: 15px;
    font-weight: 300;
    color: #8D8D8D;
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
    margin-top: 20px;
}

.invalid-feedback{
    color: #ff606e;
}
.valid-feedback{
   color: #2acc80;
}
</style>
