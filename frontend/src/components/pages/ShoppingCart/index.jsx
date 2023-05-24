import React, { useState, useEffect } from "react";
import axios from "axios";

const ShoppingCart = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const token = localStorage.getItem("token");

  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  useEffect(() => {
    const getData = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/v1/shopping-cart/",
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
      setData(response.data.books_to_purchase);
      // setError(null);
    } catch (err) {
      // setError(err.message);
      // setData(null);
    } finally {
      // setLoading(false);
    }
  };

  return (
    <>
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
        </>
      )}
      {data && (
        <>
          <h2>Your shopping cart</h2>
          <button
            type="button"
            // disabled={!data.length}
            onClick={(e) => {
              makePurchaseHandler(e);
            }}
          >
            Make a purchase
          </button>
          <div>
            {data.map((item, index) => (
              <div
                // onClick={() => handleClick(item.id)}
                key={`key_${index}`}
              >
                <h3>Title: {item.title}</h3>
                {/* <h3>ID: {item.id}</h3> */}
                <img src={item.image} alt="book cover" />
                <p>Price: {item.price} rub</p>
                <p>Author: {item.author}</p>
                <p>Reviews: {item.reviews_quantity}</p>
                <button
                  type="button"
                  // disabled={item.is_favourite}
                  onClick={(e) => {
                    e.stopPropagation();
                    removeFromShoppingCartHandler(item.id);
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
