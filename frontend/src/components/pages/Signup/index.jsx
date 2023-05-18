import React, { useState } from "react";
import axios from "axios";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const [passwordError, setPasswordError] = useState("");

  const createToken = async (e) => {
    // e.preventDefault();
    try {
      await axios
        .post("http://localhost:8000/token/", {
          username: username,
          password: password,
        })
        .then((res) => {
          localStorage.setItem("token", res.data.access);
          localStorage.setItem("refresh", res.data.refresh);
        });
    } catch (err) {
      console.log("err", err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === password2) {
      try {
        await axios
          .post("http://localhost:8000/api/v1/profile/registration/", {
            username: username,
            password: password,
            password2: password2,
          })
          .then((res) => {
            createToken();
            // console.log("res.data", res.data);
            setUsername("");
            setPassword("");
            setPassword2("");
            // and then redirect to the main page
          });
      } catch (err) {
        console.log("err", err);
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
