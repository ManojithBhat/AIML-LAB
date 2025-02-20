def minimax(node, depth, alpha,beta, maximisingPlayer):

    if depth == 0 or isinstance(node,int):
        return node
    
    if maximisingPlayer:
        maxEval = float("-inf")
        for child in node:
            eval = minimax(child,depth-1,alpha,beta,False)
            maxEval = max(maxEval,eval)
            alpha = max(alpha,maxEval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float("inf")
        for child in node:
            eval = minimax(child,depth-1,alpha,beta,True)
            minEval = min(minEval,eval)
            beta = min(beta,minEval)
            if beta <= alpha:
                break
        return minEval

def make_tree(flat_tree,depth):
    if depth == 0:
        return flat_tree.pop(0)
    childern = []
    for _ in range(2):
        childern.append(make_tree(flat_tree,depth-1))
    return childern

flat_list = list(map(int,input("Enter the values of the tree as the flatlist separated by spaces ").split(' ')))

depth = int(input("Enter the depth of the serch to be done : "))
tree = make_tree(flat_list,depth)

value = minimax(tree,depth,alpha=float("-inf"),beta=float("inf"),maximisingPlayer = True)
print(value)

