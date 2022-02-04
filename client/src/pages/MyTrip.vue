<template>
    <div>
        <h1>My new trips</h1>
        <div v-if="!country">
            <form v-on:submit="handleCountry">
                <label> Country </label>
                <input type="text"
                name = 'country'
                :value="country"
                placeholder="Country to remember"
                @change="handleCountry"
                />
                <button>Submit</button>
            </form>
        </div>
        <div v-if="country">
            <form v-on:submit="handleSubmitC">
                <label>Name</label> 
                <input type="text"
                name='name'
                :value="name"
                placeholder="Destination's name"
                @input="handleChange"
                /> <br>

                <label>Food</label>
                <input type="text"
                name='food'
                :value="food"
                placeholder="Food to remember"
                @input="handleChange"
                /> <br>

                <label>Photo</label>
                <input type="text"
                name='photo_url'
                :value="photo_url"
                placeholder="Photo url"
                @input="handleChange"
                /> <br>

                <label>Description</label>
                <textarea
                name='description'
                :value='description'
                @input="handleChange"
                /> <br>

                <label>Landmarks</label>
                <input type="text"
                name='landmarks'
                :value="landmarks"
                placeholder="Landmarks to remember"
                @input="handleChange"
                /> <br>

                <label>Cost</label>
                <input type="number"
                name='cost'
                :value="cost"
                placeholder="How much did I spent"
                @input="handleChange"
                /> <br>

                <button>Submit</button>
            </form>
        </div>
    </div> 
</template>




<script>

export default {
    name: 'MyTrip',
    props: {
    },
    components: {

    },
    data: () => ({
        newCountry: [],
        newDestination: [],
        country: '',
        destination: {
            name: '',
            food: '',
            photo_url: '',
            description: '',
            landmarks: '',
            cost: null,
        }
    }),
    mounted(){

    },
    methods: {
        handleSubmit(e){
            e.preventDefault()
            console.log(this.added)
            this.added.push(this.destination)
        },
        handleChange(e){
            this.destination[e.target.name] = e.target.value
        },
        handleCountry(e){
            this[e.target.name] = e.target.value
            console.log([e.target.value])
        },
        handleSubmitC(e){
        e.preventDefault()
        }
    }
}
</script>