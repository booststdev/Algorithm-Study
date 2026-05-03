# 세 정수를 입력받아 최댓값 구하기

a, b, c = map(int, input().split())

maximum = a

if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

print(f'최댓값은 {maximum} 입니다.')

