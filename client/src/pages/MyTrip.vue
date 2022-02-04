<template>
  <div>
    <h1>My new trips</h1>
    <div v-if="!updated">
      <form @submit="handleSubmit">
        <label> Country </label>
        <input
          type="text"
          name="name"
          :value="name"
          placeholder="Country to remember"
          @input="handleCountry"
        />
        <br />

        <label> Photo </label>
        <input
          type="text"
          name="photo_url"
          :value="photo_url"
          placeholder="Photo Url"
          @input="handleCountry"
        />
        <br />
        <button>Submit</button>
      </form>
    </div>

    <div v-if="updated">
      <form  @submit="handleSubmitC">
        <div class="dest">
        <label>Name</label>
    
    
        <input
          type="text"
          name="name"
          :value="name"
          placeholder="Name"
          @input="handleChange"
        />
        <br />
      </div>

        <label>Good Eats </label>
        <input
          type="text"
          name="Food"
          :value="food"
          placeholder="Food"
          @input="handleChange"
        />
        <br />

        <label>Photo</label>
      
        <input
          type="text"
          name="photo_url"
          :value="photo_url"
          placeholder="URL"
          @input="handleChange"
        />
        <br />
      <div class="dest">
        <label className="description" >Description</label>
      
        <textarea
          name="description"
          :value="description"
          @input="handleChange"
        />
        <br />
      </div>
        <label>Things To Do</label>
        <input
          type="text"
          name="landmarks"
          :value="landmarks"
          placeholder="Landmarks, Activities, etc."
          @input="handleChange"
        />
        <br />

        <label>Average Cost</label>
        <input
          type="text"
          name="cost"
          :value="cost"
          placeholder="$$$"
          @input="handleChange"
        />
        <br />

        <button>Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const BASE_URL = "http://localhost:8000";
export default {
  name: "MyTrip",
  props: {
    id: null
  },
  components: {},

  data: () => ({
    currentCountry: '',
    updated: false,
    country: {
      name: "",
      photo_url: "",
    },
    destination: {
      name: "",
      food: "",
      photo_url: "",
      description: "",
      landmarks: "",
      cost: null,
      country_id: null,
    },
  }),
  methods: {
    async handleSubmit(e) {
      let payload = this.country
      e.preventDefault();
      const response = await axios.post(`${BASE_URL}/countries/`, payload)
      this.currentCountry = response.data
      this.currentCountry ? this.updated = true : null
      this.destination.country_id = this.currentCountry.id
      
    },
    handleChange(e) {
      this.destination[e.target.name] = e.target.value;
    },
    handleCountry(e) {
      this.country[e.target.name] = e.target.value;
    },
    async handleSubmitC(e) {
      let payload = this.destination
      e.preventDefault();
      await axios.post(`${BASE_URL}/destinations/`, payload);
      this.$router.push('/home')
    },
  },
};
</script>


<style scoped>
h1{
font-weight: 900;
font-size:40px;
}

label{
  font-size: 30px;
  padding: 20px;
  
  
}

input{
  font-size: 18px;
  border-radius: 1vh;
}

::placeholder{
  color:rgb(69, 202, 171);
  font-size: 0.8em;
  text-align: center;
}

.dest{
  display: flex;
  /* flex-direction: column; */
  justify-content:center;
  align-items: center;
}



button{
  margin-top: 50px;
  font-size: 24px;
  color:cornflowerblue;
  background-color: rgb(234, 255, 245);
  display: inline-block;
  border-radius: 1.4vh;
}


</style>
