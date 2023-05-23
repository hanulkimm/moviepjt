<template>
  <div>
    <router-link to="/">Main</router-link> |
    <router-link :to="{name:'signup'}">Signup</router-link> |
    <router-link :to="{name:'login'}">Login</router-link> |
    <p class="btn" @click="logout" >LogOut</p>
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
</style>
