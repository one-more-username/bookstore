import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./styles.scss";

const Main = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const token = localStorage.getItem("token");
  // const refresh = localStorage.getItem("refresh");

  const navigate = useNavigate();

  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  useEffect(() => {
    const getData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/v1/book/random/"
        );
        setData(response.data);
        setError(null);
      } catch (err) {
        setError(err.message);
        setData(null);
      } finally {
        setLoading(false);
      }
    };
    getData();
  }, []);

  const handleClick = (book_id) => {
    navigate(`/book/${book_id}`);
  };

  const addToFavouritesHandler = async (book_id) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/book/${book_id}/add-favourite/`,
        config
      );
      console.log("response.data", response.data);
    } catch (err) {
      console.log("error", err);
    }
  };

  const addToShoppingCartHandler = async (book_id) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/shopping-cart/add-book/${book_id}/`,
        config
      );
      console.log("response.data", response.data);
    } catch (err) {
      console.log("error", err);
    }
  };

  return (
    <div className="main_wrapper">
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
          <button onClick={() => navigate("/login")}>Go to login page</button>
          <p>or</p>
          <button onClick={() => navigate("/signup")}>Go to signup page</button>
        </>
      )}
      {data && (
        <div className="books_wrapper">
          {data.map((item, index) => (
            <div
              onClick={() => handleClick(item.id)}
              className="book_wrapper"
              key={`key_${index}`}
            >
              <h3>Title: {item.title}</h3>
              <img src={item.image} alt="book cover" />
              <p>Price: {item.price} rub</p>
              <p>Author: {item.author}</p>
              <p>Reviews: {item.reviews_quantity}</p>
              <button
                type="button"
                // disabled={item.is_favourite}
                onClick={(e) => {
                  e.stopPropagation();
                  addToFavouritesHandler(item.id);
                }}
              >
                Add to favourites
              </button>
              <button
                type="button"
                // disabled={item.is_favourite}
                onClick={(e) => {
                  e.stopPropagation();
                  addToShoppingCartHandler(item.id);
                }}
              >
                Add to shopping cart
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Main;
