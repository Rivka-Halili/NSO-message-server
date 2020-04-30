import sqlite3

def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    create_message_table ='{}{}{}{}{}{}'.format(
                          'CREATE TABLE IF NOT EXISTS',
                          ' message(message_id INTEGER PRIMARY KEY,',
                          ' application_id INTEGER NOT NULL,',
                          ' session_id INTEGER NOT NULL,',
                          ' participants text NOT NULL,',
                          ' content text NOT NULL);'
                          )
    cursor.execute(create_message_table)

    cursor.execute('INSERT OR REPLACE INTO message VALUES(1, 100,200,"David ,Avi","how are you?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(2, 100,200,"David ,Asaf","business?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(3, 102,220,"David ,Asaf","What to do?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(4, 110,220,"David ,Avi","how are you?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(5, 110,220,"David ,Avi","When are you comming?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(6, 110,220,"Asaf ,Avi","how are you?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(7, 110,200,"Asaf ,Avi","some problems?")')
    cursor.execute('INSERT OR REPLACE INTO message VALUES(8, 110,200,"Asaf ,Avi","how are you?")')


    connection.commit()
    connection.close()

    print('Database successfully created and populated with data!')
