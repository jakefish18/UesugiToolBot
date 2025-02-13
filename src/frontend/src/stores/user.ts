import { defineStore } from "pinia";
import axios from "axios";
import { UserProfile } from "@/types/user";
import { getUserProfile } from "@/api/userService";

export const useUserStore = defineStore("user", {
    state: () => ({
        user: {id: -1} as UserProfile,
        isLoggedIn: false
    }),

    actions: {
        async fetchUser() {
            try {
                const result = await getUserProfile();
                this.user = result;
                this.isLoggedIn = true;
            } catch (err) {
                console.log("User is not authorized, attempt failed.");
            }
        }
    },
})