import { useState, useEffect } from "react"
import { fetchLeagues } from "../../services/fetchLeagues"

export default function LeagueSelector({onSelect }) {
    const [leagues, setLeagues] = useState([])
    const [loading, setLoading] = useState(false)
    
    useEffect(() => {
        setLoading(true)
        fetchLeagues()
      .then(setLeagues)
      .catch(err => {
        console.error("Failed to load leagues:", err)
        setLeagues([])
      })
      .finally(() => setLoading(false))
    }, []);

    return (
        <div>
            <h3>Choose league</h3>
            {loading && <p>loading leagues ... </p>}
            <select onChange={(e) => onSelect(e.target.value)} disabled={loading || leagues.length == 0}>
                <option value="">Select a league</option>
                {leagues.map((league) => (
                    <option key={league.strLeague} value={league.strLeague}>{league.strLeague}</option>
                ))}
            </select>
        </div>
    );
}
