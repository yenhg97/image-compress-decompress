import numpy as np
import cv2
import sys
import os.path
import pickle

def lzw_encode(img_path, save_path):
    img = cv2.imread(img_path)
    shape = img.shape
    flatten_img = img.reshape(-1)
    dictionary = dict()
    dict_size = 256
    for i in range(256):
        dictionary[chr(i)] = i

    code_arr = list()
    
    s = chr(flatten_img[0])
    for i in range(1, len(flatten_img)):
        c = chr(flatten_img[i])
        sc = s + c
        if sc in dictionary.keys():
            s = sc
        else:
            code_arr.append(dictionary[s])
            dictionary[sc] = dict_size
            dict_size = dict_size + 1
            s = c
    if s:
        code_arr.append(dictionary[s])
    #print (code_arr)
    with open(save_path, "wb") as f:
        pickle.dump((code_arr, shape), f)
    
def lzw_decode(save_path, img_path):
    with open(save_path, "rb") as f:
        code_arr, shape = pickle.load(f)
    dictionary = dict()
    dict_size = 256
    for i in range(256):
        dictionary[i] = chr(i) 
        
    img = ""
    s = chr(code_arr.pop(0))
    img += s
    for k in code_arr:
        if k in dictionary.keys():
            entry = dictionary[k]
        elif k == dict_size:
            entry = s + s[0]
        img += entry    
        
        dictionary[dict_size] = s + entry[0]
        dict_size += 1
        s = entry
        
    img = [ord(x) for x in img]
    img = np.array(img, dtype=np.uint16).reshape(shape)
    cv2.imwrite(img_path, img)
    #cv2.imshow("img", img)
    
if __name__ == '__main__':
    img_path1 = sys.argv[1]
    save_path = sys.argv[2]
    img_path2 = sys.argv[3]
    lzw_encode(img_path1, save_path)
    lzw_decode(save_path, img_path2)
    