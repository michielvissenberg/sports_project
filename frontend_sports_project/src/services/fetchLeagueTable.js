import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
})

export async function fetchLeagueTable(leagueId) {
    try {
        const response = await api.get(`/leagueTable?league=${leagueId}`)
        return response.data
    } catch (error) {
        console.error("Error fetching league-table:", error)
        throw error
    }
}