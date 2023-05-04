BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation = [',', '.', '!', ':', ';', '?']
    end = min(start + size, len(text))
    for i in range(end - 1, start, -1):
        if text[i:i + 2] in ['..']:
            for j in range(i - 2, start, -1):
                if text[j] in punctuation:
                    return text[start:j + 1], j + 1 - start
        elif text[i] in punctuation:
            return text[start:i + 1], i + 1 - start

    return text[start:end], end - start


# Функция, формирующая словарь книги
def prepare_book(path: str) -> dict[int, str]:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        start = 0
        page_num = 1
        while start < len(text):
            page_text, page_size = _get_part_text(text, start, PAGE_SIZE)
            book[page_num] = page_text.lstrip()
            start += page_size
            page_num += 1
    return book


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
