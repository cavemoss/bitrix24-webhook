import psycopg2
import os


connection = psycopg2.connect(
    host='localhost',
    dbname='webhookdb',
    user='postgres',
    password='pass',
    port=5432
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS names_woman (honorific VARCHAR(255), name VARCHAR(255) UNIQUE);
CREATE TABLE IF NOT EXISTS names_man (honorific VARCHAR(255), name VARCHAR(255) UNIQUE);
""")

connection.commit()


def insert_names(honorific: str, names: list):

    if(honorific == 'HNR_RU_1'):
        for name in names:
            try: 
                cursor.execute(F"""
                            INSERT INTO names_man (honorific, name)
                            VALUES ('HNR_RU_1', '{name}')
                            """)
                connection.commit()
            except: continue

    if(honorific == 'HNR_RU_2'):
        for name in names:
            try: 
                cursor.execute(F"""
                            INSERT INTO names_woman (honorific, name)
                            VALUES ('HNR_RU_2', '{name}')
                            """)
                connection.commit()
            except: continue


if __name__ == '__main__':

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

    with open(f'{ROOT_DIR}/female_names_rus.txt', 'r', encoding="utf-8") as file:
        names_woman = file.read().split('\n')

    with open(f'{ROOT_DIR}/male_names_rus.txt', 'r', encoding="utf-8") as file:
        names_man = file.read().split('\n')

    insert_names('HNR_RU_1', names_woman)
