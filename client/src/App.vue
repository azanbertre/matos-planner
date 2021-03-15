<template>
    <v-app>
        <Appbar/>
        <v-main>
            <router-view />
        </v-main>
    </v-app>
</template>

<script>
import Appbar from "@/components/Appbar.vue"
import './static/main.css'
export default {
    name: "App",

    components: {
        Appbar
    },

    computed: {
        authenticated() {
            return this.$store.getters.token !== '';
        },
    },

    watch: {
        authenticated() {
            if (!this.authenticated) {
                this.$router.replace("/login");
            }
        }
    },

    mounted() {
            this.checkAuth();
    },

    methods: {
        checkAuth(){
            this.$store.dispatch('refresh');
        },
        logout() {
            this.$store.commit('logout');
            this.$router.push("/login");
        }
    },

    data: () => ({
        //
    })
};
</script>
