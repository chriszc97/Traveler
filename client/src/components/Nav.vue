<template>
  <nav class='nav'>
    <router-link to='/home'>Home</router-link>
    <router-link to='/post'>Post</router-link>
  </nav>
</template>

<script>
export default{
  name: 'Nav'
}
</script>


<style scoped >
  .nav{
    justify-content: space-evenly;
    gap: 10px;
    margin: 20px 0 0 ;
    padding: 10px 0;
  }

  
</style>