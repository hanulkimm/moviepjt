<template>
  <div class="">
    <div class="d-flex justify-content-center">
      <img :src="require(`@/assets/map_remove/${this.region}.png`)" usemap="#image-map" class="map">
      <map name="image-map">
        <area v-for="region in regions" :key="`${region.title}`" @mouseout="unselectRegion" @mouseover="selectRegion" @click="clickRegion" target="" :alt="region.title" :title="region.title" :coords="region.coords" shape="poly">
      </map>
    </div>
    <div>
      <h4><strong>영화 리스트</strong></h4>
    </div>
    <movieList :region="region"/>
  </div>
  
</template>

<script>
import $ from 'jquery'
import movieList from '@/components/movieList.vue'

export default {
  name: 'MiddleMapView',
  components:{
    movieList,
  },
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
      this.$emit('selectCity', event.target.title)
      const payload = {
        region: this.region,
        city: event.target.title
      }
      this.$store.dispatch('getMovieList', payload)
    },
    selectRegion(event){
      console.log(event.target.title)
      this.$emit('selectCity', event.target.title)
    },
    unselectRegion(){
      this.$emit('unselectCity')
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