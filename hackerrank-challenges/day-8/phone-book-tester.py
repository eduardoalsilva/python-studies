# file = open(phone-book-input.txt)
#
# lines_number = 0
# for line in file:
#     lines_number += 1
#     l.append().split()
#
# file = open()
#
# print(f'Number of lines: {lines_number}')

names = []
while True:
    name = input()
    if name:
        names.append(name)
    else:
        break

print(names)
