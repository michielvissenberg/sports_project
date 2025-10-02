import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
});

export async function fetchVenue(venueName) {
    try {
        const response = await api.get(`/venueinfo?venue=${venueName}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching venue info:", error);
        throw error;
    }
}

