<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <div class="d-flex justify-center align-center login-head">
                <h3>Smart Math</h3>
              </div>
              <v-card-text>
                <v-form>
                  <v-text-field
                    placeholder="Usuário"
                    name="username"
                    v-model="username"
                    prepend-inner-icon="mdi-account"
                    type="text"
                    solo
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    placeholder="Senha"
                    v-model="password"
                    name="password"
                    prepend-inner-icon="mdi-lock"
                    type="password"
                    solo
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn block color="primary" @click="login">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
<style>
  .login-head {
    height: 15vh;
  }
</style>
<script>
  import axios from "axios";
  export default {
    data() {
      return {
        username: null,
        password: null,
      };
    },
    created() {
      console.log(this.$api);
    },
    methods: {
      checkData() {
        return !this.username || !this.password;
      },
      login() {
        if(this.checkData()) return;
        const payload = { username: this.username, password: this.password };
        // http://" + window.location.hostname + ":8000
        axios.post("/api/auth/login", payload).then(result => {
          let data = result.data;

          if (data.message !== undefined) {
            this.message = data.message;
          } else if (data.token !== undefined) {
            this.$store.commit("setToken", data);
            this.$router.push("/");

            // localStorage.setItem("is_admin", data.is_admin);
          }
        });
      },
    },
  };
</script>
