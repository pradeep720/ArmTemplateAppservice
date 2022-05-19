#!/usr/bin/env python3
#
# A hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
import sys, re

#Required parts 
requiredRegex = "(^AB#)(\d{1,6})\s(\w+)"
requiredLength = 15

#Get the commit file
commitMessageFile = open(sys.argv[1]) #The first argument is the file
commitMessage = commitMessageFile.read().strip()

# # # if len(commitMessage) < requiredLength:
    # # # print ("Commit message is less than the required 15 characters.")
    # # # sys.exit(1)

# if re.search(requiredRegex, commitMessage):
    # print ("commit message is validated")
    # sys.exit(0)
# else
# print ("Commit message is validated")
# sys.exit(0)


if re.search(requiredRegex, commitMessage):
	print(f"'{commitMessage}' is an valid msg!")
	exit(0)
else:
	print(f"'{commitMessage}' is NOT a valid commit msg!")
	exit(1)