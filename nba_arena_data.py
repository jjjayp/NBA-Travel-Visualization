import json
import os

def load_arena_data(json_path='arena_coords.json'):
    """Load NBA arena data from a JSON file or fallback."""
    from nba_arena_data import NBA_ARENAS  # ensure access

    if not os.path.exists(json_path):
        print("Arena coordinates file not found. Using fallback NBA_ARENAS.")
        return NBA_ARENAS

    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        if not data:
            print("Empty JSON file. Using fallback NBA_ARENAS.")
            return NBA_ARENAS
        return data
    except Exception as e:
        print(f"Error loading arena data: {e}. Using fallback NBA_ARENAS.")
        return NBA_ARENAS

# Fallback NBA arena data dictionary.
NBA_ARENAS = {
    "Atlanta Hawks": {"city": "Atlanta", "lat": 33.757, "lon": -84.396},
    "Boston Celtics": {"city": "Boston", "lat": 42.366, "lon": -71.062},
    "Brooklyn Nets": {"city": "Brooklyn", "lat": 40.682, "lon": -73.975},
    "Charlotte Hornets": {"city": "Charlotte", "lat": 35.225, "lon": -80.839},
    "Chicago Bulls": {"city": "Chicago", "lat": 41.880, "lon": -87.674},
    "Cleveland Cavaliers": {"city": "Cleveland", "lat": 41.496, "lon": -81.688},
    "Dallas Mavericks": {"city": "Dallas", "lat": 32.790, "lon": -96.810},
    "Denver Nuggets": {"city": "Denver", "lat": 39.748, "lon": -105.007},
    "Detroit Pistons": {"city": "Detroit", "lat": 42.341, "lon": -83.055},
    "Golden State Warriors": {"city": "San Francisco", "lat": 37.768, "lon": -122.387},
    "Houston Rockets": {"city": "Houston", "lat": 29.750, "lon": -95.362},
    "Indiana Pacers": {"city": "Indianapolis", "lat": 39.764, "lon": -86.155},
    "LA Clippers": {"city": "Los Angeles", "lat": 34.043, "lon": -118.267},
    "Los Angeles Lakers": {"city": "Los Angeles", "lat": 34.043, "lon": -118.267},
    "Memphis Grizzlies": {"city": "Memphis", "lat": 35.138, "lon": -90.050},
    "Miami Heat": {"city": "Miami", "lat": 25.781, "lon": -80.187},
    "Milwaukee Bucks": {"city": "Milwaukee", "lat": 43.045, "lon": -87.917},
    "Minnesota Timberwolves": {"city": "Minneapolis", "lat": 44.979, "lon": -93.276},
    "New Orleans Pelicans": {"city": "New Orleans", "lat": 29.949, "lon": -90.082},
    "New York Knicks": {"city": "New York", "lat": 40.750, "lon": -73.993},
    "Oklahoma City Thunder": {"city": "Oklahoma City", "lat": 35.463, "lon": -97.515},
    "Orlando Magic": {"city": "Orlando", "lat": 28.539, "lon": -81.383},
    "Philadelphia 76ers": {"city": "Philadelphia", "lat": 39.901, "lon": -75.166},
    "Phoenix Suns": {"city": "Phoenix", "lat": 33.445, "lon": -112.067},
    "Portland Trail Blazers": {"city": "Portland", "lat": 45.531, "lon": -122.666},
    "Sacramento Kings": {"city": "Sacramento", "lat": 38.580, "lon": -121.491},
    "San Antonio Spurs": {"city": "San Antonio", "lat": 29.426, "lon": -98.437},
    "Toronto Raptors": {"city": "Toronto", "lat": 43.643, "lon": -79.379},
    "Utah Jazz": {"city": "Salt Lake City", "lat": 40.768, "lon": -111.901},
    "Washington Wizards": {"city": "Washington, D.C.", "lat": 38.898, "lon": -77.020}
}
