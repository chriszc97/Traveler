<template>
  <div class="post" @click="selectTheTrip(trip.id)">   
    <h2>Name:{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
    <h3>Location: {{trip.destinations.name}}</h3>
  </div>

</template>

<script>

export default{
  name: 'DestinationPost',
  props: ['trip'],
  methods: {
    selectTheTrip(){
      this.$emit('selectTrip', this.trip.id)
    },
  },

}



</script>


<style >
h2{
  font-weight: bold;
  margin: 20px;
  padding: 0;
  color: rgb(1, 10, 9);
}
img{

}
.post{
  display: grid;
  padding: 50px;
 
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  background-color: rgb(225, 236, 233);
  border: 3px solid rgb(35, 95, 85);
  border-radius: 0.9vh;

  cursor: pointer;
  transition: all 0.2s;
  color: black 
}
img{
    max-width: 300px;
  max-height: 380px;
  margin: auto;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding:  0;
}

</style>
