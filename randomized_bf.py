import math
import random


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def rand_bruteforce(points, r):
    # This is very similar to the bruteforce, except the points are randomly sampled
    best_center = None
    max_points_in_circle = 0
    sample_size = int(len(points)/100)
    random_points=list(random.sample(list(points), sample_size))

    for i in range(len(random_points)):
        for j in range(i + 1, len(random_points)):
            p1, p2 = random_points[i], random_points[j]

            # Calculate midpoint between points p1 and p2
            cx = (p1[0] + p2[0]) / 2
            cy = (p1[1] + p2[1]) / 2

            # Count how many points are inside the disc
            count = 0
            for p in random_points:
                if distance(p, (cx, cy)) <= r:
                    count += 1

            # Update the best center if this disc contains more points
            if count > max_points_in_circle:
                max_points_in_circle = count
                best_center = (cx, cy)

    return best_center

