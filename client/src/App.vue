<template>
  <div id="app">
    <h1 class='header'>Traveler</h1>
    <Nav />
    <router-view> 
        
    </router-view>
  </div> 
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Nav from './components/Nav.vue'
export default {
  name: 'App',
  components: {
    Nav,

    
  }
}
</script>

<style>
#app {
  text-align: center;
  /* color: #2c3e50;   */

}
.header{
  background-color: rgba(31, 58, 109, 0.979);
  /* padding:0;  */
  margin:0
}
Nav{
  margin: 0
}
</style>
