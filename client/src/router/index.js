import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";
import Members from "@/views/Members.vue";
import Projects from "@/views/Projects.vue";
import Others from "@/views/Others.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard
    },
    {
        path: "/projetos",
        name: "Projects",
        component: Projects
    },
    {
        path: "/membros",
        name: "Members",
        component: Members
    },
    {
        path: "/outros",
        name: "Others",
        component: Others
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
