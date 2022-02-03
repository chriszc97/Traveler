import VueRouter from 'vue-router'
import Home from './pages/Home'
import MyTrip from './pages/MyTrip'
import TripDetails from './pages/TripDetails'

const routes = [
    {path: '/home', component: Home, name: 'Home'},
    {path: '/trip-details/:id', component: TripDetails, name: 'TripDetails', props: true},
    {path: '/my-trip', component: MyTrip, name: 'MyTrip', props: true}, 
]

export default new VueRouter({ routes, mode:'history'})