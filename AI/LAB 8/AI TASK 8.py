#Task 1: Code of "Min Max Algorithm
import math 
def min_max(depth, node, alpha, beta, maximizingPlayer):
    if depth == 0:
        return node
    if maximizingPlayer:
        maxEval = -math.inf
        for child in node.children:
            eval = min_max(depth-1, child, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
            return maxEval
        else:
            return maxEval
    else:
        minEval = math.inf
        for child in node.children:
            eval = min_max(depth-1, child, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break 
            return minEval
        else:
            return minEval 
        
