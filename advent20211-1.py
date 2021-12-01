down = 0
last = 0
with open("c:\\data\\code\\input1.txt") as file:
        lista = file.read().split()
        for actual in lista:
                if int(actual) > last:
                        down += 1
                last = int(actual)
        print(down - 1)

        down = 0
        last = 0
        pos = 0
        while pos < len(lista)-2:
                actual = int(lista[pos]) + int(lista[pos+1]) + int(lista[pos+2])
                if int(actual) > last:
                        down += 1
                last = actual
                pos +=1
        print(down -1)
                
