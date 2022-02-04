<template>
  <div class="details" >  
    <div :key='destination.id' v-for='destination in destination'>
    <h2>{{destination.name}} </h2> 
    <img :src='destination.photo_url' alt="" />
    <h4>Description: {{destination.description}} </h4>
    <h4>Good Eats: {{destination.food}}</h4>
    <h4>landmarks, Activities, Attractions, etc.: {{destination.landmarks}}</h4>
    <h4>Average Cost of Trip: {{destination.cost}}</h4>
    <h4>Country: {{destination.name}}</h4>
    <button @click='deleteDestination(trip.destinations[e.target.value])' >Delete</button>
  </div>
  </div>
</template>

<script>

export default {
  name: 'DestinationDetails',
  props: ['destination','trip'],
  mounted(){

  },
  methods:{
    deleteDestination(id){
      console.log(id)
      this.$emit('deleteDestination', id)
    }

  
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
