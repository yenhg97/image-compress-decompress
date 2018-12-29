import numpy as np
import cv2
#--------FUNCTION--------#
class node:
	def __init__(self):
		self.dense = None
		self.grayvalue = None

		self.isleaf = None
		self.id = None

		self.left = None
		self.right = None
def binaryTreePaths(root):
    if root is None: 
        return []
    if (root.left == None and root.right == None):
        root.id.append(root.grayvalue)
        return [root.id]

    left_subtree= binaryTreePaths(root.left)  
    right_subtree= binaryTreePaths(root.right)
    full_subtree = left_subtree + right_subtree

    list1 = []
    for leaf in full_subtree:
        list1.append(root.id + leaf)
    return list1
#--------FUNCTION--------#

img = cv2.imread('meo.png',0)
height, width = img.shape[:]

#VARIABLES
dictionary=[None]*256
hist=np.zeros((256),dtype=int)

arr=[]
count=0

#HISTOGRAM HIST
for i in range(0,height):
	for j in range(0,width):
		hist[img[i,j]]+=1
#-------------------------------
for i in range(0,256):
	newnode=node()
	newnode.grayvalue=i
	newnode.dense=hist[i]
	newnode.isleaf=True
	arr.append(newnode)
arr.sort(key=lambda x:x.dense)

#tree generate
while(len(arr)>1):
	newnode=node()
	newnode.left=arr[0]
	arr[0].id=[0]
	newnode.right=arr[1]
	arr[1].id=[1]
	newnode.dense=arr[0].dense+arr[1].dense
	del arr[0]
	del arr[0]
	arr.append(newnode)
	arr.sort(key=lambda x :x.dense)

arr[0].id=[1]
treecode=binaryTreePaths(arr[0])
#print (treecode)
#-----------------------------COMPRESS-------------------------------
for i in treecode:
	index=i[len(i)-1]
	i.pop()
	del i[0]
	#dictionary[index]=i
	dictionary[index]=''.join(str(e)for e in i)

#for i in dictionary:
#	print (i)

dict=open('dictionary_meo.txt','w')
for i in range (0,len(dictionary)):
	dict.write(str(i)+' '+dictionary[i]+'\n')
dict.write(str(256)+' '+str(height)+'\n')
dict.write(str(257)+' '+str(width)+'\n')

bit_count=0
compress=open('imageinBit_meo.txt','w')
for i in range(0,height):
	for j in range (0,width):
		icode=dictionary[img[i,j]]
		bit_count=bit_count+len(icode)
		compress.write(icode)
	compress.write('\n')
print ('----------------------------------------')
print ('HUFFMAN COMPRESSION FOR GRAYSCALE IMAGE:')
print ('Total bits before compressing:',height*width*8)
print ('Total bits after compressing :',bit_count)
compress_percent=round(((height*width*8-bit_count)/(height*width*8))*100,2)
print ('Compressed                   :',compress_percent,' percent')

#-----------------------------DECOMPRESS-----------------------------

