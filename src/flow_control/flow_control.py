# if elif else
'''
marks = 75 
if(marks>80):
    print("Grad A")
elif (marks>60) and (marks<=80):
    print("Grad B")
elif (marks>40) and (marks<=60):
    print("Grad C")
else:
    print("Grad D")
'''

#while

'''
num  = int(input('Enter the value of n = '))
if num <= 0:
    print("Enter a valid value")
else:
    sum = 0
    while num>0 :
        sum += num
        num -= 1

    print(sum)
'''



#for loop
'''
for quant in range(99, 0, -1):
    if quant > 1:
        print(quant, "Bottles of bear on the wall,", quant, " Bottles of bear")
        if(quant > 2):
            suffix = str(quant) + "bottles of bear on the wall"
        else:
            suffix = '1 bottle of bear on the wall'
    elif quant == 1:
        print("1 bottle of bear on the wall")
        suffix = "No more bear on the wall"
    print("Take one down and pass it around", suffix)
    print("===============") 
'''

#break
'''
count = 0
while True:
    print(count)
    count += 1
    if count > 10:
        break
'''

#continue

for x in range(20):
    if x % 2 == 0:
        continue    
    print(x)
