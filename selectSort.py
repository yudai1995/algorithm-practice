data = [12, 3, 17, 5, 8]

n = len(data)
print('Before sorting:', data)

# Selection Sort Algorithm
# Time : n(n-1)/2
# Time Complexity: O(n^2)
for i in range(0, n-1, 1):
    max_index = i
    for j in range(i+1, n, 1):
        if data[j] > data[max_index]:
            max_index = j
    data[i], data[max_index] = data[max_index], data[i]
    print(f'Compared {data[i]} and {data[max_index]} => {data}')
