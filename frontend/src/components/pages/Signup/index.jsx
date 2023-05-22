import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (password === password2) {
      try {
        await axios
          .post("http://localhost:8000/api/v1/profile/registration/", {
            username: username,
            password: password,
            password2: password2,
          })
          .then((res) => {
            console.log("res.data", res.data);
            setUsername("");
            setPassword("");
            setPassword2("");
          });

        await axios
          .post("http://localhost:8000/token/", {
            username: username,
            password: password,
          })
          .then((res) => {
            localStorage.setItem("token", res.data.access);
            localStorage.setItem("refresh", res.data.refresh);
            navigate("/main");
          });
      } catch (err) {
        console.log("registration error", err);
      }
    } else {
      setPasswordError("Password's didn't mutch");
    }
  };

  return (
    <div>
      <h1>Signup page</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Username</p>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label>
          <p>Password</p>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <label>
          <p>Repeat password</p>
          <input
            type="password"
            value={password2}
            onChange={(e) => setPassword2(e.target.value)}
          />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      {passwordError && <p>{passwordError}</p>}
    </div>
  );
};

export default Signup;
