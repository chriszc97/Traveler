<template>
  <div class="details">  
    <h2>{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
    <h4>{{trip.description}} </h4>
    <h4>Good Eats: {{trip.food}}</h4>
    <h4>Things To Do: {{trip.landmarks}}</h4>
    <h4>Average Cost of Trip: {{trip.cost}}</h4>
    
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
  font-size: 20px;
  background-color: white;
  cursor: pointer;
  transition: all 0.2s;
  color: black;
  justify-content: center;
  height: 100vh;
}
button{
  font-size: 24px;
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
  margin-top: 25px;
}
</style>
