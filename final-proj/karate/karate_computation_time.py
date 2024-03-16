import networkx as nx
import matplotlib.pyplot as plt
import time

# Load Zachary's Karate Club graph
karate_graph = nx.karate_club_graph()

# Print basic information about the graph
print("Number of nodes:", karate_graph.number_of_nodes())
print("Number of edges:", karate_graph.number_of_edges())

# Example implementation of PageRank and HITS algorithms for all nodes
def compare_algorithms_for_all_nodes(graph):
    # Initialize variables to store total computation times for each algorithm
    total_time_pagerank = 0
    total_time_hits = 0

    # Run the algorithms for each node
    num_iterations = 20
    for _ in range(num_iterations):
        # Implement PageRank algorithm
        start_time = time.time()
        page_rank_scores = nx.pagerank(graph)
        total_time_pagerank += time.time() - start_time

        # Implement HITS algorithm
        start_time = time.time()
        hub, authority = nx.hits(graph)
        total_time_hits += time.time() - start_time

    # Print total computation times for each algorithm
    print("Total computation time for PageRank across all nodes:", total_time_pagerank, "seconds")
    print("Total computation time for HITS across all nodes:", total_time_hits, "seconds")

# Compare algorithms for all nodes
compare_algorithms_for_all_nodes(karate_graph)