print("DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20))

def swap(a, b):
    return b, a

a, b =10, 20

a, b = swap(a, b)

print("A = ",a, " \nB = ",b)

x = 10
print("Umesh test", x)

msg = "hello world"
print(msg)

msg.capitalize()
print(msg.capitalize())
print(msg.split())

print(2 > 5)

name = "Umesh Singh"

greetings = "My name is {}".format(name)
print(greetings)

str = "                 Happy             "
print(str)
print(str.strip())


num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

num1, num2 = num2, num1
print("Num1 :", num1)
print("Num2 :", num2)
print("Addition :", num1+num2)

