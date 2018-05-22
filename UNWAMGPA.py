"""
        WAM and GPA Calculator for University of Newcastle

        The scores of the transcript need to be saved in the file called score.txt
        The format of data file is as follow

        {COURSE CODE NAME} {COURSE CODE} {MARK} {GRADE} {Units Earned}

        Example:
        SENG 1110 85 HD 10
        MATH 1050 60 C 10
        PHYS 1210 55 P 10

        Author: Kelvin
        Email: contact@kelvinyin.com
"""

# Cumulative WAM Variables
C_WAM_D = 0 # WAM Total Denominator
C_WAM_N = 0 # WAM Total Numerator

# Bachelor Honours WAM Variables
B_WAM_D = 0 # WAM Total Denominator
B_WAM_N = 0 # WAM Total Numerator

# GPA Grades
GPA_SUM = 0 # Sum of GPA Value
GPA_UNIT = 0 # Total Units

# Get course weighting
def get_course_weighting(c_code):
	if (c_code >= 1000 and c_code < 2000):
		return 1
	elif (c_code >= 2000 and c_code < 3000):
		return 2
	elif (c_code >= 3000 and c_code < 4000):
		return 3
	else:
		return 4

# Get GPA Value
def get_gpa_value(c_grade):
	if (c_grade == 'HD'):
		return 7
	elif (c_grade == 'D'):
		return 6
	elif (c_grade == 'C'):
		return 5
	elif (c_grade == 'P'):
		return 4
	else :
		return 0

# Print Transcript Header
print("\n")
print("+++++++++++++++++++++++++++++++++++")
print("+           Transcript            +")
print("+++++++++++++++++++++++++++++++++++")
print("\n")

print("====================================")
print("{:12s}".format("Course Code"), "{:5s}".format("Mark"), "{:6s}".format("Grade"), "{:6s}".format("Units"))
print("====================================")

with open("score.txt") as _file:
	# Read data line by line
	lines = _file.readlines()

	# Get each line from lines
	for line in lines:
		c_name = line[:].split()[0]
		c_code = int(line[:].split()[1])
		c_mark = int(line[:].split()[2])
		c_grade = line[:].split()[3]
		c_unit = int(line[:].split()[4])

		weight = get_course_weighting(c_code)

		# for Cumulative WAM
		C_WAM_N += (c_mark * weight * c_unit)
		C_WAM_D += (c_unit * weight)

		# for Bachelor Honours
		if (c_code >= 2000):
			B_WAM_N += (c_mark * weight * c_unit)
			B_WAM_D += (c_unit * weight)

		# Calculate GPA
		gpa_value = get_gpa_value(c_grade)
		GPA_SUM += c_unit * gpa_value
		GPA_UNIT += c_unit
	
		# Print Transcript
		print("{:12s}".format(c_name + " " + str(c_code)), "{:<5d}".format(c_mark), "{:6s}".format(c_grade), "{:<6d}".format(c_unit))

print("====================================")
print("{:25s}".format("Total Units"), GPA_UNIT)
# New line
print("\n")

# Print Cumulative WAM
print("{:23s}".format("Cumulative WAM: "), "{:.2f}".format((C_WAM_N/C_WAM_D)))
print("{:23s}".format("Bachelor Honours WAM: "), "{:.2f}".format((B_WAM_N/B_WAM_D)))
print("{:23s}".format("GPA: "), "{:.1f}".format((GPA_SUM/GPA_UNIT)))
print("\n")
