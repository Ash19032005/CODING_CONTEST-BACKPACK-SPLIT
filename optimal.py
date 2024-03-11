def findPages(arr,n,m):
       if m>n:
              return -1
       low=max(arr)
       high=sum(arr)
       while low<=high:
              mid=(low+high)//2
              book_allocated=0
              student=1
              for i in range(len(arr)):
                     if book_allocated+arr[i]<=mid:
                            book_allocated+=arr[i]
                     else:
                            student+=1
                            book_allocated=arr[i]
              if student>m:
                     low=mid+1
              else:
                     high=mid-1
       return low
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
n,m, elements = read_input_from_file("testcase9.txt")
# n,m,elements=4,2,[12, 34, 67, 90]
print(findPages(elements,n,m))