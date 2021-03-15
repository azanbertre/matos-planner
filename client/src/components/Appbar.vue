<template>
    <div>
        <v-app-bar color="white" light>
            <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

            <v-toolbar-title class="title pl-10 text-primary">
                <span class="font-weight-bold">Matos</span>
                <span class="font-weight-light">Planner</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon v-if="$store.getters.authenticated" @click="$store.commit('logout')">
                <v-icon>mdi-logout-variant</v-icon>
            </v-btn>
            <v-btn text class="text-primary" v-else @click="login">
                Login
            </v-btn>

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
