<template>
    <div>
        <v-app-bar color="white" light>
            <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

            <v-toolbar-title class="title pl-10">
                <span class="font-weight-bold">Matos</span>
                <span class="font-weight-light">Planner</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>
            <!-- <v-btn icon class="" v-if="isAuthenticated" @click="$store.commit('logout')">
                    <v-icon>mdi-logout-variant</v-icon>
            </v-btn> -->
        </v-app-bar>
    </div>
</template>
<style>
    .title {
        color: #33395E;
    }
</style>
<script>
    export default {
        data(){
            return{
                isAuthenticated: true,
            }
        },
        methods: {

        },
    };
</script>

<style></style>
