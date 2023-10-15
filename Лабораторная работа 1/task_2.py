# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_diskette = 1.44
volume_inf = volume_of_diskette * 1024 * 1024
count_of_pages = 100
count_of_lines = 50
count_of_characters = 25
volume_of_character = 4
volume_book = count_of_pages * count_of_lines * count_of_characters * volume_of_character
count_of_books = int(volume_inf / volume_book)
print("Количество книг, помещающихся на дискету:", count_of_books)
