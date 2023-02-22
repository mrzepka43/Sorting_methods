from math import ceil
import sys
import random
import time
import threading
sys.setrecursionlimit(10000000)
threading.stack_size(2**26)

# zmienne w ktorych zliczana jest ilosc operacji w algorytmie
ilosc_porownan_quick = 0
ilosc_zamian_quick = 0
iteracja = 0

ilosc_porownan_merge = 0
ilosc_scalen_podzbiorow = 0

ilosc_porownan_heap = 0
ilosc_zamian_heap = 0

ilosc_porownan_bubble = 0
ilosc_zamian_bubble = 0

ilosc_porownan_select = 0
ilosc_zamian_select = 0

ilosc_porownan_insert = 0
ilosc_zamian_insert = 0

def main():
    ##### heap sort #################################
    global ilosc_porownan_heap
    global ilosc_zamian_heap

    def sorting(heap,i):
        global ilosc_porownan_heap
        global ilosc_zamian_heap
        if i == 0 or heap[i] > heap[ceil((i / 2) - 1)]:
            ilosc_porownan_heap += 1
            return heap
        elif heap[i] < heap[ceil((i / 2) - 1)]:
            ilosc_porownan_heap += 1
            ilosc_zamian_heap += 1
            temp = heap[ceil((i / 2) - 1)]
            heap[ceil((i / 2) - 1)] = heap[i]
            heap[i] = temp
        return sorting(heap,ceil((i / 2) - 1))


    def creating_heap(tab):
        heap = []
        heap.append(tab[0])
        i = 1
        while i < len(tab):
            heap.append(tab[i])
            sorting(heap,i)
            i += 1
        return heap


    def repair(tab,iter):
        global ilosc_porownan_heap
        global ilosc_zamian_heap
        left = (iter * 2) + 1
        right = (iter * 2) + 2
        largest = iter
        if left < len(tab):
            if tab[largest] > tab[left]:
                largest = left
            ilosc_porownan_heap += 1
        if right < len(tab):
            if tab[largest] > tab[right]:
                largest = right
            ilosc_porownan_heap += 1
        if largest != iter:
            temp = tab[iter]
            tab[iter] = tab[largest]
            tab[largest] = temp
            ilosc_zamian_heap += 1
            return repair(tab, largest)
        else:
            return tab


    def sorting_heap(tab):
        global ilosc_zamian_heap
        sorted = []
        i = len(tab) - 1
        while i >= 0:
            sorted.append(tab[0])
            tab[0] = tab[i]
            i -= 1
            tab.pop()
            if len(tab) != 0:
                ilosc_zamian_heap += 1
                repair(tab,0)
        return sorted


    ##########################################################
    ##### merge sort #########################################


    global ilosc_porownan_merge
    global ilosc_scalen_podzbiorow

    def merge_sort(tab):
        global ilosc_porownan_merge
        global ilosc_scalen_podzbiorow
        halfsize = int(len(tab) / 2)
        if len(tab) == 1:
            return tab
        else:
            ilosc_scalen_podzbiorow += 1
            left = []
            right = []
            for i in range(halfsize):
                left.append(tab[i])
            for i in range(halfsize, len(tab)):
                right.append(tab[i])

            merge_sort(left)
            merge_sort(right)

            i = 0 #iteracja lewej tablicy
            j = 0 #iteracja prawej tablicy
            k = 0 #iteracja wynikowej tablicy
            while i < len(left) and j < len(right):
                ilosc_porownan_merge += 1
                if left[i] < right[j]:
                    tab[k] = left[i]
                    i += 1
                    k += 1
                else:
                    tab[k] = right[j]
                    j += 1
                    k += 1
            if i == len(left):
                while j < len(right):
                    tab[k] = right[j]
                    k += 1
                    j += 1
            if j == len(right):
                while i < len(left):
                    tab[k] = left[i]
                    k += 1
                    i += 1
            return tab


    ##########################################################
    #### quick sort ##########################################


    global ilosc_porownan_quick
    global ilosc_zamian_quick
    global iteracja


    def partition(tab, k, l):

        global ilosc_porownan_quick
        global ilosc_zamian_quick
        global iteracja

        #iteracja += 1
        pivot = tab[l]
        i = k  # przeglada tablice do przedosttaniego elementu
        j = k  # wskazuje z jakim elemenetem ostatnim wymienilismy liczbe
        while i < l:
            ilosc_porownan_quick += 1
            if tab[i] <= pivot:
                ilosc_zamian_quick += 1
                temp = tab[j]
                tab[j] = tab[i]
                tab[i] = temp
                i += 1
                j += 1
            else:
                i += 1
        temp = tab[j]
        tab[j] = tab[l]
        tab[l] = temp
        ilosc_zamian_quick += 1
        return j


    def quick_sort(tab, k, l):
        if k >= l:
            return tab
        else:
            j = partition(tab, k, l)
            quick_sort(tab, j + 1, l)
            quick_sort(tab, k, j - 1)
        return tab


    #############################################################
    #### bubble sort ############################################


    global ilosc_porownan_bubble
    global ilosc_zamian_bubble

    def bombelkowe(table):
        global ilosc_porownan_bubble
        global ilosc_zamian_bubble
        for i in range(len(table)):
            for j in range(len(table) - 1):
                ilosc_porownan_bubble += 1
                if table[j] > table[j + 1]:
                    ilosc_zamian_bubble += 1
                    helping = table[j + 1]
                    table[j + 1] = table[j]
                    table[j] = helping
        return table


    #############################################################
    #### insertion sort #########################################


    global ilosc_porownan_insert
    global ilosc_zamian_insert


    def wstawianie(table):
        global ilosc_porownan_insert
        global ilosc_zamian_insert
        for i in range(len(table) - 1, 0, -1):
            for j in range(i - 1, len(table) - 1, 1):
                ilosc_porownan_insert += 1
                if table[j] > table[j + 1]:
                    ilosc_zamian_insert += 1
                    help = table[j + 1]
                    table[j + 1] = table[j]
                    table[j] = help
                else:
                    break
        return table


    #############################################################
    #### selection sort #########################################


    global ilosc_porownan_select
    global ilosc_zamian_select


    def wybor(table):
        global ilosc_zamian_select
        global ilosc_porownan_select
        for i in range(len(table)):
            smallest = table[i]
            position = i
            for j in range(i, len(table)):
                ilosc_porownan_select += 1
                if table[j] < smallest:
                    ilosc_zamian_select += 1
                    smallest = table[j]
                    position = j
            ilosc_zamian_select += 1
            table[position] = table[i]
            table[i] = smallest
        return table


    #############################################################
    #### random table creation ##################################


    def randomtable(elem_quan, random_range):
        table = []
        for i in range(elem_quan):
            table.append(random.randint(0, random_range))
        return table

    #############################################################
    #### increasing table creation ##############################


    def increasingtable(elem_quan, random_range):
        border = random_range / elem_quan
        first = random.randint(0, border)
        table = [first]
        i = 0
        while len(table) < elem_quan:
            elem = random.randint(border, border + 10)
            if elem >= table[i]:
                border += random_range / elem_quan
                i += 1
                table.append(elem)
        return table


    #############################################################
    #### decreasing table creation ##############################


    def decreasingtable(elem_quan, random_range):
        decrease = 10
        border = random_range - decrease
        first = random.randint(border, random_range)
        table = [first]
        i = 0
        while len(table) < elem_quan:
            elem = random.randint(border, random_range)
            if elem <= table[i]:
                border -= decrease
                random_range -= decrease
                i += 1
                table.append(elem)
        return table


    #############################################################
    #### A shaped table creation ################################


    def Ashapedtable(elem_quan, random_range):
        border = 40
        first = random.randint(0, border)
        table = [first]
        i = 0
        while len(table) < elem_quan / 2:
            elem = random.randint(border, border + 20)
            if elem >= table[i]:
                border += 20
                i += 1
                table.append(elem)

        decrease = 20
        border = random_range - decrease
        while len(table) < elem_quan:
            elem = random.randint(border, random_range)
            if elem < table[i]:
                border -= decrease
                random_range -= decrease
                i += 1
                table.append(elem)
        return table


    #############################################################
    #### V shaped table creation ################################


    def Vshapedtable(elem_quan, random_range):
        decrease = 20
        border = random_range - decrease
        first = random.randint(border, random_range)
        border -= decrease
        random_range -= decrease
        table = [first]
        i = 0
        while len(table) < elem_quan / 2:
            elem = random.randint(border, random_range)
            if elem < table[i]:
                border -= decrease
                random_range -= decrease
                i += 1
                table.append(elem)
        border = 0
        while len(table) < elem_quan:

            elem = random.randint(border, border + 20)
            if elem >= table[i]:
                border += 20
                i += 1
                table.append(elem)
        return table



    #############################################################
    ##### testy heap ############################################


    def testheap(table):
        global ilosc_porownan_heap
        global ilosc_zamian_heap

        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        zamiany_na_poczatku = ilosc_zamian_heap
        porownania_na_poczatku = ilosc_porownan_heap

        start = time.time()
        sorting_heap(creating_heap(table))
        end = time.time()

        local_porownania = ilosc_porownan_heap - porownania_na_poczatku
        local_zamiany = ilosc_zamian_heap - zamiany_na_poczatku
        worktime = end - start
        '''
        file.write("Czas trwania algorytmu heap sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan heap: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian heap: \n")
        file.write(str(local_zamiany))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_zamiany
        return worktime, ilosc_operacji


    ###########################################################
    #### testy merge ##########################################


    def testmerge(table):
        global ilosc_scalen_podzbiorow
        global ilosc_porownan_merge
        scalenia_na_poczatku = ilosc_scalen_podzbiorow
        porownania_na_poczatku = ilosc_porownan_merge

        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        start = time.time()
        merge_sort(table)
        end = time.time()
        worktime = end - start

        local_porownania = ilosc_porownan_merge - porownania_na_poczatku
        local_scalenia = ilosc_scalen_podzbiorow - scalenia_na_poczatku
        '''
        file.write("Czas trwania algorytmu merge sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan merge: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian merge: \n")
        file.write(str(scalenia_na_poczatku))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_scalenia
        return worktime, ilosc_operacji


    ########################################################
    #### testy quick sort ##################################


    def testquick(table):
        global ilosc_porownan_quick
        global ilosc_zamian_quick
        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        zamiany_na_poczatku = ilosc_zamian_quick
        porownania_na_poczatku = ilosc_porownan_quick

        start = time.time()
        quick_sort(table, 0, len(table) - 1)
        end = time.time()
        worktime = end - start

        local_porownania = ilosc_porownan_quick - porownania_na_poczatku
        local_zamiany = ilosc_zamian_quick - zamiany_na_poczatku
        '''
        file.write("Czas trwania algorytmu quick sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan quick: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian quick: \n")
        file.write(str(local_zamiany))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_zamiany
        return worktime, ilosc_operacji


    ########################################################
    #### bubble sort #######################################


    def testbubble(table):
        global ilosc_zamian_bubble
        global ilosc_porownan_bubble
        zamiany_na_poczatku = ilosc_zamian_bubble
        porownania_na_poczatku = ilosc_porownan_bubble

        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        start = time.time()
        bombelkowe(table)
        end = time.time()

        local_porownania = ilosc_porownan_bubble - porownania_na_poczatku
        local_zamiany = ilosc_zamian_bubble - zamiany_na_poczatku
        worktime = end - start
        '''
        file.write("Czas trwania algorytmu bubble sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan bubble: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian bubble: \n")
        file.write(str(local_zamiany))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_zamiany
        return worktime, ilosc_operacji


    ########################################################
    #### insertion sort ####################################


    def testinsert(table):
        global ilosc_zamian_insert
        global ilosc_porownan_insert
        zamiany_na_poczatku = ilosc_zamian_insert
        porownania_na_poczatku = ilosc_porownan_insert

        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        start = time.time()
        wstawianie(table)
        end = time.time()

        local_porownania = ilosc_porownan_insert - porownania_na_poczatku
        local_zamiany = ilosc_zamian_insert - zamiany_na_poczatku
        worktime = end - start
        '''
        file.write("Czas trwania algorytmu insertion sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan insert: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian insert: \n")
        file.write(str(local_zamiany))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_zamiany
        return worktime, ilosc_operacji
    ########################################################
    #### selection sort ####################################


    def testselect(table):
        global ilosc_zamian_select
        global ilosc_porownan_select
        zamiany_na_poczatku = ilosc_zamian_select
        porownania_na_poczatku = ilosc_porownan_select

        #mierzenie czasu, ilosci zamian i porownan i odpalenie algorytmu

        start = time.time()
        wybor(table)
        end = time.time()

        local_porownania = ilosc_porownan_select - porownania_na_poczatku
        local_zamiany = ilosc_zamian_select - zamiany_na_poczatku
        worktime = end - start
        '''
        file.write("Czas trwania algorytmu insertion sort: \n")
        file.write(str(worktime))
        file.write("\n")
        file.write("Ilosc porownan insert: \n")
        file.write(str(local_porownania))
        file.write("\n")
        file.write("Ilosc zamian insert: \n")
        file.write(str(local_zamiany))
        file.write("\n\n")
        '''
        ilosc_operacji = local_porownania + local_zamiany
        return worktime, ilosc_operacji


    ########################################################
    #### strefa testowania ##################################




    def testyrosnace(algorytm, a):
        file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki sortowania/Wyniki_quick.txt", "a")
        how_many = a
        range = how_many * 10

        table1 = increasingtable(how_many, range)
        table2 = increasingtable(how_many, range)
        table3 = increasingtable(how_many, range)
        table4 = increasingtable(how_many, range)
        table5 = increasingtable(how_many, range)
        table6 = increasingtable(how_many, range)
        table7 = increasingtable(how_many, range)
        table8 = increasingtable(how_many, range)
        table9 = increasingtable(how_many, range)
        table10 = increasingtable(how_many, range)


        #Tutaj zminiac naglowek sekcji wyniku
        print("jestem")
        file.write("Testy ")
        file.write(str(algorytm))
        file.write(" dane rosnace, ")
        file.write(str(a))
        file.write(" elementow \n\n")

        file.write("Test1 \n\n")
        res1 = algorytm(table1)
        file.write("Test2 \n\n")
        res2 = algorytm(table2)
        file.write("Test3 \n\n")
        res3 = algorytm(table3)
        file.write("Test4 \n\n")
        res4 = algorytm(table4)
        file.write("Test5 \n\n")
        res5 = algorytm(table5)
        file.write("Test6 \n\n")
        res6 = algorytm(table6)
        file.write("Test7 \n\n")
        res7 = algorytm(table7)
        file.write("Test8 \n\n")
        res8 = algorytm(table8)
        file.write("Test9 \n\n")
        res9 = algorytm(table9)
        file.write("Test10 \n\n")
        res10 = algorytm(table10)

        whole_time = res1[0] + res2[0] + res3[0] + res4[0] + res5[0] + res6[0] + res7[0] + res8[0] + res9[0] + res10[0]
        mid_time = whole_time / 10

        file.write("\n\n\n")
        file.write("Sredni czas trwania algorytmu w sekundach: \n")
        file.write(str(mid_time))
        file.write("\n\n\n")

        operations = res1[1] + res2[1] + res3[1] + res4[1] + res5[1] + res6[1] + res7[1] + res8[1] + res9[1] + res10[1]
        mid_op = operations / 10

        file.write("Srednia ilosc operacji algorytmu: \n")
        file.write(str(mid_op))
        file.write("\n\n\n")
        file.close()


    def testyrandom(algorytm, a):
        file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki sortowania/Wyniki_quick.txt", "a")
        how_many = a
        range = how_many * 10

        table1 = randomtable(how_many, range)
        table2 = randomtable(how_many, range)
        table3 = randomtable(how_many, range)
        table4 = randomtable(how_many, range)
        table5 = randomtable(how_many, range)
        table6 = randomtable(how_many, range)
        table7 = randomtable(how_many, range)
        table8 = randomtable(how_many, range)
        table9 = randomtable(how_many, range)
        table10 = randomtable(how_many, range)


        #Tutaj zminiac naglowek sekcji wyniku
        file.write("Testy ")
        file.write(str(algorytm))
        file.write(" dane random, ")
        file.write(str(a))
        file.write(" elementow \n\n")
        file.write("Test1 \n\n")
        res1 = algorytm(table1)
        file.write("Test2 \n\n")
        res2 = algorytm(table2)
        file.write("Test3 \n\n")
        res3 = algorytm(table3)
        file.write("Test4 \n\n")
        res4 = algorytm(table4)
        file.write("Test5 \n\n")
        res5 = algorytm(table5)
        file.write("Test6 \n\n")
        res6 = algorytm(table6)
        file.write("Test7 \n\n")
        res7 = algorytm(table7)
        file.write("Test8 \n\n")
        res8 = algorytm(table8)
        file.write("Test9 \n\n")
        res9 = algorytm(table9)
        file.write("Test10 \n\n")
        res10 = algorytm(table10)

        whole_time = res1[0] + res2[0] + res3[0] + res4[0] + res5[0] + res6[0] + res7[0] + res8[0] + res9[0] + res10[0]
        mid_time = whole_time / 10

        file.write("\n\n\n")
        file.write("Sredni czas trwania algorytmu w sekundach: \n")
        file.write(str(mid_time))
        file.write("\n\n\n")

        operations = res1[1] + res2[1] + res3[1] + res4[1] + res5[1] + res6[1] + res7[1] + res8[1] + res9[1] + res10[1]
        mid_op = operations / 10

        file.write("Srednia ilosc operacji algorytmu: \n")
        file.write(str(mid_op))
        file.write("\n\n\n")
        file.close()


    def testymalejace(algorytm, a):
        file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki sortowania/Wyniki_quick.txt", "a")
        how_many = a
        range = how_many * 10

        table1 = decreasingtable(how_many, range)
        table2 = decreasingtable(how_many, range)
        table3 = decreasingtable(how_many, range)
        table4 = decreasingtable(how_many, range)
        table5 = decreasingtable(how_many, range)
        table6 = decreasingtable(how_many, range)
        table7 = decreasingtable(how_many, range)
        table8 = decreasingtable(how_many, range)
        table9 = decreasingtable(how_many, range)
        table10 = decreasingtable(how_many, range)


        #Tutaj zminiac naglowek sekcji wyniku
        file.write("Testy ")
        file.write(str(algorytm))
        file.write(" dane malejace, ")
        file.write(str(a))
        file.write(" elementow \n\n")
        file.write("Test1 \n\n")
        res1 = algorytm(table1)
        print("1")
        file.write("Test2 \n\n")
        res2 = algorytm(table2)
        file.write("Test3 \n\n")
        res3 = algorytm(table3)
        file.write("Test4 \n\n")
        res4 = algorytm(table4)
        file.write("Test5 \n\n")
        res5 = algorytm(table5)
        file.write("Test6 \n\n")
        res6 = algorytm(table6)
        file.write("Test7 \n\n")
        res7 = algorytm(table7)
        file.write("Test8 \n\n")
        res8 = algorytm(table8)
        file.write("Test9 \n\n")
        res9 = algorytm(table9)
        file.write("Test10 \n\n")
        res10 = algorytm(table10)
        print("10")

        whole_time = res1[0] + res2[0] + res3[0] + res4[0] + res5[0] + res6[0] + res7[0] + res8[0] + res9[0] + res10[0]
        mid_time = whole_time / 10

        file.write("\n\n\n")
        file.write("Sredni czas trwania algorytmu w sekundach: \n")
        file.write(str(mid_time))
        file.write("\n\n\n")

        operations = res1[1] + res2[1] + res3[1] + res4[1] + res5[1] + res6[1] + res7[1] + res8[1] + res9[1] + res10[1]
        mid_op = operations / 10

        file.write("Srednia ilosc operacji algorytmu: \n")
        file.write(str(mid_op))
        file.write("\n\n\n")
        file.close()


    def testyA(algorytm, a):
        file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki sortowania/Wyniki_quick.txt", "a")
        how_many = a
        range = how_many * 10

        table1 = Ashapedtable(how_many, range)
        print("1")
        table2 = Ashapedtable(how_many, range)
        print("2")
        table3 = Ashapedtable(how_many, range)
        print("3")
        table4 = Ashapedtable(how_many, range)
        print("4")
        table5 = Ashapedtable(how_many, range)
        print("5")
        table6 = Ashapedtable(how_many, range)
        print("6")
        table7 = Ashapedtable(how_many, range)
        print("7")
        table8 = Ashapedtable(how_many, range)
        print("8")
        table9 = Ashapedtable(how_many, range)
        print("9")
        table10 = Ashapedtable(how_many, range)
        print("10")


        #Tutaj zminiac naglowek sekcji wyniku
        file.write("Testy ")
        file.write(str(algorytm))
        file.write(" dane A shaped, ")
        file.write(str(a))
        file.write(" elementow \n\n")
        file.write("Test1 \n\n")
        res1 = algorytm(table1)
        file.write("Test2 \n\n")
        res2 = algorytm(table2)
        file.write("Test3 \n\n")
        res3 = algorytm(table3)
        file.write("Test4 \n\n")
        res4 = algorytm(table4)
        file.write("Test5 \n\n")
        res5 = algorytm(table5)
        file.write("Test6 \n\n")
        res6 = algorytm(table6)
        file.write("Test7 \n\n")
        res7 = algorytm(table7)
        file.write("Test8 \n\n")
        res8 = algorytm(table8)
        file.write("Test9 \n\n")
        res9 = algorytm(table9)
        file.write("Test10 \n\n")
        res10 = algorytm(table10)

        whole_time = res1[0] + res2[0] + res3[0] + res4[0] + res5[0] + res6[0] + res7[0] + res8[0] + res9[0] + res10[0]
        mid_time = whole_time / 10

        file.write("\n\n\n")
        file.write("Sredni czas trwania algorytmu w sekundach: \n")
        file.write(str(mid_time))
        file.write("\n\n\n")

        operations = res1[1] + res2[1] + res3[1] + res4[1] + res5[1] + res6[1] + res7[1] + res8[1] + res9[1] + res10[1]
        mid_op = operations / 10

        file.write("Srednia ilosc operacji algorytmu: \n")
        file.write(str(mid_op))
        file.write("\n\n\n")
        file.close()


    def testyV(algorytm, a):
        file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki sortowania/Wyniki_quick.txt", "a")
        how_many = a
        range = how_many * 10

        table1 = Vshapedtable(how_many, range)
        table2 = Vshapedtable(how_many, range)
        table3 = Vshapedtable(how_many, range)
        table4 = Vshapedtable(how_many, range)
        table5 = Vshapedtable(how_many, range)
        table6 = Vshapedtable(how_many, range)
        table7 = Vshapedtable(how_many, range)
        table8 = Vshapedtable(how_many, range)
        table9 = Vshapedtable(how_many, range)
        table10 = Vshapedtable(how_many, range)


        #Tutaj zminiac naglowek sekcji wyniku
        file.write("Testy ")
        file.write(str(algorytm))
        file.write(" dane V shaped, ")
        file.write(str(a))
        file.write(" elementow \n\n")
        file.write("Test1 \n\n")
        res1 = algorytm(table1)
        print("1")
        file.write("Test2 \n\n")
        res2 = algorytm(table2)
        file.write("Test3 \n\n")
        res3 = algorytm(table3)
        file.write("Test4 \n\n")
        res4 = algorytm(table4)
        file.write("Test5 \n\n")
        res5 = algorytm(table5)
        file.write("Test6 \n\n")
        res6 = algorytm(table6)
        file.write("Test7 \n\n")
        res7 = algorytm(table7)
        file.write("Test8 \n\n")
        res8 = algorytm(table8)
        file.write("Test9 \n\n")
        res9 = algorytm(table9)
        file.write("Test10 \n\n")
        print("10")
        res10 = algorytm(table10)

        whole_time = res1[0] + res2[0] + res3[0] + res4[0] + res5[0] + res6[0] + res7[0] + res8[0] + res9[0] + res10[0]
        mid_time = whole_time / 10

        file.write("\n\n\n")
        file.write("Sredni czas trwania algorytmu w sekundach: \n")
        file.write(str(mid_time))
        file.write("\n\n\n")

        operations = res1[1] + res2[1] + res3[1] + res4[1] + res5[1] + res6[1] + res7[1] + res8[1] + res9[1] + res10[1]
        mid_op = operations / 10

        file.write("Srednia ilosc operacji algorytmu: \n")
        file.write(str(mid_op))
        file.write("\n\n\n")
        file.close()

    # Gdy zmieniamy algorytm jaki chcemy tesowac oprocz zmiany zmiennej 'jaki' w kazdej funkcji 'testy' musimy zmienic
    # nazwe pliku do jakiego zapisujemy dane (do rozwiazania pozniej)

    jaki = testquick
    testyrandom(jaki, 100)
    testyrandom(jaki, 200)
    testyrandom(jaki, 300)
    testyrandom(jaki, 400)
    testyrandom(jaki, 500)
    testyrandom(jaki, 1500)
    testyrandom(jaki, 2500)


    print("zrobione")
    testyrosnace(jaki, 100)
    testyrosnace(jaki, 200)
    testyrosnace(jaki, 300)
    testyrosnace(jaki, 400)
    testyrosnace(jaki, 500)
    testyrosnace(jaki, 1500)
    testyrosnace(jaki, 2500)


    print("zrobione")

    testyA(jaki, 100)
    testyA(jaki, 200)
    testyA(jaki, 300)
    testyA(jaki, 400)
    testyA(jaki, 500)
    testyA(jaki, 1500)
    testyA(jaki, 2500)



    print("zrobione")

    testyV(jaki, 100)
    testyV(jaki, 200)
    testyV(jaki, 300)
    testyV(jaki, 400)
    testyV(jaki, 500)
    testyV(jaki, 1500)
    testyV(jaki, 2500)


    print("zrobione")
    testymalejace(jaki, 100)
    testymalejace(jaki, 200)
    testymalejace(jaki, 300)
    testymalejace(jaki, 400)
    testymalejace(jaki, 500)
    testymalejace(jaki, 1500)
    testymalejace(jaki, 2500)


x = threading.Thread(target=main)
x.start()
