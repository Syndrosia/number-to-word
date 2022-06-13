while 2 > 1:
   teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "zero"]
   s = [["twenty", 2], ["thirty", 3], ["forty", 4], ["fifty", 5], ["sixty", 6], ["seventy", 7], ["eighty", 8], ["ninty", 9] ]
   p = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9], [""]]
   t = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
   var = input("Enter a number: ")
   if len(var) == 1:
      if var[0] == "0":
         print(" >>", teen[int(((5**2) / 2.5))])
      else:
         print(" >>", p[(int(var) - 1)][0])
   elif len(var) == 2:
      if var[0] == "1":
         print(" >>", str(teen[(int(var[1]))]))
      elif var[1] == "0":
         print(" >>", s[(int(var[0]) - 2)][0])
      else:
         twoFirst = s[(int(var[0]) - 2)][0]
         twoSecond = p[(int(var[1]) - 1)][0]
         print(" >>", twoFirst + "-" + twoSecond)
   elif len(var) == 3:
      if var[1] == "1":
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", str(teen[(int(var[2]))]))
      elif var[1] and var[2] == "0":
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0])
      elif var[2] == "0" and var[2 != "0"]:
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", s[(int(var[1]) - 2)][0])
      elif var[2] != "0" and var[1] == "0":
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", p[(int(var[2]) - 1)][0])
      else:
         beginnerFir = p[(int(var[0]) - 1)][0]
         K2 = s[(int(var[1]) - 2)][0]
         tThi = p[(int(var[2]) - 1)][0]
         print(" >>", beginnerFir + "-" + t[0], "and", K2 + "-" + tThi)
   elif len(var) == 4: 
      fFir = p[(int(var[0]) - 1)][0]
      hunSec = p[(int(var[1]) - 1)][0]
      fThi = s[(int(var[2]) - 2)][0]
      fFor = p[(int(var[3]) - 1)][0]
      print(" >>", fFir + "-" + t[1] + ",", hunSec + "-" + t[0], "and", fThi + "-" + fFor)
