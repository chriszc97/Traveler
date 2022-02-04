<template>
<div>
  <div class="post" @click="selectTheTrip(trip.id)">   
    <h2>{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
  </div>
  <div>
    <button @click="deleteTrip(trip.id)">Delete</button>
  </div>
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
    deleteTrip(id){
      this.$emit('deleteTrip', id)
    }
  },

}



</script>


<style >
h2{
  margin: 10px;
  font-size: 30px;
  padding: 0;
  color: rgb(1, 10, 9);
}


img{
  max-width: 400px;
  max-height: 480px;
  margin: auto;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding:  0;
}

</style>
