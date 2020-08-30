# importing the module for copy/paste and regex
import pyperclip, re

# getting the copied content 
text = pyperclip.paste()

# making a object of REgex
extchange = re.compile(r'msi-ggsip\.org')
newtext = extchange.sub('janakpuri.com',text)


# find all the new emails in the newtext
newemail = re.compile(r'''
	\w+ 	#name of student
	\d+	#enrollment of student
	@	#as obvious in email
	janakpuri\.com	#domain
''', re.VERBOSE)

# making a list of the emails

emails = newemail.findall(newtext)
emails.sort()
print(type(emails))
print(len(emails))
# join all the elements of the list
result = '\n'.join(emails)

# copying the updated text
pyperclip.copy(result)


# open a file and save it 
file = open('emails_data.txt', 'w')
file.write(result)

# close the file
file.close()
#----end of programme ----#
