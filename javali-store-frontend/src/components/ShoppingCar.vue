<template>
  <div class="px-3 py-2">
    <b-list-group>
      <b-list-group-item class="d-flex justify-content-between align-items-center"
                         v-for="product in products"
                         :key="product.name">
        <div>{{ product.name }}</div>
        <small>
          {{ product.price }}
        </small>
        <b-badge variant="primary" pill>{{ product.quantity }}</b-badge>
      </b-list-group-item>
    </b-list-group>
    <div class="text-center"><h3>Total: ${{ total }}</h3></div>

    <b-button class="mt-4" v-b-modal.modal-1 variant="danger" block>Pagar</b-button>

    <b-modal id="modal-1" title="Confirmar compra" ok-title="Confirmar" @ok="pay" cancel-title="cancelar"
             no-close-on-esc>
      <p class="my-4">Por favor confirme su compra</p>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ShoppingCar",
  data() {
    return {
      //obtenemos los productos de la store vuex
      products: this.$store.state.products
    }
  },
  computed: {
    total() {
      if (this.products.length > 0) {
        return this.products.reduce((a, b) => a + b.price, 0);
      } else return 0;
    }
  }, methods: {
    pay() {
      const self = this;
      axios.post("http://127.0.0.1:8000/sale/", this.products, {
        auth: {
          username: 'javali',
          password: 'admin'
        }
      }).then(() => {
        self.toast()
      }).catch(() => {
        self.toast(true)
      })
    },
    toast(error) {
      console.log(error)
      const msg = error ? 'Ha ocurrido un error al finalizar su compra' : 'La compra se ha realizado con exito'
      this.$bvToast.toast(msg, {
        title: error ? 'Compra no finalizada' : 'Compra realizada',
        autoHideDelay: 5000,
        variant: !error ? 'success' : 'danger'
      })
    },
  }
}
</script>

<style scoped>

</style>
