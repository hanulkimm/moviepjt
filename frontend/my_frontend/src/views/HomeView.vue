<template>
  <div class="home">
    <img alt="main map" src="../assets/map-remove.png" usemap="#image-map">
    <map name="image-map">
      <area @click="printRegion" id="강원도" coords="85,26,126,28,139,10,171,63,185,87,150,95,134,85,114,87,114,65,101,62,101,44" shape="poly">
      <area @click="printRegion" id="경기도" coords="55,53,67,39,81,26,95,42,99,60,113,66,113,86,87,104,71,103,59,97,66,73,82,70,78,75,85,62,76,57,68,64,57,63" shape="poly">
      <area @click="printRegion" id="서울" coords="78,58,81,64,80,72,69,70,68,64" shape="poly">
      <area @click="printRegion" id="인천" coords="52,49,35,58,44,73,61,74,67,68,56,62,66,69" shape="poly">
      <area @click="printRegion" id="전라남도" coords="48,188,49,196,59,197,68,185,79,195,102,196,116,232,103,234,102,246,91,243,79,251,57,253,51,246,41,248,36,257,22,257,25,235,25,223,32,213,32,203" shape="poly">
    </map>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  methods: {
    printRegion(event){
      console.log(event.target.id)
    }
  }
}
</script>
