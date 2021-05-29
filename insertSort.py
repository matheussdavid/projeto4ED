import time
import sys
sys.setrecursionlimit(40000)
from algoritmo import Algoritmo

def insertSort(alist):
   inicio = time.time()
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
   fim = time.time()
   tempoInsert = fim - inicio
   insert = Algoritmo("InsertionSort", tempoInsert, alist)
   return insert