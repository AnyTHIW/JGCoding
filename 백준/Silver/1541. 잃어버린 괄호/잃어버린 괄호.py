# 입력 받기
_N = input()

# "-"를 기준으로 수식을 나눕니다.
parts = _N.split("-")

# 첫 번째 부분 식을 계산하여 초기 결과를 설정합니다.
result = sum(map(int, parts[0].split("+")))

# 나머지 부분 식을 처리하면서 결과를 빼줍니다.
for part in parts[1:]:
    result -= sum(map(int, part.split("+")))

print(result)