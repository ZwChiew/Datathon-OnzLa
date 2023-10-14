import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./components/Home";
import { SentimentAnalysis } from "./components/Sentiment";
import { LSTM } from "./components/LSTM";
import PersistentDrawerLeft from "./SideBar";
import { LoadingOverlay } from "./components/Loading-overlay";
import { SigninPage } from "./components/Signin";
import { Classifier } from "./components/Classifier";

export const Routers = () => {
  return (
    <BrowserRouter>
      <LoadingOverlay />
      <PersistentDrawerLeft>
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/lstm" element={<LSTM />} />
          <Route path="/sentiment" element={<SentimentAnalysis />} />
          <Route path="/signin" element={<SigninPage />} />
          <Route path="/classifier" element={<Classifier />} />
        </Routes>
      </PersistentDrawerLeft>
    </BrowserRouter>
  );
};
