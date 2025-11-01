import csv
from typing import List, Dict


def read_books_csv(file_path: str) -> List[Dict]:
    """Reads a CSV file with books
    读取包含书籍信息的CSV文件"""
    books = []
    encodings = ['cp1251', 'utf-8']  # Encodings to try for reading the file
    # 尝试读取文件的编码格式
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=';')  # Read CSV as dictionary
                # 以字典形式读取CSV
                for row in reader:
                    books.append(row)
                return books
        except UnicodeDecodeError:
            continue  # Try next encoding if current one fails
            # 如果当前编码失败，尝试下一种编码
    print("❌ Error reading file books.csv")
    return books


def create_bibliography(books: List[Dict], output_path: str = "bibliography_list.txt") -> None:
    """Generates 20 bibliography entries (price ≥ 150 rubles)
    生成20条参考文献记录（价格≥150卢布）"""
    # Filter books with price ≥ 150 rubles
    # 筛选价格≥150卢布的书籍
    suitable_books = []
    for book in books:
        price_str = book.get("Цена поступления", "0").strip().replace(",",
                                                                      ".")  # "Цена поступления" is CSV column name (keep original)
        # "Цена поступления"是CSV列名（保留原名称）
        try:
            price = float(price_str)
        except ValueError:
            price = 0.0
        if price >= 150:
            suitable_books.append(book)

    # Take first 20 (or all if fewer than 20)
    # 取前20条（如果不足20条则取全部）
    selected_books = suitable_books[:20] if len(suitable_books) >= 20 else suitable_books

    # Write to file
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        for number, book in enumerate(selected_books, 1):
            author = book.get("Автор", "Unknown author").strip()  # "Автор" is CSV column name (keep original)
            # "Автор"是CSV列名（保留原名称）
            title = book.get("Название", "Unknown title").strip()  # "Название" is CSV column name (keep original)
            # "Название"是CSV列名（保留原名称）

            # Extract year from date (format: DD.MM.YYYY)
            # 从日期中提取年份（格式：日.月.年）
            date = book.get("Дата поступления", "").strip()  # "Дата поступления" is CSV column name (keep original)
            # "Дата поступления"是CSV列名（保留原名称）
            if date:
                try:
                    year = date.split(".")[2]  # DD.MM.YYYY → take the third element
                    # 日.月.年 → 取第三个元素（年份）
                except IndexError:
                    year = "Unknown year"
            else:
                year = "Unknown year"

            f.write(f"{number}. {author}. {title} - {year}\n")

    print(f"\n📄 Bibliography list saved to {output_path} (entries: {len(selected_books)})")


if __name__ == "__main__":
    PATH_TO_BOOKS = "books.csv"
    books_data = read_books_csv(PATH_TO_BOOKS)
    if books_data:
        create_bibliography(books_data)