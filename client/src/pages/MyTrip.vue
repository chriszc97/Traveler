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
      <form @submit="handleSubmitC">
        <label>Name</label>
        <input
          type="text"
          name="name"
          :value="name"
          placeholder="Destination's name"
          @input="handleChange"
        />
        <br />

        <label>Food</label>
        <input
          type="text"
          name="food"
          :value="food"
          placeholder="Food to remember"
          @input="handleChange"
        />
        <br />

        <label>Photo</label>
        <input
          type="text"
          name="photo_url"
          :value="photo_url"
          placeholder="Photo url"
          @input="handleChange"
        />
        <br />

        <label>Description</label>
        <textarea
          name="description"
          :value="description"
          @input="handleChange"
        />
        <br />

        <label>Landmarks</label>
        <input
          type="text"
          name="landmarks"
          :value="landmarks"
          placeholder="Landmarks to remember"
          @input="handleChange"
        />
        <br />

        <label>Cost</label>
        <input
          type="text"
          name="cost"
          :value="cost"
          placeholder="How much did I spent"
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
  props: {},
  components: {},
  data: () => ({
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
      country: 1,
    },
  }),
  methods: {
    async handleSubmit(e, country) {
      e.preventDefault();
      this.updated = true;
      await axios.post(`${BASE_URL}/countries/`, {
        country,
      });
    },
    handleChange(e) {
      this.destination[e.target.name] = e.target.value;
    },
    handleCountry(e) {
      this.country[e.target.name] = e.target.value;
    },
    async handleSubmitC(e, destination) {
      e.preventDefault();
      await axios.post(`${BASE_URL}/destinations/`, {
        destination,
      });
    },
  },
};
</script>