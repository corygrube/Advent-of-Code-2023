def get_input(path): 
	"""Open input text file, return as list of lines (strings)"""
	with open(path) as file:
		return file.readlines()

def get_first_digit(string):
	"""Returns first numeric digit (e.g. '1') of a string"""
	for char in string:
		if char.isdigit():
			# return first numeric digit found (first in string)
			return char
	
	# fallback
	return None

def get_last_digit(string):
	"""Returns last numeric digit (e.g. '1') of a string"""
	for char in reversed(string):
		if char.isdigit():
			# return first numeric digit found (last in string)
			return char
	
	# fallback
	return None

def get_digit_index(string):
	"""Returns a dict index of all numeric digits (e.g. '1') and string digits (e.g. 'one') within a string.
	Format: {
		# index of string (int) : digit (string, e.g. '1')
	}
	"""
	digit_index = {}
	# get index of all numeric digits in string
	for i, char in enumerate(string):
		if char.isdigit():
			digit_index[i] = char
	
	# dict of possible digit strings (e.g. 'one')
	digit_strings = {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five": "5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9"
	}
	# locate all digit first and last instances of digit strings in string
	for key in digit_strings.keys():
		if key in string:
			# left/right find used to cover case when string has >1 of the same digit string
			index_left = string.find(key)
			index_right = string.rfind(key)
			digit_index[index_left] = digit_strings[key]
			digit_index[index_right] = digit_strings[key]
	
	return digit_index

def get_first_digit_alphanumeric(string):
	"""Returns first numeric digit (e.g. '1') or string digit (e.g. 'one') of a string. Returns as digit ('1')"""
	# dict of all numeric digits and most string digits in string
	digit_index = get_digit_index(string)
	
	# sort by index and get lowest index (first digit)
	digit_index_keys = list(digit_index.keys())
	digit_index_keys.sort()
	lowest_index = digit_index_keys[0]
	
	return digit_index[lowest_index]

def get_last_digit_alphanumeric(string):
	"""Returns last numeric digit (e.g. '1') or string digit (e.g. 'one') of a string. Returns as digit ('1')"""
	# dict of all numeric digits and most string digits in string
	digit_index = get_digit_index(string)
	
	# sort by index and get highest index (last digit)
	digit_index_keys = list(digit_index.keys())
	digit_index_keys.sort()
	highest_index = digit_index_keys[-1]
	
	return digit_index[highest_index]

def solution_1(input_):
	calibration_values = []
	
	# get first and last digit (numeric only) for each line of input. Append to value list
	for line in input_:
		first_digit = get_first_digit(line)
		last_digit = get_last_digit(line)
		calibration_values.append('{}{}'.format(first_digit, last_digit))
	
	# sum values in value list
	sum = 0
	for value in calibration_values:
		sum += int(value)
	return sum

def solution_2(input_):
	calibration_values = []
	
	# get first and last digit (numeric or string) for each line of input. Append to value list
	for i, line in enumerate(input_):
		first_digit = get_first_digit_alphanumeric(line)
		last_digit = get_last_digit_alphanumeric(line)
		calibration_values.append('{}{}'.format(first_digit, last_digit))

	# sum values in value list	
	sum = 0
	for value in calibration_values:
		sum += int(value)
	return sum

# main
DAY = 1
# get input files
sample_1_input = get_input("sample_1.txt")
sample_2_input = get_input("sample_2.txt")
real_input = get_input("input.txt")

# solution 1, sample
sample_solution_1 = solution_1(sample_1_input)
print("Day {} - Sample solution 1: {}".format(DAY, sample_solution_1))

# solution 1, real
real_solution_1 = solution_1(real_input)
print("Day {} - Real solution 1: {}".format(DAY, real_solution_1))

# solution 2, sample
sample_solution_2 = solution_2(sample_2_input)
print("Day {} - Sample solution 2: {}".format(DAY, sample_solution_2))

# solution 2, real
real_solution_2 = solution_2(real_input)
print("Day {} - Real solution 2: {}".format(DAY, real_solution_2))