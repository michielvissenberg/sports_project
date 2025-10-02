import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
});

export async function fetchTeamInfo(teamName) {
    try {
        const response = await api.get(`/teaminfo?team=${teamName}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching team info:", error);
        throw error;
    }
}

