import { createApp } from 'vue'
import Antd from 'ant-design-vue';
import App from './App.vue'
import router from './router/router'
import 'ant-design-vue/dist/antd.css';
import store from './vuex/store'


const app = createApp(App);
app.use(router);
app.use(store);
app.config.productionTip = false;
app.use(Antd).mount("#app");