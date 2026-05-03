# 세 정수의 최대값 구하기

# max3 : a, b, c중 최대값 찾아서 반환하는 함수
def max3(a,b,c):
    # a가 maximum이라고 가정
    maximum = a
    if b > maximum :
        maximum = b
    if c > maximum:
        c > maximum
        maximum = c

    # 최대값 반환
    return maximum

# return : 최대값을 호출한 곳으로 반환 → 변수 저장 및 재사용 가능
#          (함수 밖으로 값 전달 O)

# print  : 값 출력만 수행 → 반환값은 None (재사용 불가)
#          (함수 안에서 출력만, 값 전달 X)