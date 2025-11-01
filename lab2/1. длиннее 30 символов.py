import csv
from typing import List, Dict


def read_books_csv(path_to_file: str) -> List[Dict]:
    """
    Reads CSV file with books, handles encodings / 读取包含书籍的CSV文件，处理编码问题
    """
    books = []
    encodings = ['cp1251', 'utf-8', 'utf-8-sig']
    for encoding in encodings:
        try:
            with open(path_to_file, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=';')
                if "Название" not in reader.fieldnames:
                    continue
                # Read all records / 读取所有记录
                for row in reader:
                    books.append(row)
                print(f" Successfully read {len(books)} records (encoding: {encoding}) /  成功读取 {len(books)} 条记录（编码：{encoding}）")
                return books
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    print(" Error: failed to read books.csv (check encoding and path) /  错误：无法读取 books.csv（请检查编码和路径）")
    return books


def count_long_titles(books: List[Dict]) -> int:
    """
    Counts the number of records where title length > 30 characters / 统计标题长度超过30个字符的记录数量
    """
    count = 0
    for book in books:
        # Extract title, handle empty values / 提取标题，处理空值
        title = book.get("Название", "").strip()
        if len(title) > 30:
            count += 1
    print(f"\n Number of books with title length > 30 characters: {count} /  标题长度超过30个字符的书籍数量：{count}")
    return count


if __name__ == "__main__":
    # Path to the file (in the same folder) / 文件路径（在同一文件夹中）
    PATH_TO_BOOKS = "books.csv"
    # Execute the task / 执行任务
    books_data = read_books_csv(PATH_TO_BOOKS)
    if books_data:
        count_long_titles(books_data)