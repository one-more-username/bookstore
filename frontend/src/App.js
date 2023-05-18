import "./App.css";
import { useState } from "react";
// import axios from "axios";
import { Routes, Route, useNavigate } from "react-router-dom";

import Login from "./components/pages/Login";
import Signup from "./components/pages/Signup";
import Main from "./components/pages/Main";
import Profile from "./components/pages/Profile";
import ShoppingCart from "./components/pages/ShoppingCart";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token")); // todo: change it
  const navigate = useNavigate();

  const Redirect = () => {
    return (
      <>
        <h1>Register or log in please</h1>
        <button
          onClick={() => {
            navigate(`/login`);
          }}
        >
          Login
        </button>
      </>
    );
  };

  return (
    <div className="App">
      <Routes>
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/signup" element={<Signup setToken={setToken} />} />
        <Route path="/main" element={token ? <Main /> : <Redirect />} />
        {/* <Route path="/main" element={<Main />} /> */}
        <Route path="/profile" element={token ? <Profile /> : <Redirect />} />
        <Route
          path="/shopping-cart"
          element={token ? <ShoppingCart /> : <Redirect />}
        />
      </Routes>
    </div>
  );
}

export default App;
