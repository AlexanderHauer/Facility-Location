import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def bruteforce(points, r):
    best_center = None
    max_points_in_circle = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]

            # Calculate midpoint between points p1 and p2
            cx = (p1[0] + p2[0]) / 2
            cy = (p1[1] + p2[1]) / 2

            # Count how many points are inside the disc
            count = 0
            for p in points:
                if distance(p, (cx, cy)) <= r:
                    count += 1

            # Update the best center if this disc contains more points
            if count > max_points_in_circle:
                max_points_in_circle = count
                best_center = (cx, cy)

    return best_center

