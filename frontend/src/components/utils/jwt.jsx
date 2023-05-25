import axios from "axios";

const checkAuth = async () => {
  const access_token = localStorage.getItem("token");
  const refresh_token = localStorage.getItem("refresh");

  await axios
    .post("http://localhost:8000/token/verify/", {
      token: access_token,
    })
    .then((res) => {
      console.log("res.data", res.response);
    })
    .catch((err) => console.log("err", err));
};

export default checkAuth;
