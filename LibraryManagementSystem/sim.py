import random
import matplotlib.pyplot as plt
import numpy as np # For drawing the circle

def estimate_pi_with_visualization_data(num_points):
    """
    Estimates Pi using a Monte Carlo simulation and collects data for visualization.

    Args:
        num_points (int): The total number of random points (darts) to generate.

    Returns:
        tuple: (pi_estimate, points_inside_x, points_inside_y, points_outside_x, points_outside_y)
               pi_estimate (float): The estimated value of Pi.
               points_inside_x (list): List of x-coordinates of points inside the circle.
               points_inside_y (list): List of y-coordinates of points inside the circle.
               points_outside_x (list): List of x-coordinates of points outside the circle (but inside square).
               points_outside_y (list): List of y-coordinates of points outside the circle (but inside square).
    """
    if num_points <= 0:
        return 0.0, [], [], [], []

    points_inside_circle_count = 0
    points_inside_x, points_inside_y = [], []
    points_outside_x, points_outside_y = [], []

    # We'll simulate throwing darts at a square that goes from
    # x = -1 to 1 and y = -1 to 1.
    # The circle inside this square will have a radius of 1, centered at (0,0).

    for _ in range(num_points):
        # Generate a random x and y coordinate between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Calculate the squared distance of the point from the origin (0,0)
        # The distance formula is sqrt(x^2 + y^2).
        # If distance_squared <= radius_squared (which is 1*1 = 1),
        # the point is inside or on the circle of radius 1.
        distance_squared = x**2 + y**2

        if distance_squared <= 1: # Point is inside or on the circle
            points_inside_circle_count += 1
            points_inside_x.append(x)
            points_inside_y.append(y)
        else: # Point is outside the circle but within the square
            points_outside_x.append(x)
            points_outside_y.append(y)

    # Calculate Pi based on the ratio: pi / 4 = points_inside / total_points
    if num_points == 0: # Should be caught by the initial check, but good for robustness
        pi_estimate = 0.0
    else:
        pi_estimate = 4 * (points_inside_circle_count / num_points)
        
    return pi_estimate, points_inside_x, points_inside_y, points_outside_x, points_outside_y

# --- Main part of the script ---

# Get the number of darts from user input
while True:
    try:
        number_of_darts_str = input("Enter the number of darts to simulate (e.g., 1000): ")
        number_of_darts = int(number_of_darts_str) # Convert the input string to an integer
        if number_of_darts > 0:
            if number_of_darts > 50000: # Warn if too many points for plotting
                print("Warning: Plotting a very large number of points might be slow and make the plot dense.")
            break # Exit the loop if input is a positive integer
        else:
            print("Please enter a positive number for the darts.")
    except ValueError:
        print("Invalid input. Please enter a whole number (integer).")

# --- Run the simulation ---
# Unpack the returned values from the function
estimated_value_of_pi, inside_x, inside_y, outside_x, outside_y = \
    estimate_pi_with_visualization_data(number_of_darts)

# --- Print the result ---
print(f"the value of pi is {estimated_value_of_pi} based on a simulation with {number_of_darts} darts.")

# --- Create the visualization ---
if number_of_darts > 0 : # Only attempt to plot if there are points
    # Create a figure and an axes object (the plot area)
    # figsize=(8, 8) makes the plot window 8x8 inches.
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot points inside the circle
    # 's' controls the marker size
    ax.scatter(inside_x, inside_y, color='blue', s=5, label=f'Inside Circle ({len(inside_x)})')

    # Plot points outside the circle
    ax.scatter(outside_x, outside_y, color='red', s=5, label=f'Outside Circle ({len(outside_x)})')

    # Draw the circle
    # We generate points for a smooth circle: (x = r*cos(theta), y = r*sin(theta))
    # Radius r=1 for our unit circle
    circle_angles = np.linspace(0, 2 * np.pi, 150) # 150 points for a smooth curve
    circle_x = np.cos(circle_angles) # Radius is 1, so r*cos(theta) is just cos(theta)
    circle_y = np.sin(circle_angles) # Radius is 1, so r*sin(theta) is just sin(theta)
    ax.plot(circle_x, circle_y, color='green', linewidth=2, label='Unit Circle Boundary')

    # Draw the square boundaries
    # The square extends from -1 to 1 on both axes
    square_x_coords = [-1, 1, 1, -1, -1] # X-coordinates for the corners of the square
    square_y_coords = [-1, -1, 1, 1, -1] # Y-coordinates for the corners of the square
    ax.plot(square_x_coords, square_y_coords, color='black', linewidth=2, label='Square Boundary')

    # Set plot properties
    ax.set_title(f'Monte Carlo Estimation of Pi with {number_of_darts} Darts')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')

    # Set the limits of the plot to be slightly larger than the square
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)

    # Ensure the plot is square (circle doesn't look like an ellipse)
    ax.set_aspect('equal', adjustable='box')

    ax.legend() # Display the legend (labels for plotted elements)
    ax.grid(True, linestyle='--', alpha=0.7) # Add a grid for better readability

    plt.show() # Display the plot window
else:
    print("No points were generated, so no plot will be displayed.")