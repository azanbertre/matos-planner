<template>
    <v-app>
        <Appbar/>
        <v-main>
            <router-view />
            <snack-bar/>
        </v-main>
    </v-app>
</template>

<script>
import Appbar from "@/components/Appbar.vue"
import SnackBar from "@/components/SnackBar.vue"
import './static/main.css'

export default {
    name: "App",

    components: {
        Appbar,
        SnackBar
    },

    computed: {
        authenticated() {
            return this.$store.getters.authenticated;
        },
    },

    watch: {
        authenticated() {
            if (!this.authenticated) {
                this.$router.replace("/");
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
            this.$router.push("/");
        }
    },

    data: () => ({
        //
    })
};
</script>
