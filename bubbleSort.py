import time
import sys
sys.setrecursionlimit(40000)
from algoritmo import Algoritmo

def bubbleSort(alist):
    inicio = time.time()
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    fim = time.time()
    tempoBubble = fim - inicio
    bubble = Algoritmo("BubbleSort", tempoBubble, alist)
    return bubble
