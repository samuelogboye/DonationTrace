import axios from "axios";
// import { jwtDecode } from "jwt-decode";
// import dayjs from "dayjs";
// import { useContext } from "react";
// import AuthContext from "../auth/context/AuthContext";

const authToken = localStorage.getItem("authTokens")
  ? JSON.parse(localStorage.getItem("authTokens")).access
  : null;

// const baseURL = process.env.REACT_APP_API_URL;
const apiService = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  headers: {
    Authorization: authToken ? `Bearer ${authToken}` : undefined,
  },
});

export default apiService;
