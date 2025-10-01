from calendar import monthrange
# 제일 중요한 거 : 마지막 날, 1일이 무슨 요일인지
# 월요일이 '0'임

year = int(input('연도?'))
month = int(input('월?'))

week, last_day = monthrange(year, month)
print(week, last_day)

# print(week, last_day)
print(f'{year}년 {month}월')
print()
print('Mo Tu We Th Fr Sa Su')

c = 0
for i in range(week):
    print('  ', end=' ')
    c += 1

for d in range(1, last_day+1):
    print(f'{d:2}', end=' ')
    c += 1
    if c%7 == 0:
        print()