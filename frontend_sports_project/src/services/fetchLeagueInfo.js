import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
});

export async function fetchLeagueInfo(leagueId) {
    try {
        const response = await api.get(`/leagueinfo?league=${leagueId}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching league info:", error);
        throw error;
    }
}
