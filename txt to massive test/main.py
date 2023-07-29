import string
file1 = open('../test2.txt', encoding='utf-8')
# print(file.read()) # вывести весь текст

with open('../test2.txt', encoding='utf-8') as fp: #Подсчёт количества строк
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

arr = file1.read().split(" ")   #текст в массив слов     скорее всего бесполезен для нас
print(arr)


#--------------------------

file2 = open('../test3.txt', encoding='utf-8')
# print(file.read()) # вывести весь текст

with open('../test3.txt', encoding='utf-8') as fp: #Подсчёт количества строк
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

arr = file2.read().split(".")   #текст в массив строк
print(arr)