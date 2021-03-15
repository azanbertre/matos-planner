<template>
    <div>
        <v-app-bar color="white" light>
            <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

            <v-toolbar-title class="title pl-10 text-primary" style="cursor: pointer;" @click="$router.push('/')">
                <span class="font-weight-bold">Matos</span>
                <span class="font-weight-light">Planner</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <template v-if="$store.getters.authenticated">
                <v-btn v-if="$route.path !== '/dashboard'" to="dashboard" class="block-primary mr-5">
                    Dashboard
                </v-btn>

                <span class="mr-2">Logado como {{ $store.getters.user.nickname }}</span>
                <v-btn icon @click="$store.commit('logout')">
                    <v-icon>mdi-logout-variant</v-icon>
                </v-btn>
            </template>
            <template v-else>
                <v-btn text class="text-primary" @click="login">
                    Login
                </v-btn>
            </template>

        </v-app-bar>
    </div>
</template>
<style>

</style>
<script>
    export default {
        data() {
            return {}
        },
        methods: {
            login() {
                if (this.$route.path === '/login') return;
                this.$router.push('/login');
            }
        },
    };
</script>

<style></style>
