from main import BooksCollector
import pytest

class TestBooksCollector:

    # ТЕСТЫ ДЛЯ МЕТОДА __init__ КЛАССА BooksCollector
    # Тест: books_genre является словарем
    def test_books_genre_is_dict(self, collector):
        assert isinstance(collector.books_genre, dict)
    
    # Тест: books_genre инициализируется пустым
    def test_books_genre_is_empty(self, collector):
        assert collector.books_genre == {}
    
    # Тест: favorites является списком
    def test_init_favorites_is_list(self, collector):
        assert isinstance(collector.favorites, list)

    # Тест: favorites инициализируется пустым
    def test_init_favorites_is_empty(self, collector):
        assert collector.favorites == []
    
    
    # Тест: genre содержит жанры"
    def test_init_genre_contains_genres(self, collector):
        assert len(collector.genre) > 0
    
    # Тест: genre является списком"
    def test_init_genre_is_list(self, collector):
        assert isinstance(collector.genre, list)
    
    # Тест: genre_age_rating содержит жанры с возрастным рейтингом"""
    def test_init_genre_age_rating_contains_genres(self, collector):
        assert len(collector.genre_age_rating) > 0
    
    # Тест: genre_age_rating является списком 
    def test_init_genre_age_rating_is_list(self, collector):
        assert isinstance(collector.genre_age_rating, list)
    
    # Тесты для метода add_new_book
    # Тесты: add_new_book на добавление новой книги
    def test_add_new_book_basic_functionality(self, collector):
        collector.add_new_book("Новая книга")
        assert "Новая книга" in collector.books_genre
    
    # Тест: add_new_book добавляем две книги
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    # Тест: add_new_book на граничные значения длины названия: от 1 до 40 символов
    @pytest.mark.parametrize('name', ['A','A' * 2, 'AAAAAAAA','A' * 39, 'A' * 40])
    def test_add_new_book_permissible_length(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    # Тест: add_new_book с некорректной длиной названия (0 или >40 символов) не добавляются в books_genre
    @pytest.mark.parametrize('name', ['', 'A' * 41, 'A' * 66])
    def test_add_new_book_invalid_length(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # Тест: add_new_book нельзя добавить книгу с одинаковым названием дважды
    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert len(collector.books_genre) == 1
    
    # Тест: add_new_book на пустой жанр
    def test_add_new_book_sets_empty_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.books_genre['Книга без жанра'] == ''

    # ТЕСТЫ ДЛЯ МЕТОДА set_book_genre - добавляем новую книгу
    # Тест: set_book_genre установка жанра для существующей книги с допустимым жанром
    def test_set_book_genre_valid_book_and_genre(self, collector):
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        assert collector.get_book_genre('Фантастическая книга') == 'Фантастика'

    # Тест: set_book_genre попытка установить жанр для несуществующей книги
    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.books_genre.get('Несуществующая книга') is None

    # Тест: set_book_genre попытка установить недопустимый жанр для существующей книги
    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Книга с недопустимым жанром')
        collector.set_book_genre('Книга с недопустимым жанром', 'Несуществующий жанр')
        assert collector.books_genre.get('Книга с недопустимым жанром') == ''

    # Тест: set_book_genre попытка установить жанр для книги, которой нет в коллекции, с недопустимым жанром
    def test_set_book_genre_nonexistent_book_invalid_genre(self, collector):
        initial_books_genre = dict(collector.books_genre)
        collector.set_book_genre('Несуществующая книга', 'Несуществующий жанр')
        assert collector.books_genre == initial_books_genre  # Словарь не изменился

    # Тест: set_book_genre установка всех доступных жанров из списка genre
    @pytest.mark.parametrize('name_genre', BooksCollector().genre)
    def test_set_book_genre_all_available_genres(self, collector, name_genre):
        name_book = f'Книга в жанре {name_genre}'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, name_genre)
        assert collector.books_genre.get(name_book) == name_genre

    # Тест: set_book_genre попытка установить пустой жанр
    def test_set_book_genre_empty_genre(self, collector):
        collector.add_new_book('Книга с пустым жанром')
        collector.set_book_genre('Книга с пустым жанром', '')
        assert collector.books_genre.get('Книга с пустым жанром') == ''

    # Тест: set_book_genre изменение жанра книги
    def test_set_book_genre_change_existing_genre(self, collector):
        collector.add_new_book('Книга с изменяемым жанром')
        collector.set_book_genre('Книга с изменяемым жанром', 'Фантастика')        
        collector.set_book_genre('Книга с изменяемым жанром', 'Комедии')
        assert collector.books_genre.get('Книга с изменяемым жанром') == 'Комедии'

    # ТЕСТЫ ДЛЯ МЕТОДА get_book_genre - получаем жанр книги по её имени
    # Тест: test_get_book_genre_existing_book_with_genre получение жанра для существующей книги с установленным жанром"
    def test_get_book_genre_existing_book_with_genre(self, collector):
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        assert collector.get_book_genre('Фантастическая книга') == 'Фантастика'
    
    # Тест: test_get_book_genre_existing_book_without_genre получение жанра для существующей книги без жанра (пустая строка)
    def test_get_book_genre_existing_book_without_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''
    
    # Тест: test_get_book_genre_after_genre_change получение жанра после изменения жанра книги
    def test_get_book_genre_after_genre_change(self, collector):
        collector.add_new_book('Книга с изменяемым жанром')
        collector.set_book_genre('Книга с изменяемым жанром', 'Фантастика') 
        collector.set_book_genre('Книга с изменяемым жанром', 'Комедии')
        assert collector.get_book_genre('Книга с изменяемым жанром') == 'Комедии'
    
    # Тест: test_get_book_genre_case_sensitivity чувствительность к регистру в названиях книг
    def test_get_book_genre_case_sensitivity(self, collector):
        collector.add_new_book('Книга с регистром')
        collector.set_book_genre('Книга с регистром', 'Фантастика')
        assert collector.get_book_genre('книга с регистром') is None  # другой регистр
    
    # Тест: test_get_book_genre_nonexistent_book получение жанра для несуществующей книги (должен вернуть None)
    def test_get_book_genre_nonexistent_book(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None

    # Тест: test_get_book_genre_empty_string получение жанра для пустого названия книги
    def test_get_book_genre_empty_string(self, collector):
        assert collector.get_book_genre('') is None
    
    # Тест: test_get_book_genre_none_name получение жанра для None в качестве названия книги
    def test_get_book_genre_none_name(self, collector):
        assert collector.get_book_genre(None) is None
        
    # ТЕСТЫ ДЛЯ МЕТОДА get_books_with_specific_genre - выводим список книг с определённым жанром
    # Тест: получение книг для существующего жанра, для которого есть книги
    def test_get_books_with_specific_genre_existing_genre_with_books(self, collector):
        # Добавляем книги разных жанров
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_new_book('Ужасы 1')
        
        # Устанавливаем жанры
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        collector.set_book_genre('Фантастика 2', 'Фантастика')
        collector.set_book_genre('Ужасы 1', 'Ужасы')
        
        # Получаем книги с жанром 'Фантастика'
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        # Проверяем результат
        assert set(fantasy_books) == {'Фантастика 1', 'Фантастика 2'}

    # Тест: получение книг для существующего жанра, для которого нет книг
    def test_get_books_with_specific_genre_existing_genre_no_books(self, collector):
        # Добавляем книгу, но не устанавливаем нужный жанр
        collector.add_new_book('Фантастика 1')
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        
        # Получаем книги с жанром 'Ужасы' (для которого нет книг)
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        
        assert len(horror_books) == 0
    
    # Тест: получение книг для несуществующего жанра
    def test_get_books_with_specific_genre_nonexistent_genre(self, collector):
        # Добавляем книгу
        collector.add_new_book('Фантастика 1')
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        
        # Получаем книги с несуществующим жанром
        nonexistent_genre_books = collector.get_books_with_specific_genre('Несуществующий жанр')

        assert len(nonexistent_genre_books) == 0
   
    # Тест: получение книг, когда словарь books_genre пуст
    def test_get_books_with_specific_genre_empty_books_genre(self, collector):
        books = collector.get_books_with_specific_genre('Фантастика')
        
        assert len(books) == 0
    
    # Тест: чувствительность к регистру в названиях жанров
    @pytest.mark.parametrize('wrong_case_genre', ['фантастика', 'ФАНТАСТИКА', 'ФаНтАсТиКа'])
    def test_get_books_with_specific_genre_case_sensitivity(self, collector, wrong_case_genre):
        # Добавляем книгу
        collector.add_new_book('Фантастика 1')
        collector.set_book_genre('Фантастика 1', 'Фантастика')
    
        books = collector.get_books_with_specific_genre(wrong_case_genre)
    
        assert books == []
    
    # Тест: получение книг, когда есть книги разных жанров
    def test_get_books_with_specific_genre_multiple_genres(self, collector):
        # Добавляем книги разных жанров
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_new_book('Ужасы 1')
        collector.add_new_book('Детективы 1')
        collector.add_new_book('Комедии 1')
        
        # Устанавливаем жанры
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        collector.set_book_genre('Фантастика 2', 'Фантастика')
        collector.set_book_genre('Ужасы 1', 'Ужасы')
        collector.set_book_genre('Детективы 1', 'Детективы')
        collector.set_book_genre('Комедии 1', 'Комедии')
        
        # Получаем книги с жанром 'Фантастика'
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        assert set(fantasy_books) == {'Фантастика 1', 'Фантастика 2'}

    # Тест: книги без жанра не включаются в результат
    def test_get_books_with_specific_genre_books_without_genre(self, collector):
        # Добавляем книги с жанром и без
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Книга без жанра')
        
        # Устанавливаем жанр только для одной книги
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        
        # Получаем книги с жанром 'Фантастика'
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        assert set(fantasy_books) == {'Фантастика 1'}
    
    # Тест: Параметризованный тест для всех доступных жанров
    @pytest.mark.parametrize('name_genre', BooksCollector().genre)
    def test_get_books_with_specific_genre_all_available_genres(self, collector, name_genre):
        # Добавляем книгу для каждого жанра
        book_name = f'Книга в жанре {name_genre}'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, name_genre)
        
        # Получаем книги с текущим жанром
        books = collector.get_books_with_specific_genre(name_genre)
        
        assert set(books) == {book_name}

    # ТЕСТЫ ДЛЯ МЕТОДА get_books_genre - получаем словарь books_genre
    # Тест: получение пустого словаря книг при инициализации
    def test_get_books_genre_empty(self, collector):
        assert len(collector.get_books_genre()) == 0
    
    # Тест: получение словаря книг после добавления нескольких книг
    def test_get_books_genre_after_adding_books(self, collector):
        # Добавляем книги
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_new_book('Ужасы 1')
        
        # Устанавливаем жанры
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        collector.set_book_genre('Фантастика 2', 'Фантастика')
        collector.set_book_genre('Ужасы 1', 'Ужасы')
        
        # Получаем словарь книг
        books_genre = collector.get_books_genre()
        
        # Проверяем результат
        expected_dict = {
            'Фантастика 1': 'Фантастика',
            'Фантастика 2': 'Фантастика',
            'Ужасы 1': 'Ужасы'
        }
        assert books_genre == expected_dict
    
    # Тест: получение словаря книг, включая книги без жанра
    def test_get_books_genre_with_books_without_genre(self, collector):
        # Добавляем книги с жанром и без
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Книга без жанра')
        
        # Устанавливаем жанр только для одной книги
        collector.set_book_genre('Фантастика 1', 'Фантастика')
                
        expected_dict = {
            'Фантастика 1': 'Фантастика',
            'Книга без жанра': ''
        }
        assert collector.get_books_genre() == expected_dict

    # ТЕСТЫ ДЛЯ МЕТОДА get_books_for_children - возвращаем книги, подходящие детям
    # Тест: возврат книг, подходящих для детей
    def test_get_books_for_children_only_child_friendly_books(self, collector):
        # Добавляем книги с детскими жанрами
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Мультфильм 1')
        collector.add_new_book('Комедия 1')
        
        # Устанавливаем детские жанры
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        collector.set_book_genre('Мультфильм 1', 'Мультфильмы')
        collector.set_book_genre('Комедия 1', 'Комедии')
        
        # Проверяем результат
        assert collector.get_books_for_children() == ['Фантастика 1', 'Мультфильм 1', 'Комедия 1']
 
    # Тест: книги с возрастным рейтингом не возвращаются
    def test_get_books_for_children_with_age_rating_books(self, collector):
        # Добавляем книги с детскими и взрослыми жанрами
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Ужасы 1')
        collector.add_new_book('Детектив 1')
        
        # Устанавливаем жанры
        collector.set_book_genre('Фантастика 1', 'Фантастика')
        collector.set_book_genre('Ужасы 1', 'Ужасы')
        collector.set_book_genre('Детектив 1', 'Детективы')
        
        assert collector.get_books_for_children() == ['Фантастика 1']

    # Тест: книги без жанра не возвращаются
    def test_get_books_for_children_books_without_genre(self, collector):
        # Добавляем книги с жанром и без
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Книга без жанра')
        
        # Устанавливаем жанр только для одной книги
        collector.set_book_genre('Фантастика 1', 'Фантастика')

        assert collector.get_books_for_children() == ['Фантастика 1']

    # Тест: книги с недопустимым жанром не возвращаются
    def test_get_books_for_children_books_with_invalid_genre(self, collector):
        # Добавляем книгу и устанавливаем недопустимый жанр
        collector.add_new_book('Книга с недопустимым жанром')
        collector.books_genre['Книга с недопустимым жанром'] = 'Несуществующий жанр'
        
        assert collector.get_books_for_children() == []

    # Тест: Параметризованный тест для всех детских жанров
    @pytest.mark.parametrize('child_friendly_genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_all_child_friendly_genres(self, collector, child_friendly_genre):
        # Добавляем книгу
        book_name = f'Книга в жанре {child_friendly_genre}'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, child_friendly_genre)
        
        assert collector.get_books_for_children() == [book_name]

    # Тест: тест для всех взрослых жанров
    @pytest.mark.parametrize('adult_genre', BooksCollector().genre_age_rating)
    def test_get_books_for_children_all_adult_genres(self, collector, adult_genre):
        # Добавляем книгу
        book_name = f'Книга в жанре {adult_genre}'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, adult_genre)
        
        # Получаем книги для детей
        books_for_children = collector.get_books_for_children()
        
        # Проверяем, что книга не вернулась
        assert books_for_children == []
    
    # Тест: возврат пустого списка, когда нет книг
    def test_get_books_for_children_no_books(self, collector):
        assert collector.get_books_for_children() == []

    # ТЕСТЫ ДЛЯ МЕТОДА add_book_in_favorites - добавляем книгу в Избранное
    # Тест: добавление существующей книги в избранное
    def test_add_book_in_favorites_existing_book(self, collector):
        collector.add_new_book('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 1')
        
        assert 'Фантастика 1' in collector.favorites
    
    # Тест: нельзя добавить книгу в избранное дважды
    def test_add_book_in_favorites_duplicate_book(self, collector):
        collector.add_new_book('Фантастика 1')
        
        # Первое добавление
        collector.add_book_in_favorites('Фантастика 1')
        
        # Второе добавление
        collector.add_book_in_favorites('Фантастика 1')
        
        assert len(collector.favorites) == 1  
    
    # Тест: добавление нескольких разных книг в избранное
    def test_add_book_in_favorites_multiple_books(self, collector):
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_new_book('Ужасы 1')
        
        collector.add_book_in_favorites('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 2')
        collector.add_book_in_favorites('Ужасы 1')
        
        assert collector.favorites == ['Фантастика 1', 'Фантастика 2', 'Ужасы 1']
    
    # Тест: добавление книги без жанра в избранное
    def test_add_book_in_favorites_book_without_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        collector.add_book_in_favorites('Книга без жанра')
        
        assert 'Книга без жанра' in collector.favorites
    
    # Тест: несуществующая книга не добавляется в избранное
    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites

    # Тест: обработку пустого названия книги
    def test_add_book_in_favorites_empty_name(self, collector): 
        collector.add_book_in_favorites('')
        assert '' not in collector.favorites

    # Тест: чувствительность к регистру в названиях книг
    def test_add_book_in_favorites_case_sensitivity(self, collector):
        collector.add_new_book('Фантастика 1')

        # Пытаемся добавить книгу с другим регистром
        collector.add_book_in_favorites('фантастика 1')
        
        assert 'фантастика 1' not in collector.favorites

    # ТЕСТЫ ДЛЯ МЕТОДА delete_book_from_favorites - удаляем книгу из Избранного
    # Тест: удаление существующей книги из избранного
    def test_delete_book_from_favorites_existing_book(self, collector):
        collector.add_new_book('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 1')
        collector.delete_book_from_favorites('Фантастика 1')
        
        assert 'Фантастика 1' not in collector.favorites

    # Тест: удаление одной книги из списка с несколькими книгами
    def test_delete_book_from_favorites_multiple_books(self, collector):
        # Добавляем несколько книг
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_new_book('Ужасы 1')
        
        # Добавляем все книги в избранное
        collector.add_book_in_favorites('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 2')
        collector.add_book_in_favorites('Ужасы 1')
        
        collector.delete_book_from_favorites('Фантастика 2')
        
        assert 'Фантастика 2' not in collector.favorites

    # Тест: попытку удаления книги дважды
    def test_delete_book_from_favorites_twice(self, collector):
        collector.add_new_book('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 1')

        # Первое удаление
        collector.delete_book_from_favorites('Фантастика 1')
        
        # Второе удаление (не должно вызвать ошибок)
        collector.delete_book_from_favorites('Фантастика 1')
        
        assert 'Фантастика 1' not in collector.favorites

    # Тест: попытку удаления несуществующей книги из избранного
    def test_delete_book_from_favorites_nonexistent_book(self, collector):
        # Добавляем книгу в избранное
        collector.add_new_book('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 1')
        collector.delete_book_from_favorites('Несуществующая книга')
 
        assert collector.favorites == ['Фантастика 1']
        
    # Тест: попытку удаления из пустого списка избранного
    def test_delete_book_from_favorites_empty_favorites(self, collector):
        collector.delete_book_from_favorites('Любая книга') #collector.favorites == []
        assert collector.favorites == []

    # Тест: чувствительность к регистру при удалении
    def test_delete_book_from_favorites_case_sensitivity(self, collector):
        collector.add_new_book('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 1')
        
        # Пытаемся удалить книгу с другим регистром
        collector.delete_book_from_favorites('фантастика 1')
        
        # Проверяем, что книга осталась в избранном
        assert 'Фантастика 1' in collector.favorites

    # ТЕСТЫ ДЛЯ МЕТОДА get_list_of_favorites_books - получаем список Избранных книг
    # Тест: получение списка избранных книг
    def test_get_list_of_favorites_books_with_books(self, collector):
        # Добавляем книги в избранное
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_book_in_favorites('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 2')
        
        assert collector.get_list_of_favorites_books() == ['Фантастика 1', 'Фантастика 2']

    # Тест: получение списка после удаления книги из избранного
    def test_get_list_of_favorites_books_after_removal(self, collector):
        # Добавляем книги в избранное
        collector.add_new_book('Фантастика 1')
        collector.add_new_book('Фантастика 2')
        collector.add_book_in_favorites('Фантастика 1')
        collector.add_book_in_favorites('Фантастика 2')
        
        # Удаляем одну книгу из избранного
        collector.delete_book_from_favorites('Фантастика 1')
        
        assert collector.get_list_of_favorites_books() == ['Фантастика 2']
    
    # Тест: получение пустого списка избранных книг
    def test_get_list_of_favorites_books_empty(self, collector):
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []