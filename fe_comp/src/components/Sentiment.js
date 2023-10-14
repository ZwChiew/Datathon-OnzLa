import React, { useState } from "react";
import { Button, Typography, Grid, TextField } from "@mui/material";
import axios from "axios";
import { setGlobalState } from "./context";
import Speedometer from "react-d3-speedometer";
import { useEffect } from "react";

export const SentimentAnalysis = () => {
  const [messages, setMessages] = useState("");
  const [link, setLink] = useState("");
  const [sentiment, setSentiment] = useState(0);
  const [trend, setTrend] = useState("");

  useEffect(() => {
    // Check if the sentiment is not null
    if (sentiment !== null) {
      // Determine the trend based on sentiment
      if (sentiment < 0) {
        setTrend("negative");
      } else if (sentiment > 0) {
        setTrend("positive");
      } else {
        setTrend("neutral");
      }
    }
  }, [sentiment]);

  const handleMessagesChange = (e) => {
    setMessages(e.target.value);
  };
  const handleLinkChange = (e) => {
    setLink(e.target.value);
  };

  const handleReset = (e) => {
    setLink("");
    setMessages("");
    setSentiment(0);
  };

  const handleSubmit = async (e) => {
    setGlobalState("loading", true);
    var myParams = {
      data: link,
    };
    await axios
      .post("http://localhost:5000/api/sentiment", myParams)
      .then(function (response) {
        let output1 = response.data;
        console.log(output1);
        setMessages(output1["article"]);
        setSentiment(output1["sentiment_score"]);
      })
      .catch(function (error) {
        console.log(error);
      });
    setGlobalState("loading", false);
  };

  return (
    <>
      <Typography variant="h4" marginTop="50px">
        Sentiment Analysis
      </Typography>
      <Grid container spacing={2.5}>
        <Grid item xs={12} style={{ marginTop: "50px" }}>
          <TextField
            onChange={handleLinkChange}
            variant="outlined"
            label="News Article Link"
            value={link}
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            disabled
            onChange={handleMessagesChange}
            variant="outlined"
            label="Scrapped Data"
            multiline
            rows={20}
            value={messages}
            fullWidth
          />
        </Grid>
        <Grid item xs={2}>
          <Button onClick={handleSubmit} size="large" variant="contained">
            Submit
          </Button>
        </Grid>
        <Grid item xs={2}>
          <Button onClick={handleReset} size="large" variant="contained">
            Reset
          </Button>
        </Grid>
        <Grid item xs={10}>
          <Typography variant="h5" sx={{ marginBottom: "30px" }}>
            {messages === ""
              ? "No article detected"
              : `This article has a ${trend} sentiment`}
          </Typography>
          <Speedometer
            value={sentiment}
            minValue={-1}
            maxValue={1}
            width={400}
            height={300}
          />
        </Grid>
      </Grid>
    </>
  );
};
