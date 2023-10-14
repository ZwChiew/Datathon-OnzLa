import * as React from "react";
import { Grid } from "@mui/material";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ReferenceLine,
} from "recharts";
import { data } from "./data";
import { data1 } from "./data";
export const LSTM = () => {
  const priceData = data.map((item) => item.price);
  const minPrice = Math.min(...priceData);
  const maxPrice = Math.max(...priceData);
  const colorChangeDate = new Date("2022-12-29");
  // Calculate the Y-axis scale range, adding some buffer
  const yScaleMin = minPrice - 0.5; // Adjust this buffer as needed
  const yScaleMax = maxPrice + 0.5; // Adjust this buffer as needed
  const combinedData = [...data, ...data1];
  console.log(new Date(combinedData[0]["date"]));
  return (
    <Grid
      container
      style={{
        marginTop: "25px",
      }}
      spacing={2.5}
    >
      <div>
        <h2>Price Over Time</h2>
        <LineChart width={1700} height={700} data={combinedData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis domain={[yScaleMin, yScaleMax]} />
          <Tooltip />
          <Legend />
          <Line
            type="monotone"
            dataKey="price"
            name="price"
            activeDot={{ r: 8 }}
            stroke={"#8884d8"} // Change line color based on the date
          />
          <ReferenceLine x={"2022-12-29"} stroke="orange" label="Predicted" />
        </LineChart>
      </div>
    </Grid>
  );
};
