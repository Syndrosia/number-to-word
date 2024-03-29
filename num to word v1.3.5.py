cfg = [
   "point", # set to "dot" for an output of "three dot one-four" when you input "3.14"
   "thousand", # set to "teendrud" for things such as "sixteen-hundred and twenty-three" when you input "1623"
   "and" # the word described to seperates number groups
]
deci = False 
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "zero"]
s = [["twenty", 2], ["thirty", 3], ["forty", 4], ["fifty", 5], ["sixty", 6], ["seventy", 7], ["eighty", 8], ["ninty", 9], ["ten", 0] ]
p = [["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9], []]
t = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", 
"duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septemdecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion", 
"duovigintillion", "trevigintillion", "quattuorvigintillion", "quinvigintillion", "sexvigintillion", "septvigintillion", "octovigintillion", "nonvigintillion", "trigintillion",
"untrigintillion", "duotrigintillion", "googol"]
while 2 > 1:
   var = input("Enter a number: ")
   #resolvers
   if len(var) > 4:
      overrideA = True
   else: overrideA = False
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

   # add dynamic config resolvers

   # decimal numbers
   if var.find(".") != -1 and not overrideA:
      deci = True
      y, f, h, ran = [], [], [], []
      var = var.split(".")
      if len(var[0]) == 1:
         if var[0][0] != "0":
            y.append(p[(int(var[0]) - 1)][0])
         else: y.append("zero")
         y.append(cfg[0])
         for i in range(len(var[1])):
            if var[1][i] != "0":
               y.append(p[(int(var[1][i]) - 1)][0])
            else: y.append("zero")
         print(" >>", "-".join(y))
      elif len(var[0]) == 2: # two digit
         for xr in range(len(var[1])):
            if var[1][xr] != "0":
               f.append(p[(int(var[1][xr]) - 1)][0])
            else: f.append("zero") 
         for ko in range(len(var[0])): # remove for big o notation
            h.append(var[0][ko]) 
         if "".join(h)[0] == "1": # o((log n)^k):
            print(" >>", str(teen[(int("".join(h)[1]))]), cfg[0], "-".join(f))
         elif "".join(h)[0] == "0": 
            print(" >>", s[(int("".join(h)[0]) - 2)][0], cfg[0], "-".join(f))
         else: # change back to elif for big o 
            if "".join(h)[1] != "0":
               print(" >>", s[(int("".join(h)[0]) - 2)][0] + "-" + p[(int("".join(h)[1]) - 1)][0], cfg[0], "-".join(f))
            else: # forgot to add support for 90, 30 so this will do lol
               print(" >>", s[(int("".join(h)[0]) - 2)][0] + p[(int("".join(h)[1]) - 1)][0], cfg[0], "-".join(f))
      elif len(var[0]) == 3: # three digit 
         for msc in range(len(var[1])): 
            if var[1][msc] != "0": #gpedit.msc lol
               ran.append(p[int(var[1][msc]) - 1][0])
            else: # "00216.23" skips to [4:] instead of [2:]
               ran.append("zero")
         if var[0][1] == "1": # 218, 714, 410
            print(" >>", p[int(var[0][0]) - 1][0] + "-" + t[0], cfg[2], teen[int(var[0][2])], cfg[0], "-".join(ran))
         elif var[0][1] == "0" and var[0][2] != "0": # 702, 207
            print(" >>", p[int(var[0][0]) - 1][0] + "-" + t[0], cfg[2], p[int(var[0][2]) - 1][0], cfg[0], "-".join(ran)) 
         elif var[0][1] == "0" and var[0][2] == "0": # 200, 900
            print(" >>", p[int(var[0][0]) - 1][0] + "-" + t[0], cfg[0], "-".join(ran))  
         elif var[0][1] != "0" and var[0][2] == "0": # 520, 860
            print(" >>", p[int(var[0][0]) - 1][0] + "-" + t[0], cfg[2], s[int(var[0][1]) - 2][0], cfg[0], "-".join(ran))
         elif var[0][1] != "1" and var[0][2] != "0" and var[0][1] != "0": # 234, 723
            print(" >>", p[int(var[0][0]) - 1][0] + "-" + t[0], cfg[2], s[int(var[0][1]) - 2][0], p[int(var[0][2]) - 1][0], cfg[0], "-".join(ran)) 
      f, h, y, ran = [], [], [], []
      deci = False 
   
   #single digit
   elif len(var) == 1 and deci == False and var[0] != "0" and not overrideA:
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
   elif len(var) == 3 and deci == False and not overrideA:
      if var[1] == "1": # 118, 112
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], cfg[2], str(teen[(int(var[2]))]))
      elif var[1] == "0" and var[2] == "0": #  200, 600
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0])
      elif var[2] == "0" and var[1] != "0": # 220, 680
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], cfg[2], s[(int(var[1]) - 2)][0])
      elif var[2] != "0" and var[1] == "0": # 209, 804
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], cfg[2], p[(int(var[2]) - 1)][0])
      else: # 273, 823
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[0], cfg[2], s[(int(var[1]) - 2)][0] + "-" + p[(int(var[2]) - 1)][0])
         
   #four digits
   elif len(var) == 4 and deci == False and not overrideA:
      if var[2] != "1" and var[1] != "0" and var[2] != "0" and var[3] != "0":        
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], cfg[2], s[(int(var[2]) - 2)][0] + "-" + p[(int(var[3]) - 1)][0])
      elif var[1] != "0" and var[2] != "0" and var[2] == "1" and var[3] != "0": # 4918, 8213
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], cfg[2], teen[int(var[3])])
      elif var[2] == "0" and var[1] != "0" and var[3] != "0": # 4203, 8908
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], cfg[2], p[int(var[3]) - 1][0])
      elif var[1] == "0" and var[2] == "0" and var[3] != "0": # 7003, 4006
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1], cfg[2], p[int(var[3]) - 1][0])
      elif var[1] == "0" and var[2] != "0" and var[3] != "0" and var[2] == "1": # 4019, 2018
         print(" >>", p[int(var[0]) - 1][0] + "-" + t[1], cfg[2], teen[int(var[3])])
      elif var[1] == "0" and var[2] == "0" and var[3] == "0": # 3000, 8000
         print(" >>", p[int(var[0]) - 1][0] + "-" + t[1])
      elif var[1] != "0" and var[2] != "0" and var[3] == "0": # 3130, 8590
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1] + ",", p[(int(var[1]) - 1)][0] + "-" + t[0], cfg[2], s[int(var[2]) - 2][0])
      elif var[1] == "0" and var[2] != "0" and var[2] != "1" and var[3] == "0": # 4040, 3060
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1], cfg[2], s[int(var[2]) - 2][0])
      elif var[1] == "0" and var[2] != "0" and var[2] != "1" and var[3] != "0": # 4024, 5072
         print(" >>", p[(int(var[0]) - 1)][0] + "-" + t[1], cfg[2], s[int(var[2]) - 2][0], p[int(var[3]) - 1][0])

   if overrideA == True:
      if var.find(","):
         var = var.replace(",", "")
      rs, clone, stack = [], str(var[::-1]), ""
      if clone.find(".") != -1:
         decimal, obj = clone[0:clone.find(".")][::-1], int(clone.find("."))
         clone, clone = clone.replace(".", ""), clone[obj + 1:len(clone)]
      for x in range(len(var) // 3):
         rs.append((clone[0:3])[::-1])
         clone = clone.replace(clone[0:3], "")
      rs.insert(len(rs), clone[::-1])
      rs, zed, column, com = rs[::-1], "null", len(rs) - 1, ", "
      for n in range(len(rs)):
         zed, column = t[column], column - 1
         if len(rs[n]) == 1:
            stack = stack + str(p[int(rs[n][0]) - 1][0]) + " " + zed + com
         elif len(rs[n]) == 2:
            if rs[n][0] == "1": # 16, 11, (teens)
               stack = stack + str(teen[(int(rs[n][1]))]) + " " + zed + com
            elif rs[n][1] == "0": # 30, 80
               stack = stack + str(s[(int(rs[n][0]) - 2)][0]) + " " + zed + com
            else: # 82, 47
               stack = stack + str(s[(int(rs[n][0])) - 2][0] + "-" + p[(int(rs[n][1]) - 1)][0] + " " + zed + com)
         elif len(rs[n]) == 3:
            if rs[n][1] == "1": # 118, 112
               stack = stack + "" + p[(int(rs[n][0]) - 1)][0] + "-" + t[0] + " " + cfg[2] + " " + str(teen[(int(rs[n][2]))]) + " " + zed + com
            elif rs[n][1] == "0" and rs[n][2] == "0": #  200, 600
               stack = stack + "" + p[(int(rs[n][0]) - 1)][0] + "-" + t[0] + " " + zed + com
            elif rs[n][2] == "0" and rs[n][1] != "0": # 220, 680
               stack = stack + "" + p[(int(rs[n][0]) - 1)][0] + "-" + t[0] + " " + cfg[2] + " " + s[(int(rs[n][1]) - 2)][0] + " " +zed + com
            elif rs[n][2] != "0" and rs[n][1] == "0": # 209, 804
               stack = stack + "" + p[(int(rs[n][0]) - 1)][0] + "-" + t[0] + " " + cfg[2] + " " + p[(int(rs[n][2]) - 1)][0] + " " + zed + com
            else: # 273, 823
               stack = stack + "" + p[(int(rs[n][0]) - 1)][0] + "-" + t[0] + " " + cfg[2] + " " + s[(int(rs[n][1]) - 2)][0] + "-" + p[(int(rs[n][2]) - 1)][0] + " " + zed + com
      stack = stack[0:(len(stack) - 10)]
      if len(decimal) > 0:
         stack = stack + " point "
         for kv in range(len(decimal)): 
            if decimal[kv] != "0": 
               stack = stack + p[int(decimal[kv]) - 1][0] + ", "
            else: stack = stack + "zero, "
      print(stack)
