import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import ShopView from "../views/ShopView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/shop",
    name: "Shop",
    component: ShopView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
