<template>
  <div>
    <h1>Add a New Trip</h1>
    <div v-if="!updated">
      <form @submit="handleSubmit">
        <label> Country </label>
        <input class='textbox'
          type="text"
          name="name"
          :value="name"
          placeholder="Type Here"
          @input="handleCountry"
        />
        <br />

        <label> Photo </label>
        <input class='textbox'
          type="text"
          name="photo_url"
          :value="photo_url"
          placeholder="URL"
          @input="handleCountry"
        />
        <br />
        <button>Submit</button>
      </form>
    </div>

    <div v-if="updated">
      <form @submit="handleSubmitC">
        <label>Destination</label>
        <input
          type="text"
          name="name"
          :value="name"
          placeholder="Name"
          @input="handleChange"
        />
        <br />

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

        <label>Description</label>
        <textarea
          name="description"
          :value="description"
          @input="handleChange"
        />
        <br />

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

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

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
      country_id: 1
    },
  }),
  methods: {
    async handleSubmit(e) {
        let payload = this.country
      e.preventDefault();
      this.updated = true;
      await axios.post(`${BASE_URL}/countries/`, payload);
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
    },
  },
};
</script>
