<template>
  <nav class='nav'>
    <router-link class='link' to='/home'>Home</router-link>
    <router-link class='link' to='/post'>Post</router-link>
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
    justify-content: space-evenly;
    gap: 10px;
    margin: 20px 0 0 ;
    padding: 10px 0;
    background-color: rgb(91, 77, 114);
    border:0;
    margin: 0;
    /* font-color: black */
    
    
  }
  .link{
    text-decoration: none;
    color: black;
    /* border: 3px solid black; */
    
  }


  
</style>