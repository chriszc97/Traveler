<template>
  <div id="app">
    <Nav />
    <DestinationPost />
    <DestinationDetails />


    
  </div> 
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Nav from './components/Nav.vue'
import DestinationPost from './components/DestinationoPost.vue'
import DestinationDetails from './components/DestinationDetails.vue'

export default {
  name: 'App',
  components: {
    Nav,
    DestinationPost,
    DestinationDetails
    
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
