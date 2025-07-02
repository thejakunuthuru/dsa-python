def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                continue
            else:
                sum += matrix[i][j]
    return sum

def diagonal_sum2(matrix):
    # Initialize the sum to 0
    total = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
 
    return total

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
print(diagonal_sum(myList2D)) # 15