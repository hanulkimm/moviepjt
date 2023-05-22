import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MiddleMapView from '../views/MiddleMapView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import UserSignUpView from '../views/UserSignUpView.vue'
import UserLoginView from'../views/UserLoginView.vue'
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
    path: '/signup',
    name: 'signup',
    component: UserSignUpView
  },
  {
    path: '/login',
    name: 'login',
    component : UserLoginView
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
