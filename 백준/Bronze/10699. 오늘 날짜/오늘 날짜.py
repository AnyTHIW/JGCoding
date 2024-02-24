from datetime import datetime, timedelta
import time

# datetime.today() # 현재날짜 가져오기
# datetime.today().year # 현재 연도 가져오기
# datetime.today().month # 현재 월
# datetime.today().day # 현재 일
# datetime.today().hour # 현재 시간
today=datetime.now() + timedelta(hours=9)
print(today.strftime("%Y-%m-%d"))
