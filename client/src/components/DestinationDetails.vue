<template>
  <div class="details" >  
    <div :key='destination.id' v-for='destination in destination'>
    <h2>{{destination.name}} </h2> 
    <img :src='destination.photo_url' alt="" />
    <h4>Description: {{destination.description}} </h4>
    <h4>Foods: {{destination.food}}</h4>
    <h4>landmarks: {{destination.landmarks}}</h4>
    <h4>Cost: {{destination.cost}}</h4>
    <h4>Country: {{destination.name}}</h4>
    <!-- <button @click='deletedestination(destination.id)' >Delete</button> -->
  </div>
  </div>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'http://localhost:8000'
export default {
  name: 'DestinationDetails',
  props: ['destination'],
  mounted(){
    // this.deletedestination()

  },
  methods:{
    
        //     async deletedestination(id){
        //     const response = await axios.delete(`${BASE_URL}/destinations/${id}`)
        //     console.log(response)
            
        // }
  
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
