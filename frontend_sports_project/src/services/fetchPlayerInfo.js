import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
});

export async function fetchPlayerInfo(playerName) {
    try {
        const response = await api.get(`/playerinfo?player=${playerName}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching player info:", error);
        throw error;
    }
}
