import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'

import {BootstrapVueIcons} from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'

Vue.use(BootstrapVueIcons)
Vue.config.productionTip = false

import {store} from "./store"

import Vuex from 'vuex'

Vue.use(Vuex)

new Vue({
    store,
    render: h => h(App),
}).$mount('#app')
