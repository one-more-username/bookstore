from essential_generators import DocumentGenerator
from datetime import date
from random import randint
from books.models import Book
#
import json

# from randimage import get_random_image
# from matplotlib import image
#
# img_size = (128, 128)
#
# for _ in range(100):
#     image.imsave("../../../Desktop/randimage_" + str(_) + ".png", get_random_image(img_size))
# ../../../Desktop/randimage.png


def fill_datefield(source_date):
    if len(source_date) < 10:
        return date(randint(1980, 2020), randint(1, 12), randint(1, 28))
    return source_date


def fill_database():
    # Opening JSON file
    file = open('backend/books.json')

    # returns JSON object as
    # a dictionary
    data = json.load(file)

    books = [
        Book(
            title=data[i]['title'],  # 'title'
            description=data[i]['description'],  # 'description'
            image='book_images/randimages/randimage_' + str(i) + '.png',
            # release_date=data[i]['original_publication_date'],  # 'original_publication_date'
            release_date=fill_datefield(data[i]['original_publication_date']),  # 'original_publication_date'
            price=randint(200, 800),
            author=data[i]['author_name'],  # 'author_name'
        )
        for i in range(110)
    ]
    Book.objects.bulk_create(books)
    file.close()


if __name__ == "__main__":
    fill_database()
