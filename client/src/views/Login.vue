<template>
    <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
            <v-col cols="12" sm="8" md="4">
                <v-card class="elevation-12 pa-5">
                    <div class="d-flex justify-center align-center login-head">
                        <h3>Planner</h3>
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
                        <v-btn block class="block-primary" @click="login">Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
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
            if (this.$store.getters.authenticated) {
                this.$router.push("/dashboard");
            }
        },
        methods: {
            checkData() {
                return !this.username || !this.password;
            },
            login() {
                if(this.checkData()) return;

                const payload = { username: this.username, password: this.password };

                axios.post("/api/auth/login", payload).then(result => {
                    let data = result.data;

                    if (!data.success) {
                        this.message = data.message;
                    } else {
                        this.$store.commit("setToken", data);
                        this.$store.commit("setUser", data);
                        this.$router.push("/dashboard");
                    }
                });
            },
        },
    };
</script>
