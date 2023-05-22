<template>
  <div>
    <router-link to="/">Main</router-link> |
    <router-link :to="{name:'signup'}">Signup</router-link> |
    <router-link :to="{name:'login'}">Login</router-link>
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
    }
  }
</script>


<style>
</style>
