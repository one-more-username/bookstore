import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./styles.scss";

const Search = () => {
  const [searchedTitle, setSearchedTitle] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [pagination, setPagination] = useState({
    previous: false,
    next: false,
  });
  const navigate = useNavigate();

  const handleSubmit = async (
    e,
    url_api = `http://localhost:8000/api/v1/book/search/?search=${searchedTitle}`
  ) => {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await axios.get(url_api);
      setData(response.data.results);
      setPagination({
        previous: response.data.previous,
        next: response.data.next,
      });
      setError(null);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  const handleClick = (book_id) => {
    navigate(`/book/${book_id}`);
  };

  return (
    <>
      <h1>Search</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Enter title of searched book</p>
          <input
            type="text"
            value={searchedTitle}
            onChange={(e) => setSearchedTitle(e.target.value)}
          />
        </label>
        <div className="buttons_wrapper">
          <button
            type="button"
            disabled={!pagination.previous}
            onClick={(e) => {
              handleSubmit(e, pagination.previous);
            }}
          >
            Previous
          </button>
          <button type="submit">Search</button>
          <button
            type="button"
            disabled={!pagination.next}
            onClick={(e) => {
              handleSubmit(e, pagination.next);
            }}
          >
            Next
          </button>
        </div>
      </form>
      {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
          {/* <button onClick={() => navigate("/login")}></button>
          <button onClick={() => navigate("/signup")}></button> */}
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
              <p>Rating: {item.rating ? item.rating : 0}</p>
            </div>
          ))}
        </div>
      )}
    </>
  );
};

export default Search;
