# qa_python

# ТЕСТЫ ДЛЯ КЛАССА BooksCollector - класс управления коллекцией книг
## Основные функции
- Добавление и удаление книг
- Установка и получение жанров книг
- Работа с избранными книгами
- Фильтрация по жанрам и возрастным ограничениям
- Получение книг, подходящих для детей

# Метод __init__ - инициализация коллекции книг
test_books_genre_is_dict - проверяет, что books_genre является словарем
test_books_genre_is_empty - проверяет, что books_genre инициализируется пустым
test_init_favorites_is_list - проверяет, что favorites является списком
test_init_favorites_is_empty - проверяет, что favorites инициализируется пустым
test_init_genre_contains_genres - проверяет, что genre содержит жанры
test_init_genre_is_list - проверяет, что genre является списком
test_init_genre_age_rating_contains_genres - проверяет, что genre_age_rating содержит жанры с возрастным рейтингом
test_init_genre_age_rating_is_list - проверяет, что genre_age_rating является списком

# Метод add_new_book - добавляет новую книгу в коллекцию
test_add_new_book_basic_functionality - проверяет базовую функциональность добавления новой книги
test_add_new_book_add_two_books - проверяет добавление двух книг
test_add_new_book_permissible_length - проверяет добавление книг с допустимой длиной названия (1-40 символов)
test_add_new_book_invalid_length - проверяет, что книги с некорректной длиной названия не добавляются
test_add_new_book_duplicate - проверяет, что нельзя добавить книгу с одинаковым названием дважды
test_add_new_book_sets_empty_genre - проверяет, что при добавлении книги устанавливается пустой жанр

# Метод set_book_genre - устанавливает жанр для книги
test_set_book_genre_valid_book_and_genre - проверяет установку жанра для существующей книги с допустимым жанром
test_set_book_genre_nonexistent_book - проверяет попытку установить жанр для несуществующей книги
test_set_book_genre_invalid_genre - проверяет попытку установить недопустимый жанр для существующей книги
test_set_book_genre_nonexistent_book_invalid_genre - проверяет попытку установить недопустимый жанр для несуществующей книги
test_set_book_genre_all_available_genres - проверяет установку всех доступных жанров из списка genre
test_set_book_genre_empty_genre - проверяет попытку установить пустой жанр
test_set_book_genre_change_existing_genre - проверяет изменение жанра книги

# Метод get_book_genre - получает жанр книги по её имени
test_get_book_genre_existing_book_with_genre - проверяет получение жанра для существующей книги с установленным жанром
test_get_book_genre_existing_book_without_genre - проверяет получение жанра для существующей книги без жанра
test_get_book_genre_after_genre_change - проверяет получение жанра после изменения жанра книги
test_get_book_genre_case_sensitivity - проверяет чувствительность к регистру в названиях книг
test_get_book_genre_nonexistent_book - проверяет получение жанра для несуществующей книги
test_get_book_genre_empty_string - проверяет получение жанра для пустого названия книги
test_get_book_genre_none_name - проверяет получение жанра для None в качестве названия книги

# Метод get_books_with_specific_genre - получает список книг с определённым жанром
test_get_books_with_specific_genre_existing_genre_with_books - проверяет получение книг для существующего жанра с книгами
test_get_books_with_specific_genre_existing_genre_no_books - проверяет получение книг для существующего жанра без книг
test_get_books_with_specific_genre_nonexistent_genre - проверяет получение книг для несуществующего жанра
test_get_books_with_specific_genre_empty_books_genre - проверяет получение книг при пустом словаре books_genre
test_get_books_with_specific_genre_case_sensitivity - проверяет чувствительность к регистру в названиях жанров
test_get_books_with_specific_genre_multiple_genres - проверяет получение книг при наличии книг разных жанров
test_get_books_with_specific_genre_books_without_genre - проверяет, что книги без жанра не включаются в результат
test_get_books_with_specific_genre_all_available_genres - проверяет получение книг для всех доступных жанров

# Метод get_books_genre - получает словарь books_genre
test_get_books_genre_empty - проверяет получение пустого словаря при инициализации
test_get_books_genre_after_adding_books - проверяет получение словаря после добавления книг
test_get_books_genre_with_books_without_genre - проверяет получение словаря с книгами без жанра

# Метод get_books_for_children - возвращает книги, подходящие для детей
test_get_books_for_children_only_child_friendly_books - проверяет возврат книг, подходящих для детей
test_get_books_for_children_with_age_rating_books - проверяет, что книги с возрастным рейтингом не возвращаются
test_get_books_for_children_books_without_genre - проверяет, что книги без жанра не возвращаются
test_get_books_for_children_books_with_invalid_genre - проверяет, что книги с недопустимым жанром не возвращаются
test_get_books_for_children_all_child_friendly_genres - проверяет все детские жанры
test_get_books_for_children_all_adult_genres - проверяет все взрослые жанры
test_get_books_for_children_no_books - проверяет возврат пустого списка при отсутствии книг

# Метод add_book_in_favorites - добавляет книгу в избранное
test_add_book_in_favorites_existing_book - проверяет добавление существующей книги в избранное
test_add_book_in_favorites_duplicate_book - проверяет, что нельзя добавить книгу в избранное дважды
test_add_book_in_favorites_multiple_books - проверяет добавление нескольких книг в избранное
test_add_book_in_favorites_book_without_genre - проверяет добавление книги без жанра в избранное
test_add_book_in_favorites_nonexistent_book - проверяет, что несуществующая книга не добавляется в избранное
test_add_book_in_favorites_empty_name - проверяет обработку пустого названия книги
test_add_book_in_favorites_case_sensitivity - проверяет чувствительность к регистру при добавлении

# Метод delete_book_from_favorites - удаляет книгу из избранного
test_delete_book_from_favorites_existing_book - проверяет удаление существующей книги из избранного
test_delete_book_from_favorites_multiple_books - проверяет удаление одной книги из списка с несколькими книгами
test_delete_book_from_favorites_twice - проверяет попытку удаления книги дважды
test_delete_book_from_favorites_nonexistent_book - проверяет попытку удаления несуществующей книги
test_delete_book_from_favorites_empty_favorites - проверяет попытку удаления из пустого списка избранного
test_delete_book_from_favorites_case_sensitivity - проверяет чувствительность к регистру при удалении

# Метод get_list_of_favorites_books - получает список избранных книг
test_get_list_of_favorites_books_with_books - проверяет получение списка избранных книг
test_get_list_of_favorites_books_after_removal - проверяет получение списка после удаления книги из избранного
test_get_list_of_favorites_books_empty - проверяет получение пустого списка избранных книг