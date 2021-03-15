import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from 'axios'
import VueClipboard from 'vue-clipboard2'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

Vue.config.productionTip = false;

// const host = window.location.protocol + "//" + window.location.hostname + ":8000";
const host = "";

const api = {
  get(url, authentication=true, defaultRoute="/api") {
    url = host + defaultRoute + url;

    if (store.state.token === '' && authentication) {
        return new Promise((resolve, reject) => {
            reject("No authorization token");
        });
    }

    var options = {
        url: url,
        method: 'get'
    }
    if (authentication) options.headers = { Authorization: `Bearer ${store.state.token}` }

    return axios(options);
  },

  post(url, data, authentication=true, defaultRoute="/api") {
    url = host + defaultRoute + url;

    if (store.state.token === '' && authentication) {
        return new Promise((resolve, reject) => {
          reject("No authorization token")
        });
    }

    var headers = {};
    if (authentication) headers = {Authorization: `Bearer ${store.state.token}`}

    return axios.post(url, data, {headers: headers});
  }
}

Vue.prototype.$api = api;

Vue.use(VueAwesomeSwiper, VueClipboard)

new Vue({
  router,
  store,
  vuetify,
  VueClipboard,
  render: h => h(App)
}).$mount("#app");
