import {useState, useEffect} from 'react';
import {fetchLeagueTable} from '../../services/fetchLeagueTable';
import {fetchLeagues} from '../../services/fetchLeagues';
import {fetchLeagueInfo} from '../../services/fetchLeagueInfo';

export default function LeagueInfo({ leagueName }) {
    const [leagueTable, setLeagueTable] = useState(null);
    const [leagueInfo, setLeagueInfo] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!leagueName) {
            setLeagueTable(null);
            return;
        }
        const fetchData = async () => {
            setLoading(true);
            try {
                const leagues = await fetchLeagues();
                const league = leagues.find(l => l.strLeague === leagueName);
                const leagueInfo = await fetchLeagueInfo(league.idLeague);
                setLeagueInfo(leagueInfo);
                const table = await fetchLeagueTable(league.idLeague);
                setLeagueTable(table);
            } catch (err) {
                console.error("Failed to load league data:", err);
                setLeagueTable(null);
            } finally {
                setLoading(false);
            }
        }
        fetchData();
    }, [leagueName]);
    
    return (
        <div>
            {loading && <p>Loading league info...</p>}
            {!loading && leagueInfo && leagueTable && (
                <div>
                    <div className='league-header'>
                        {leagueInfo.strLogo ? (
                            <img src={leagueInfo.strLogo} alt={`${leagueInfo.strLeague} Logo`} style={{width: '200px'}} />
                        ) : (
                            <h3>{leagueInfo.strLeague}</h3>
                        )}
                    </div>

                    <div className='leagueInfo-essentials'>
                        <table className='league-info-table' id='greenbox'>
                            <h3 id='headerInfo'>Basic info:</h3>
                            <tbody>
                                <tr>
                                    <td><strong>Full name:</strong></td>
                                    <td>{leagueInfo.strLeague}</td>
                                </tr>
                                <tr>
                                    <td><strong>Founded:</strong></td>
                                    <td>{leagueInfo.intFormedYear}</td>
                                </tr>
                                <tr>
                                    <td><strong>Website:</strong></td>
                                    <td><a href={`https://${leagueInfo.strWebsite}`} target="_blank" rel="noopener noreferrer">{leagueInfo.strWebsite}</a></td>
                                </tr>
                                <tr>
                                    <td><strong>Trophy:</strong></td>
                                    <td>{leagueInfo.strTrophy && <img src={leagueInfo.strTrophy} alt={`${leagueInfo.strLeague} Trophy`} style={{height: '100px'}} />}</td>
                                </tr>
                            </tbody>
                        </table>
                        
                        <table className='league-table' id='greenbox'>
                            <thead>
                                <tr>
                                    <th></th>
                                    <th>Team</th>
                                    <th>Points</th>
                                    <th>Played</th>
                                    <th>Win</th>
                                    <th>Draw</th>
                                    <th>Loss</th>
                                    <th>Goals +</th>
                                    <th>Goals -</th>
                                    <th>Form</th>
                                </tr>
                            </thead>
                            <tbody>
                                {leagueTable && leagueTable.length > 0 ? (
                                    leagueTable.map((entry) => (
                                        <tr key={entry.idTeam}>
                                            <td><strong>{entry.intRank}</strong></td>
                                            <td>{entry.strTeam}</td>
                                            <td>{entry.intPoints}</td>
                                            <td>{entry.intPlayed}</td>
                                            <td>{entry.intWin}</td>
                                            <td>{entry.intDraw}</td>
                                            <td>{entry.intLoss}</td>
                                            <td>{entry.intGoalsFor}</td>
                                            <td>{entry.intGoalsAgainst}</td>
                                            <td>{entry.strForm.split("").reverse().join("")}</td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
                                        <td colSpan="7">No league table data found.</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                    <p className='description' id='greenbox'><strong>Description:</strong> {leagueInfo.strDescriptionEN}</p>
                    <div className='league-banner' id='greenbox'>
                        {leagueInfo.strBanner && <img src={leagueInfo.strBanner} alt={`${leagueInfo.strLeague} Banner`} style={{width: '100%'}} />}
                    </div>                    
                </div>
            )}

        </div>
    );
}