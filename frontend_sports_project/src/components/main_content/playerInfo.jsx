import { useState, useEffect } from "react";
import { fetchPlayerInfo } from "../../services/fetchPlayerInfo";
import { fetchFormerTeams } from "../../services/fetchFormerTeams";

export default function PlayerInfo({ playerName }) {
    const [playerInfo, setPlayerInfo] = useState(null);
    const [formerTeams, setFormerTeams] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!playerName) {
            setPlayerInfo(null);
            return;
        }
        const fetchData = async () => {
            setLoading(true);
            try {
                const info = await fetchPlayerInfo(playerName);
                setPlayerInfo(info);
                const teams = await fetchFormerTeams(info.idPlayer);
                setFormerTeams(teams);
            } catch (err) {
                console.error("Failed to load player data:", err);
                setPlayerInfo(null);
                setFormerTeams(null);
            } finally {
                setLoading(false);
            }
        }
        fetchData();
    }, [playerName]);

    return (
        <div>
            {loading && <p>Loading player info...</p>}
            {!loading && playerInfo && (
                <div>
                    <div className="player-header">
                        {playerInfo.strCutout ? (
                            <img src={playerInfo.strCutout} />
                        ) : (
                            <h3>Info about: {playerInfo.strName}</h3>
                        )}
                    </div>
                    <div className="playerInfo-essentials">
                        <table className="player-info-table" id="greenbox">
                            <h3 id="headerInfo">Basic info:</h3>
                            <tbody>
                                <tr>
                                    <td><strong>Team:</strong></td>
                                    <td>{playerInfo.strTeam}</td>
                                </tr>
                                <tr>
                                    <td><strong>Position:</strong></td>
                                    <td>{playerInfo.strPosition}</td>
                                </tr>
                                <tr>
                                    <td><strong>Date born:</strong></td>
                                    <td>{playerInfo.dateBorn}</td>
                                </tr>
                                <tr>
                                    <td><strong>Nationality:</strong></td>
                                    <td>{playerInfo.strNationality}</td>
                                </tr>
                            </tbody> 
                        </table>
                        <div className="former-teams" id="greenbox">
                            <h3>Former Teams:</h3>
                            {formerTeams ? (
                                <table className="former-teams-table">
                                    <thead>
                                        <tr>
                                            <th>Team</th>
                                            <th>Joined</th>
                                            <th>Left</th>
                                            <th>Type</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {formerTeams.teams && formerTeams.teams.length > 0 ? (
                                            formerTeams.teams
                                            .slice()
                                            .sort((a, b) => Number(a.strJoined) - Number(b.strJoined))
                                            .map((team) => (
                                            <tr>
                                                <td>{team.strFormerTeam}</td>
                                                <td>{team.strJoined}</td>
                                                <td>{team.strDeparted}</td>
                                                <td>{team.strMoveType}</td>
                                            </tr>
                                            ))
                                        ) : (
                                            <tr>
                                                <td colSpan={4}>No former teams found.</td>
                                            </tr>
                                        )}
                                    </tbody>
                                </table>
                                
                            ) : (
                                    <p id="no-former-teams">No former teams provided for this player</p>
                            )}
                        </div>
                        <div className="thumb" id="greenbox">
                            {playerInfo.strThumb ? (
                                <img src={playerInfo.strThumb} style={{width: '250px', height: '250px'}}/>
                            ) : (
                                <p>No picture provided for this player</p>
                            )}
                        </div>
                    </div>
                    
                    
                </div>
            )}
        </div>
    );
}