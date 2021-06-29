image = []
current = [0 for i in range(1300)]
#current[1300//2]=1
image.append(current)
new = []
import random
for i in range(10):
        current[random.randint(0,1299)] = 1

def println(l):
        output = ""
        #for i in l:
        #        output=output+i*" "+(1-i)*"&"
        #print(output)

def rules(a,b,c,rule):
	rule_bin = bin(rule)[2:]
	padding = 8-len(rule_bin)
	rule_bin = "0"*padding + rule_bin
	situation = int(str(a)+str(b)+str(c),2)
	fate = bool(int(rule_bin[situation]))
	return fate


rule = int(input("Enter rule: "))
println(current)

def gen():
        global current,new,image
        for i in range(1300):
                new.append(rules(current[i-1],current[i],current[(i+1)%1300], rule)*1)
        current = new
        println(current)
        new = []
        image.append(current)

for i in range(1300):
        gen()

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
