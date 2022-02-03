<template>
  <div class="post">   
    <h2>Name: </h2> 
    <img :src= "url" alt="" />
    <p>description: </p>
  </div>

</template>

<script>

export default{
  name: 'DestinationPost'
}


</script>


<style >
.post{
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  background-color: #25464b;
  cursor: pointer;
  transition: all 0.2s;
  color: black 
}

</style>
