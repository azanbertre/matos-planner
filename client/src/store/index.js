import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: localStorage.getItem("token") || '',
    refresh_token: localStorage.getItem("refreshToken") || '',
    user: JSON.parse(localStorage.getItem("user")) || {}
  },
  mutations: {
    setToken(state, data) {
      state.token = data.token;
      if (data.refresh_token !== undefined){
        state.refresh_token = data.refresh_token;
        localStorage.setItem("refreshToken", data.refresh_token);
      }
      localStorage.setItem("token", data.token);
    },
    setUser(state, data) {
      state.user = data.user;
      localStorage.setItem("user", JSON.stringify(data.user));
    },
    logout(state) {
      state.token = '';
      localStorage.setItem("token", '');
      localStorage.setItem("user", {});
    }
  },
  getters: {
    token(state) {
      return state.token;
    },
    user(state) {
      return state.user;
    }
  },
  actions: {
    refresh(store) {
      // window.location.protocol + "//" + window.location.hostname + ":8000
      axios.get("/api/auth/refresh",
        { headers: { Authorization: `Bearer ${store.state.refresh_token}` } }).then(result => {
          if ("refresh check", result.data.success) {
            store.commit('setToken', result.data);
            store.commit('setUser', result.data);
          } else {
            store.commit('logout');
          }
        }).catch(error => {
          store.commit("logout");
        });
    },
  }
});


export default store;
