<template>
    <div>
        <DestinationDetails :trip='trip' :key='trip.id' :destination='destination' @deleteDestination='deleteDestination'  />
    </div> 
</template>



<script>
import axios from 'axios'

const BASE_URL = 'http://localhost:8000'

import DestinationDetails from '../components/DestinationDetails.vue'
export default {
    name: 'MyTrip',
    props: {
        id: null
    },    
    components: {
        DestinationDetails
    },
    data: () => ({
        trip: {},
        destination: []
    }),
    mounted(){
        this.getTrip()
    },
    methods: {
        async getTrip(){
            const response = await axios.get(`${BASE_URL}/countries/${this.id}`)
            this.trip = response.data
            console.log(this.trip)
            for(let i =0;i<this.trip.destinations.length;i++){
                let res = await axios.get(`${this.trip.destinations[i]}`)
                this.destination.push(res.data)
            }
        },
        async deleteDestination(id){
            const response = await axios.delete(`${BASE_URL}/destinations/${id}`)
            console.log(response)
            
        }
    }
}
</script>
