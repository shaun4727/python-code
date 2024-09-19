myString = "I'm a programmer"
myString2 = 'I\'m a programmer'
myString3 = """hello
world"""

print(myString,myString2,myString3)

subString = myString[1:5]

print(subString)

var = "Tom"
newString = "The variable is %s" %var;

# old way of printing number
num = 2
fLnumb = 2.234
newNum = "The variable is %d" %num
flNum = "The variable is %.2f" %fLnumb
print(flNum)

# new way of printing number
var1 = 4
var2 = 3.1234
newString2 = "Two numbers are {} and {:.2f}".format(var1,var2)

print(newString2)