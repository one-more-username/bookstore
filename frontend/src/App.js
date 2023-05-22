import "./App.css";
import { useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./components/pages/Login";
import Signup from "./components/pages/Signup";
import Main from "./components/pages/Main";
import Profile from "./components/pages/Profile";
import ShoppingCart from "./components/pages/ShoppingCart";
import Book from "./components/pages/Book";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token")); // todo: change it
  const [bookID, setBookID] = useState(null);

  return (
    <div className="App">
      <header>Header</header>
      <Routes>
        <Route path="/login" element={<Login setToken={setToken} />} />
        <Route path="/signup" element={<Signup setToken={setToken} />} />
        <Route
          path="*"
          element={<Main />}
          // element={<Main bookID={bookID} setBookID={setBookID} />}
        />
        <Route path="/profile" element={<Profile />} />
        <Route path="/shopping-cart" element={<ShoppingCart />} />
        {/* <Route path="/book/*" element={<Book book_id={bookID} />} /> */}
        <Route path="/main" element={<Navigate to={"/"} />} />
      </Routes>
      <footer>Footer</footer>
    </div>
  );
}

export default App;
