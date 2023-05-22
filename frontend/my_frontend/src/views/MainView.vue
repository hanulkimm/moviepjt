<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Logo</a>
        <router-link @click.native="resetMovieList" to="/">Home</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">Dark offcanvas</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
          </div>
          <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu dropdown-menu-dark">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
            </ul>
            <form class="d-flex mt-3" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </div>
    </nav>
    <div class="home">
      <div class="d-flex justify-content-center">
        <div class="map-space">
          <router-view @select-state="selectState" @unselect-state="unselectState"/>
        </div>
        <div>
          <div class="form-body">
            <div class="row">
              <div class="form-holder">
                <div class="form-content">
                  <div class="form-items">
                    <h3>Register Today</h3>
                    <p>Fill in the data below.</p>
                    <form class="requires-validation" novalidate>

                      <div class="col-md-12">
                        <input v-model="state" class="form-control" type="text" name="name" placeholder="행정구역" required>
                        <div class="valid-feedback">Username field is valid!</div>
                        <div class="invalid-feedback">Username field cannot be blank!</div>
                      </div>

                      <div class="col-md-12">
                        <select class="form-select mt-3" required>
                          <option selected disabled value="">City</option>
                          <option v-for="city in cityList" :value="city.title" :key="city.title">{{city.title}}</option>
                        </select>
                          <div class="valid-feedback">You selected a position!</div>
                          <div class="invalid-feedback">Please select a position!</div>
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
  </div>
</template>

<script>
  export default {
    name: 'MainView',
    data(){
      return {
        state: '',
        city: '',
      }
    },
    methods: {
      resetMovieList(){
        this.$store.dispatch('resetMovieList')
      },
      selectState(state){
        this.state = state
      },
      unselectState(){
        this.state = ''
      },
      selectCity(city){
        this.city = city
      },
      unselectCity(){
        this.city = ''
      }
    },
    computed: {
      cityList(){
        return this.$store.state.regions[this.state]
      }

    }
  }


</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
