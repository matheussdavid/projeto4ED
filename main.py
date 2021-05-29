import random 
import time
from bubbleSort import *
from insertSort import *
from mergeSort import *
from shellSort import *
from quickSort import *
from algoritmo import *

# Gerador da lista
def gerarLista():
    lista = []
    tamanho = int(input("Informe o tamanho desejado para a lista: "))
    while len(lista) < tamanho:
        x = random.randint(1,5001)
        lista.append(x)
    return lista


novaLista = []
algoritmos = []
tempoBubble = 0
tempoInsert = 0
tempoMerge = 0
tempoQuick = 0
tempoShell = 0
while True:
    print("---------------- PROJETO 4 - ALGORTIMOS DE ORDENAÇÃO ----------------\n")
    print("1 - Gerar Lista")
    print("2 - BubbleSort")
    print("3 - InsertSort")
    print("4 - MergeSort")
    print("5 - QuickSort")
    print("6 - ShellSort")
    print("7 - Tamanho da lista de chaves")
    print("8 - Algoritmos ordenados por tempo de execução")
    print("9 - Sair do programa\n")
    opcao = input("Informe o que opção desejada: ")
    print("")
    if opcao == '1':
        novaLista = gerarLista()
        # print(f'\nLista de chaves:\n{novaLista}\n')
                 
    elif opcao == '2':
        bubble = bubbleSort(novaLista)
        print("--- BUBBLESORT ---")
        print(f'Tempo de execução do BubbleSort: {bubble.tempo}')
        # print(f'Lista BubbleSort: {bubble.lista}\n')
        algoritmos.append(bubble)
    
    elif opcao == '3':
        insert = insertSort(novaLista)
        print("--- INSERTSORT ---")
        print(f'Tempo de execução do InsertSort: {insert.tempo}')
        # print(f'Lista InsertSort: {insert.lista}\n')
        algoritmos.append(insert)
    
    elif opcao == '4':
        merge = mergeSort(novaLista)
        print("--- MERGESORT ---")        
        print(f'Tempo de execução do MergeSort: {merge.tempo}')
        # print(f'Lista MergeSort: {merge.lista}\n')
        algoritmos.append(merge)
    
    elif opcao == '5':
        quick = quickSort(novaLista)
        print("--- QUICKSORT ---")    
        print(f'Tempo de execução do QuickSort: {quick.tempo}')
        # print(f'Lista QuickSort: {quick.lista}')
        algoritmos.append(quick)
    
    elif opcao == '6':
        shell = shellSort(novaLista)
        print("--- SHELLSORT ---")    
        print(f'Tempo de execução do ShellSort: {shell.tempo}')
        # print(f'Lista ShellSort: {shell.lista}')
        algoritmos.append(shell)
    
    elif opcao == '7':
        print(f'Tamanho da lista: {len(novaLista)}\n')
        
    elif opcao == '8':
       print("\nAlgoritmos desordenados: ")
       tempos = []
       for x in algoritmos:
           tempos.append(x.tempo)
       tempos.sort()
       for j in algoritmos:
           print(f'{j}')
       print("\nClassificação dos Algoritmos pelo tempo de resposta:\n")
       aux = 1
       for i in tempos:
           for j in algoritmos: 
               if i == j.tempo:
                   print(f'{aux}º - Nome: {j.nome}, tempo: {j.tempo}')
                   aux += 1
       print()
        
    elif opcao == '9':
        break    
    else:
        print("Opção inválida, informar um valor entre os listados")