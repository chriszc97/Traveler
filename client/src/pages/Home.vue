<template>
    <div>
        <h1>Travel Posts</h1>
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