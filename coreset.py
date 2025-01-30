# this is a previously used method, but I decided to cut it out of the project because the sublinear one was better

import random


def center_finder(points, r, sample_size):
    # Step 1: Create the coreset by sampling points
    coreset = create_coreset(points, sample_size, r)

    # Step 2: Use weighted k-means (or another method) to find the center
    center = weighted_k_means(coreset)

    return center


def create_coreset(points, sample_size, r):
    # Compute the center (mean of all points) as a first approximation
    center = (sum(x for x, y in points) / len(points), sum(y for x, y in points) / len(points))

    # Calculate distance from center to each point
    distances = [(point, ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5) for point in points]

    # Sort points by distance (to give higher probability to farther points)
    distances.sort(key=lambda x: x[1], reverse=True)

    # Sampling points from the sorted list
    sampled_points = random.choices([p[0] for p in distances], k=sample_size)

    return sampled_points


def weighted_k_means(points, k=1):
    # Initialize centroids randomly
    centroid = random.choice(points)

    # Run k-means iteration (just one since we only need one centroid)
    for _ in range(100):  # Limit iterations to prevent infinite loops
        clusters = {i: [] for i in range(k)}

        # Assign points to the closest centroid
        for point in points:
            dist = ((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2) ** 0.5
            clusters[0].append((point, dist))

        # Update centroids (average of assigned points)
        new_centroid = (sum(p[0] for p, _ in clusters[0]) / len(clusters[0]),
                        sum(p[1] for p, _ in clusters[0]) / len(clusters[0]))

        # Compare the centroids by checking if the components are the same
        if abs(new_centroid[0] - centroid[0]) < 1e-6 and abs(new_centroid[1] - centroid[1]) < 1e-6:
            break

        centroid = new_centroid

    return centroid



