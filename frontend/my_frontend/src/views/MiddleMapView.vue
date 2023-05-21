<template>
  <div>
    <img :src="require(`@/assets/map_remove/${this.region}.png`)" usemap="#image-map" class="map">

    <map name="image-map">
      <area v-for="region in regions" :key="`${region.title}`" @click="clickRegion" target="" :alt="region.title" :title="region.title" :coords="region.coords" shape="poly">
    </map>
  </div>
</template>

<script>
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
}
</script>

<style>

</style>