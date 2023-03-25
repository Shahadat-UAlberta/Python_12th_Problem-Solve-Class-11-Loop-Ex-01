"""
1. Empty List - Declare
2. How many data want to add in the list ? -> input()
3. [Loop] -> Input and add in the list

[10, 130, 30, 50]

# Is  Divisible by 10 ?  Print
# 120 >
"""


lst= []
start = 0
end = int(input())

while start < end:
    number = int(input())
    lst.append(number)

    start+=1
print(lst)

value = 0
while value < end:
    if lst [value] > 120:
        break
    elif lst [value] % 10 == 0:
     print (lst[value])
    lst.append (lst[value])

    value += 1

print(lst)


















