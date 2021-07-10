<template>
  <div>
    <b-container>
      <div class="">
        <b-row>
          <b-col cols="6">
            <b-form id="form-sofi">
              <div class="form-group">
                <label for="name">Nombre:</label>
                <b-form-input v-model="product.name" class="form-control" type="text" name="nombre" id="name"
                              placeholder="Nombre" required></b-form-input>
              </div>

              <div class="form-group">
                <label for="desc">Cantidad:</label>
                <b-form-input v-model="product.description" class="form-control" type="text" name="nombre" id="desc"
                              placeholder="Cantidad" required></b-form-input>

              </div>

              <div class="form-group">
                <label for="price">Precio:</label>
                <b-form-input v-model="product.quantity" class="form-control" type="text" name="nombre" id="price"
                              placeholder="Precio" required></b-form-input>

              </div>
              <div class="form-group">
                <label for="cate">Categoria:</label>
                <b-form-input v-model="product.quantity" class="form-control" type="text" name="nombre" id="cate"
                              placeholder="Precio" required></b-form-input>

              </div>
              <div class="form-group">
                <label for="brand">Marca:</label>
                <b-form-input v-model="product.quantity" class="form-control" type="text" name="nombre" id="brand"
                              placeholder="Precio" required></b-form-input>

              </div>
              <div class="form-group">
                <label for="img">Imagen:</label>
                <b-form-input v-model="product.quantity" class="form-control" type="text" name="nombre" id="img"
                              placeholder="Precio" required></b-form-input>

              </div>
            </b-form>

          </b-col>

        </b-row>
      </div>
    </b-container>

  </div>
</template>

<script>

function Product() {
  this.name = "";
  this.quantity = "";
  this.price = "";
  this.category = "";
  this.brand = "";
}

export default {
  name: "ProductNew",
  data() {
    return {
      product: new Product()
    }
  }
}
</script>

<style scoped>

</style>
