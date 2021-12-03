pos=0
down = 0
last = 0
with open("c:\\data\\code\\input2.txt") as file:
        lista = file.read().split('\n')
        for command in lista:
                #print(command)
                command = command.split()
                action = command[0]
                param = int(command[1])
                if action == "forward":
                        pos += param
                elif action == "down":
                        down += param
                elif action == "up":
                        down -= param
                #print(pos,down)
        print(pos*down)
                
        
pos=0
down = 0
aim = 0
with open("c:\\data\\code\\input2.txt") as file:
        lista = file.read().split('\n')
        for command in lista:
                #print(command)
                command = command.split()
                action = command[0]
                param = int(command[1])
                if action == "forward":
                        pos += param
                        down += aim * param
                elif action == "down":
                        aim += param
                elif action == "up":
                        aim -= param
                #print(pos,down)
        print(pos*down)
                
