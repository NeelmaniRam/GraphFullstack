// frontend/src/services/api.js
import axios from "axios";

// Use your deployed backend URL here
const BACKEND_URL = "https://graphfulstack.onrender.com"; 

export const fetchGraph = async () => {
  try {
    const res = await axios.get(`${BACKEND_URL}/graph`);
    return res.data;
  } catch (err) {
    console.error("Error fetching graph:", err);
    return { nodes: [], edges: [] };
  }
};

export const queryAPI = async (query) => {
  try {
    const res = await axios.post(`${BACKEND_URL}/query`, { query });
    return res.data;
  } catch (err) {
    console.error("Error querying backend:", err);
    return { nodes: [], edges: [], answer: "Error fetching response" };
  }
};