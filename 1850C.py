t = int(input())
for _ in range(t):
    grid = [input() for _ in range(8)]
    
    result = ""
    for col in range(8):
        for row in range(8):
            if grid[row][col] != '.':
                result += grid[row][col]
    
    print(result)