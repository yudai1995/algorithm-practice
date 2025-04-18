data = [12, 3, 17, 5, 8]

print('Before sorting:', data)

# Bubble Sort Algorithm
# Time : n(n-1)/2
# Time Complexity: O(n^2)
n = len(data)
for i in range(n, 1, -1):
    for j in range(0, i-1, 1):
        if data[j] < data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            print(f'Compared {data[j+1]} and {data[j]} => {data}')

print('After sorting:', data)
