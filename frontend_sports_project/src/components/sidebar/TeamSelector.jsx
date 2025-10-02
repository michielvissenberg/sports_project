import { useState, useEffect } from "react";
import { fetchTeamsByLeague } from "../../services/fetchTeams";

export default function TeamSelector({league, onSelect }) {
    const [teams, setTeams] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
      if (!league) return;
      setLoading(true);
      fetchTeamsByLeague(league)
        .then(setTeams)
        .catch(err => {
          console.error("Failed to load teams:", err);
          setTeams([]);
        })
      .finally(() => setLoading(false));
    }, [league]);  


    return (
        <div>
            <h3>Choose team</h3>
            {loading && <p>loading teams ... </p>}
            <select onChange={(e) => onSelect(e.target.value)} disabled={loading || teams.length == 0}>
                <option value="">Select a team</option>
                {teams.map((team) => (
                    <option key={team.strTeam} value={team.strTeam}>{team.strTeam}</option>
                ))}
            </select>
        </div>
    );
}
