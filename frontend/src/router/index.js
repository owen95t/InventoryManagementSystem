import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Item from '../views/adminView/Item'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {title: 'Home'}
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {title: 'About'}
  },
  {
    path: '/transfermenu',
    name: 'Transfer Menu',
    component: () => import('../views/TransferMenu'),
    meta: {title: 'Transfer Menu'}
  },
  {
    path: '/inventorymenu',
    name: 'Inventory Menu',
    component: () => import('../views/InventoryMenu'),
    meta: {title: 'Inventory Menu'}
  },
  {
    path: '/ordermenu',
    name: 'Order Menu',
    component: () => import('../views/OrderMenu'),
    meta :{ title: 'Order Menu'},
  },
  {
    path: '/customermenu',
    name: 'Customer Menu',
    component: () => import('../views/CustomerMenu'),
    meta: {title: 'Customer Menu'}
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin'),
    meta: {title: 'Admin Menu'}
  },
  {
    path: '/adminView/item',
    name: 'Item',
    component: Item,
    meta: {title: 'Item Edit'}
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

export default router
