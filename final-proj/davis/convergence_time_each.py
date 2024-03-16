# import networkx as nx
# import matplotlib.pyplot as plt
# import time

# # Load Davis Southern Women Graph
# davis_women_graph = nx.davis_southern_women_graph()

# # Print basic information about the graph
# print("Number of nodes:", davis_women_graph.number_of_nodes())
# print("Number of edges:", davis_women_graph.number_of_edges())

# # Example implementation of PageRank and HITS algorithms for all nodes
# def compare_algorithms_for_all_nodes(graph):
#     # Initialize dictionary to store convergence times for all nodes
#     convergence_times = {node: {'PageRank': [], 'HITS': []} for node in graph.nodes()}

#     # Run the algorithms and measure convergence time for each node
#     num_iterations = 100
#     tolerance = 1e-5  # Convergence threshold

#     # Run the algorithms for stability analysis and convergence time for each node
#     for node in graph.nodes():
#         for _ in range(num_iterations):
#             # Implement PageRank algorithm
#             start_time = time.time()
#             page_rank_scores = nx.pagerank(graph)
#             convergence_times[node]['PageRank'].append(time.time() - start_time)

#             # Implement HITS algorithm
#             start_time = time.time()
#             hub, authority = nx.hits(graph)
#             convergence_times[node]['HITS'].append(time.time() - start_time)

#     # Plot convergence time for each node
#     plt.figure(figsize=(10, 5))
#     for node, times in convergence_times.items():
#         plt.plot(range(num_iterations), times['PageRank'][:num_iterations], label=f"PageRank Node {node}")
#         plt.plot(range(num_iterations), times['HITS'][:num_iterations], label=f"HITS Node {node}")
#     plt.xlabel("Iteration")
#     plt.ylabel("Convergence Time")
#     plt.title("Convergence Time for Each Node")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Compare algorithms for all nodes
# compare_algorithms_for_all_nodes(davis_women_graph)


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
    # Run the algorithms and measure convergence time for each node
    num_iterations = 100
    tolerance = 1e-5  # Convergence threshold

    # Run the algorithms for stability analysis and convergence time for each node
    for node in graph.nodes():
        page_rank_times = []
        hits_times = []
        for _ in range(num_iterations):
            # Implement PageRank algorithm
            start_time = time.time()
            page_rank_scores = nx.pagerank(graph)
            page_rank_times.append(time.time() - start_time)

            # Implement HITS algorithm
            start_time = time.time()
            hub, authority = nx.hits(graph)
            hits_times.append(time.time() - start_time)

        # Print convergence time for each node
        print(f"Node {node} - Convergence Time (PageRank): {page_rank_times}")
        print(f"Node {node} - Convergence Time (HITS): {hits_times}")

        # Plot convergence time for each node
        plt.figure(figsize=(10, 5))
        plt.plot(range(num_iterations), page_rank_times, label="PageRank")
        plt.plot(range(num_iterations), hits_times, label="HITS")
        plt.xlabel("Iteration")
        plt.ylabel("Convergence Time")
        plt.title(f"Convergence Time for Node {node}")
        plt.legend()
        plt.grid(True)
        plt.show()

# Compare algorithms for all nodes
compare_algorithms_for_all_nodes(davis_women_graph)
