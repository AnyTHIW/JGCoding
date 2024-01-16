def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 특정 수가 소수인지 판별하는 예시
input()
numbers = [ int(x) for x in input().split(' ')]   # 소수 여부를 확인하고 싶은 수

counter = 0

for item in numbers:
    if is_prime(item):
        counter +=1
    else:
        continue

print(counter)