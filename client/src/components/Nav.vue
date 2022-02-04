<template>
  <nav class='nav'>
    <router-link class='link' to='/home'>Home</router-link>
    <router-link class='link' to='/my-trip'>Post</router-link>
  </nav>
</template>

<script>
export default{
  name: 'Nav'
}
</script>


<style scoped >
  .nav{
    display: flex;
    font-size:30px;
    justify-content: space-evenly;
    gap: 10px;
    padding: 10px;
    background-color: rgb(118, 177, 164);
    border-radius: 2vh;
  }

   .nav:hover{
    background-color:  rgb(176, 238, 225);
    text-shadow: 1px 1px 2px white;
    border-radius: 2vh;
    }

  .link{
    text-decoration: none;
    color: black;
    /* border: 3px solid black; */
    
  }


  
</style>