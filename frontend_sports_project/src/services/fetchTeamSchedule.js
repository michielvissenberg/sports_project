import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
});

export async function fetchTeamSchedule(teamId) {
    try {
        const response = await api.get(`/teamschedule?team=${teamId}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching team schedule:", error);
        throw error;
    }
}