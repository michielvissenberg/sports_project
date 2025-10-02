import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:8000/api",
  timeout: 5000,
});

export async function fetchTeamsByLeague(league) {
  try {
    const response = await api.get(`/teams?league=${league}`)
    return response.data
  } catch (error) {
    console.error("Error fetching teams by league:", error)
    throw error
  }
}