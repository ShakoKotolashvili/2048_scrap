import numpy as np

# Initialize the grid
grid = np.array([[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]])

# Function to add a new tile to the grid
def add_tile():
    # Choose a random position for the new tile
    row = np.random.randint(4)
    col = np.random.randint(4)
    while grid[row, col] != 0:
        row = np.random.randint(4)
        col = np.random.randint(4)
    # Add the new tile to the grid
    grid[row, col] = np.random.choice([2, 4])

# Function to move the tiles on the grid
def move(direction):

    if direction == "up":
        # Move tiles up
        for c in range(4):
            col = grid[:, c]
            non_zero = col[col != 0]
            zeros = col[col == 0]
            grid[:, c] = np.concatenate((non_zero, zeros))
        # Merge tiles
        for r in range(3):
            for c in range(4):
                if grid[r, c] == grid[r+1, c] and grid[r, c] != 0:
                    grid[r, c] = 2*grid[r, c]
                    grid[r+1, c] = 0
                    # Shift tiles down
        for rr in range(r+1, 3):
            grid[rr, c] = grid[rr+1, c]
        grid[3, c] = 0
        #add tile to the grid
        add_tile()



    elif direction == "down":
        # Move tiles down
        for c in range(4):
            col = grid[:, c]
            non_zero = col[col != 0]
            zeros = col[col == 0]
            grid[:, c] = np.concatenate((zeros, non_zero))
        # Merge tiles
        for r in range(3, 0, -1):
            for c in range(4):
                if grid[r, c] == grid[r-1, c] and grid[r, c] != 0:
                    grid[r, c] = 2*grid[r, c]
                    grid[r-1, c] = 0
                    # Shift tiles up
        for rr in range(r-1, 0, -1):
            grid[rr, c] = grid[rr-1, c]
        grid[0, c] = 0
        add_tile()


    elif direction == "left":
        # Move tiles left
        for r in range(4):
            row = grid[r, :]
            non_zero = row[row != 0]
            zeros = row[row == 0]
            grid[r, :] = np.concatenate((non_zero, zeros))
        # Merge tiles
        for c in range(3):
            for r in range(4):
                if grid[r, c] == grid[r, c + 1] and grid[r, c] != 0:
                    grid[r, c] = 2 * grid[r, c]
                    grid[r, c + 1] = 0
        # Shift tiles right
        for cc in range(c + 1, 3):
            grid[r, cc] = grid[r, cc + 1]
        grid[r, 3] = 0
        add_tile()


    elif direction == "right":
        # Move tiles right
        for r in range(4):
            row = grid[r, :]
            non_zero = row[row != 0]
            zeros = row[row == 0]
            grid[r, :] = np.concatenate((zeros, non_zero))
        # Merge tiles
        for c in range(3, 0, -1):
            for r in range(4):
                if grid[r, c] == grid[r, c - 1] and grid[r, c] != 0:
                    grid[r, c] = 2 * grid[r, c]
                    grid[r, c - 1] = 0
        # Shift tiles left
        for cc in range(c - 1, 0, -1):
            grid[r, cc] = grid[r, cc - 1]
        grid[r, 0] = 0
        add_tile()



# Add a new tile to the grid
add_tile()

# Main game loop
while True:
    # Print the current state of the grid
    print(grid)

    # Get the player's next move
    direction = input("Enter move (up, down, left, right): ")

    # Move the tiles on the grid
    move(direction)
