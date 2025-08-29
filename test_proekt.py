import pytest


class TestBooksCollector:

    def test_add_new_book_get_new_book(self, collector):

        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        assert len(collector.get_books_genre()) == 2

    # Тест 1. Проверка успешного добавления новой книги с названием.
    # Длиной не более 40 символов (валидное значение)
    def test_add_new_book_with_max_length_name(self, collector):
        collector.add_new_book("Властелин колец")
        assert "Властелин колец" in collector.get_books_genre()

    # Тест 2. Параметризованный тест для добавления книг с невалидными
    # названиями (пустая строка и строка длиной более 40 символов)
    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_add_new_book_invalid_names_not_added(self, book_name, collector):

        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # Тест 3. Проверка, что одну книгу нельзя добавить дважды
    def test_add_duplicate_book_not_added(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Оно")

        assert len(collector.get_books_genre()) == 1

    # Тест 4. Проверка, что у добавленной книги нет жанра
    def test_add_new_book_no_genre(self, collector):
        collector.add_new_book("Оно")
        assert collector.get_book_genre("Оно") == ""

    # Тест 5. Проверка, что у книги можно установить жанр
    def test_set_book_genre_valid_genre_book_exists(self, collector):
        name = "Железный человек"
        genre = "Фантастика"
        collector.books_genre[name] = ""
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # Тест 6. Получение списка книг определенного жанра
    def test_get_books_with_specific_genre_returns_correct_books(
        self,
        collector,
    ):
        books_name_genres = {
            "Звездные войны: Новая надежда": "Фантастика",
            "Звездные войны: Империя наносит ответный удар": "Фантастика",
            "Оно": "Ужасы",
        }

        collector.books_genre = books_name_genres

        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert "Звездные войны: Новая надежда" in fantasy_books
        assert "Звездные войны: Империя наносит ответный удар" in fantasy_books
        assert "Оно" not in fantasy_books

    # Тест 7: Проверка получения жанра существующей книги
    def test_get_book_genre_existing_book_with_genre(self, collector):
        expected_books = {
            "Преступление и наказание": "Детективы",
        }

        collector.books_genre = expected_books

        result = collector.get_book_genre("Преступление и наказание")
        assert result == "Детективы"

    # Тест 8: Проверка получения словаря всех книг и жанров
    def test_get_books_genre_returns_books_genre_dictionary(self, collector):
        expected_books = {
            "Книга 1": "Фантастика",
            "Книга 2": "Комедии",
            "Книга 3": "Детективы",
        }
        collector.books_genre = expected_books
        assert collector.get_books_genre() == expected_books

    # Тест 9. Получение книг для детей (проверка возрастного рейтинга)
    def test_get_books_for_children_only_child_friendly_genres(
        self,
        collector,
    ):
        chidren_list = {
            "Смешарики": "Мультфильмы",
            "Даша следопыт": "Мультфильмы",
            "Оно": "Ужасы",
        }
        collector.books_genre = chidren_list
        chidren_list = collector.get_books_for_children()
        assert "Смешарики" in chidren_list
        assert "Даша следопыт" in chidren_list
        assert "Оно" not in chidren_list

    # Тест 10. Добавление книги в избранное
    def test_add_book_in_favorites_book_added_to_favorites(self, collector):
        expected_books = {"Дневник памяти": "Романтика"}
        collector.books_genre = expected_books
        collector.add_book_in_favorites("Дневник памяти")
        

        assert "Дневник памяти" in collector.get_list_of_favorites_books()

    # Тест 11. Удаление книги из избранного
    def test_delete_book_from_favorites_deletes_existing_book(self, collector):
        books_favorites = ["Дневник памяти"]
        collector.favorites = books_favorites
        collector.delete_book_from_favorites("Дневник памяти")

        assert "Дневник памяти" not in collector.get_list_of_favorites_books()

    # Тест 12. Проверка получения списка избранных книг
    def test_get_list_of_favorites_books_returns_favorites(self, collector):
        expected_favorites = ["Книга 1", "Книга 2", "Книга 3"]
        collector.favorites = expected_favorites

        result = collector.get_list_of_favorites_books()
        assert result == expected_favorites