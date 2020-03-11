# Python program to Remove leading zeros from an IP address

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression for
# finding leading zeros in ip address
regex = '\.[0]*'

# Define a function for Remove
# leading zeros from an IP address


def removeLeadingZeros(ip):

    modified_ip = re.sub(regex, '.', ip)

    print(modified_ip)


# Main code
if __name__ == '__main__':

	# Enter ip address
	ip = "216.08.094.196"

	# call function
	removeLeadingZeros(ip)

	ip = "216.08.004.096"

	removeLeadingZeros(ip)
