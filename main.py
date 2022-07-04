cfg = [
   "point", # set to "dot" for an output of "three dot one-four" when you input "3.14"
   "thousand", # set to "teendrud" for things such as "sixteen-hundred and twenty-three" when you input "1623"
   False # change to true if you want the first letter to be capital e.g. "Forty-two" when you input "42"
]

deci = False 
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "zero"]
s = [["twenty", 2], ["thirty", 3], ["forty", 4], ["fifty", 5], ["sixty", 6], ["seventy", 7], ["eighty", 8], ["ninty", 9] ]
p = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9], [""]]
t = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
while 2 > 1:
   var = input("Enter a number: ")
   
#resolvers
   if var == "0" or var == "00" or var == "000" or var == "0000" or var == "00000" or var == "000000":
      print(" >> zero")
   elif var.startswith("000000"):
      if var.find(".") != -1:
         var = var[(var.find(".") - 1):]
      else:
         var = var[6:]
   elif var.startswith("00000"):
      if var.find(".") != -1:
         var = var[(var.find(".") - 1):]
      else:
         var = var[5:]
   elif var.startswith("0000"):
      if var.find(".") != -1:
         var = var[(var.find(".") - 1):]
      else:
         var = var[4:]
   elif var.startswith("000"): 
      if var.find(".") != -1:
         var = var[(var.find(".") - 1):]
      else:
         var = var[3:]
   elif var.startswith("00"):
      if var.find(".") != -1:
         var = var[(var.find(".") - 1):]
      else:
         var = var[2:]
   elif var.startswith("0") and var.find(".") >= 2:
      var = var[1:]
   elif var.startswith("0") and var.find(".") == -1:
      var = var[1:]

   # decimal numbers
   if var.find(".") != -1:
      deci = True
      y, f, h = [], [], []
      var = var.split(".")
      if len(var[0]) == 1:
         if var[0][0] != "0":
            y.append(p[(int(var[0]) - 1)][0])
         else:
            y.append("zero")
         y.append(cfg[0])
         for i in range(len(var[1])):
            if var[1][i] != "0":
               y.append(p[(int(var[1][i]) - 1)][0])
            else:
               y.append("zero")
         print(" >>", "-".join(y))
         y = []
      elif len(var[0]) == 2:
         for xr in range(len(var[1])):
            if var[1][xr] != "0":
               f.append(p[(int(var[1][xr]) - 1)][0])
            else:
               f.append("zero")
         q = " ".join(f)
         for ko in range(len(var[0])):
            h.append(var[0][ko])
         if "".join(h)[0] == "1": 
            print(" >>", str(teen[(int("".join(h)[1]))]), cfg[0], "-".join(f))
         elif "".join(h)[1] == "0": 
            print(" >>", s[(int("".join(h)[0]) - 2)][0], cfg[0], "-".join(f))
         else: # this code is way too complex
            print(" >>", (s[(int("".join(h)[0]) - 2)][0] + "-" + p[(int("".join(h)[1]) - 1)][0]), cfg[0], "-".join(f))
         f, h, y = [], [], []
      deci = False 

   #single digit
   elif len(var) == 1 and deci == False:
      print(" >>", p[(int(var) - 1)][0]) # 8, 2

   # two digits
   elif len(var) == 2 and deci == False:
      if var[0] == "1": # 16, 11, (teens)
         print(" >>", str(teen[(int(var[1]))]))
      elif var[1] == "0": # 30, 80
         print(" >>", s[(int(var[0]) - 2)][0])
      else: # 82, 47
         print(" >>", s[(int(var[0]) - 2)][0] + "-" + p[(int(var[1]) - 1)][0])

   # three digits
   elif len(var) == 3 and deci == False:
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
   elif len(var) == 4 and deci == False:
      if var[0] != "0" and var[1] != "0" and var[2] != "0" and var[3] != "0":        
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], "and", s[(int(var[2]) - 2)][0] + "-" + p[(int(var[3]) - 1)][0])

   
   # dynamic number finding system (million++)

