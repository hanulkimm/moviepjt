<template>
  <div>
    <div class="text-container">
      <h1>Welcome to CineMap</h1>
      <p>Click on the image to continue</p>
    </div>
    <img @click="goToLogin" src="../assets/earthImg.png" class="earth" alt="">
  </div>
</template>

<script>
export default {
  name: 'EntryView',
  methods: {
    goToLogin() {
      if (this.$store.state.token) {
        this.$router.push({ name: 'home' });
      } else {
        this.$router.push({ name: 'login' });
      }
    }
  }
}
</script>

<style>
.earth {
  width: 25vw;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: transform 0.3s ease;
}

.earth:hover {
  transform: translate(-50%, -50%) scale(1.1);
}

.text-container {
  text-align: center;
  position: absolute;
  top: calc(20% - 100px); /* Adjust the value to position the text as desired */
  left: 50%;
  transform: translateX(-50%);
}

.text-container h1 {
  color: aliceblue;
  font-size: 24px;
  margin-bottom: 10px;
}

.text-container p {
  font-size: 14px;
}
</style>
