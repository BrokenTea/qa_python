# qa_python

# BooksCollector - система управления коллекцией книг
## Описание:
    BooksCollector — это класс для управления коллекцией книг, позволяющий добавлять книги, устанавливать жанры, управлять избранными книгами и фильтровать книги по различным критериям.

## Функциональность:
    - Добавление новых книг в коллекцию
    - Установка жанров книг
    - Управление списком избранных книг
    - Фильтрация книг по жанрам и возрастным ограничениям
    - Получение книг, подходящих для детей

## Требования:
    - Python 3.6+
    - pytest (для запуска тестов)

# ТЕСТЫ ДЛЯ КЛАССА BooksCollector - класс управления коллекцией книг
## Метод __init__ - инициализация коллекции книг
    test_books_genre_is_empty - Проверяет, что словарь books_genre инициализируется пустым
    test_init_favorites_is_empty - Проверяет, что список избранного инициализируется пустым
    test_init_genre_contains_genres - Проверяет наличие предопределенных жанров
    test_init_genre_age_rating_contains_genres - Проверяет наличие жанров с возрастным рейтингом

## Метод add_new_book - добавляет новую книгу в коллекцию
    test_add_new_book_basic_functionality - Проверяет базовое добавление книги
    test_add_new_book_add_two_books - Проверяет добавление двух книг
    test_add_new_book_permissible_length - Проверяет добавление книг с допустимой длиной названия (1-40 символов)
    test_add_new_book_invalid_length - Проверяет, что книги с некорректной длиной названия не добавляются
    test_add_new_book_duplicate - Проверяет невозможность добавления дубликатов
    test_add_new_book_sets_empty_genre - Проверяет установку пустого жанра по умолчанию

## Метод set_book_genre - устанавливает жанр для книги
    test_set_book_genre_valid_book_and_genre - Проверяет установку жанра для существующей книги
    test_set_book_genre_nonexistent_book - Проверяет обработку несуществующей книги
    test_set_book_genre_invalid_genre - Проверяет обработку недопустимого жанра
    test_set_book_genre_all_available_genres - Проверяет установку всех доступных жанров
    test_set_book_genre_empty_genre - Проверяет установку пустого жанра
    test_set_book_genre_change_existing_genre - Проверяет изменение существующего жанра

## Метод get_book_genre - получает жанр книги по её имени
    test_get_book_genre_existing_book_with_genre - Проверяет получение жанра для книги с установленным жанром
    test_get_book_genre_existing_book_without_genre - Проверяет получение жанра для книги без жанра
    test_get_book_genre_after_genre_change - Проверяет получение жанра после его изменения
    test_get_book_genre_case_sensitivity - Проверяет чувствительность к регистру
    test_get_book_genre_nonexistent_book - Проверяет обработку несуществующей книги
    test_get_book_genre_empty_string - Проверяет обработку пустой строки
    test_get_book_genre_none_name - Проверяет обработку None в качестве названия

## Метод get_books_with_specific_genre - получает список книг с определённым жанром
    test_get_books_with_specific_genre_existing_genre_with_books - Проверяет получение книг по существующему жанру
    test_get_books_with_specific_genre_existing_genre_no_books - Проверяет обработку жанра без книг
    test_get_books_with_specific_genre_nonexistent_genre - Проверяет обработку несуществующего жанра
    test_get_books_with_specific_genre_empty_books_genre - Проверяет обработку пустой коллекции
    test_get_books_with_specific_genre_case_sensitivity - Проверяет чувствительность к регистру жанров
    test_get_books_with_specific_genre_books_without_genre - Проверяет, что книги без жанра не включаются
    test_get_books_with_specific_genre_all_available_genres - Проверяет все доступные жанры

## Метод get_books_genre - получает словарь books_genre
    test_get_books_genre_empty - Проверяет получение пустой коллекции
    test_get_books_genre_returns_correct_dict_with_various_books - Проверяет получение корректного словаря

## Метод get_books_for_children - возвращает книги, подходящие для детей
    test_get_books_for_children_all_child_friendly_genres - Проверяет все детские жанры
    test_get_books_for_children_returns_only_valid_children_books - Проверяет возврат только детских книг
    test_get_books_for_children_all_adult_genres - Проверяет обработку взрослых жанров
    test_get_books_for_children_no_books - Проверяет обработку отсутствия книг

## Метод add_book_in_favorites - добавляет книгу в избранное
    test_add_book_in_favorites_existing_book - Проверяет добавление существующей книги
    test_add_book_in_favorites_duplicate_book - Проверяет невозможность дублирования
    test_add_book_in_favorites_various_books - Проверяет добавление различных книг
    test_add_book_in_favorites_nonexistent_book - Проверяет обработку несуществующей книги
    test_add_book_in_favorites_empty_name - Проверяет обработку пустого названия
    test_add_book_in_favorites_case_sensitivity - Проверяет чувствительность к регистру

## Метод delete_book_from_favorites - удаляет книгу из избранного
    test_delete_book_from_favorites_existing_book - Проверяет удаление существующей книги
    test_delete_book_from_favorites_multiple_books - Проверяет удаление из нескольких книг
    test_delete_book_from_favorites_twice - Проверяет повторное удаление
    test_delete_book_from_favorites_nonexistent_book - Проверяет удаление несуществующей книги
    test_delete_book_from_favorites_empty_favorites - Проверяет удаление из пустого списка
    test_delete_book_from_favorites_case_sensitivity - Проверяет чувствительность к регистру

## Метод get_list_of_favorites_books - получает список избранных книг
    test_get_list_of_favorites_books_with_books - Проверяет получение списка избранного
    test_get_list_of_favorites_books_after_removal - Проверяет получение после удаления
    test_get_list_of_favorites_books_empty - Проверяет получение пустого списка