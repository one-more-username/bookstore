import React, { useState, useEffect } from "react";
import axios from "axios";
import { Routes, Route, useNavigate } from "react-router-dom";
import Book from "../Book";
import "./styles.scss";

const Main = ({ setBookID }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const token = localStorage.getItem("token");

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
          "http://localhost:8000/api/v1/book/random/",
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

  const handleClick = (book_id) => {
    // setBookID(book_id);
    console.log("book.id", book_id);
    navigate(`/book/${book_id}`);
  };

  return (
    <div>
      <header className="App-header">
        {loading && <div>A moment please...</div>}
        {error && (
          <>
            <div>{`There is a problem fetching the data - ${error}`}</div>
            <button onClick={() => navigate("/login")}>Go to login page</button>
            <p>or</p>
            <button onClick={() => navigate("/signup")}>
              Go to signup page
            </button>
          </>
        )}
        <div className="books_wrapper">
          {data &&
            data.map((item, index) => (
              <div
                onClick={() => handleClick(item.id)}
                className="book_wrapper"
                key={`key_${index}`}
              >
                <h3>Title: {item.title}</h3>
                {/* <h3>ID: {item.id}</h3> */}
                {/* <p>Description: {item.description}</p> */}
                <img src={item.image} alt="book cover" />
                {/* <p>Release_date: {item.release_date}</p> */}
                <p>Price: {item.price} rub</p>
                <p>Author: {item.author}</p>
                <p>Reviews: {item.reviews_quantity}</p>
                {/* <p>Quantity at the store: {item.quantity}</p> */}
                <Routes>
                  <Route
                    path={`/book/${item.id}`}
                    element={<Book book_id={item.id} />}
                  />
                </Routes>
              </div>
            ))}
        </div>
      </header>
    </div>
  );
};

export default Main;
