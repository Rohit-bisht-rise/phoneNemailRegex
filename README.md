# phoneNemailRegex
Using Regex to scrap out the phone no and emails

FORMAT

  phone = (area code) (exact number for phone)            EX:- (413)-123-2345
  email = (name)(number)@msi-ggsip.org                    EX:- dinesh12365472817@msi-ggsip.org
  
Working of phone:
  It can find the following type of phone number's enter
  
  wihout area code                        Ex:       123-3123
  area code within parenthesis            Ex: (413)-123-3214
  area code without parenthesis           Ex: 413-123-2345
  
  with hyphen                             Ex: 123-222-2234
  with space                              Ex: 123 222 2234
  with dot                                Ex: 123.222.2234
  
  
Working of email:
  It does following steps:
  
step 1:   grab all the content of file which has emails.
step 2:   change the extension of emails from (msi-ggsip.org) to (janakpuri.com)
step 3:   sort the required emails in alphabatic increasing order
step 4:   open a file and save it, also you can paste the output after running this script


Procedure:
  Phone :
    import the PhoneRex.py file
    run isPhoneNum() methord, which take a text as argument, and then return it to a variable if             gets.
  Email :
    copy the text which have email in it
    run emailRex.py script
    it makes a output file email_data.txt
    also you can paste it after running it.
  
    
