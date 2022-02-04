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
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@100;400&display=swap');
#app {
  font-family: Raleway, sans-serif;
  font-weight: bold;
  text-align: center;
  font-family: Raleway, sans-serif;
  
}
.header{
 margin:70px;
 font-size: 70px;
 font-weight: 100px;

}
Nav{
  margin: 0
  
}
</style>
