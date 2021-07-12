image = []
current = [0 for i in range(500)]
current[500//2]=1
image.append(current)
new = []

# Code for random initial state
##import random
##for i in range(10):
##        current[random.randint(0,499)] = 1

def rules(a,b,c,rule):
        rule_bin = bin(rule)[2:]
        padding = 8-len(rule_bin)
        rule_bin = "0"*padding + rule_bin
        situation = 7-int(str(a)+str(b)+str(c),2)
        fate = bool(int(rule_bin[situation]))
        return fate

def gen():
        global current,new,image
        for i in range(500):
                new.append(rules(current[i-1],current[i],current[(i+1)%500], rule)*1)
        current = new
        new = []
        image.append(current)

rule = int(input("Enter rule: "))

for i in range(500):
        gen()

# for visualizing
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.imshow(image)
plt.axis("off")
plt.axis("tight")
plt.axis("image")

saveit = input("Would you like to save the figure? (Y/N): ")
if saveit == "Y":
        fname = input("Enter filename: ")
        plt.savefig("{}.png".format(fname),bbox_inches='tight')
        
plt.show()
