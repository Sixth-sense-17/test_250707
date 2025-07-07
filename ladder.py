import random

def print_just_line(c): # 얘가 옆으로
    for _ in range(c):
        print("ㅣ   ", end="")
    print()

def print_s_line(c, before):
    ran_n = random.randint(1, c // 2)
    dot_line = set()
    if c%2 == 1:
        while len(dot_line) < (c // 2):
            rand = random.randint(0, c-2)
            if rand - 1 in dot_line or rand + 1 in dot_line:
                continue
            dot_line.add(rand)
    else:
        while len(dot_line) < (c // 2) - 1:
            rand = random.randint(0, c-2)
            if rand - 1 in dot_line or rand + 1 in dot_line:
                continue
            dot_line.add(rand)

            rand1 = random.randint(0, c-2)
            if rand1 - 1 in dot_line or rand1 + 1 in dot_line\
                  or rand1 in before:
                continue
            dot_line.add(rand1)
        
    for i in range(c):
        if i in dot_line:
            print("ㅣ___", end="")
        else:
            print("ㅣ   ", end="")
    print()

    return dot_line

c = int(input("라인 개수를 적으세요 (숫자): "))
# name = input("사람 이름을 적으세요 (ex. 다람쥐 강사님 ...): ").split()
for n in range(c):
    print(f"{n+1}    ", end="")
print()

before = {}
dic_line = list(0 for _ in range(c-1))
for i in range(10): 
    before = print_s_line(c, before)
    for x in before:
        dic_line[x] += 1
    if i == 7:
        minkey = dic_line.index(min(dic_line))
        for i in range(c):
            if i == minkey:
                print("ㅣ___", end="")
            else:
                print("ㅣ   ", end="") 
        print()       


print_just_line(c)
rand = random.randint(0, c-2)
for i in range(c):
    if i == rand:
        print("*    ", end="")
    else:
        print("     ", end="")