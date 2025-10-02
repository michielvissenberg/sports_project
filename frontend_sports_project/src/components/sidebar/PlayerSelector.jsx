import { useState, useEffect } from "react";
import { fetchPlayersByTeam } from "../../services/fetchPlayers";
import { fetchTeamInfo } from "../../services/fetchTeamInfo";

export default function PlayerSelector({team, onSelect }) {
    const [players, setPlayers] = useState([]);
    const [loading, setLoading] = useState(false);
    const [teamInfo, setTeamInfo] = useState(null);

    useEffect(() => {
      if (!team) return;
      const fetchData = async () => {
        setLoading(true);
        try {
          const info = await fetchTeamInfo(team);
          setTeamInfo(info);
          const players = await fetchPlayersByTeam(info.idTeam);
          setPlayers(players);
        } catch (err) {
          console.error("Failed to load data:", err);
          setTeamInfo(null);
          setPlayers([]);
        } finally {
          setLoading(false);
        }
      };

      fetchData();
    }, [team]);


    return (
        <div>
            <h3>Choose Player</h3>
            {loading && <p>loading players ... </p>}
            <select onChange={(e) => onSelect(e.target.value)} disabled={loading || players.length == 0}>
                <option value="">Select a player</option>
                {players.map((player) => (
                    <option key={player.strPlayer} value={player.strPlayer}>{player.strPlayer}</option>
                ))}
            </select>
        </div>
    );
}
