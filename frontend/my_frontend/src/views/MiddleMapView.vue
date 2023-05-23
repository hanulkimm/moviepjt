<template>
  <div class="">
    <div class="d-flex justify-content-center">
      <img :src="require(`@/assets/map_remove/${this.region}.png`)" usemap="#image-map" class="map">
      <map name="image-map">
        <area v-for="region in regions" :key="`${region.title}`" @mouseout="unselectRegion" @mouseover="selectRegion" @click="clickRegion" target="" :alt="region.title" :title="region.title" :coords="region.coords" shape="poly">
      </map>
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
    clickRegion(){
      this.$emit('get-movie-list')
    },
    selectRegion(event){
      this.$emit('select-city', event.target.title)
    },
    unselectRegion(){
      this.$emit('unselect-city')
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