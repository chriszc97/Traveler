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
    font-weight: bold;
    justify-content: space-evenly;
    gap: 10px;
    margin: 20px 0 0 ;
    padding: 10px 0;
    background-color: rgb(118, 177, 164);
    border:0;
    margin: 0;
    border-radius: 2vh;
    /* font-color: black */
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