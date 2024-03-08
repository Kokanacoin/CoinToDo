import { createRouter, createWebHashHistory } from "vue-router";

import EveryDay from '../components/todoMainPage/EveryDay.vue';
import Setting from '../components/todoMainPage/Setting.vue';
import DataStatistics from '../components/todoMainPage/DataStatistics.vue';
import todoMainPage from '../components/todoMainPage/todoMainPage.vue';


const router = createRouter({
    history: createWebHashHistory(),
    routes: [

        {
            path: '/todo', component: todoMainPage, name: 'TodoMainPage',
            redirect: "/todo/everyday",
            children: [
                { path: 'everyday', component: EveryDay, name: 'Everyday' },
                { path: 'setting', component: Setting, name: 'Setting' },
                { path: 'datastatistics', component: DataStatistics, name: 'DataStatistics' },
            ]
        },
    ]
});

export default router;