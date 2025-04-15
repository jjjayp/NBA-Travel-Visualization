import csv
from travel_optimizer import build_nba_graph

def load_schedule(csv_path):
    """
    Load NBA schedule data from a CSV file.
    Expects columns: Date, HomeTeam, AwayTeam.
    Returns a list of dictionaries.
    """
    schedule = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            schedule.append(row)
    return schedule

def analyze_team_schedule(team, schedule, graph):
    """
    For a given team, compute the total travel distance for all away games.
    For each away game, the travel distance is determined via the graph's shortest path (in miles) between the team's arena and the opponent's arena.
    
    Returns:
      - total_distance: Sum of distances for all away trips.
      - trips: List of tuples (AwayTeam, HomeTeam, distance).
        (Here we interpret "away game" as the team traveling from its own arena to the opponent’s arena.)
    """
    total_distance = 0
    trips = []
    sp = graph.shortest_path(team)
    for game in schedule:
        if game['AwayTeam'] == team:
            opponent = game['HomeTeam']
            distance = sp[opponent][1]
            total_distance += distance
            trips.append((team, opponent, distance))
    return total_distance, trips

def compare_schedule(team, schedule, graph):
    """
    Print an analysis report comparing the total optimal travel distance against the team's schedule.
    """
    total_distance, trips = analyze_team_schedule(team, schedule, graph)
    print(f"Total travel distance for {team} (away games): {total_distance:.2f} miles")
    for away, home, distance in trips:
        print(f"  {away} -> {home}: {distance:.2f} miles")

def rank_teams_by_travel_distance(schedule, graph):
    """
    For every team, compute the total travel distance for all away games and return a list of teams ranked by the total distance they fly (descending order). Returns a list of tuples (team, total_distance)
    """
    ranking = []
    # Iterate over every team
    for team in graph.vertices:
        total_distance, _ = analyze_team_schedule(team, schedule, graph)
        ranking.append((team, total_distance))
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

if __name__ == "__main__":
    # Build the graph, load the schedule
    graph = build_nba_graph()
    schedule = load_schedule("nba_schedule.csv")
    team_to_analyze = "Los Angeles Lakers"
    print(f"Mapping away games for {team_to_analyze}:")
    compare_schedule(team_to_analyze, schedule, graph)

    # Rank all teams by total away-game travel distance:
    ranking = rank_teams_by_travel_distance(schedule, graph)
    print("\nRank teams by total away-game travel distance:")
    for rank, (team, distance) in enumerate(ranking, start=1):
        print(f"{rank}. {team}: {distance:.2f} miles")
