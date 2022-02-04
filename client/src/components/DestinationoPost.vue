<template>
  <div class="post" @click="selectTheTrip(trip.id)">   
    <h2>{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
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
<<<<<<< HEAD
  margin: 10px;
  font-size: 30px;
=======
  font-weight: bold;
  margin: 20px;
>>>>>>> c9cc9b1955f6c173bd43fb6eec40cb034fbafb08
  padding: 0;
  color: rgb(1, 10, 9);
}
img{

}
<<<<<<< HEAD

=======
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
>>>>>>> c9cc9b1955f6c173bd43fb6eec40cb034fbafb08
img{
  max-width: 400px;
  max-height: 480px;
  margin: auto;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding:  0;
}

</style>
