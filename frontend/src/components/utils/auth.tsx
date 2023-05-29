import { createAuthProvider } from "react-token-auth";

type Session = { access: string; refresh: string };

export const { useAuth, authFetch, login, logout } =
  createAuthProvider<Session>({
    getAccessToken: (session) => session.access,
    storage: localStorage,
    onUpdateToken: (token) =>
      fetch("/token/refresh/", {
        method: "POST",
        body: token.refresh,
      }).then((r) => r.json()),
  });
