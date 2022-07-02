teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "zero"]
s = [["twenty", 2], ["thirty", 3], ["forty", 4], ["fifty", 5], ["sixty", 6], ["seventy", 7], ["eighty", 8], ["ninty", 9] ]
p = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9], [""]]
t = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
while 2 > 1:
   var = input("Enter a number: ")
   
#resolvers
   if var == "0" or var == "00" or var == "000" or var == "0000":
      print(" >> zero")
   elif var.startswith("000000"):
      var = var[6:]
   elif var.startswith("00000"):
      var = var[5:]
   elif var.startswith("0000"):
      var = var[4:]
   elif var.startswith("000"): 
      var = var[3:]
   elif var.startswith("00"):
      var = var[2:]
   elif var.startswith("0"):
      var = var[1:]

   #single digit
   if len(var) == 1:
      print(" >>", p[(int(var) - 1)][0]) # 8, 2

   # two digits
   elif len(var) == 2:
      if var[0] == "1": # 16, 11, (teens)
         print(" >>", str(teen[(int(var[1]))]))
      elif var[1] == "0": # 30, 80
         print(" >>", s[(int(var[0]) - 2)][0])
      else: # 82, 47
         print(" >>", s[(int(var[0]) - 2)][0] + "-" + p[(int(var[1]) - 1)][0])

   # three digits
   elif len(var) == 3:
      if var[1] == "1": # 118, 112
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", str(teen[(int(var[2]))]))
      elif var[1] == "0" and var[2] == "0": #  200, 600
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0])
      elif var[2] == "0" and var[1] != "0": # 220, 680
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", s[(int(var[1]) - 2)][0])
      elif var[2] != "0" and var[1] == "0": # 209, 804
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", p[(int(var[2]) - 1)][0])
      else: # 273, 823
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], "and", s[(int(var[1]) - 2)][0] + "-" + p[(int(var[2]) - 1)][0])
         
   #four digits
   elif len(var) == 4:
      if var[0] != "0" and var[1] != "0" and var[2] != "0" and var[3] != "0":        
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], "and", s[(int(var[2]) - 2)][0] + "-" + p[(int(var[3]) - 1)][0])
