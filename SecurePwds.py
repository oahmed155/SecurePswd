# SecurePwds.py
# Omar Ahmed
# 12/13/23
# This creates a list pf 10 extreml secure passwords

import random
pw = 0

for pw in range(10):
  charcount = random.randint(8,16)
  pwd = ""
  for x in range(charcount):
    match random.randint(1,8):
      case 1:
         thisChar = random.randint(65,90)
      case 2:
        thisChar = random.randint(97,122)
      case 3:
         thisChar = random.randint(48,57)
      case 4:
         thisChar = 33
      case 5:
         thisChar = random.randint(35,38)
      case 6:
         thisChar = random.randint(39,47)
      case 7:
         thisChar = random.randint(58,63)
      case 8:
         thisChar = random.randint(123,126)
    pwd += chr(thisChar)

  print(pwd)
  
  
  
  