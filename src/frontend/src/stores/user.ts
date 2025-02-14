import { defineStore } from "pinia";
import axios from "axios";
import { UserProfile } from "@/types/user";
import { getUserProfile } from "@/api/userService";
import {reactive} from "vue";

export const useUserStore = defineStore("user", {
    state: () => ({
        id: -1,
        isLoggedIn: false
    }),

    actions: {
        async fetchUser() {
            try {
                const result = await getUserProfile();
                this.id = result.id;
                this.isLoggedIn = true;
            } catch (err) {
                console.log("User is not authorized, attempt failed.");
            }
        }
    },
})