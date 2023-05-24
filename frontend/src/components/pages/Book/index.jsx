import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

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
          <div
            onClick={() => console.log("data", data)}
            className="book_wrapper"
          >
            <h3>Title: {data.title}</h3>
            <img src={data.image} alt="book cover" />
            <p>Price: {data.price} rub</p>
            <p>Author: {data.author}</p>
            <p>Reviews: {data.reviews_quantity}</p>
            <p>Rating: {data.rating}</p>
          </div>
        )}
      </div>
    </>
  );
};

export default Book;
