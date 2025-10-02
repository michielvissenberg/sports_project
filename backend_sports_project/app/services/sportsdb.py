import httpx # type: ignore

def fetch_teams_from_api(league: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/search_all_teams.php?l={league}"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("teams", [])
    else:
        return []

def fetch_leagues_from_api(api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/all_leagues.php?s=Soccer"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("leagues", [])
    else:
        return []

def fetch_team_info_from_api(team_name: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchteams.php?t={team_name}"
    response = httpx.get(url)
    if response.status_code == 200:
        teams = response.json().get("teams", [])
        return teams[0] if teams else None
    else:
        return []

def fetch_team_players_from_api(team_id: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookup_all_players.php?id={team_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("player", [])
    else:
        return []
    
def fetch_player_info_from_api(player_name: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchplayers.php?p={player_name}"
    response = httpx.get(url)
    if response.status_code == 200:
        players = response.json().get("player", [])
        return players[0] if players else None
    else:
        return None
    
def fetch_former_teams_from_api(player_id: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookupformerteams.php?id={player_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("formerteams", [])
    else:
        return []
    
def fetch_league_table_from_api(league_id: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookuptable.php?l={league_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        return response.json().get("table", [])
    else:
        return []
    
def fetch_league_info_from_api(league_id: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookupleague.php?id={league_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        leagues = response.json().get("leagues", [])
        return leagues[0] if leagues else None
    else:
        return None
    
def fetch_venue_info_from_api(venue: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchvenues.php?v={venue}"
    response = httpx.get(url)
    if response.status_code == 200:
        venues = response.json().get("venues", [])
        return venues[0] if venues else None
    else:
        return None
    
def fetch_team_schedule_from_api(team_id: str, api_key="123"):
    url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/eventsnext.php?id={team_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        events = response.json().get("events", [])
        return events[0] if events else None
    else:
        return []