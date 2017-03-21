import os

if __name__ == '__main__':
	# Make sure this begins and ends with a "/" character
	#     e.g. /Users/joshuachen/Documents/
	directory = '/'

	# Name of the textbooks that you want to add. Should end with a
	# ".pdf" extension and be named for the course with additional
	# identifiers as necessary.
	#     e.g. [cs21-sipser.pdf, cs24.pdf]
	courses = []

	# For all the inputted courses, rename them to begin with "new"
	for course in courses:
		os.rename(directory + course + '.pdf', directory + 'new' + course + '.pdf')
		# Rename "new" marked files back to their original name
		# Is handled by the main script, for if you make a mistake or something
		# os.rename(directory + 'new' + course + '.pdf', directory + course + '.pdf')
