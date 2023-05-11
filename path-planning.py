import heapq
import math

# Define the grid size
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Define the robot class
class Robot:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def heuristic(self, a, b):
        # Calculate the Euclidean distance between two points
        return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

    def get_neighbors(self, point):
        # Generate the neighboring points
        x, y = point
        neighbors = []
        if x < GRID_WIDTH - 1:
            neighbors.append((x + 1, y))
        if x > 0:
            neighbors.append((x - 1, y))
        if y < GRID_HEIGHT - 1:
            neighbors.append((x, y + 1))
        if y > 0:
            neighbors.append((x, y - 1))
        return neighbors

    def a_star(self):
        # Initialize the open and closed sets
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                # Reconstruct the path when the goal is reached
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update the g and f scores
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None  # No path found

# Create a robot instance
start = (0, 0)
goal = (9, 9)
robot = Robot(start, goal)

# Find the path using A*
path = robot.a_star()

if path:
    print("Path found:")
    for point in path:
        print(point)
else:
    print("No path found.")
