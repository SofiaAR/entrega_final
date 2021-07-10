<template>
  <div>
    <h1>Contacto</h1>
    <b-container>
      <b-row>
        <b-col cols="6">
          <b-form id="form-sofi">
            <div class="form-group">
              <label for="name">Nombre:</label>
              <b-form-input v-model="form.name" class="form-control" type="text" name="nombre" id="name"
                            placeholder="Ingresa tu nombre" required :state="name"></b-form-input>
              <b-form-invalid-feedback :state="name">
              </b-form-invalid-feedback>
            </div>
            <div class="form-group">
              <label for="mail" class="font-weight-bold">Email:</label>
              <!--font-weight-bold = negrita-->
              <b-form-input v-model="form.email" class="form-control" type="text" name="mail" id="mail"
                            placeholder="Ingresa tu correo" :state="email"/>
            </div>
            <div class="form-group">
              <label for="msg" class="font-weight-bold">RUT:</label>
              <!--font-weight-bold = negrita-->
              <b-form-textarea v-model="form.message" class="form-control" type="text" name="msg" id="msg" rows="5"
                               placeholder="Dejanos tu mensaje" :state="msg"/>
            </div>
            <!--Botones-->
            <div class="form-group">
              <b-button variant="secondary" @click="save">Button</b-button>
            </div>
          </b-form>
        </b-col>
        <b-col cols="6">
          <b-img src="@/assets/Sin título-1-01.png/" width="500"></b-img>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

function Form() {
  this.message = '';
  this.name = '';
  this.email = '';
}

export default {
  name: "Contact",
  data() {
    return {
      form: new Form(),
    }
  },
  computed: {
    name() {
      return this.form && this.form.name !== '';
    },
    email() {
      return this.form && this.form.email !== '';
    },
    msg() {
      return this.form && this.form.message !== '';
    },
  },
  methods: {
    save() {
      const self = this;
      this.form.created = new Date().toISOString();
      axios.post("http://127.0.0.1:8000/contact/", this.form, {
        auth: {
          username: 'javali',
          password: 'admin'
        }
      }).then(() => {
        self.toast()
      }).catch(() => {
        self.toast(true)
      }).finally(() => {
        self.form = new Form();
      })
    },
    toast(error) {
      console.log(error)
      const msg = error ? 'Ha ocurrido un error al enviar su mensaje' : 'El mensaje se ha enviado con exito'
      this.$bvToast.toast(msg, {
        title: error ? 'Mensaje no enviado' : 'Mensaje Enviado',
        autoHideDelay: 5000,
        variant: !error ? 'success' : 'danger'
      })
    }

  }
}
</script>

<style scoped>

</style>
