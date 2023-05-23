import React, { useEffect, useState } from "react";
import axios from "axios";

const Profile = () => {
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
          "http://localhost:8000/api/v1/book/favourites/",
          config
        );
        setData(response.data.favourites);
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

  const removeFromFavouritesHandler = async (book_id) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/book/${book_id}/remove-favourite/`,
        config
      );
      setData(response.data.favourites);
      setError(null);
    } catch (err) {
      console.log("err", err);
      setError(err.message);
      setData(null);
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
      {data && (
        <>
          <h2>Your favourites</h2>
          <div className="books_wrapper">
            {data.map((item, index) => (
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
        </>
      )}
    </div>
  );
};

export default Profile;
