import React, { useState } from "react";
import { TextField, Grid, Button, Typography } from "@mui/material";
import axios from "axios";
import { setGlobalState } from "./context";

export const Classifier = () => {
  const initialFormData = {
    price: "",
    rsi: "",
    k: "",
    macd: "",
    interest: "",
    stock: "",
  };
  const [formData, setFormData] = useState(initialFormData);
  const [value, setValue] = useState("null");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.id || e.target.name]: e.target.value,
    });
  };

  const handleReset = (e) => {
    setFormData(initialFormData);
    setValue("null");
  };

  const handleClick = async (e) => {
    setGlobalState("loading", true);
    // console.log(formData);
    var myParams = {
      data: formData,
    };
    await axios
      .post("http://localhost:5000/api/classify", myParams)
      .then(function (response) {
        let output1 = response.data;
        setValue(output1);
      })
      .catch(function (error) {
        console.log(error);
      });
    setGlobalState("loading", false);
  };

  return (
    <Grid
      container
      style={{
        marginTop: "20px",
      }}
      spacing={2}
    >
      <Grid item sm={12} xs={12} style={{ marginTop: "15px" }}>
        <Typography variant="h4">Bond Trend Predictor</Typography>
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          id="price"
          label="Price"
          type="number"
          value={formData.price}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          style={{ marginTop: "15px" }}
          id="rsi"
          label="RSI"
          type="number"
          value={formData.rsi}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          style={{ marginTop: "15px" }}
          id="k"
          label="K Percent"
          type="number"
          value={formData.k}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          style={{ marginTop: "15px" }}
          id="macd"
          label="MACD"
          type="number"
          value={formData.macd}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          style={{ marginTop: "15px" }}
          id="interest"
          label="Interest Overnight Rate"
          type="number"
          value={formData.interest}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={12} xs={12}>
        <TextField
          fullWidth
          required
          style={{ marginTop: "15px" }}
          id="stock"
          label="TNB Stock Price"
          type="number"
          value={formData.stock}
          onChange={handleChange}
        />
      </Grid>
      <Grid item sm={2} xs={2}>
        <Button
          size="large"
          variant="contained"
          // sx={{
          //   backgroundColor: "gold",
          //   color: "white",
          //   "&:hover": {
          //     backgroundColor: "gold",
          //     color: "black",
          //   },
          // }}
          onClick={handleClick}
        >
          Calculate
        </Button>
      </Grid>
      <Grid item sm={1} xs={1}>
        <Button
          size="large"
          variant="contained"
          // sx={{
          //   backgroundColor: "gold",
          //   color: "white",
          //   "&:hover": {
          //     backgroundColor: "gold",
          //     color: "black",
          //   },
          // }}
          onClick={handleReset}
        >
          Reset
        </Button>
      </Grid>
      <Grid item sm={12} xs={12}>
        <Typography variant="h4">Predicted Trend: {value}</Typography>
      </Grid>
    </Grid>
  );
};
