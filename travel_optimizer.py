import math
from graph import Graph
from nba_arena_data import load_arena_data, NBA_ARENAS


def haversine(lat1, lon1, lat2, lon2):
    """
    Compute the great-circle distance between two points on Earth specified in degrees.
    Returns the distance in miles.
    """
    R = 6371.0 # Earth's radius
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_km = R * c
    return distance_km * 0.621371  # Convert to miles

def build_nba_graph():
    """
    Build and return a Graph of NBA arenas.
    Vertices are team names; edges are weighted by the distance between arenas based on their geographic coordinates.
    Build a complete graph connecting every pair.
    """
    arena_data = load_arena_data()
    teams = list(arena_data.keys())

    edges = []
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            team_a = teams[i]
            team_b = teams[j]
            coord_a = arena_data[team_a]
            coord_b = arena_data[team_b]
            distance = haversine(coord_a["lat"], coord_a["lon"], coord_b["lat"], coord_b["lon"])
            edges.append((team_a, team_b, distance))
    g = Graph(V=teams, E=edges)
    g.arena_data = arena_data
    return g

def get_optimal_route(graph, start_team, end_team, algorithm='shortest'):
    """
    Get the optimal travel route between two NBA teams.
    
    Returns:
      - path: A list of teams representing the route.
      - details: The dictionary returned from the respective traversal method.
    """
    if algorithm == 'shortest':
        result = graph.shortest_path(start_team)
        pred = {v: info[0] for v, info in result.items()}
    elif algorithm == 'fewest':
        result = graph.fewest_flights(start_team)
        pred = result
    else:
        raise ValueError("Algorithm must be 'shortest' or 'fewest'.")

    # Reconstruct the path from end_team back to start_team.
    path = []
    current = end_team
    while current is not None:
        path.insert(0, current)
        current = pred[current]
    return path, result
