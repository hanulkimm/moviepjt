<template>
  <img @click="goToHome" src="../assets/earthImg.png" class="earth" alt="">
</template>

<script>
export default {
  name: 'EntryView',
  methods:{
    goToHome(){
      this.$router.push({name: 'home'})
    }
  }

}
</script>

<style>
.earth{
  width: 25vw;
  /* height: rem; */
  position: absolute;
  top: 30%;
  transform:translateX(-70%);
}
</style>