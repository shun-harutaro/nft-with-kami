import { defineStore } from "pinia";
import apiAxios from "@/plugin/axios";

export const useUserProfileStore = defineStore("userProfile", {
  state: () => ({
    isLoggedIn: false,
    displayName: "",
    profileImageUrl: "",
  }),
  actions: {
    async fetchUserProfile() {
      try {
        const response = await apiAxios.get("/api/users/me/profile");
        this.isLoggedIn = true;
        this.displayName = response.data.name;
        this.profileImageUrl = response.data.picture;
      } catch (error) {
        this.isLoggedIn = false;
        console.error("Failed to fetch user profile:", error);
      }
    },
    logout() {
      this.isLoggedIn = false;
      this.displayName = "";
      this.profileImageUrl = "";
    },
  },
});
