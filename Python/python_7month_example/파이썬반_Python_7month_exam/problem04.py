from re import L


def turn(temperatures):
    date_temperatures = {
        "maximum": [],
        "minimum": []
    }

    for idx in range(len(temperatures)):
        date_temperatures["maximum"].append(temperatures[idx][0])
        date_temperatures["minimum"].append(temperatures[idx][1])
        
    return date_temperatures


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
