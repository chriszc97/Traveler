<template>
  <div class="details">  
    <h2>{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
    <h4>Description: {{trip.description}} </h4>
    <h4>Foods: {{trip.food}}</h4>
    <h4>landmarks: {{trip.landmarks}}</h4>
    <h4>Cost: {{trip.cost}}</h4>
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
  margin-top: 60px;
  font-size: 25px;
  background-color: white;
  cursor: pointer;
  transition: all 0.2s;
  color: black;
  justify-content: center;
  height: 100vh;
}
button{
  font-size: 24px;
  color:cornflowerblue;
  background-color: rgb(227, 255, 249);
  display: inline-block;
  border-radius: 1.5vh;
}
img{
  margin: auto;
  justify-content: center;
  padding: 0

  
}

h2{
  margin-top: 250px;
}
</style>
