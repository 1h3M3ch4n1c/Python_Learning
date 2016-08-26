#!/usr/bin/python
#There are four possible inputs
#of lengths 4n+1, 4n+2, 4n+3, 4n

#Input
bn_ry = raw_input("Enter the binary number:")
temp_bn_ry = bn_ry

#Length calculation
l_en = len(bn_ry)

#octal number variables
hx_temp = ''
hx = ''

bn_ry_dct = {'0':'0','1':'1','10':'2','11':'3','100':'4','101':'5','110':'6','111':'7','000':'0','001':'1','010':'2','011':'3',
             '1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F',
             '0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7'
            }


f_rm = l_en%4

#If length is <= 4
#For 0,10,110,1000 inputs -- one block input
if l_en <= 4:
    hx = bn_ry_dct[bn_ry]
    print hx

#First length: 4n+1
elif (f_rm == 1):
    n = n_blocks = l_en/4           #number of blocks of four bits
    co_unt = 0
    k = l_en-1
    while(k <= 4*n+1 and k > 0):
        #print k
        if (n_blocks >= 1):
            co_unt += 1
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
            if co_unt == 4:
                hx = bn_ry_dct[hx_temp]+hx
                hx_temp = ''
                co_unt = 0
                n_blocks -= 1
            elif n_blocks == 0:
                break
    if n_blocks == 0:
        hx_temp = bn_ry[k]
        hx = bn_ry_dct[hx_temp]+hx
    print hx

#Second length: 4n+2
elif (f_rm == 2):
    n = n_blocks = l_en/4
    #print n
    co_unt = 0
    k = l_en-1
    while (k <= 4*n+2 and k > 1):
        #print k
        if (n_blocks >= 1):
            #print n_blocks
            co_unt += 1
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
            #print k
            if co_unt == 4:
                hx = bn_ry_dct[hx_temp]+hx
                hx_temp = ''
                co_unt = 0
                n_blocks -= 1
                #print n_blocks
            elif n_blocks == 0:
                break
    if n_blocks == 0:
        hx_temp = ''
        while (k >=0 ):
            #print k,bn_ry[k]
            hx_temp = bn_ry[k]+hx_temp
            #print oc_t_temp
            k -= 1
        hx = bn_ry_dct[hx_temp]+hx
    print hx

#Third length: 4n+3
elif (f_rm == 3):
    n = n_blocks = l_en/4
    co_unt = 0
    k = l_en-1
    while (k <= 4*n+3 and k > 2):
        if (n_blocks >= 1):
            co_unt += 1
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
            if co_unt == 4:
                hx = bn_ry_dct[hx_temp]+hx
                hx_temp = ''
                co_unt = 0
                n_blocks -= 1
            elif n_blocks == 0:
                break
    if n_blocks == 0:
        hx_temp = ''
        while (k >= 0):
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
        hx = bn_ry_dct[hx_temp]+hx
    print hx
elif (f_rm == 0):
    n = n_blocks = l_en/4
    co_unt = 0
    k = l_en-1
    while (k <= 4*n+4 and k > 3):
        if (n_blocks >= 1):
            #print n_blocks
            co_unt += 1
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
            if co_unt == 4:
                #print n_blocks
                hx = bn_ry_dct[hx_temp]+hx
                hx_temp = ''
                co_unt = 0
                n_blocks -= 1
            elif n_blocks == 0: 
                break
    if n_blocks == 1:
       # print k
        hx_temp = ''
        while k >= 0:
            hx_temp = bn_ry[k]+hx_temp
            k -= 1
        hx = bn_ry_dct[hx_temp]+hx
    print hx
