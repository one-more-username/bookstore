import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Snackbar } from "@mui/material";
import "./styles.scss";

const ShoppingCart = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [totalPrice, setTotalPrice] = useState(0);
  const [sbOpen, setSbOpen] = useState(false);
  const [sbMessage, setSbMessage] = useState("");

  const token = localStorage.getItem("token");

  const snackBarHandleClose = (e, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setSbOpen(false);
  };

  const navigate = useNavigate();

  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  const calculateTotalPrice = (arr) => {
    let result = 0;
    arr.map((item) => (result += item.price));
    return result;
  };

  useEffect(() => {
    const getData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/v1/shopping-cart/",
          config
        );
        setData(response.data.books_to_purchase);
        setTotalPrice(calculateTotalPrice(response.data.books_to_purchase));
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

  const removeFromShoppingCartHandler = async (book_id) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/shopping-cart/remove-book/${book_id}/`,
        config
      );
      setData(response.data.books_to_purchase);
      setError(null);
    } catch (err) {
      setError(err.message);
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  const makePurchaseHandler = async (e) => {
    e.stopPropagation();

    try {
      const response = await axios.get(
        "http://localhost:8000/api/v1/shopping-cart/buy/",
        config
      );
      console.log("response.data", response.data);
      setData([]);
      setTotalPrice(0);
    } catch (err) {
      console.log("err", err);
    }
  };

  const handleClick = (book_id) => {
    navigate(`/book/${book_id}`);
  };

  return (
    <>
      <Snackbar
        anchorOrigin={{
          vertical: "top",
          horizontal: "center",
        }}
        open={sbOpen}
        autoHideDuration={2500}
        onClose={snackBarHandleClose}
        message={sbMessage}
      />
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
        </>
      )}
      {data && (
        <>
          <h2>Your shopping cart</h2>
          <p>Total price for current purchase: {totalPrice} rub</p>
          <button
            type="button"
            disabled={!data.length}
            onClick={(e) => {
              makePurchaseHandler(e);
              setSbMessage("Purchase successful");
              setSbOpen(true);
            }}
          >
            Make a purchase
          </button>
          <div className="books_wrapper">
            {data.map((item, index) => (
              <div
                className="book_wrapper"
                onClick={() => handleClick(item.id)}
                key={`key_${index}`}
              >
                <h3
                  onClick={(e) => {
                    e.stopPropagation();
                  }}
                >
                  Title: {item.title}
                </h3>
                <img src={item.image} alt="book cover" />
                <p>Price: {item.price} rub</p>
                <p>Author: {item.author}</p>
                <p>Reviews: {item.reviews_quantity}</p>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    removeFromShoppingCartHandler(item.id);
                    setSbMessage("Removed from shopping cart");
                    setSbOpen(true);
                  }}
                >
                  Remove from shopping cart
                </button>
              </div>
            ))}
          </div>
        </>
      )}
    </>
  );
};

export default ShoppingCart;
