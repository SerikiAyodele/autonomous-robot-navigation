# Define the obstacle locations
OBSTACLES = [(2, 2), (3, 3), (4, 4), (5, 5)]

# Define the robot class
class Robot:
    # ... (Code for the Robot class remains the same as in the previous section) ...

    def a_star(self):
        # ... (Code for the A* algorithm remains the same as in the previous section) ...
        
        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                # ... (Code for reconstructing the path remains the same as in the previous section) ...

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor in OBSTACLES:
                    continue  # Skip if the neighbor is an obstacle

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # ... (Code for updating the g and f scores






