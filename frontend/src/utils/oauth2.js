export function generateOAuth2URL() {
  const baseAuthURL = "https://access.line.me/oauth2/v2.1/authorize";

  const params = {
    response_type: "code",
    client_id: "2006588655",
    redirect_uri: "http://localhost:3000/callback",
    state: generateRandomState(),
    scope: "profile openid",
  };

  return `${baseAuthURL}?${new URLSearchParams(params).toString()}`;
}

function generateRandomState() {
  return [...Array(16)]
    .map(() => Math.random().toString(36)[2])
    .join("");
}
