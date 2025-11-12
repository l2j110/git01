from datetime import datetime

def log(name,cont):
    현재시간 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    기록내용 = f'이름: {name} / {cont} / {현재시간}\n'
    with open('log.txt', 'a',encoding='utf-8') as f:
        f.write(기록내용)
    print('기록이 저장 되었습니다.')
log('dltpgur','cnftjd')