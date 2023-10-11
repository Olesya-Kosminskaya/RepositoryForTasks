# TODO Найдите количество книг, которое можно разместить на дискете
volume_inf = 1.44 * 1024 * 1024
volume_book = 100 * 50 * 25 * 4
count_of_books = int(volume_inf / volume_book)
print("Количество книг, помещающихся на дискету:", count_of_books)
