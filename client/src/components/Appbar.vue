<template>
  <div v-if="!isGamePage()">
    <v-app-bar color="white" light>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

      <v-toolbar-title class="title pl-10"
        ><span class="font-weight-bold">Smart</span>
        <span class="font-weight-light">Math</span></v-toolbar-title
      >
      <v-spacer></v-spacer>
      <!-- <v-btn icon class="" v-if="isAuthenticated" @click="$store.commit('logout')">
        <v-icon>mdi-logout-variant</v-icon>
      </v-btn> -->
    </v-app-bar>
  </div>
</template>
<style>
  .title {
    color: #0077ff;
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
      isGamePage(){
        const path = this.$router.currentRoute.path
        return this.$router.currentRoute.name == "Game"
      },
      isRoomPage(){
        const path = this.$router.currentRoute.path
        return this.$router.currentRoute.path.includes("/turma")
      },
      navigateTabs(tab) {
        const path = this.$router.currentRoute.path
        if (tab !== path) return this.$router.push(tab);
      },
    },
  };
</script>

<style></style>
