def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start a new row with '1'
        row = [1]
        # Add the values in the middle of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End the row with '1'
        row.append(1)
        triangle.append(row)

    return triangle

