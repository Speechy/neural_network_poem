file = open('../test.txt', encoding='utf-8')
# print(file.read()) # вывести весь текст

with open('../test.txt', encoding='utf-8') as fp: #Подсчёт количества строк
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
arr =file.read().split()    #текст в массив слов
print(arr)