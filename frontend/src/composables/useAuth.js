import { generateOAuth2URL } from "@/utils/oauth2";

export function useAuth() {
  function login() {
    const oauth2URL = generateOAuth2URL();
    window.location.href = oauth2URL;
  }

  return {
    login,
  };
}
