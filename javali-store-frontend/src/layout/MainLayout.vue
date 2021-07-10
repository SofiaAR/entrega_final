<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="#">Javali Store</b-navbar-brand>
      <b-button v-b-toggle.sidebar-right>
        <b-icon icon="cart2" variant="warning"></b-icon>
        Ver carro {{ products.length }}
      </b-button>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>

        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item @click="content = 'home'">Home</b-nav-item>
          <b-nav-item @click="content = 'products'">Productos</b-nav-item>
          <b-nav-item @click="content = 'product'">Nuevo Producto</b-nav-item>
          <b-nav-item @click="content = 'contact'">Contacto</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <b-container :fluid="true">
      <b-row>
        <b-col cols="12">
          <ProductsList v-if="content === 'products'"/>
          <Contact v-if="content === 'contact'"/>
          <Gallery v-if="content === 'gallery'"/>
          <Home v-if="content === 'home'"/>
          <ProductNew v-if="content === 'product'"/>
        </b-col>
      </b-row>

    </b-container>

    <div>

      <b-sidebar id="sidebar-right" title="Carro de compra" right shadow>
        <ShoppingCar/>
      </b-sidebar>
    </div>
  </div>
</template>

<script>
import ProductsList from "../components/ProductsList";
import Contact from "../components/Contact";
import Gallery from "../components/Gallery";
import Home from "../components/Home";
import ShoppingCar from "../components/ShoppingCar";
import axios from "axios";
import ProductNew from "../components/ProductNew";


export default {
  name: "MainLayout",
  components: {ProductNew, ShoppingCar, Home, Gallery, Contact, ProductsList},
  data() {
    return {
      //obtenemos los productos de la store vuex
      products: this.$store.state.products,
      content: 'products',
      store: null
    }
  }, mounted() {
    const self = this;
    axios.get("http://127.0.0.1:8000/store/", {
      auth: {
        username: 'javali',
        password: 'admin'
      }
    }).then(response => {
      self.store = response.data;
    })
  }
}
</script>

<style scoped>

</style>
