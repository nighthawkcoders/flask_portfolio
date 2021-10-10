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

carry = False
def oneBit(a, b, c=False):
	sum = xor(xor(a, b), c)
	global carry
	carry = orGate(andGate(a, b), andGate(c, xor(a,b)))
	#See this: https://youtu.be/QZwneRb-zqA?t=639
	return (sum, carry)

def decToBin(dec):
    dec = int(dec)
    bitlen = 0
    while dec >= 2**bitlen:
        bitlen += 1 #determine bitlength in binary

    byte1=[]*bitlen #create an empty bus
        
    while bitlen > 0:
        if dec - 2^bitlen > 0:
            bitlen -= 1
            dec -= 2**bitlen
            byte1.append(True)
            print(dec)
        else:
            bitlen -= 1
            dec -= 2**bitlen
            byte1.append(False)
            print(dec)
            
    return byte1

print("Enter your first number in base-10.")
num1 = input()
byte1 = decToBin(num1)
print(byte1)

print("Enter your second number in base-10.")
num2 = input()
byte2 = decToBin(num2)
print(byte2)


#might need to reverse bit order in each byte?
#ok lol maybe make a global carry var like last time

while len(byte2) != bitness:
	b = input()
	if b == "1":
		byte2.append(True)
	elif b == "0":
		byte2.append(False)
	else:
		print("Only valid inputs are 0 and 1.")


for count, b in enumerate(byte1):
	n = -abs(count + 1)
	byte3.append(oneBit(byte1[n], byte2[n], carry))

print("Byte 3:")

for i, j in enumerate(byte3):
	if byte3[i][0] == True:
		print("1")
	else:
		print("0")
