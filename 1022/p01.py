import sqlite3

# 1. connection 생성
con = sqlite3.connect('sj2.db')

# 2. 커서 생성
cur = con.cursor()

# 3. 쿼리 실행
con.execute('''
create table if not exists member(
    id integer primary key autoincrement,
    name text not null, 
    phone text, 
    address text, 
    course text, 
    created_at timestamp default current_timestamp
    )
''')

# 4. commit()
con.commit()

# 5.
con.close()
