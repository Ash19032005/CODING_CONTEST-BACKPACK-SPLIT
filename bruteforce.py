def allocate_books_brute_force(arr, n, m):
    if m > n:
        return -1
    min_max_weight = float('inf')
    min_max_weight_allocation = -1
    for mid in range(max(arr), sum(arr) + 1):
        book_allocated = 0
        student = 1
        for i in range(len(arr)):
            if book_allocated + arr[i] <= mid:
                book_allocated += arr[i]
            else:
                student += 1
                book_allocated = arr[i]
        if student <= m:
            if mid < min_max_weight:
                min_max_weight = mid
                min_max_weight_allocation = mid
    return min_max_weight_allocation
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        # Read the total number of elements from the first line
        n,m = map(int, file.readline().strip().split())
        # Initialize an empty list to store elements
        elements = []
        # Read the elements in chunks
        chunk_size = 10000  # Adjust the chunk size as needed
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file
            elements.extend(map(int, chunk.split()))
    return n,m, elements
# Example usage: Read input from a text file named "input.txt"
n,m, elements = read_input_from_file("testcase7.txt")
print(allocate_books_brute_force(elements,n,m))





