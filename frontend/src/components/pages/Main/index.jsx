import React, { useState, useEffect } from "react";
import axios from "axios";

const Main = () => {
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

  return (
    <div>
      <header className="App-header">
        <h1>Bookstore</h1>
        {loading && <div>A moment please...</div>}
        {error && (
          <div>{`There is a problem fetching the data - ${error}`}</div>
        )}
        <div>
          {data &&
            data.map((item, index) => (
              <div key={`key_${index}`}>
                <h3>Title: {item.title}</h3>
                <p>Description: {item.description}</p>
                <img src={item.image} alt="book cover" />
                <p>Release_date: {item.release_date}</p>
                <p>Price: {item.price} rub</p>
                <p>Author: {item.author}</p>
                <p>Reviews: {item.reviews_quantity}</p>
                <p>Quantity at the store: {item.quantity}</p>
              </div>
            ))}
        </div>
      </header>
    </div>
  );
};

export default Main;
