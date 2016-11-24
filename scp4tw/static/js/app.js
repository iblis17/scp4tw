import Vue from 'vue'
import VueResource from 'vue-resource'

import 'bulma'  // css
import 'fa'

import App from './vue/App.vue'

Vue.use(VueResource)


const app = new Vue({
  el: '#app',
  render: h => h(App),
})
