<template>
  <div id="main">
    <nav class="navbar navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <img src="../assets/movie_icon.png" alt="">
        <router-link to="/">Main</router-link> |
        <router-link @click.native="resetMovieList" to="/home">CineMap</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
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
    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-rocket text-white position-fixed top-btn" viewBox="0 0 16 16">
      <path d="M8 8c.828 0 1.5-.895 1.5-2S8.828 4 8 4s-1.5.895-1.5 2S7.172 8 8 8Z"/>
      <path d="M11.953 8.81c-.195-3.388-.968-5.507-1.777-6.819C9.707 1.233 9.23.751 8.857.454a3.495 3.495 0 0 0-.463-.315A2.19 2.19 0 0 0 8.25.064.546.546 0 0 0 8 0a.549.549 0 0 0-.266.073 2.312 2.312 0 0 0-.142.08 3.67 3.67 0 0 0-.459.33c-.37.308-.844.803-1.31 1.57-.805 1.322-1.577 3.433-1.774 6.756l-1.497 1.826-.004.005A2.5 2.5 0 0 0 2 12.202V15.5a.5.5 0 0 0 .9.3l1.125-1.5c.166-.222.42-.4.752-.57.214-.108.414-.192.625-.281l.198-.084c.7.428 1.55.635 2.4.635.85 0 1.7-.207 2.4-.635.067.03.132.056.196.083.213.09.413.174.627.282.332.17.586.348.752.57l1.125 1.5a.5.5 0 0 0 .9-.3v-3.298a2.5 2.5 0 0 0-.548-1.562l-1.499-1.83ZM12 10.445v.055c0 .866-.284 1.585-.75 2.14.146.064.292.13.425.199.39.197.8.46 1.1.86L13 14v-1.798a1.5 1.5 0 0 0-.327-.935L12 10.445ZM4.75 12.64C4.284 12.085 4 11.366 4 10.5v-.054l-.673.82a1.5 1.5 0 0 0-.327.936V14l.225-.3c.3-.4.71-.664 1.1-.861.133-.068.279-.135.425-.199ZM8.009 1.073c.063.04.14.094.226.163.284.226.683.621 1.09 1.28C10.137 3.836 11 6.237 11 10.5c0 .858-.374 1.48-.943 1.893C9.517 12.786 8.781 13 8 13c-.781 0-1.517-.214-2.057-.607C5.373 11.979 5 11.358 5 10.5c0-4.182.86-6.586 1.677-7.928.409-.67.81-1.082 1.096-1.32.09-.076.17-.135.236-.18Z"/>
      <path d="M9.479 14.361c-.48.093-.98.139-1.479.139-.5 0-.999-.046-1.479-.139L7.6 15.8a.5.5 0 0 0 .8 0l1.079-1.439Z"/>
    </svg>
    <div class="home">
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
                    <h3>Register Today</h3>
                    <p>Fill in the data below.</p>
                    <form class="requires-validation" novalidate @submit.prevent="getMovieList">
                      <div class="col-md-12">
                        <input v-model="state" class="form-control" type="text" name="name" placeholder="행정구역" disabled required>
                      </div>
                      <div class="col-md-12">
                        <select class="form-select mt-3" required v-model="city">
                          <option selected disabled value="">City</option>
                          <option v-for="city in cityList" :value="city.title" :key="city.title">{{city.title}}</option>
                        </select>
                      </div>

                      <div class="form-button mt-3">
                        <button id="submit" type="submit" class="btn btn-primary">Register</button>
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
      <div></div>
      <h3 class="movie-list">{{state}} {{city}}</h3>
      <movieList/>
      <h3><strong>{{message}}</strong></h3>
    </div>
  </div>
</template>

<script>

import movieList from '@/components/movieList.vue'

export default {
  name: 'MainView',
  components:{
    movieList,
  },
  data(){
    return {
      city: '',
      scrollto: this.$refs["movie-list"]
    }
  },
  methods: {
    logout(){
        this.$store.dispatch('logout')
      },
    resetMovieList(){
      this.$store.dispatch('resetMovieList')
    },
    getMovieList(){
      const payload = {
        state: this.state,
        city: this.city,
        scrollto: this.$refs["movie-list"]
      }
      this.$store.dispatch('getMovieList', payload)
    },
    selectCity(city){
      this.city = city
    },
    unselectCity(){
      this.city = ''
    },
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
    }
  },
}

</script>


<style>
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
}

/* body {
  overflow: auto;
} */

.movie-list {
    color: #fff;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 5px;
}

.map-space{
  margin-top: 250px;
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


.btn-primary{
    background-color: #6C757D;
    outline: none;
    border: 0px;
    box-shadow: none;
}

.btn-primary:hover, .btn-primary:focus, .btn-primary:active{
    background-color: #467baa;
    outline: none !important;
    border: none !important;
    box-shadow: none;
}

.invalid-feedback{
    color: #ff606e;
}

.valid-feedback{
   color: #2acc80;
}
</style>
