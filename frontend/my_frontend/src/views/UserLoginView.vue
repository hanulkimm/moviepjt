<template>
  <div class="form-body">
    <div class="row">
      <div class="form-holder">
        <div class="form-content">
          <div class="form-items">

            <b class="loginStyle">로그인 </b>
            <hr style="border-color:white">
            <!-- <br> -->

            <form @submit.prevent='logIn' class="requires-validation" novalidate>
              <div class="col-md-12">
                <input v-model="username" class="form-control" type="text" name="name" placeholder="username" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
              </div>
              <br>
              
              <div class="col-md-12">
                <input v-model="password" class="form-control" type="password" name="name" placeholder="password" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
              </div>
              <div class="error-message" v-if="loginValid" >로그인 정보가 올바르지 않습니다 </div>
              <br>
               
              <p>CineMap 회원이 아니신가요? <router-link style="text-decoration:none" :to="{name:'signup'}">지금 바로 가입해보세요!</router-link>  </p>
              <div class="form-button mt-3">
                <button id="submit" type="submit" class="btn btn-primary">Login</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserLoginView',
  data(){
    return {
      username : null,
      password : null,
      loginTry: false,

    }
  },
  computed:{
    loginValid(){
      return this.$store.state.loginTry && !this.$store.state.token
    }
  },
  methods:{
    logIn(){
      this.loginTry = true 
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      this.$store.dispatch('logIn',payload)
    },
  },
}
</script>

<style>
.loginStyle {
  font-size: 30px;
  color: white;
}

.error-message {
  color: red;
  font-size: 14px;
  margin-top: 10px;
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

.form-content .form-user-items {
    border: 3px solid #fff;
    padding: 13px;
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
    font-size: 40px;
    font-weight: 600;
    margin-bottom: 5px;
}

.form-content h3.form-title {
    margin-bottom: 20px;
}

.form-content p {
    color: #fff;
    text-align: left;
    font-size: 17px;
    font-weight: 300;
    line-height: 20px;
    margin-bottom: 20px;
}


.form-content label, .was-validated .form-check-input:invalid~.form-check-label, .was-validated .form-check-input:valid~.form-check-label{
    color: #fff;
}

.form-content input[type=text], .form-content input[type=password], .form-content select {
    width: 100%;
    padding: 13px 20px;
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
    margin-top: 15px;
}


.btn-primary{
    background-color: #6C757D;
    outline: none;
    border: 0px;
    box-shadow: none;
}

.btn-primary:hover, .btn-primary:focus, .btn-primary:active{
    background-color: #495056;
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
