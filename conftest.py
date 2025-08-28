#фикстура для добавления новой книги
    @pytest.fixture
    def collector():
        return BooksCollector()
    