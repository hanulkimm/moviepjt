<template>
  <div class="form-body">
    <div class="row">
      <div class="form-holder">
        <div class="form-content">
          <div class="form-items">
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
                <input v-model="password1" class="form-control" type="password" name="name" placeholder="Password" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
              </div>
              <br>

              <div class="col-md-12">
                <input v-model="password2" class="form-control" type="password" name="name" placeholder="Password Check" required>
                <div class="valid-feedback">Username field is valid!</div>
                <div class="invalid-feedback">Username field cannot be blank!</div>
              </div>
              <br>

              <div class="form-button mt-3">
                <button id="submit" type="submit" class="btn btn-primary">Register</button>
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
    }

  },
  methods:{
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

*, body {
    font-family: 'Poppins', sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    -moz-osx-font-smoothing: grayscale;
}

html, body {
    height: 100%;
    background-color: #152733;
    overflow: hidden;
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

.form-content input[type=text], .form-content input[type=email], .form-content select {
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
