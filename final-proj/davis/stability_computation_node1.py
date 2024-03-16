import networkx as nx
import matplotlib.pyplot as plt
import time

# Load Davis Southern Women graph
women_graph = nx.davis_southern_women_graph()

# Print basic information about the graph
print("Number of nodes:", women_graph.number_of_nodes())
print("Number of edges:", women_graph.number_of_edges())

# Example implementation of PageRank and HITS algorithms
def compare_algorithms_for_node(graph, node):
    # Initialize lists to store convergence time and scores for the specified node
    page_rank_times = []
    hits_times = []
    page_rank_scores = []
    hub_scores = []
    authority_scores = []

    # Run the algorithms multiple times to measure stability and convergence time
    num_iterations = 20
    for _ in range(num_iterations):
        # Implement PageRank algorithm
        start_time = time.time()
        page_rank_scores.append(nx.pagerank(graph)[node])
        page_rank_times.append(time.time() - start_time)

        # Implement HITS algorithm
        start_time = time.time()
        hub, authority = nx.hits(graph)
        hub_scores.append(hub[node])
        authority_scores.append(authority[node])
        hits_times.append(time.time() - start_time)

    # Print stability analysis for the specified node
    print("\nStability Analysis:")
    print("PageRank Scores for Node", node, ":", page_rank_scores)
    print("Hub Scores for Node", node, ":", hub_scores)
    print("Authority Scores for Node", node, ":", authority_scores)

    # Print convergence time analysis for the specified node
    print("\nConvergence Time Analysis:")
    print("PageRank Computation Times for Node", node, ":", page_rank_times)
    print("HITS Computation Times for Node", node, ":", hits_times)

    # Plot stability analysis for node 2
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_iterations + 1), page_rank_scores, label="PageRank")
    plt.plot(range(1, num_iterations + 1), hub_scores, label="Hub")
    plt.plot(range(1, num_iterations + 1), authority_scores, label="Authority")
    plt.xlabel("Iteration")
    plt.ylabel("Score")
    plt.title(f"Stability Analysis for Node {node}")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot convergence time for the specified node
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_iterations + 1), page_rank_times, label="PageRank")
    plt.plot(range(1, num_iterations + 1), hits_times, label="HITS")
    plt.xlabel("Iteration")
    plt.ylabel("Computation Time (seconds)")
    plt.title(f"Computation Time for Node {node}")
    plt.legend()
    plt.grid(True)
    plt.show()

# Compare algorithms for node 2 in the Davis Southern Women graph
compare_algorithms_for_node(women_graph, node="Evelyn Jefferson")
