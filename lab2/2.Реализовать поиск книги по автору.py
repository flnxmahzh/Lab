import csv
from typing import List, Dict


def read_books_csv(path_to_file: str) -> List[Dict]:
    """
    # 读取包含书籍的CSV文件 / Reads CSV file with books
    """
    books = []
    encodings = ['cp1251', 'utf-8']  # 尝试的编码格式 / Encodings to try
    for encoding in encodings:
        try:
            with open(path_to_file, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=';')
                if "Автор" not in reader.fieldnames:  # 检查是否有"Автор"（作者）字段 / Check if "Author" field exists
                    continue
                for row in reader:
                    books.append(row)
                return books
        except UnicodeDecodeError:
            continue
    print("❌ Error reading books.csv file")
    return books


def search_by_author(books: List[Dict], author_name: str) -> List[Dict]:
    """
    # 搜索价格≥150卢布的作者书籍 / Searches for the author's books with price ≥ 150 rubles
    """
    found_books = []
    for book in books:
        # 提取并解析价格（俄语格式，用逗号作为分隔符） / Extract and parse price (Russian format with comma as separator)
        price_str = book.get("Цена поступления", "0").strip().replace(",", ".")
        try:
            price = float(price_str)
        except ValueError:
            price = 0.0  # 价格格式错误→不符合条件 / Incorrect price format → does not meet criteria

        # 检查作者（不区分大小写） / Check author (case-insensitive)
        book_author = book.get("Автор", "").strip().lower()
        target_author = author_name.strip().lower()

        # 筛选条件：作者匹配 + 价格≥150 / Filter: author matches + price ≥ 150
        if target_author in book_author and price >= 150:
            found_books.append(book)
    return found_books


def print_results(found_books: List[Dict], author_name: str):
    """
    # 打印找到的书籍 / Prints the found books
    """
    if not found_books:
        print(f"\n❌ No books by author «{author_name}» with price ≥ 150 rubles found")
        return
    print(f"\n Found {len(found_books)} books by author «{author_name}» (price ≥ 150 rubles):")
    for i, book in enumerate(found_books, 1):
        print(f"""
{i}. Title: {book.get("Название", "Unknown")}
   Author: {book.get("Автор", "Unknown")}
   Price: {book.get("Цена поступления", "Unknown")} rubles
   Loans: {book.get("Кол-во выдач", "0")}
        """)


if __name__ == "__main__":
    PATH_TO_BOOKS = "books.csv"
    books_data = read_books_csv(PATH_TO_BOOKS)
    if books_data:
        author_input = input("Enter the author's name to search: ")
        results = search_by_author(books_data, author_input)
        print_results(results, author_input)