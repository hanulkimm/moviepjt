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

        <font-awesome-icon :icon="['fas', 'earth-americas']"  size="2xl" style="color: #ffffff;" />
        <!-- <font-awesome-icon :icon="['fas', 'video']" size="xl" style="color: #ffffff;" /> -->
        <!-- <img src="../assets/movie_icon.png" alt=""> -->
        <router-link class="big-link " @click.native="resetMovieList" to="/home">C<font-awesome-icon :icon="['fas', 'map-pin']" />neMap</router-link>
        <button @click="profile" class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <font-awesome-icon :icon="['fas', 'user']" size="xl" style="color: #ffffff;" />
          <!-- <span class="navbar-toggler-icon"></span> -->
        </button>
        <!-- 프로필 페이지 -->
        <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
          <div class="offcanvas-header pb-0">
            <h5 style="font-size:20px" class="offcanvas-title" id="offcanvasDarkNavbarLabel">{{this.$store.state.nickname}}님의 프로필</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <hr style="border-color:white">
          <div class="offcanvas-body">
            <div class="profile">
              <!-- 프로필!!! -->
              <img  :src="getImageUrl" alt="Uploaded Image">
              <br><br>
              <!-- 업로두 -->
              <label for="file-upload" class="file-upload" >
                Change Profile
                <input class="inputfile"  id="file-upload" type="file" style="display: none;" @change="handleFileUpload" accept="image/*">
              </label>
              
              <br>
              <br><br>
              <!-- -----------------FORM---------------->
              <hr style="border-color:white">
              <form  @submit.prevent='edit' class="requires-validation" novalidate>
              <div class="col-md-12">
                <label for="">Username</label>
                <input style="color:gray" disabled class="form-control" type="text" name="name" v-model="username" >
              </div>
              <br>
              
              <div class="col-md-12">
                <label for="">Nickname</label>
                <input v-model="nickname" class="form-control" type="text" name="name" required>
              </div>
            
              <br>

              <div class="col-md-12">
                <label for="">Password</label>
                <input v-model="password1" @input="passwordLengthValid" class="form-control" type="password" name="name" placeholder="New Password" required>
                <div class="error-message" v-if="passwordError">비밀번호는 8자 이상이어야 합니다.</div>
                
              </div>
              <br>

              <div class="col-md-12">
                <input v-model="password2" @input="passwordMatchValid" class="form-control" type="password" name="name" placeholder="Enter Password Again" required>
                <div class="error-message" v-if="matchError">비밀번호가 일치하지 않습니다.</div>
              </div>

              <div class="form-button mt-3">
                <button id="edit" type="submit" class="btn btn-primary">Save </button>
              </div>
            </form>
            <hr style="border-color:white">
              <!----------------END FORM------------------>

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
      username : this.$store.state.username,
      nickname: this.$store.state.nickname,
      alertMessage:null,
      passwordError: false,
      matchError: false,
      password1:null,
      password2:null,
    }
  },
  methods:{
    passwordLengthValid(){
      // var reg_pwd = /[`~!@#$%^&*()_|+\-=?;:'",.<>]/
      if (this.password1.length < 8) {
        this.passwordError = true
      } else {
        this.passwordError = false
      }
    },
    passwordMatchValid(){
      if (this.password1 !== this.password2){
        this.matchError = true
      } else {
        this.matchError = false
      }
    },
    edit(){
      const nickname = this.nickname
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      axios({
          method:'post',
          url: `http://127.0.0.1:8000/accounts/nickname/${username}/`,
          data :{
            nickname
          }
        })
      this.$store.commit('SAVE_NICKNAME', nickname)
      if (password1) {
        const token = this.$store.state.token
        axios({
          method:'post',
          url:'http://127.0.0.1:8000/accounts/password/change/',
          headers: {
          'Authorization': `Token ${token}`
          },
          data:{
            new_password1: password1,
            new_password2: password2
          }
        })
        .then(()=>console.log('success in changing password'))
        .catch(err=>console.log(err))
        this.password1 = null
        this.password2 = null
      }
    },
    profile(){
      this.getImageUrl = this.$store.state.profile
      this.nickname = this.$store.state.nickname
    },
    handleFileUpload(e) {
      const file = e.target.files[0];
      console.log(file.size)
      if (file.size > 6000) {
        alert("업로드 가능한 파일 용량을 초과하였습니다.")
      } else {

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
      }
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
    this.nickname = this.$store.state.nickname
  },
  mounted(){
    this.$refs['movie-detail'].scrollIntoView()
  }
}
</script>

<style>
.error-message {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}
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
  height: 40vh;
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