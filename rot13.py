alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message, like HELLO: ")
shift = 13

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   newloc = (loc + shift)%26
   str_out += alpha[newloc]

print("Ciphertext:", str_out)
