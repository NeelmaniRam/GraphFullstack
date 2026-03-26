// frontend/src/services/api.js
import axios from "axios";

const BACKEND_URL = "https://graphfulstack.onrender.com/"; // replace after backend is deployed

export const fetchGraph = async () => {
  const res = await axios.get(`${BACKEND_URL}/graph`);
  return res.data;
};

export const queryAPI = async (query) => {
  const res = await axios.post(`${BACKEND_URL}/query`, { query });
  return res.data;
};