# 세 정수의 중앙값 구하기

def median3(a, b, c):
    # 중앙값: 세 값 중 "다른 두 값 사이에 있는 값"

    if a >= b:
        # 케이스1: a ≥ b
        if b >= c:
            return b          # a ≥ b ≥ c → b가 중앙값
        elif a <= c:
            return a          # c ≥ a ≥ b → a가 중앙값
        else:
            return c          # a > c > b → c가 중앙값
    else:
        # 케이스2: a < b
        if a >= c:
            return a          # b > a ≥ c → a가 중앙값
        elif b <= c:
            return b          # c ≥ b > a → b가 중앙값
        else:
            return c          # b > c > a → c가 중앙값


# 입력 및 결과 출력
a, b, c = map(int, input().split())
print(f'중앙값은 {median3(a, b, c)}입니다.')