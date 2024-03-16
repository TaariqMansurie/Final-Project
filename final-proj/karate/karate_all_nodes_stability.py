import networkx as nx
import matplotlib.pyplot as plt

# Load Karate Club graph
karate_graph = nx.karate_club_graph()

# Example implementation of PageRank and HITS algorithms for stability analysis
def stability_analysis(graph):
    # Initialize lists to store scores for each iteration
    page_rank_scores = []
    hub_scores = []
    authority_scores = []

    # Run the algorithms for stability analysis for a fixed number of iterations
    num_iterations = 100
    for _ in range(num_iterations):
        # Implement PageRank algorithm
        page_rank = nx.pagerank(graph)
        page_rank_scores.append(list(page_rank.values()))

        # Implement HITS algorithm
        hits = nx.hits(graph)
        hub_scores.append(list(hits[0].values()))
        authority_scores.append(list(hits[1].values()))

    # Calculate the average score across all nodes for each iteration
    avg_page_rank_scores = [sum(iteration) / len(graph.nodes) for iteration in zip(*page_rank_scores)]
    avg_hub_scores = [sum(iteration) / len(graph.nodes) for iteration in zip(*hub_scores)]
    avg_authority_scores = [sum(iteration) / len(graph.nodes) for iteration in zip(*authority_scores)]

    # Print average scores
    print("Average PageRank Scores:", avg_page_rank_scores)
    print("Average Hub Scores:", avg_hub_scores)
    print("Average Authority Scores:", avg_authority_scores)

    # Plot stability analysis for all iterations
    plt.figure(figsize=(10, 5))
    # plt.plot(range(len(avg_page_rank_scores)), avg_page_rank_scores, label="PageRank")
    # plt.plot(range(len(avg_hub_scores)), avg_hub_scores, label="Hub")
    # plt.plot(range(len(avg_authority_scores)), avg_authority_scores, label="Authority")
    plt.plot(np.linspace(0, num_iterations - 1, len(avg_page_rank_scores)), avg_page_rank_scores, label="PageRank")
    plt.plot(np.linspace(0, num_iterations - 1, len(avg_hub_scores)), avg_hub_scores, label="Hub")
    plt.plot(np.linspace(0, num_iterations - 1, len(avg_authority_scores)), avg_authority_scores, label="Authority")
    plt.xlabel("Iteration")
    plt.ylabel("Average Score")
    plt.title("Stability Analysis for All Nodes")
    plt.xticks(np.arange(0, num_iterations, 10))  # Set x-axis ticks at intervals of 10

    plt.legend()
    plt.grid(True)
    plt.show()

# Perform stability analysis for all nodes in the Karate Club graph
stability_analysis(karate_graph)
