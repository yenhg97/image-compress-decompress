import numpy as np
import cv2
#---------------------------------------------------------
class node:
    def __init__(self):
        self.grayvalue=None
        self.isleaf=None
        self.id=None
        self.left=None
        self.right=None

def tree_builder(nut,array,i,index):
    if i==len(array)-1:
        if array[i]==0:
            if nut.left==None:
                newnode=node()
                newnode.id=0
                nut.left=newnode
                newnode.grayvalue=index
                newnode.isleaf=True
                return
        if array[i]==1:
            if nut.right==None:
                newnode=node()
                newnode.id=1
                nut.right=newnode
                newnode.grayvalue=index
                newnode.isleaf=True
                return
    else:
        if array[i]==0:
            if nut.left==None:
                newnode=node()
                newnode.id=0
                nut.left=newnode
                newnode.isleaf=False
                tree_builder(newnode,array,i+1,index)
            else:
                tree_builder(nut.left,array,i+1,index)
        if array[i]==1:
            if nut.right==None:
                newnode=node()
                newnode.id=1
                nut.right=newnode
                newnode.isleaf=False
                tree_builder(newnode,array,i+1,index)
            else:
                tree_builder(nut.right,array,i+1,index)
#tree test
def binaryTreePaths(root):
    if root is None: 
        return []
    if (root.left == None and root.right == None):
        return [str(root.id)]
    left_subtree = binaryTreePaths(root.left)  
    right_subtree = binaryTreePaths(root.right)
    full_subtree = left_subtree + right_subtree
    list1 = []
    for leaf in full_subtree:
        list1.append(str(root.id) + '-'+ leaf)
    return list1

def find(mang,nod,chiso):
    if nod.isleaf==True:
        e.append(nod.grayvalue)
        idx.append(chiso)
        return 
    else:
        if mang[chiso]=='0':
            find(mang,nod.left,chiso+1)
        if mang[chiso]=='1':
            find(mang,nod.right,chiso+1)

#---------------------------------------------------------
dict=open('dictionary_meo.txt','r')
file=open('imageinBit_meo.txt','r')
tree_array=[]
ii=0
#---------------------------------------------------------
for i in dict:
    temp=i.split(' ')
    j=list(temp[1])
    j.pop()# remove \n
    for i in range(0,len(j)):
        j[i]=int(j[i])
    tree_array.append(j)
    ii+=1
#get width and height from dict
width=tree_array.pop()
height=tree_array.pop()
width=int(''.join(str(e)for e in width))
height=int(''.join(str(e)for e in height))
print(height,width)
#for i in tree_array:
#    print(i)
#Tree generate
root=node()
for index in range(0,len(tree_array)):
    i=0
    tree_builder(root,tree_array[index],i,index)
#ss=binaryTreePaths(root)
#print(root.left.left.left.left.left.left.grayvalue)

#--------------------------------------------------------
array=[]#<---[['1010101'],['1000101]]
img=[]
for line in file:
    array.append(line.split())
    
for i in array:
    code=i[0]
    code=list(code)

    m=0
    e=[]
    idx=[]
    while(m<len(code)-1):
        find(code,root,m)
        m=idx[len(idx)-1]
    img.append(e)


#--------------------------------------------------------

#--------------------------------------------------------
img=np.array(img,dtype=np.uint8)
cv2.imshow('DECOMPRESS',img)
cv2.imwrite('meo-decompress.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()