def orGate(a,b):
	if a==True or b==True:
		return True
	else:
		return False

def andGate(a,b):
	if a==True and b==True:
		return True
	else:
		return False

def notGate(a):
	return not a

def nand(a, b):
	if a == True and b == True:
		return False
	else:
		return True

def xor(a, b):
	if a != b:
		return True
	else:
		return False

def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst

carry = False
def oneBit(a, b, c=False):
	holesum = xor(xor(a, b), c)
	global carry
	carry = orGate(andGate(a, b), andGate(c, xor(a,b)))
	#See this: https://youtu.be/QZwneRb-zqA?t=639
	return (holesum, carry)

def decToBin(dec):
	dec = int(dec)
	bitlen = 0
	while dec >= 2**bitlen:
		bitlen += 1 #determine bitlength in binary

	bus=[] #create an empty bus

	while bitlen > 0: #do this for every bit
		if dec - 2**(bitlen-1) >= 0:
			dec = dec - 2**(bitlen-1)
			bus.append(True)
			bitlen -= 1
		else:
			bus.append(False)
			bitlen -= 1
	return bus

print("Enter your first number in base-10.")
input1 = input()
byte1 = ""
for i in decToBin(input1):
	if i == True:
		byte1 = byte1 + "1"
	else:
		byte1 = byte1 + "0"
print(input1 + " is " + byte1 + " in binary.")

print("Enter your second number in base-10.")
input2 = input()
byte2 = ""
for i in decToBin(input2):
	if i == True:
		byte2 = byte2 + "1"
	else:
		byte2 = byte2 + "0"
print(input2 + " is " + byte2 + " in binary.")

num1 = [False] + decToBin(input1)
num2 = [False] + decToBin(input2)

while len(num1) > len(num2):
	num2 = [False] + num2
while len(num2) > len(num1):
	num1 = [False] + num1

num3 = []
byte3 = ""

num1 = Reverse(num1)
num2 = Reverse(num2)

for count, b in enumerate(num1):
	num3.append(oneBit(num1[count], num2[count], carry))

for count, i in enumerate(num3):
	if num3[count][0] == True:
		byte3 = "1" + byte3
	else:
		byte3 = "0" + byte3

#bin to dec
output = 0
bitpos = 0
for i in num3:
	if i[0] == True:
		output += 2**bitpos
		bitpos += 1
	else:
		bitpos += 1

print("These add up to " + str(byte3) + " in binary.")
print("The decimal output is " + str(output)+".")