<template>
  <div>
    <router-link to="/">Home</router-link> |
    <router-link :to="{name:'login'}">login</router-link>
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
