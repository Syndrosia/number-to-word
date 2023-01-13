cfg = [
   "point", # set to "dot" for an output of "three dot one-four" when you input "3.14"
   "thousand", # set to "teendrud" for things such as "sixteen-hundred and twenty-three" when you input "1623"
   "and"
]
deci = False 
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "zero"]
s = [["twenty", 2], ["thirty", 3], ["forty", 4], ["fifty", 5], ["sixty", 6], ["seventy", 7], ["eighty", 8], ["ninty", 9], ["ten", 0] ]
p = [["zero", 0],["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9], []]
t = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", 
"duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septemdecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion", 
"duovigintillion", "trevigintillion", "quattuorvigintillion", "quinvigintillion", "sexvigintillion", "septvigintillion", "octovigintillion", "nonvigintillion", "trigintillion",
"untrigintillion", "duotrigintillion", "googol", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
 "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while 2 > 1:
   var = input("Enter a number: ")
   #resolvers
   if var[0] == "0":
      for i in range(len(var)):
         if var[i] != "0":
            var = var[i - 1:]

   for g in range(len(var)):
      if var[g] == ".":
         odin = True
   
   if odin == True:
      for t in range(len(var), 0):
         if var[t] == "0":
            var = var[0:len(var) - 1]
         
   if var.find(","):
      var = var.replace(",", "")

   # conversion

   rs, clone, stack, decimal = [], str(var[::-1]), "", ""
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
         stack = stack + "" + str(p[str(int(rs[n]))[0]][0]) + " " + zed + com
      elif len(rs[n]) == 2:
         if rs[n][0] == "1": # 16, 11, (teens)
            stack = stack + str(teen[(int(rs[n][1]))]) + " " + zed + com
         elif rs[n][1] == "0": # 30, 80
            stack = stack + str(s[(int(rs[n][0]) - 2)][0]) + " " + zed + com
         else: # 82, 47
            stack = stack + str(s[(int(rs[n][0]) - 2)][0]) + "-" + str(p[int(rs[n][1])][0]) + " " + zed + com
      elif len(rs[n]) == 3:
         if rs[n][1] == "1": # 118, 112
            stack = stack + "" + str(p[int(rs[n][0])][0]) + "-" + t[0] + " " + cfg[2] + " " + str(teen[(int(rs[n][2]))]) + " " + zed + com
         elif rs[n][1] == "0" and rs[n][2] == "0": #  200, 600
            stack = stack + "" + str(p[int(rs[n][0])][0]) + "-" + t[0] + " " + zed + com
         elif rs[n][2] == "0" and rs[n][1] != "0": # 220, 680
            stack = stack + "" + str(p[int(rs[n][0])][0]) + "-" + t[0] + " " + cfg[2] + " " + s[int(rs[n][1]) - 2][0] + " " +zed + com
         elif rs[n][2] != "0" and rs[n][1] == "0": # 209, 804
            stack = stack + "" + str(p[int(rs[n][0])][0]) + "-" + t[0] + " " + cfg[2] + " " + str(p[int(rs[n][2])][0]) + " " + zed + com
         else: # 273, 823
            stack = stack + "" + str(p[int(rs[n][0])][0]) + "-" + t[0] + " " + cfg[2] + " " + s[int(rs[n][1]) - 2][0] + "-" + str(p[int(rs[n][2])][0]) + " " + zed + com
   stack = stack[0:(len(stack) - 10)]
   if len(decimal) > 0:
      stack = stack + " point "
      for kv in range(len(decimal)):   
         stack = stack + p[int(decimal[kv])][0] + ", "
   print(stack)
   # recheckers for 900.090 saying "point zero nine zero"
