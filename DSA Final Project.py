#DSA Code 

import pandas as pd
from heapq import heappush, heappop

# Loading data from a CSV file
data = pd.read_csv("Graph Structure.csv")

# Constructing the graph
edges = {}
for index, row in data.iterrows():
    start, end, distance = row["Start"], row["End"], row["Distance"]
    if start not in edges:
        edges[start] = []
    if end not in edges:  
        edges[end] = []
    edges[start].append((end, distance))
    edges[end].append((start, distance))  

# Dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
                
    return distances

# Function showing the shortest path from a starting node to all charging stations.
def main():
    charging_stations = ['H', 'K', 'Q', 'T']
    
    while True:
        start_node = input("\nEnter the start node (or type 'exit' to quit): ").strip()
        
        # Allowing the user to exit the loop
        if start_node.lower() == 'exit':
            print("Exiting program.")
            break
        
        if start_node not in edges:
            print(f"Node {start_node} not found in the graph. Please enter a valid node.")
            continue
        
        distances = dijkstra(edges, start_node)
        
        
        print(f"\nShortest paths from {start_node} to each charging station:")
        min_distance = float('inf')
        nearest_station = None
        for station in charging_stations:
            distance = distances.get(station, float('inf'))
            if distance < float('inf'):
                print(f" - To {station}: {distance} units")
                if distance < min_distance:
                    min_distance = distance
                    nearest_station = station
            else:
                print(f" - To {station}: No path found or unreachable")

        if nearest_station is not None:
            print(f"\nThe nearest charging station from {start_node} is {nearest_station}, at {min_distance} units distance.")
        else:
            print("\nNo charging station is reachable from the starting node.")

if __name__ == "__main__":
    main()

