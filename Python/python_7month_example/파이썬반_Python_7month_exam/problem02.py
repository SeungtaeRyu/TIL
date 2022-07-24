def over(scores):
    over_60_count = 0
    for score in scores:
        if score >= 60:
            over_60_count += 1
    return over_60_count


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
