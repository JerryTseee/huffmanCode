string = "Hello world!"

dic = dict()#initialize a dictionary

#define a node class
class Node:
    def __init__(self, frequency, char = None):
        self.frequency = frequency
        self.char = char
        self.left = None
        self.right = None

#add each character into the dictionary, and the corresponding frequency
for i in string:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

#sort the values in ascending order, and then sort the keys in ascending order of ASCII code if they have the same count
dic = dict( sorted(dic.items(), key=lambda item: (item[1], ord(item[0]) )) )


#build the huffman tree
nodes = [ Node(frequency, char) for char, frequency in dic.items() ]#create a list to store all the nodes in a list
while len(nodes) > 1:
    #two smallest nodes (first and second in the list)
    left = nodes.pop(0)
    right = nodes.pop(0)

    #check ASCII Code first, make sure value of left node must be smaller than the right node
    if left.char > right.char:
        temp = left
        left = right
        right = temp

    #finally add together to form a new node
    combine = left.frequency + right.frequency

    #add back the combined new node, assigned the attached properties and then append it to the list
    parent = Node(combine)
    parent.char = left.char#new node value must be the left(smallest value) node
    parent.left = left
    parent.right = right
    nodes.append(parent)

    #everytime, we need to sort it again
    #sort the frequency first, and then the ASCII code
    nodes = sorted(nodes, key=lambda node: (node.frequency, ord(node.char)))

#create a new dictionary
dic2 = dict()

def printhuff(node, code = ""):
    if node == None: #end
        return
    elif node.left == None and node.right == None: #then this node is a leave
        dic2[node.char] = code
    else:
        printhuff(node.left, code + "0")#go to left child
        printhuff(node.right, code + "1")#go to right child

#call the function
printhuff(nodes[0])

#sort according to ASCII code, to print out the output in ascending order of ASCII code.
dic3 = dict( sorted(dic2.items(), key=lambda item: (ord(item[0])) ) )

#print the values of the dictionary
for i in dic3.values():
    print(i)


#get the average number of bits used for each symbol: [summation(length * frequency) / summation(frequency)]
sum = 0
for i in dic3.keys():
    sum += len(dic3[i])*dic[i]#length*frequency
sum = sum/len(string)
num = format(sum, ".5f")#output 5 decimal numbers
print(num)