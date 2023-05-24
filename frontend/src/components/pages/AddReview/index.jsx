import React, { useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "./styles.scss";

const AddReview = () => {
  const [review, setReview] = useState("");
  const [rating, setRating] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const { book_id } = useParams();

  const token = localStorage.getItem("token");

  const config = {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };

  const handleSubmit = async (e) => {
    e.stopPropagation();
    try {
      const response = await axios.post(
        `http://localhost:8000/api/v1/book/${book_id}/add-review/`,
        { review: review, rating: rating },
        config
      );
      console.log("response.data", response.data);
      // setFavourites(response.data.favourites);
      setError(null);
    } catch (err) {
      console.log("err", err);
      setError(err.message);
      // setFavourites(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Add Review */}
      {/* {loading && <div>A moment please...</div>}
      {error && (
        <>
          <div>{`There is a problem fetching the data - ${error}`}</div>
        </>
      )} */}
      <form onSubmit={handleSubmit}>
        <label>
          <p>Review text</p>
          <input
            type="text"
            value={review}
            onChange={(e) => setReview(e.target.value)}
          />
        </label>
        <label>
          <p>Rating</p>
          <input
            type="number"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
          />
        </label>
        <div>
          <button type="submit">Add review</button>
        </div>
      </form>
    </div>
  );
};

export default AddReview;
