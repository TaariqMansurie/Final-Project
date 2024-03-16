# import networkx as nx
# import matplotlib.pyplot as plt

# # Load Zachary's Karate Club graph
# karate_graph = nx.davis_southern_women_graph()

# # Print basic information about the graph
# print("Number of nodes:", karate_graph.number_of_nodes())
# print("Number of edges:", karate_graph.number_of_edges())

# # Example implementation of PageRank and HITS algorithms for all nodes
# def compare_algorithms_for_all_nodes(graph):
#     # Initialize dictionary to store convergence times for all nodes
#     convergence_times = {node: {'PageRank': [], 'HITS': []} for node in graph.nodes()}

#     # Run the algorithms and measure convergence time for each node
#     num_iterations = 100
#     tolerance = 1e-5  # Convergence threshold

#     for node in graph.nodes():
#         # Initialize scores for current node
#         prev_page_rank_score = None
#         prev_hub_score = None
#         prev_authority_score = None

#         # PageRank algorithm
#         for _ in range(num_iterations):
#             page_rank_scores = nx.pagerank(graph)
#             if prev_page_rank_score is not None and abs(prev_page_rank_score - page_rank_scores[node]) < tolerance:
#                 break
#             prev_page_rank_score = page_rank_scores[node]
#             convergence_times[node]['PageRank'].append(_)

#         # HITS algorithm
#         for _ in range(num_iterations):
#             hub, authority = nx.hits(graph)
#             if (
#                 prev_hub_score is not None and
#                 prev_authority_score is not None and
#                 abs(prev_hub_score - hub[node]) < tolerance and
#                 abs(prev_authority_score - authority[node]) < tolerance
#             ):
#                 break
#             prev_hub_score = hub[node]
#             prev_authority_score = authority[node]
#             convergence_times[node]['HITS'].append(_)

#     # Aggregate convergence times for all nodes
#     all_page_rank_times = [time for node_times in convergence_times.values() for time in node_times['PageRank']]
#     all_hits_times = [time for node_times in convergence_times.values() for time in node_times['HITS']]

#     # Plot convergence time for all nodes
#     plt.figure(figsize=(10, 5))
#     plt.plot(all_page_rank_times, label="PageRank")
#     plt.plot(all_hits_times, label="HITS")
#     plt.xlabel("Iteration")
#     plt.ylabel("Convergence Time")
#     plt.title("Convergence Time for All Nodes")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Compare algorithms for all nodes
# compare_algorithms_for_all_nodes(karate_graph)

import networkx as nx
import matplotlib.pyplot as plt
import time

# Load Davis Southern Women Graph
davis_women_graph = nx.davis_southern_women_graph()

# Print basic information about the graph
print("Number of nodes:", davis_women_graph.number_of_nodes())
print("Number of edges:", davis_women_graph.number_of_edges())

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
compare_algorithms_for_all_nodes(davis_women_graph)



