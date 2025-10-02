import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
})

export async function fetchLeagues() {
    try {
        const response = await api.get("/leagues")
        return response.data
    } catch (error) {
        console.error("Error fetching leagues:", error)
        throw error
    }
}