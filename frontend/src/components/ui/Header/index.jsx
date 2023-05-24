import React from "react";
import { useNavigate } from "react-router-dom";
import "./styles.scss";

const Header = () => {
  const navigate = useNavigate();

  return (
    <header className="header">
      <h1>Bookstore</h1>
      <div className="buttons">
        <button type="button" onClick={() => navigate("/main")}>
          Main
        </button>
        <button type="button" onClick={() => navigate("/profile")}>
          Profile
        </button>
        <button type="button" onClick={() => navigate("/shopping-cart")}>
          Shopping cart
        </button>
        <button type="button" onClick={() => navigate("/book/search")}>
          Search
        </button>
      </div>
    </header>
  );
};

export default Header;
