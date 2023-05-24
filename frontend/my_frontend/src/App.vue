<template>
  <div class="universe">

    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data(){
      return {
        state: '',
        city: '',
      }
    },
    methods: {
      logout(){
        this.$store.dispatch('logout')
      },
    }
  }
</script>


<style>
.universe{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url(@/assets/uni.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  height: 100vh;
  width: 100vw;
  overflow: auto;
}
</style>
