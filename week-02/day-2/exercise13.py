# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

a = []
b = []
size = 4

for i in range(size):
   b = []
   for j in range(size):
       if i == j:
           b.append('1')
       else:
           b.append('0')
   a.append(b)

for i in range(size):
    print(a[i])

#training

a = int(input('Enter a number: '))

def concate(input):
    for i in range(a):
        p = ""
        for j in range(a):
            if i == j:
                p += "1 "             
            else:
                p += "0 "
        print(p)
(concate(a))