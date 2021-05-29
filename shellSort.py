import time
import sys
sys.setrecursionlimit(40000)
from algoritmo import Algoritmo

def shellSort(alist):
    inicio = time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
      sublistcount = sublistcount // 2
      
    fim = time.time()
    tempoShell = fim - inicio
    shell = Algoritmo("ShellSort", tempoShell, alist)  
    return shell
    
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

