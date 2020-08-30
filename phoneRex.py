# for running this we have to import this 
# than call the function isPhoneNum()
phoneRegex = re.compile(r'''
  (\d{3}|\(\d{3}\))?  #areacode
  (\s|-|\.)?      # seperator
  \d{3}           # first 3 digits
  (\s|-|\.)?      # seperator
  \d{4}           # last 4 digits
  (\s*(ext|x|ext.)\s*\d{2,5})?
''', re.VERBOSE)


def isPhoneNum(text):
  mo = phoneRegex.search(text)
  if mo !=None:
    return mo.group()

#------end of programe --------