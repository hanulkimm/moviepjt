import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MiddleMapView from '../views/MiddleMapView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import UserRegisterView from '../views/UserRegisterView.vue'
import MainView from '../views/MainView.vue'
import 'maphilight'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'main',
    children:[
      {
        path: '/home',
        name: 'home',
        component: HomeView
      },
      {
        path: '/:region',
        name: 'region',
        component: MiddleMapView
      },
      {
        path: '/:region/:movie_pk',
        name: 'movie',
        component: MovieDetailView
      },

    ],
    component: MainView
  },
  {
    path: '/login',
    name: 'login',
    component: UserRegisterView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
