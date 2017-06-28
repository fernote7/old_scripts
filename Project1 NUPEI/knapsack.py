__author__ = 'Fernando'

def knapsack_without_rep(items, W):
    K={}
    backpack=[]
    for j in range(len(items)+1):
        K.update({(0,j):0})
    for w in range(1,W+1):
        K.update({(w,0):0})

    for w in range(1,W+1): #1 ate W
        for j in range(1,1+len(items)):
            item=items[j-1]
            aux=K[(w,j-1)]
            #for item in items:#(wi,vi)
            if item[0]<=w:
                if K[(w-item[0],j-1)]+item[1]>aux:
                    aux=K[(w-item[0],j-1)]+item[1]
            K.update({(w,j):aux})
    return K[W,len(items)]

def knapsack_with_rep(items, W):
    K={0:0}
    for w in range(1,W+1): #1 ate W
        aux=0
        for item in items:#(peso, valor)
            if item[0]<=w:
                aux=max(K[w-item[0]]+item[1],aux)
            K.update({w:aux})
    return K[W]

items = [(12,4), (1,2), (4,6), (1, 1), (2, 2)]
W = 15
print knapsack_without_rep(items, W)