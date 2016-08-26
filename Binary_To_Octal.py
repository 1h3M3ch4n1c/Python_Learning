#!/usr/bin/python
#There are three possible inputs
#of lengths 3n+1, 3n+2, 3n

#Input
bn_ry = raw_input("Enter the binary number:")
temp_bn_ry = bn_ry

#Length calculation
l_en = len(bn_ry)

#octal number variables
oc_t_temp = ''
oc_t = ''

bn_ry_dct = {'0':'0','1':'1','10':'2','11':'3','100':'4','101':'5','110':'6','111':'7','000':'0','001':'1','010':'2','011':'3'}

f_rm = l_en%3

#If length is <= 3
#For 0,10,110 inputs -- one block input
if l_en <= 3:
    oc_t = bn_ry_dct[bn_ry]
    print oc_t
#First length: 3n+1
elif (f_rm == 1):
    n = n_blocks = l_en/3            #number of blocks of three bits
    co_unt = 0
    k = l_en-1
    while(k <= 3*n+1 and k > 0):
        #print k
        if (n_blocks >= 1):
            co_unt += 1
            oc_t_temp = bn_ry[k]+oc_t_temp
            k -= 1
            if co_unt == 3:
                oc_t = bn_ry_dct[oc_t_temp]+oc_t
                oc_t_temp = ''
                co_unt = 0
                n_blocks -= 1
            elif n_blocks == 0:
                break
    if n_blocks == 0:
        oc_t_temp = bn_ry[k]
        oc_t = bn_ry_dct[oc_t_temp]+oc_t
    print oc_t

#Second length: 3n+2
elif (f_rm == 2):
    n = n_blocks = l_en/3
    #print n
    co_unt = 0
    k = l_en-1
    while (k <= 3*n+2 and k > 1):
        #print k
        if (n_blocks >= 1):
            #print n_blocks
            co_unt += 1
            oc_t_temp = bn_ry[k]+oc_t_temp
            k -= 1
            #print k
            if co_unt == 3:
                oc_t = bn_ry_dct[oc_t_temp]+oc_t
                oc_t_temp = ''
                co_unt = 0
                n_blocks -= 1
                #print n_blocks
            elif n_blocks == 0:
                break
    if n_blocks == 0:
        oc_t_temp = ''
        while (k >=0 ):
            #print k,bn_ry[k]
            oc_t_temp = bn_ry[k]+oc_t_temp
            #print oc_t_temp
            k -= 1
        oc_t = bn_ry_dct[oc_t_temp]+oc_t
    print oc_t

#Third method: 3n
elif (f_rm == 0):
    n = n_blocks = l_en/3
    co_unt = 0
    k = l_en-1
    while (k <= 3*n+3 and k > 2):
        if (n_blocks >= 1):
            #print n_blocks
            co_unt += 1
            oc_t_temp = bn_ry[k]+oc_t_temp
            k -= 1
            if co_unt == 3:
                #print n_blocks
                oc_t = bn_ry_dct[oc_t_temp]+oc_t
                oc_t_temp = ''
                co_unt = 0
                n_blocks -= 1
            elif n_blocks == 0: 
                break
    if n_blocks == 1:
       # print k
        oc_t_temp = ''
        while k >= 0:
            oc_t_temp = bn_ry[k]+oc_t_temp
            k -= 1
        oc_t = bn_ry_dct[oc_t_temp]+oc_t
    print oc_t
