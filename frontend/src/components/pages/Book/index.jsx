import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import "./styles.scss";

const Book = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const navigate = useNavigate();
  const { book_id } = useParams();

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
          `http://localhost:8000/api/v1/book/${book_id}/`,
          config
        );
        setData(response.data);
        console.log("response.data", response.data.reviews);
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
    <>
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
          <button onClick={() => navigate("/login")}>Go to login page</button>
          <p>or</p>
          <button onClick={() => navigate("/signup")}>Go to signup page</button>
        </>
      )}
      <div className="book_detail">
        {data && (
          <div className="wrapper">
            <div className="book_wrapper">
              <h3>Title: {data.title}</h3>
              <img src={data.image} alt="book cover" />
              <p>Price: {data.price} rub</p>
              <p>Author: {data.author}</p>
              <p>Reviews: {data.reviews_quantity}</p>
              <p>Rating: {data.rating ? data.rating : 0}</p>
              <p>Description: {data.description}</p>
              <div className="buttons">
                <button
                  type="button"
                  // disabled={item.is_favourite}
                  onClick={(e) => {
                    e.stopPropagation();
                    addToFavouritesHandler(data.id);
                  }}
                >
                  Add to favourites
                </button>
                <button
                  type="button"
                  // disabled={item.is_favourite}
                  onClick={(e) => {
                    e.stopPropagation();
                    addToShoppingCartHandler(data.id);
                  }}
                >
                  Add to shopping cart
                </button>
              </div>
            </div>
            {data.reviews && (
              <>
                <h3>Detailed reviews</h3>
                <div className="reviews_wrapper">
                  {data.reviews.map((item, index) => {
                    return (
                      <div
                        className="review_wrapper"
                        key={`review_${index + 1}`}
                      >
                        <p>{item.review}</p>
                        <p>{item.rating}</p>
                      </div>
                    );
                  })}
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </>
  );
};

export default Book;
