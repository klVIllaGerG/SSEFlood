import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";

const app = createApp(App)


axios.defaults.baseURL = 'http://114.55.246.213:8080'

app.use(createPinia())
app.use(router)

app.mount('#app')
