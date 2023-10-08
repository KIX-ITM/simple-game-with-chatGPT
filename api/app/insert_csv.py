import csv

from app.model.setting import session
from app.model.word import WordGenre


def insert_csv():

    csv_file = './model/csv/word_genres.csv'

    data_list = []

    with open(csv_file, encoding="utf_8") as f:
        reader = csv.reader(f)
        data_list = [row for row in reader]

    session.bulk_save_objects(
        [WordGenre(id=d[0],
                   genre=d[1])
         for d in data_list], return_defaults=True)

    session.commit()

    users = session.query(WordGenre).all()

    for user in users:
        print(user.id, user.genre)

    session.close()


if __name__ == '__main__':
    insert_csv()