# Python3 program for optimal allocation of pages

# Utility function to check if
# current minimum value is feasible or not.


def isPossible(arr, n, m, curr_min):
	studentsRequired = 1
	curr_sum = 0

	# iterate over all books
	for i in range(n):

		# check if current number of pages are
		# greater than curr_min that means
		# we will get the result after
		# mid no. of pages
		if (arr[i] > curr_min):
			return False

		# count how many students are required
		# to distribute curr_min pages
		if (curr_sum + arr[i] > curr_min):

			# increment student count
			studentsRequired += 1

			# update curr_sum
			curr_sum = arr[i]

			# if students required becomes greater
			# than given no. of students, return False
			if (studentsRequired > m):
				return False

		# else update curr_sum
		else:
			curr_sum += arr[i]

	return True

# function to find minimum pages


def findPages(arr, n, m):

	sum = 0

	# return -1 if no. of books is
	# less than no. of students
	if (n < m):
		return -1

	# Count total number of pages
	for i in range(n):
		sum += arr[i]

	# initialize start as 0 pages and
	# end as total pages
	start, end = 0, sum
	result = 10**9

	# traverse until start <= end
	while (start <= end):

		# check if it is possible to distribute
		# books by using mid as current minimum
		mid = (start + end) // 2
		if (isPossible(arr, n, m, mid)):

			# update result to current distribution
			# as it's the best we have found till now.
			result = mid

			# as we are finding minimum and books
			# are sorted so reduce end = mid -1
			# that means
			end = mid - 1

		else:
			# if not possible means pages should be
			# increased so update start = mid + 1
			start = mid + 1

	# at-last return minimum no. of pages
	return result
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
n,m, elements = read_input_from_file("testcase1.txt")
print(findPages(elements,n,m))




