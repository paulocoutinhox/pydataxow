import { createRouter, createWebHistory } from "vue-router";

import AboutPage from '@/components/AboutPage';
import HomePage from '@/components/HomePage';
import NotFoundPage from '@/components/NotFoundPage';

const routes = [
    {
        path: "/",
        name: "Home",
        component: HomePage,
    },
    {
        path: "/about",
        name: "About",
        component: AboutPage,
    },
    {
        path: "/:catchAll(.*)",
        component: NotFoundPage,
    },
];

const base = process.env.NODE_ENV === 'production' ? '/panel/' : '/';

const router = createRouter({
    history: createWebHistory(base),
    routes,
});

export default router;
