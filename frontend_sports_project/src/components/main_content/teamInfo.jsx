import { useState, useEffect, use } from "react";
import { fetchTeamInfo } from "../../services/fetchTeamInfo";
import { fetchPlayersByTeam } from "../../services/fetchPlayers";
import { fetchVenue } from "../../services/fetchVenue";
import { fetchTeamSchedule } from "../../services/fetchTeamSchedule";
import Countdown from "./Countdown";

export default function TeamInfo({ teamName }) {
    const [teamInfo, setTeamInfo] = useState(null);
    const [loading, setLoading] = useState(false);
    const [players, setPlayers] = useState([]);
    const [venue, setVenue] = useState(null);
    const [schedule, setSchedule] = useState([]);

    useEffect(() => {
        if (!teamName) {
            setTeamInfo(null);
            return;
        }
        const fetchData = async () => {
            setLoading(true);
            try {
                const info = await fetchTeamInfo(teamName);
                setTeamInfo(info);
                const players = await fetchPlayersByTeam(info.idTeam);
                setPlayers(players);
                const venue = await fetchVenue(info.strStadium);
                setVenue(venue);
                const schedule = await fetchTeamSchedule(info.idTeam);
                setSchedule(schedule);
            } catch (err) {
                console.error("Failed to load data:", err);
                setTeamInfo(null);
                setPlayers([]);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [teamName]);

    return (
        <div>
            {loading && <p>Loading team info...</p>}
            {!loading && teamInfo && venue && schedule && (
                <div>
                    <div className="team-header">
                        {teamInfo.strLogo ? (
                            <img src={teamInfo.strLogo} style={{ width: '200px'}}/>
                        ) : (
                            <h3>Info about: {teamInfo.strTeam}</h3>
                        )}
                    </div>
                    <div className="teamInfo-essentials">
                        <table className="teamTable" id="greenbox">
                            <h3 id="headerInfo">Basic info:</h3>
                            <tbody>
                                <tr>
                                    <td><strong>League:</strong></td>
                                    <td>{teamInfo.strLeague}</td>
                                </tr>
                                <tr>
                                    <td><strong>Stadium:</strong></td>
                                    <td>{teamInfo.strStadium}</td>
                                </tr>
                                <tr>
                                    <td><strong>Stadium capacity:</strong></td>
                                    <td>{teamInfo.intStadiumCapacity}</td>
                                </tr>
                                <tr>
                                    <td><strong>Formed Year:</strong></td>
                                    <td>{teamInfo.intFormedYear}</td>
                                </tr>
                                <tr>
                                    <td><strong>Nickname(s):</strong></td>
                                    <td>{teamInfo.strKeywords ? (teamInfo.strKeywords) : ("/")}</td>
                                </tr>
                                <tr>
                                    <td><strong>Location:</strong></td>
                                    <td>{teamInfo.strLocation}</td>
                                </tr>
                                <tr>
                                    <td><strong>Website:</strong></td>
                                    <td><a href={`http://${teamInfo.strWebsite}`} target="_blank" rel="noopener noreferrer">{teamInfo.strWebsite}</a></td>
                                </tr>
                            </tbody>
                        </table>
                        <div className="players-list" id="greenbox">
                            <ul>
                                <h3>Players:</h3>
                                {players.map(player => (
                                    <li key={player.idPlayer}>{player.strPlayer}</li>
                                ))}
                            </ul>
                        </div>
                        <div className="team-badge">
                            {teamInfo.strBadge && <img src={teamInfo.strBadge} style={{width: '100%'}}/>}
                        </div>
                    </div>
                    <div className="team-schedule" id="greenbox">
                        <div style={{minHeight: '200px'}}>
                            <h3>Upcoming Match:</h3>
                            <div className="team-badges">
                                {schedule.strHomeTeamBadge && <img src={schedule.strHomeTeamBadge} style={{width: '100px', marginRight: '20px'}}/>}
                                <h3>VS</h3>
                                {schedule.strAwayTeamBadge && <img src={schedule.strAwayTeamBadge} style={{width: '100px'}}/>}
                            </div>
                        </div>
                        <Countdown dateEvent={schedule.dateEvent} strTime={schedule.strTime}/>
                        {schedule.strThumb && <img src={schedule.strThumb} style={{width: '300px', marginRight: '20px', height: 'fit-content'}}/>}
                    </div>
                    <div className="venue-info" id="greenbox">
                        <div className="venue-details">
                            <div>
                                <h3>Venue: {venue.strVenue}</h3>
                                <p><strong>Capacity:</strong> {venue.intCapacity ? venue.intCapacity : "/"}</p>
                                <p><strong>Built Year:</strong> {venue.intFormedYear ? venue.intFormedYear : "/"}</p>
                                <p><strong>Location:</strong> {venue.strLocation ? venue.strLocation : "/"}</p>
                                <p><strong>Nickname(s):</strong> {venue.strVenueAlternate ? venue.strVenueAlternate : "/"}</p>
                            </div>
                            {venue.strThumb && <img src={venue.strThumb} style={{width: '350px', marginRight: '20px', height: 'fit-content'}}/>}
                        </div>
                        <p><strong>Venue description:</strong> {venue.strDescriptionEN}</p>
                    </div>
                    

                    <p className="description" id="greenbox"><strong>Team description:</strong> {teamInfo.strDescriptionEN}</p>
                </div>
            )}  
            {!loading && !teamInfo && <p>Selecteer een team om info te krijgen.</p>}
        </div>
    );
}