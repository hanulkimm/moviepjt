<template>
  <div class="d-flex justify-content-center">
    <div class="">
      <img :src="require(`@/assets/map_remove/${this.region}.png`)" usemap="#image-map" class="map">
    </div>

    <map name="image-map">
      <area v-for="region in regions" :key="`${region.title}`" @click="clickRegion" target="" :alt="region.title" :title="region.title" :coords="region.coords" shape="poly">
    </map>
    <div>
      영화 리스트
    </div>
  </div>
  
</template>

<script>
import $ from 'jquery'
export default {
  name: 'MiddleMapView',
  data(){
    return {
      region: this.$route.params.region,
    }
  },
  computed:{
    regions(){
      return this.$store.state.regions[this.region]
    }
  },
  methods:{
    clickRegion(event){
      console.log(event.target.title)
    }
  },
  created(){
    $(function() {
      $('.map').maphilight({
        fillColor: 'ff0000',
      });
    });
  }
}
</script>

<style>
</style>