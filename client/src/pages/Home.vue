<template>
    <div>
        <h1>Explore by Country</h1>
        <div class='post'>
            <DestinationPost :trip='trip' :key='trip.id' v-for='trip in trips' @selectTrip="selectTrip"/>
        
    </div> 
    </div>
    
</template>




<script>
import axios from 'axios'
import DestinationPost from '../components/DestinationoPost.vue'

const BASE_URL = 'http://localhost:8000'


export default {
    name: 'Home',
    components: {
        DestinationPost
    },
    data: () => ({
        trips: [],
        trip: {}

    }),
    mounted(){
        this.getTrips()
        // this.getTrip()
    },
    methods: {
        async getTrips(){
            const response = await axios.get(`${BASE_URL}/countries`)
            this.trips = response.data
        },
        selectTrip(id){
            this.$router.push(`/trip-details/${id}`)
        },
        // async getTrip(id){
        //     const response = await axios.get(`${BASE_URL}/destinations/${id}`)
        //     this.trip = response.data
        // },
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@100;400&display=swap');

h1 {
    margin-top: 70px;
    margin-bottom: 70px;
}
.post {
  display: grid;
  gap: 20px;
  grid-row: 1/3;
  background-color:white
}

</style>