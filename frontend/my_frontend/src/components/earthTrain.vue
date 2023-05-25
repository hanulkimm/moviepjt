<template>
  <div ref="container"></div>
</template>

<script>
import * as THREE from 'three';

export default {
  name: 'earthTrain',
  mounted() {
    this.initialize();
  },
  methods: {
    initialize() {
      const container = this.$refs.container;

      // Three.js scene 생성
      const scene = new THREE.Scene();

      // Three.js 카메라 생성
      const camera = new THREE.PerspectiveCamera(
        75,
        container.offsetWidth / container.offsetHeight,
        0.1,
        1000
      );
      camera.position.z = 5;

      // Three.js 렌더러 생성
      const renderer = new THREE.WebGLRenderer();
      renderer.setSize(container.offsetWidth, container.offsetHeight);
      container.appendChild(renderer.domElement);

      // Three.js 지구본 생성
      const geometry = new THREE.SphereGeometry(1, 32, 32);
      const texture = new THREE.TextureLoader().load('../assets/earth_texture.jpg');
      const material = new THREE.MeshBasicMaterial({ map: texture });
      const earth = new THREE.Mesh(geometry, material);
      scene.add(earth);

      // 애니메이션 루프
      const animate = () => {
        requestAnimationFrame(animate);
        earth.rotation.y += 0.005;
        renderer.render(scene, camera);
      };
      animate();
    },
  },
};
</script>

<style>
  #container {
    width: 100%;
    height: 100%;
  }
</style>
