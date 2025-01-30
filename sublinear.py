# An attempt for a sublinear geometric method. Although it is not truly sublinear, yet
import numpy as np
import random


def sublinear_geometry(points, r, sample_size):
    # Randomly sample a subset of points
    sampled_points = randomized_sampling(points, sample_size)

    # Compute the center of the sampled points
    center = compute_center(sampled_points)

    return center


def randomized_sampling(points, sample_size):
    points_list = list(points)  # Make sure it's a list
    return random.sample(points_list, sample_size)


def compute_center(points):
    # Compute the centroid of the given set of points.
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    center_x = np.mean(x_coords)
    center_y = np.mean(y_coords)

    return center_x, center_y



