<template>
    <div>
        <h1>this is Home</h1>
        <div :key="e.id" v-for="e in trips">
            <div @click="selectTrip(e.id)">
                <div>
                    <img :src="e.photo_url" :alt="e.name" width="500px">
                </div>
                <div>
                    <h3>{{e.name}}</h3>
                </div>
            </div>
        </div>
    </div> 
    
</template>




<script>
import axios from 'axios'

const BASE_URL = 'http://localhost:8000'


export default {
    name: 'Home',
    components: {},
    data: () => ({
        trips: [],

    }),
    mounted(){
        this.getTrips()
    },
    methods: {
        async getTrips(){
            const response = await axios.get(`${BASE_URL}/countries/?format=json`)
            this.trips = response.data
        },
        selectTrip(id){
            this.$router.push(`/trip-details/${id}`)
        }
    }
}
</script>