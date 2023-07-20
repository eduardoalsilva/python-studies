# n = int(input())
phone_book = {}

# for i in range(n):
#     l = input().split()
#     if len(l) > 1:
#         phone_book[l[0]] = l[1]

l = []
# item = input()

file = list(open('phone-book-input.txt'))
for line in range(len(file)):
    if line == 0:
        n = line
    elif i in range(n):
        l = file[line].split()
        if len(l) > 1:
            phone_book[l[0]] = l[1]

# while item != '':
#     l.append(item)
#     item = input()

# for i in range(len(l)):
#     if l[i] in phone_book.keys():
#         print(f'{l[i]}={phone_book[l[i]]}')
#     else:
#         print('Not found')
