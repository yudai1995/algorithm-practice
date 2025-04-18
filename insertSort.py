data = [12, 3, 17, 5, 8]

# Insertion Sort Algorithm
# Time : n(n-1)/2
# Time Complexity: O(n^2)
print('Before sorting:', data)

n = len(data)
for i in range(1, n, 1):
    key = data[i]
    j = i - 1
    while j >= 0 and key > data[j]:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
    print(f'Inserted {key} at position {j + 1} => {data}')
