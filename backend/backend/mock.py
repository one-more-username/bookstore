from essential_generators import DocumentGenerator
from datetime import date
from random import randint
from books.models import Book


# from randimage import get_random_image
# from matplotlib import image
#
# img_size = (128, 128)
#
# for _ in range(100):
#     image.imsave("../../../Desktop/randimage_" + str(_) + ".png", get_random_image(img_size))
# ../../../Desktop/randimage.png


def fill_database():
    titles = []
    authors = []
    dg = DocumentGenerator()
    books = [
        Book(
            title=dg.word(),  # TODO change it to normal title
            description=dg.paragraph(),
            image='book_images/randimages/randimage_' + str(i) + '.png',
            #   book_images/Qwer Asdf/Screenshot_2023-04-27_at_10.25.03.png
            release_date=date(randint(1980, 2020), randint(1, 12), randint(1, 28)),
            price=randint(200, 800),
            author=dg.name(),
            # reviews_quantity = models.IntegerField(default=0)
        )
        for i in range(10)
    ]
    Book.objects.bulk_create(books)
    # return 0


if __name__ == "__main__":
    fill_database()
