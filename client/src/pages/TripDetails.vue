<template>
    <div>
        <h1>My trip to {{this.trips[0].name}}</h1>
        <div>
            <div>
                <img :src="this.trips[0].photo_url" :alt="this.trips[0].name" width="500px">
            </div>
            <div>
                <h2>Destinations:</h2>
                <div>
                    <h4>{{this.trips[0].destinations.name}}</h4>
                    <img :src="this.trips[0].destinations.photo_url" :alt="this.trips[0].destinations.name" width="450px">
                    <h5>Amount spent: {{this.trips[0].destinations.cost}}</h5>
                    <p>{{this.trips[0].destinations.description}}</p>
                    <div :key="e" v-for="e in trips[0].destinations.landmarks">
                        <h5> {{e}} </h5>
                    </div>
                    
                </div>
                
            </div>
        </div>
    </div> 
</template>




<script>
export default {
    name: 'MyTrip',
    props: {
        id: null
    },    
    components: {},
    data: () => ({
        trips: [
            {id: 1, name: 'Colombia', photo_url: 'https://ivhq.imgix.net/images/hero/volunteer-in-colombia-with-world-leaders-ivhq.jpg?w=945&h=700&fit=crop&crop=faces,top&q=85&auto=format,compress',
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

    }
}
</script>