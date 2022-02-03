<template>
    <div>
        <h1>this is Home</h1>
        <div class='post'>
            <DestinationPost :trip='trip' :key='trip.id' v-for='trip in trips'/>
        
        </div>
    </div>
    
</template>




<script>
import axios from 'axios'
import DestinationPost from '../components/DestinationoPost.vue'

const BASE_URL = 'http://localhost:8080'

export default {
    name: 'Home',
    components: {
        DestinationPost
    },
    data: () => ({
        trips: [
            {id: 1, name: 'Colombia', 
            photo_url: 'https://ivhq.imgix.net/images/hero/volunteer-in-colombia-with-world-leaders-ivhq.jpg?w=945&h=700&fit=crop&crop=faces,top&q=85&auto=format,compress',
            destinations: {
                name: 'Bogota',
                food: 'Chocolate con queso',
                photo_url: 'https://www.colombia-travels.com/wp-content/uploads/adobestock-266299444-1.jpeg',
                description:`Bogotá is Colombia’s sprawling, high-altitude capital. La Candelaria, its cobblestoned center, features colonial-era landmarks like the neoclassical performance hall Teatro Colón and the 17th-century Iglesia de San Francisco. It's also home to popular museums including the Museo Botero, showcasing Fernando Botero's art, and the Museo del Oro, displaying pre-Columbian gold pieces.`,
                landmarks: ['Zona G', 'Teatro Colon', 'Chorro del Quevedo', 'Monserrate'],
                cost: '$1,500',
            }
            }
        ],

    }),
    mounted(){

    },
    methods: {
        async getTrips(){
            const response = await axios.get(`${BASE_URL}/`)
            this.trips = response.data
        },
        selectTrip(id){
            this.$router.push(`/trip-details/${id}`)
        }
    }
}
</script>