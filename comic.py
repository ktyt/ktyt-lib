from __future__ import print_function # Import print function for printing to stderr
'''
A simple class representing a single comic strip.
'''
class Comic:
	# Constructor to create a comic class
	# date - Date object (from python's datetime library)
	# title - Comic title, as a string
	# content - Comic content, as a transcript
	# commentary - Comic commentary, as a string
	def __init__(self, date, title, content, commentary):
		# Initialize attributes
		self.date = date
		self.title = title
		self.content = content
		self.commentary = commentary
# Utility function to create a comic strip from a transcript file
# It is the responsiblity of the caller to close the file
# file - The transcript file to read from
def comicFromTranscript(file):
	dateStr = file.readline()[1:-5] # Remove enclosing brackets and newline
	print(dateStr)
	date = None
	# Parse dateStr
	if not dateStr.startswith("//"): # Check for separate timelines
		dateDataArr = dateStr.split("/") # Split up dateStr
		if len(dateDataArr) != 3:
			print("Error: Invalid date!", file=sys.stderr)
			return None
		# Assumes that the dates are in the format mm/dd/yy
		print(dateDataArr)
		month = int(dateDataArr[0])
		day = int(dateDataArr[1])
		year = int(dateDataArr[2])
		# Create date object 
		date = datetime.date(year, month, day)
	# Find title
	title = file.readline()[1:-3]
	# Keep finding content until commentary is reached or end of file
	allcontent = "" # All the content
	content = "" # A single line of content
	while True:
		content = file.readline()
		if content == "" or content[0] == "<" or content == "[No commentary]": # End of file or end of content, end
			break
		allcontent += content # Add content
	if content == "": # End of file
		print("Error: No commentary specified!", file=sys.stderr)
		return None
	commentary = content # Copy content
	
	# Create and return the Comic class
	return Comic(date, title, allcontent, commentary)
