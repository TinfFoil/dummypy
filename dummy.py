import argparse
import numpy as np

# This function returns indices of the maximum element of the array in a particular axis.
# https://devopscube.com/numpy-practical-examples/


def create_array(n=5, m=4):
	"""
	Create an nxm array
	"""
	
	array = np.arange(n*m).reshape(n, m)
	print(array)
	print()
	return array

def get_global_max(array):	
	# If no axis mentioned, then it works on the entire array
	return np.argmax(array)

def get_per_row_max(array):
	# If axis=1, then it works on each row
	return np.argmax(array, axis=1)

def get_per_col_max(array):
	# If axis=0, then it works on each column
	return np.argmax(array, axis=0)


def main():
	# create parser object
	parser = argparse.ArgumentParser(description = "A small CLI instance")

	# defining arguments for parser object
	parser.add_argument("-m", type = int, nargs = 1,
		metavar = "m", default = 1,
		help = "Define the size of dimension m.")

	parser.add_argument("-n", type = int, nargs = 1,
		metavar = "n", default = 1,
		help = "Define the size of dimension n.")
	
	parser.add_argument("-o", "--overall", default=False, action="store_true", 
		help = "Get the overall maximum value.")

	parser.add_argument("-r", "--row", default=False, action="store_true",
		help = "Get the maximum value per row.")
	
	parser.add_argument("-c", "--column", default=False, action="store_true",
		dest = "column", 
		help = "Get the maximum value per column.")
	
	parser.add_argument("-y", "--you", type=str, nargs=2,
		metavar = "name", default = ["Remy", "Lebeau"],
		help = "Let's you set your name.")


	# Other examples
	
	#parser.add_argument("-c", "--copy", type = str, nargs = 2,
		#metavar = ('file1','file2'), 
		#help = "Copy file1 contents to \ file2 Warning: file2 will get 
			#overwritten.")

	#parser.add_argument("--rename", type = str, nargs = 2,
		#metavar = ('old_name','new_name'),
		#help = "Renames the specified file to a new name.")

	
	#parser.add_argument("add", nargs = '*', metavar = "num", type = int,
			#help = "All the numbers separated by spaces will be #added.")

	# parse the arguments from standard input
	args = parser.parse_args()

	print("Hi,", " ".join(args.you), "--how's it going today?\n\n")

	array = create_array(args.m[0], args.n[0])

	# calling functions depending on type of argument
	if args.overall == True: 
		print("Global max:", get_global_max(array))
	if args.row:
		print("Cell with the highest value per row:", get_per_row_max(array))
	if args.column:
		print("Cell with the highest value col max:", get_per_col_max(array))

	print("\n\nThese are all the arguments:\n",args)
	
## parse the arguments from standard input
#args = parser.parse_args()

## check if add argument has any input data.
## If it has, then print sum of the given numbers
#if len(args.add) != 0:
	#print(sum(args.add))


if __name__ == "__main__":
	# calling the main function
	main()
