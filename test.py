def read_coordinates_from_file(file_path):
    # Initialize an empty list to store the tuples
    coordinates = []

    # Open the text file
    with open(file_path, 'r') as file:
        # Read each line
        for line in file:
            # Split the line by whitespace
            parts = line.split()
            # Extract x, y, w, and h values
            x1 = int(parts[1])
            y1 = int(parts[3])
            w = int(parts[5])
            h = int(parts[7])
            # Calculate x2 and y2
            x2 = x1 + w
            y2 = y1 + h
            # Append the tuple (x1, y1, x2, y2) to the list
            coordinates.append((x1, y1, x2, y2))

    # Return the list of tuples
    return coordinates


# Example usage
file_path = './groundtruth/sample_original/eng_03.txt'
coordinates = read_coordinates_from_file(file_path)
print(coordinates)
