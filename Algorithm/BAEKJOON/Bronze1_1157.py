word = input()
word = word.upper()

count_list = []
for i in range(65, 91):
    count_list.append((word.count(chr(i)), i))

count_list.sort(reverse=True)

if count_list[0][0] == count_list[1][0]:
    print("?")
else:
    print(chr(count_list[0][1]))
