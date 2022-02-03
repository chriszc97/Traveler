<template>
  <div class="post" @click="selectTheTrip(trip.id)">   
    <h2>Name:{{trip.name}} </h2> 
    <img :src='trip.photo_url' alt="" />
    <p>description: {{trip.description}}</p>
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
    click(){
      console.log('hello')
    }

  }
}



</script>


<style >
h2{
  margin: 0;
  padding: 0;
}
.post{
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  background-color: #25464b;
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
