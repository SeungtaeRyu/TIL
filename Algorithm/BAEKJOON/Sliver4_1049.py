broken, brand = map(int, input().split())

set_count = broken // 6
single_count = broken % 6

set_price = []
single_price = []
for i in range(brand):
    x, y = map(int, input().split())
    set_price.append(x)
    single_price.append(y)

set_price.sort()
single_price.sort()

if set_price[0] >= single_price[0] * 6:
    print(single_price[0] * broken)
else :
    if single_count * single_price[0] <= set_price[0]:
        print(single_count * single_price[0] + set_count * set_price[0])
    else:
        print(set_price[0] * (set_count + 1))
