# This was an attempt of the same sublinear method used in the M. Monemizadeh paper
# It needs more debugging before full implementation

import numpy as np
import random


def sublinear_facility_location(points, r, sample_size, grid_levels):
    n = max(max(x, y) for x, y in points)
    grids = generate_grids(n, grid_levels)
    sampled_cells = sample_cells(grids, sample_size)
    valid_cells = identify_valid_cells(sampled_cells, points)

    if not valid_cells:  # Prevent division by zero
        return None

    facility_locations = []

    for cell in valid_cells:
        _, location = solve_local_facility(cell, points, r)
        facility_locations.append(location)

    if facility_locations:
        # Compute the centroid of all selected facility locations
        center_x = sum(loc[0] for loc in facility_locations) / len(facility_locations)
        center_y = sum(loc[1] for loc in facility_locations) / len(facility_locations)
        print("balls")
        return (center_x, center_y)
    else:
        print("Total Sampled Cells:", len(sampled_cells))
        print("Valid Cells Found:", len(valid_cells))
        if not valid_cells:
            print("Warning: No valid cells found!")

        return None  # If no valid facilities were found


def generate_grids(n, levels):
    # Generate increasing grid sizes
    grids = []
    for level in range(levels):
        cell_size = n / (2 ** level)
        grids.append(cell_size)
    return grids


def sample_cells(grids, sample_size):
    # Randomly sample cells
    sampled_cells = set()
    for grid_size in grids:
        for _ in range(sample_size // len(grids)):
            x = random.randint(0, int(grid_size) - 1) * grid_size
            y = random.randint(0, int(grid_size) - 1) * grid_size
            sampled_cells.add((x, y, grid_size))
    return sampled_cells


def identify_valid_cells(sampled_cells, points):
    # Finding which cells include at least one point
    valid_cells = []
    for cell in sampled_cells:
        x, y, size = cell
        if any(x <= px < x + size and y <= py < y + size for px, py in points):
            valid_cells.append(cell)
    return valid_cells


def solve_local_facility(cell, points, r):
    x, y, size = cell
    cell_points = [(px, py) for px, py in points if x <= px < x + size and y <= py < y + size]

    if not cell_points:
        return float('inf'), None

    center_x = np.mean([p[0] for p in cell_points])
    center_y = np.mean([p[1] for p in cell_points])
    cost = sum(np.linalg.norm(np.array([px, py]) - np.array([center_x, center_y])) for px, py in cell_points)

    return cost, (center_x, center_y)

