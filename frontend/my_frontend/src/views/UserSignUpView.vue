<template>
  <div class="form-body">
    <div class="row">
      <div class="form-holder">
        <div class="form-content">
          <div class="user-items">
            <h3>회원가입</h3>
            <p>아이디로 간편하게 CineMap을 시작하세요! </p>
            
            <form @submit.prevent='signUp' class="requires-validation" novalidate>

              <div class="col-md-12">
                <input v-model="username" class="form-control" type="text" name="name" placeholder="Username" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
              </div>
              <br>
              
              <div class="col-md-12">
                <input v-model="password1" @input="passwordLengthValid" class="form-control" type="password" name="name" placeholder="Enter Password" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
                <div class="error-message" v-if="passwordError">비밀번호는 8자 이상이어야 합니다.</div>
              
              </div>
              <br>

              <div class="col-md-12">
                <input v-model="password2" @input="passwordMatchValid" class="form-control" type="password" name="name" placeholder="Enter Password Again" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
                <div class="error-message" v-if="matchError">비밀번호가 일치하지 않습니다.</div>
              </div>
              <br>
              <p>이미 회원이신가요? <router-link :to="{name:'login'}">LOGIN</router-link> </p>
              <div class="form-button mt-3">
                <button id="submit" type="submit" class="btn btn-primary">SignUp</button>
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
  name: 'UserSignUpView',
  data(){
    return {
      username : null,
      password1 : null,
      password2 : null,
      passwordError: false,
      matchError: false,
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
    signUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp',payload)
      
    }
  }
}
</script>

<style>
.form-content .user-items {
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
    height: 80vh;
    max-width: 300px;
    background-color: rgb(0, 0, 0);
    opacity: 90%;
}
</style>
