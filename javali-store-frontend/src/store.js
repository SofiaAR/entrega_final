import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        count: 0,
        products: []
    },
    mutations: {
        addProduct(state, value) {
            state.products.push(value)
        }
    }
})
