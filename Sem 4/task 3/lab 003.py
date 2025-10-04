def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    start = (0, 0)
    visited = set()
    path = []
    def dfs(state):
        x, y = state
        if x == target or y == target:
            path.append(state)
            return True
        visited.add(state)
        path.append(state)
        possible_states = [
            (jug1_capacity, y),
            (x, jug2_capacity),
            (0, y),
            (x, 0),
            (x - min(x, jug2_capacity - y), y + min(x,jug2_capacity - y)),
            (x + min(y, jug1_capacity - x), y - min(y , jug1_capacity - x))
        ]
        for next_state in possible_states:
            if next_state not in visited:
                if dfs(next_state):
                    return True
        path.pop()
        return False
    if dfs(start):
        return path
    else:
        return None
if __name__ == "__main__":
    jug1 = 4
    jug2 = 3
    target = 2
    solution = water_jug_dfs(jug1, jug2, target)
    if solution:
        print("Solution path(DFS):")
        for step in solution:
            print(step)
    else:
        print("no solution found")
         