import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
})

export async function fetchPlayersByTeam(team) {
    try {
        const response = await api.get(`/players?team=${team}`)
        return response.data
    } catch (error) {
        console.error("Error fetching players by team:", error)
        throw error
    }
}