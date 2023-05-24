import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./styles.scss";

const Profile = () => {
  const [favourites, setFavourites] = useState(null);
  const [purchaseHistory, setPurchaseHistory] = useState(null);
  // const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const navigate = useNavigate();

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
          "http://localhost:8000/api/v1/book/favourites/",
          config
        );
        // console.log("purchase_history", response.data.purchase_history);
        setFavourites(response.data.favourites);
        setPurchaseHistory(response.data.purchase_history);
        setError(null);
      } catch (err) {
        setError(err.message);
        setFavourites(null);
      } finally {
        setLoading(false);
      }
    };
    getData();
  }, []);

  // purchase history

  const removeFromFavouritesHandler = async (book_id) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/book/${book_id}/remove-favourite/`,
        config
      );
      setFavourites(response.data.favourites);
      setError(null);
    } catch (err) {
      console.log("err", err);
      setError(err.message);
      setFavourites(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
        </>
      )}
      {favourites && (
        <div className="profile_wrapper">
          <div>
            <h2>Your purchase history</h2>
            <div className="books_wrapper">
              {purchaseHistory.map((item, index) => (
                <div
                  // onClick={() => handleClick(item.id)}
                  className="book_wrapper"
                  key={`key_${index}`}
                >
                  <h3>Title: {item.title}</h3>
                  <h3>ID: {item.id}</h3>
                  <img src={item.image} alt="book cover" />
                  <p>Price: {item.price} rub</p>
                  <p>Author: {item.author}</p>
                  <p>Reviews: {item.reviews_quantity}</p>
                  <button
                    type="button"
                    // disabled={item.is_favourite}
                    onClick={(e) => {
                      e.stopPropagation();
                      // removeFromFavouritesHandler(item.id);
                      navigate(`/book/${item.id}/add-review/`);
                    }}
                  >
                    Add review
                  </button>
                </div>
              ))}
            </div>
          </div>
          <div>
            <h2>Your favourites</h2>
            <div className="books_wrapper">
              {favourites.map((item, index) => (
                <div
                  // onClick={() => handleClick(item.id)}
                  className="book_wrapper"
                  key={`key_${index}`}
                >
                  <h3>Title: {item.title}</h3>
                  <h3>ID: {item.id}</h3>
                  <img src={item.image} alt="book cover" />
                  <p>Price: {item.price} rub</p>
                  <p>Author: {item.author}</p>
                  <p>Reviews: {item.reviews_quantity}</p>
                  <button
                    type="button"
                    // disabled={item.is_favourite}
                    onClick={(e) => {
                      e.stopPropagation();
                      removeFromFavouritesHandler(item.id);
                    }}
                  >
                    Remove from favourites
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Profile;
