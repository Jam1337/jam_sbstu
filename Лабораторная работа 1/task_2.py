# Параметры книги
number_of_pages = 100
lines_per_page = 50
characters_per_line = 25
char_code_size = 4  # в байтах

# Объем дискеты
diskette_volume = 1.44 * 1024 * 1024  # переводим в байты

# Рассчитаем объем одной книги
book_volume = number_of_pages * lines_per_page * characters_per_line * char_code_size

# Рассчитаем количество книг, помещающихся на дискету
books_count = diskette_volume // book_volume

# Выведем результат
print("Количество книг, помещающихся на дискету:", books_count)

