f = open('my_file.txt', 'w')
print(f)
f.write(input('Сделайте запись в файл'))
f.close()

f = open('file.txt', 'r')
i = 0
with open(r"file.txt", "r") as file:
    for line in file:
        i = i + 1
        line = line.split()
        l = len(line)
        if l < 5:
            pass
        else:
            print('В строке', i,l, 'слов')
        if l < 5:
            print('В строке', i,l, 'слова')

f.close()

f = open('task3.txt', 'r')
with open('task3.txt', 'r') as file:
    salary = []
    p = []
    list = f.read().strip().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            p.append(i[0])
        else:
            pass
        salary.append(i[1])
    for l in salary:
        print(l)
        print(salary)
        print(len(salary))
        print(i[1])
        print(list)
        print(sum(map(int, salary)))
    print(f'Оклад меньше 20.000 имеет {p}', 'средняя зарплата', (sum(map(int, salary)) / len(salary)))
f.close()

f = open('task4.txt', 'r')
c = []
with open(r"task4.txt", "r") as file:
    for line in file:
        line = line.replace('One', 'Один')
        line = line.replace('Two', 'Два')
        line = line.replace('Three', 'Три')
        line = line.replace('Four', 'Четыре')
        c.append(line)
        print(line)
with open('task4_1.txt', 'a') as file:
    for line in c:
        file.writelines(line)
f.close()

f = open('task5.txt', 'w')
lin = []
with open('task5.txt') as file:
    line: str = "6 3 1 9 4 2"
    print(line.split())
    print(lin.append(line))
    print(sum(map(int, line)))
f.write(line)
f.close
