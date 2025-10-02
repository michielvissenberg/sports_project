import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
})

export async function fetchFormerTeams(playerId) {
    try {
        const response = await api.get(`/formerteams?player=${playerId}`)
        return response.data
    } catch (error) {
        console.error("Error fetching former teams by player id:", error)
        throw error
    }
}