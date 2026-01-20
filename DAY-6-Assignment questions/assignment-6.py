# import re
# text="please email us rangaakash2002@gmail.com"
# pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}"
# match =re.search(pattern,text)
# if match:
#     print("email found",match.group())
# else:
#     print("no email address found")



#2

# import re
# text="please email us rangaakash2002@gmail.com"
# pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}"
# match =re.search(pattern,text)
# if match:
#     print(match.group())
# else:
#     print("no email address found")


#3

# import re
#
# text = "User2 has 5 emails and 4 phone numbers."
# print(re.search(r'U.er', text).group())
# print(re.search(r'\d* emails', text).group())
# print(re.search(r'\d+ emails', text).group())
# print(re.search(r'phones?', "phone").group())
# print(re.findall(r'\d', text))
# print(re.findall(r'\w+', text))
# print(re.findall(r'\s', text))

#4

import re

text = "Name: Akash Ranga, Age: 24"
pattern = r'Name:\s(\w+\s\w+),\sAge:\s(\d+)'
match = re.search(pattern, text)
if match:
    print("Full match:", match.group(0))
    print("Name:", match.group(1))
    print("Age:", match.group(2))
else:
    print("no match found")

