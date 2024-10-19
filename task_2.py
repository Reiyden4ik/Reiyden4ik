# TODO Найдите количество книг, которое можно разместить на дискете
info_volume = 1.44
count_of_pages = 100
count_of_string_in_one_page = 50
count_symbols_in_one_string = 25
one_symbol_info = 4
count_of_bytes_in_one_book = one_symbol_info*count_symbols_in_one_string*count_of_string_in_one_page*count_of_pages
count_of_kb_in_one_book = count_of_bytes_in_one_book/1024
count_of_mb_in_one_book = count_of_kb_in_one_book/1024
count_of_similar_books = round((info_volume/count_of_mb_in_one_book))
print("Количество книг, помещающихся на дискету:", count_of_similar_books)