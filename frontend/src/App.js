import "./App.css";
// import { useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./components/pages/Login";
import Signup from "./components/pages/Signup";
import Main from "./components/pages/Main";
import Profile from "./components/pages/Profile";
import ShoppingCart from "./components/pages/ShoppingCart";
import Book from "./components/pages/Book";
import Search from "./components/pages/Search";
import Header from "./components/ui/Header";

function App() {
  // const [token, setToken] = useState(localStorage.getItem("token")); // todo: change it

  return (
    <div className="App">
      <Header />
      <div className="body_wrapper">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/*" element={<Main />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/shopping-cart" element={<ShoppingCart />} />
          <Route path="/book/:book_id" element={<Book />} />
          <Route path="/book/search" element={<Search />} />
          <Route path="/main" element={<Navigate to={"/"} />} />
        </Routes>
      </div>
      <footer>Footer</footer>
    </div>
  );
}

export default App;
