<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div>
      <video class="video" controls crossorigin="anonymous" src="https://www.kmdb.or.kr/trailer/play/MK037733_P02.mp4">
        hihihi
      </video>
    </div>
    <div id="wrap">
      <iframe 
        src="https://www.kmdb.or.kr/trailer/play/MK037733_P02.mp4" 
        frameborder="0"
        id="frame"></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data(){
    return {
      url: ''
    }
  }
}
</script>

<style>
.video {width: 200px}
</style>

