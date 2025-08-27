from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3307/test_db2"


engine = create_engine(DATABASE_CONN, poolclass=QueuePool, 
                       pool_size=10, max_overflow=0)

try:
    conn = engine.connect()
    query = "select * from blog"
    stmt = text(query)

    result = conn.execute(stmt)
    rows = result.fetchall()

    for i in range(len(rows)):
        print(rows[i])
    
    result.close()
except SQLAlchemyError as e:
    print(e)
finally:
    conn.close()