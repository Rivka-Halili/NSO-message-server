import sqlite3


class MessageModel:

    def __init__(self, message_id,application_id, session_id,participants,content):
        self.message_id = message_id                                        
        self.application_id = application_id                             
        self.session_id = session_id                             
        self.participants = participants                             
        self.content = content      
        
    @classmethod
    def find_all(cls, db_path='./db/datamessage.db'):
        messages = list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM message;'
        result = cursor.execute(query)
        rows = result.fetchall()
        if rows:
            for row in rows:
                messages.append(MessageModel(row[0], row[1], row[2],row[3],row[4]))
            return messages
        connection.close()

                                                             
    @classmethod
    def find_by_app_id(cls, app_id, db_path='./db/datamessage.db'):
        messages=list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM message WHERE application_id=?;'
        result = cursor.execute(query, (app_id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                messages.append(MessageModel(row[0], row[1], row[2],row[3],row[4]))
            return messages

    @classmethod
    def find_by_session_id(cls, session_id, db_path='./db/datamessage.db'):
        messages=list()
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM message WHERE session_id=?'
        result = cursor.execute(query, (session_id,))
        rows = result.fetchall()
        if rows:
           for row in rows:
               messages.append( MessageModel(row[0], row[1], row[2],row[3],row[4]))
           return messages
        connection.close()

    @classmethod
    def find_by_message_id(cls, message_id, db_path='./db/datamessage.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'SELECT * FROM message WHERE message_id=?'
        result = cursor.execute(query, (message_id,))
        rows = result.fetchall()
        if rows:
            for row in rows:
                message = MessageModel(row[0], row[1], row[2],row[3],row[4])
                connection.close()
            return message


    @classmethod
    def insert_into_table(cls, message_id,application_id,session_id,participants, content, db_path='./db/datamessage.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        query = 'INSERT INTO message VALUES( ?, ?,?,?,?)'
        cursor.execute(query, (message_id,application_id,session_id,participants, content))
        connection.commit()
        connection.close()
  

    @classmethod
    def delete_by_message_id(self, message_id, db_path='./db/datamessage.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        message_to_delete = 'DELETE FROM message WHERE message_id=?;'
        delete_message = cursor.execute(message_to_delete, (message_id,))
        connection.commit()
        connection.close()


    @classmethod
    def delete_by_app_id(self, app_id, db_path='./db/datamessage.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        message_to_delete = 'DELETE FROM message WHERE application_id=?;'
        delete_message = cursor.execute(message_to_delete, (app_id,))
        connection.commit()
        connection.close()


    @classmethod
    def delete_by_session_id(self, session_id, db_path='./db/datamessage.db'):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        message_to_delete = 'DELETE FROM message WHERE session_id=?;'
        delete_message = cursor.execute(message_to_delete, (session_id,))

        connection.commit()
        connection.close()


    def json(self):
        return {'message_id': self.message_id,
        'application_id': self.application_id,
        'session_id': self.session_id,
        'participants': self.participants,
        'content': self.content}
