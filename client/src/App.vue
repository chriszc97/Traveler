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
@import url(https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap);
#app {
  font-family: Raleway, sans-serif;
  font-weight: bold;
  text-align: center;
  /* color: #2c3e50;   */

}
.header{
  background-color:white;
  font-size: 70px;
  /* padding:0;  */
  margin:70px;
}
Nav{
  margin: 0
}
</style>
