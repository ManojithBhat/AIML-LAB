def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isinstance(node, int):  
        return node

    if maximizingPlayer:
        maxEva = float('-inf')  
        for child in node:
            eva = minimax(child, depth - 1, alpha, beta, False)
            maxEva = max(maxEva, eva)
            alpha = max(alpha, maxEva)
            if beta <= alpha:
                break  
        return maxEva

    else:
        minEva = float('inf')  
        for child in node:
            eva = minimax(child, depth - 1, alpha, beta, True)
            minEva = min(minEva, eva)
            beta = min(beta, minEva)
            if beta <= alpha:
                break  
        return minEva

def build_tree(flat_tree, depth):
    """Convert a flat array into a nested tree structure."""
    if depth == 0:
        return flat_tree.pop(0)  
    children = []
    for _ in range(2):  
        children.append(build_tree(flat_tree, depth - 1))
    return children

flattened_tree = list(map(int, input("Enter the flattened game tree (space-separated): ").split()))
depth = int(input("Enter the depth of the tree: "))

game_tree = build_tree(flattened_tree, depth)

evaluated_value = minimax(game_tree, depth, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)

print("Evaluated Value:", evaluated_value)


"""" sample test case :  3 5 6 9 1 2 0 -1 and depth of 3"""


"""

**Summary of Alpha-Beta Pruning**
*   Alpha-Beta Pruning is essentially an **advanced version of the Minimax algorithm**.
*   The primary goal is to **optimize the Minimax algorithm by reducing the number of nodes explored** in the game tree. Minimax explores all nodes to find the best path for the Max player. Alpha-beta pruning cuts off the search by exploring fewer nodes.
*   It achieves this by **pruning (cutting off) branches** that are not likely to influence the final decision. If a better path has already been found, the remaining paths are not explored.
*   **Alpha and Beta values**: Alpha is typically associated with Max nodes, representing the minimum score that the maximizing player is assured of, while Beta is associated with Min nodes, representing the maximum score that the minimizing player is assured of. Alpha values are taken in an increasing way while Beta values are considered in a decreasing way.
*   The algorithm uses **depth-first search** to traverse the game tree.
*   The **time complexity** of the Minimax algorithm is O(B^D), where B is the branching factor and D is the depth of the game tree. In the best or average case, Alpha-Beta Pruning can achieve a time complexity of O(B^(D/2)). However, in the worst case, it may still explore all nodes, resulting in O(B^D) complexity.

**Key Concepts and How Alpha-Beta Pruning Works**

1.  **Initialization**: Start with the initial values of alpha as negative infinity and beta as positive infinity (though the source mentions you don't strictly need to use +/- infinity).
2.  **Depth-First Traversal**: Explore the tree in a depth-first manner.
3.  **Updating Alpha Values (at Max nodes)**: The Max player aims to maximize the score. The alpha value represents the best (highest) score that the Max player can achieve so far. When visiting a Max node, update its alpha value if a child node returns a value greater than the current alpha.
4.  **Updating Beta Values (at Min nodes)**: The Min player aims to minimize the score. The beta value represents the best (lowest) score that the Min player can achieve so far. When visiting a Min node, update its beta value if a child node returns a value less than the current beta.
5.  **Pruning**: Pruning occurs when alpha is greater than or equal to beta (α >= β). This means that the current path will not lead to a better solution for either player, and the branch can be pruned.

    *   **Beta Cutoff**: At a Max node, if any child returns a value greater than or equal to the node's beta value, the remaining children can be pruned.
    *   **Alpha Cutoff**: At a Min node, if any child returns a value less than or equal to the node's alpha value, the remaining children can be pruned.

**Sample Viva Questions and Answers**

*   **Question**: Explain the core idea behind Alpha-Beta Pruning.
    *   **Answer**: Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes explored in the game tree by pruning branches that cannot possibly influence the final decision. It uses alpha and beta values to represent the best scores that the maximizing and minimizing players can achieve, respectively.
*   **Question**: How do Alpha and Beta values help in pruning?
    *   **Answer**: Alpha represents the minimum score that the Max player is guaranteed to achieve, while Beta represents the maximum score that the Min player is guaranteed to achieve. Pruning occurs when alpha becomes greater than or equal to beta (α >= β), indicating that the current branch is not worth exploring further because it won't lead to a better outcome for either player.
*   **Question**: What is the time complexity of Alpha-Beta Pruning, and how does it compare to Minimax?
    *   **Answer**: In the best or average case, Alpha-Beta Pruning has a time complexity of O(B^(D/2)), where B is the branching factor and D is the depth of the tree. This is a significant improvement over the Minimax algorithm's time complexity of O(B^D). However, in the worst case, Alpha-Beta Pruning may still have to explore all nodes, resulting in a time complexity of O(B^D).
*   **Question**: Explain the concept of Beta Cutoff with example.
    *   **Answer**: At a Max node, if we find a child node that returns a value greater than or equal to the current beta value of the Max node's ancestor (a Min node), it means the Min player will avoid this path. Therefore, we can prune the remaining children of the Max node because they will not influence the final decision. The source describes a case where a path guarantees a minimum value, so other paths are cut off.
*   **Question**: When should we use the Alpha-Beta pruning algorithm?
    *   **Answer**: We should use the Alpha-Beta pruning algorithm when we want to optimize the minimax algorithm, as Alpha-Beta is more efficient than the minimax algorithm. This makes it a better choice than the minimax algorithm.


"""