#Task 1: Code of "A* Algorithm"
import heapq
class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
class Astar:
    def __init__(self, start, end, graph):
        self.graph = graph 
        self.start = start
        self.goal = goal
    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    def reconstruct_path(self, current_node):
        path = []
        while current_node:
            path.append(current_node.name)
            current_node = current_node.parent
        return path[::-1]
    def run(self):
        open_list = []
        closed_list = set()
        start_node = Node(self.start)
        goal_node = Node(self.goal)
        heapq.heappush(open_list, start_node)
        while open_list:
            current_node = heapq.heappop(open_list)
            if current_node.name ==goal_node.name:
                return self.reconstruct_path(current_node)
            closed_list.add(current_node.name)
            for neighbor in self.get_neighbors(current_node.name):
                if neighbor in closed_list:
                    continue
                g_cost = current_node.g + 1
                h_cost = self.heuristic(neighbor)
                neighbor_node = Node(neighbor, current_node, g_cost, h_cost)
                if not any(node.name == neighbor_node.name and node.f <= neighbor_node.f for node in open_list):
                    heapq.heappush(open_list, neighbor_node)
        return None
graph = { 
    (0, 0): [(1, 1), (1, 2)],
    (1, 0): [(0, 0), (2, 0), (1, 1), (1, 2)],
    (2, 0): [(1, 0), (3, 0), (1, 1), (1, 2)],
    (3, 0): [(2, 0), (1, 1), (1, 2)],
}
start = (1, 0)
goal = (3, 0)
astar = Astar(graph, start, goal)
path = astar.run()
print("Path found:", path)

