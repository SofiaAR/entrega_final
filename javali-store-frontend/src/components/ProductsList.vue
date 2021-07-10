<template>
  <div>
    <b-container>
      <b-row>
        <b-col v-for="product in products" :key="product.name" cols="4">
          <div class="mb-2 mt-2">
            <b-card
                bg-variant="dark"
                :title="product.name"
                img-src="http://127.0.0.1:8000/images/"
                img-alt="Image"
                img-toppy
                tag="article"
                text-variant="white"
                style="max-width: 20rem;"
            >
              <b-card-text>
                {{ product.description }}
                <div>
                  $ {{ product.price }}
                </div>
                <div>
                  Uni. Disponibles: {{ product.quantity }}
                </div>
              </b-card-text>
              <div class="text-right">
                <b-button @click="addProduct(product)" :disabled="product.quantity === 0">Agregar al carro</b-button>
              </div>
            </b-card>

          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

function Product(data) {
  this.id = data.id;
  this.name = data.name;
  this.description = data.description;
  this.url = data.url;
  this.price = data.price;
  this.quantity = data.quantity;
}


export default {
  name: "ProductsList",
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      const self = this;
      axios.get("http://127.0.0.1:8000/products/", {
        auth: {
          username: 'javali',
          password: 'admin'
        }
      }).then(response => {
        response.data.forEach(p => {
          self.products.push(new Product(p))
        })
      })
    },
    addProduct(product) {
      product.quantity--;
      console.log(product)
      this.$store.commit('addProduct', product)
    }
  }
}
</script>

<style scoped>

</style>
