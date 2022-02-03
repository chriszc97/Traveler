<template>
  <div class="details">  
    <h2>{{trip.destinations.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
    <h4>Description: {{trip.destinations.description}} </h4>
    <h4>Foods: {{trip.destinations.food}}</h4>
    <h4>landmarks: {{trip.destinations.landmarks}}</h4>
    <h4>Cost: {{trip.destinations.cost}}</h4>
    <h4>Country: {{trip.name}}</h4>
    <button>Delete</button>
  </div>
</template>

<script>
export default {
  name: 'DestinationDetails',
  props: ['trip'],
  methods:{
  }
}


</script>

<style scoped>
.details{
  /* /* max-width: 300px; // */
  /* max-height: 100%;  */
  border-radius: 4px;
  background-color: #25464b;
  cursor: pointer;
  transition: all 0.2s;
  color: black;
  justify-content: center;
  height: 100vh;
}
button{
  color:cornflowerblue;
  background-color: antiquewhite;
}
img{
  width: 350px;
  justify-content: center;
  padding: 0

  
}
</style>
