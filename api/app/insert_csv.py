import csv

from model.settings import session
from model.word import Word, WordGenre


def insert_csv():

    # # csv_file = './model/csv/words.csv'
    # csv_file = './model/csv/word_genres.csv'
    #
    # data_list = []
    #
    # with open(csv_file, encoding="utf_8") as f:
    #     reader = csv.reader(f)
    #     data_list = [row for row in reader]
    #
    # # session.bulk_save_objects(
    # #     [Word(japanese=d[0],
    # #            english=d[1],
    # #            genre_id=d[2]
    # #           )
    # #      for d in data_list], return_defaults=True)
    #
    # session.bulk_save_objects(
    #     [WordGenre(id=d[0],
    #                genre=d[1])
    #      for d in data_list], return_defaults=True)
    #
    # session.commit()

    words = session.query(Word).all()

    for word in words:
        print(word.id, word.japanese, word.english, word.genre_id)
        # print(word.id, word.genre)

    session.close()


if __name__ == '__main__':
    insert_csv()