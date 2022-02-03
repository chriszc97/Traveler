<template>
  <div class="details">  
    <h2>Name: </h2> 
    <img :src= "url" alt="" />
    <h4>Description: </h4>
    <h4>Foods:</h4>
    <h4>landmarks</h4>
    <h4>Cost</h4>
    <h4>Country</h4>
    <button>Delete</button>
  </div>


</template>

<script>
export default {
  name: 'DestinationDetails'
}


</script>

<style scoped>
.details{
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  background-color: #25464b;
  cursor: pointer;
  transition: all 0.2s;
  color: black
}
button{
  color:cornflowerblue;
  background-color: antiquewhite;
}
</style>
