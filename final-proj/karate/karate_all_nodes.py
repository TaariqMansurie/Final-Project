import networkx as nx
import matplotlib.pyplot as plt
import time

# Load Zachary's Karate Club graph
karate_graph = nx.karate_club_graph()

# Print basic information about the graph
print("Number of nodes:", karate_graph.number_of_nodes())
print("Number of edges:", karate_graph.number_of_edges())

# Implement PageRank and HITS algorithms
page_rank_scores = nx.pagerank(karate_graph)
hub_scores, authority_scores = nx.hits(karate_graph)

# Example implementation of PageRank and HITS algorithms
def compare_algorithms(graph, node):
    start_time = time.time()
    page_rank_scores = nx.pagerank(graph)
    page_rank_time = time.time() - start_time

    start_time = time.time()
    hub_scores, authority_scores = nx.hits(graph)
    hits_time = time.time() - start_time

    # Print or analyze the results here
# Print or analyze the results
    print("PageRank Scores:", page_rank_scores)
    print("Hub Scores:", hub_scores)
    print("Authority Scores:", authority_scores)

     # Print PageRank scores
    print("\nPageRank Scores:")
    for node, score in page_rank_scores.items():
        print(f"Node {node}: {score:.3f}")

    # Print Hub scores
    print("\nHub Scores:")
    for node, score in hub_scores.items():
        print(f"Node {node}: {score:.3f}")

    # Print Authority scores
    print("\nAuthority Scores:")
    for node, score in authority_scores.items():
        print(f"Node {node}: {score:.3f}")

    # Print computation times
    print("\nPageRank Computation Time:", page_rank_time, "seconds")
    print("HITS Computation Time:", hits_time, "seconds")

# Load your dataset into a NetworkX graph
graph = nx.karate_club_graph()

# You can visualize the graph if needed
nx.draw(graph, with_labels=True)
plt.show()

compare_algorithms(graph, node=2)