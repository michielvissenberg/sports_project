import { useState, useEffect } from 'react';
import Header from '../components/Header';
import SideBar from '../components/SideBar';
import TeamInfo from '../components/main_content/teamInfo';
import PlayerInfo from '../components/main_content/playerInfo';
import LeagueInfo from '../components/main_content/leagueInfo';

export default function HomePage() {
    const [selection, setSelection] = useState({
        selectedLeague: null,
        selectedTeam: null,
        selectedPlayer: null
    });

    return (
    <div className="home-page">
      <Header />
      <div className="content">
        <SideBar onSelect={setSelection}/>
        <div className="main-content">
          {selection.selectedPlayer ? (
            <PlayerInfo playerName={selection.selectedPlayer} />
          ) : selection.selectedTeam ? (
            <TeamInfo teamName={selection.selectedTeam} />
          ) : selection.selectedLeague ? (
            <LeagueInfo leagueName={selection.selectedLeague} />
          ) : (
            <h3>First select a league</h3>
          )}
        </div>
      </div>
    </div>
  );
}