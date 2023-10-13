# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quicksort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quicksort(array, pi + 1, high)


# Driver code
if __name__ == '__main__':
	array = [10, 7, 8, 9, 1, 5]
	N = len(array)

	# Function call
	quicksort(array, 0, N - 1)
	print('Sorted array:')
	for x in array:
		print(x, end=" ")

// Function to partition the array and return the partition index
function partition(arr, low, high) {
	// Choosing the pivot
	let pivot = arr[high];

	// Index of smaller element and indicates the right position of pivot found so far
	let i = low - 1;

	for (let j = low; j <= high - 1; j++) {
		// If current element is smaller than the pivot
		if (arr[j] < pivot) {
			// Increment index of smaller element
			i++;
			[arr[i], arr[j]] = [arr[j], arr[i]]; // Swap elements
		}
	}

	[arr[i + 1], arr[high]] = [arr[high], arr[i + 1]]; // Swap pivot to its correct position
	return i + 1; // Return the partition index
}

// The main function that implements QuickSort
function quickSort(arr, low, high) {
	if (low < high) {
		// pi is the partitioning index, arr[pi] is now at the right place
		let pi = partition(arr, low, high);

		// Separately sort elements before partition and after partition
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

// Driver code
let arr = [10, 7, 8, 9, 1, 5];
let N = arr.length;

// Function call
quickSort(arr, 0, N - 1);
console.log("Sorted array:");
console.log(arr.join(" "));


# This code is contributed by Adnan Aliakbar
