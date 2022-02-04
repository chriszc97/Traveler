<template>
    <div>
        <DestinationDetails :trip='trip' :key='trip.id'/>
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
    }),
    mounted(){
        this.getTrip()
    },
    methods: {
        async getTrip(){
            const response = await axios.get(`${BASE_URL}/destinations/${this.id}`)
            this.trip = response.data
        },
        // async deleteTrip(){
        //     const response = await axios.delete(`${BASE_URL}/destinations/${this.id}`)
        // }
    }
}
</script>

<style scoped>
    div{
        height: 100%;
        bottom: 0
    }
</style>