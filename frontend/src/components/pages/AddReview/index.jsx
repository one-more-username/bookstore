import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Snackbar } from "@mui/material";
import axios from "axios";
import "./styles.scss";

const AddReview = () => {
  const [review, setReview] = useState("");
  const [rating, setRating] = useState("");
  const [sbOpen, setSbOpen] = useState(false);
  const [sbMessage, setSbMessage] = useState("");

  const { book_id } = useParams();

  const token = localStorage.getItem("token");

  const snackBarHandleClose = (e, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setSbOpen(false);
  };

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
    } catch (err) {
      console.log("err", err);
    }
  };

  return (
    <div>
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
          <button
            type="submit"
            onClick={() => {
              setSbMessage("Review added");
              setSbOpen(true);
            }}
          >
            Add review
          </button>
        </div>
      </form>
    </div>
  );
};

export default AddReview;
