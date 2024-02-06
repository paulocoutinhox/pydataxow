import { createWebHistory, createRouter } from "vue-router";

import Home from '@/components/Home'
import About from '@/components/About'
import NotFound from '@/components/NotFound'

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/index.html",
        name: "Home",
        component: Home,
    },
    {
        path: "/about",
        name: "About",
        component: About,
    },
    {
        path: "/:catchAll(.*)",
        component: NotFound,
    },
];

const base = process.env.NODE_ENV === 'production' ? '/panel/' : '/';

const router = createRouter({
    history: createWebHistory(base),
    routes,
});

export default router;
