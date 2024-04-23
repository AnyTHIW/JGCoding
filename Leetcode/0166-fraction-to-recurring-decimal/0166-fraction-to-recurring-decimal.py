class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # 결과를 문자열로 저장할 변수
        res = []

        # 입력받은 분수의 부호 처리
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        # 분자와 분모를 절대값으로 변경
        numerator, denominator = abs(numerator), abs(denominator)

        # 정수 부분과 나머지 부분 계산
        quotient, remainder = divmod(numerator, denominator)
        res.append(str(quotient))

        # 나머지가 0이면 순환소수가 아님
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        # 나머지가 처음 나타나는 위치를 기록하는 사전
        remainder_map = {}
        # 순환소수 시작 전까지의 소수 부분을 계산
        while remainder != 0:
            if remainder in remainder_map:
                # 순환 시작 지점을 찾은 경우
                res.insert(remainder_map[remainder], '(')
                res.append(')')
                break
            # 나머지를 기록
            remainder_map[remainder] = len(res)
            quotient, remainder = divmod(remainder * 10, denominator)
            res.append(str(quotient))

        return ''.join(res)
        