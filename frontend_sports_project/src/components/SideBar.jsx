import { useState, useEffect } from "react";
import LeagueSelector from "./sidebar/LeagueSelector";
import TeamSelector from "./sidebar/TeamSelector";
import PlayerSelector from "./sidebar/PlayerSelector";

export default function SideBar({onSelect}) {
    const [selectedLeague, setSelectedLeague] = useState(null);
    const [selectedTeam, setSelectedTeam] = useState(null);
    const [selectedPlayer, setSelectedPlayer] = useState(null);
    useEffect(() => {
        onSelect({selectedLeague, selectedTeam, selectedPlayer});
    }, [selectedLeague, selectedTeam, selectedPlayer]);

    useEffect(() => {
    setSelectedTeam(null);
    setSelectedPlayer(null);
    }, [selectedLeague]);

    useEffect(() => {
    setSelectedPlayer(null);
    }, [selectedTeam]);
    
    return (
        <div className="sidebar">
            <LeagueSelector onSelect={setSelectedLeague} />
            {selectedLeague && <TeamSelector league={selectedLeague} onSelect={setSelectedTeam} />}
            {selectedTeam && <PlayerSelector team={selectedTeam} onSelect={setSelectedPlayer} />}
            <hr />
            <p id="greenbox">Sadly, this site uses a free service to retreive the data, so only the first few leagues/teams/players are shown. (in alphabetical order)
                Some data might also be missing or incorrect.
            </p>
        </div>
    );

}
