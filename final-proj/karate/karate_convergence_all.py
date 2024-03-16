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
    # Initialize dictionary to store convergence times for all nodes
    convergence_times = {'PageRank': [], 'HITS': []}

    # Run the algorithms and measure convergence time for each node
    num_iterations = 100
    tolerance = 1e-5  # Convergence threshold

    # Run the algorithms for stability analysis and convergence time for each node
    for node in graph.nodes():
        for _ in range(num_iterations):
            # Implement PageRank algorithm
            start_time = time.time()
            page_rank_scores = nx.pagerank(graph)
            convergence_times['PageRank'].append(time.time() - start_time)

            # Implement HITS algorithm
            start_time = time.time()
            hub, authority = nx.hits(graph)
            convergence_times['HITS'].append(time.time() - start_time)

    # Plot convergence time for all nodes
    plt.figure(figsize=(10, 5))
    plt.plot(range(num_iterations), convergence_times['PageRank'][:num_iterations], label="PageRank")
    plt.plot(range(num_iterations), convergence_times['HITS'][:num_iterations], label="HITS")
    plt.xlabel("Iteration")
    plt.ylabel("Convergence Time")
    plt.title("Convergence Time for All Nodes")
    plt.legend()
    plt.grid(True)
    plt.show()

# Compare algorithms for all nodes
compare_algorithms_for_all_nodes(karate_graph)