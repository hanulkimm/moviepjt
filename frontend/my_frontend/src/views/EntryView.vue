<template>
<div >
  <img @click="goToHome" src="../assets/earthImg.png" class="earth" alt="">
</div>
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
  transition: transform 0.3s ease;
}
.earth:hover {
  transform: translateX(-70%) scale(1.1);
}
</style>