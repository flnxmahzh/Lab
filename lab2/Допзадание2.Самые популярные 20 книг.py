import csv
from typing import List, Dict


def read_books_csv(path_to_file: str) -> List[Dict]:
    """
    Reads a CSV file with books, handles encodings for Russian text
    读取包含书籍信息的CSV文件，处理俄语文本的编码问题
    """
    books = []
    encodings = ['cp1251', 'utf-8']  # Common encodings for Russian text 俄语文本常用编码
    for encoding in encodings:
        try:
            with open(path_to_file, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=';')
                # Check if there is a field for number of loans
                # 检查是否存在"借阅次数"字段
                if "Кол-во выдач" not in reader.fieldnames:
                    continue
                for row in reader:
                    books.append(row)
                print(f"✅ Successfully read {len(books)} records (encoding: {encoding})")
                return books
        except UnicodeDecodeError:
            continue
    print("❌ Error: failed to read books.csv")
    return books


def get_top20_popular(books: List[Dict]) -> List[Dict]:
    """
    Calculates and prints the top 20 most popular books (by number of loans)
    计算并输出最受欢迎的前20本书（按借阅次数排序）
    """

    def num_loans(book: Dict) -> int:
        """
        Helper function: extracts the number of loans as an integer
        辅助函数：将借阅次数提取为整数
        """
        loans_str = book.get("Кол-во выдач", "0").strip()
        try:
            return int(loans_str)  # Convert to number 转换为数字
        except ValueError:
            return 0  # If the value is invalid, count as 0 若值无效，按0处理

    # Sort books by number of loans (descending order)
    # 按借阅次数对书籍排序（从多到少）
    sorted_books = sorted(books, key=num_loans, reverse=True)
    # Take the first 20 books
    # 取前20本书
    top20 = sorted_books[:20]

    # Print results
    # 输出结果
    print(f"\n🔥 Top 20 most popular books (by number of loans):")
    for number, book in enumerate(top20, 1):
        print(f"""
{number}. Title: {book.get("Название", "Unknown title")}
   Author: {book.get("Автор", "Unknown author")}
   Number of loans: {num_loans(book)}
   Purchase price: {book.get("Цена поступления", "Unknown")} rubles
        """)
    return top20


if __name__ == "__main__":
    # Path to the file (in the same folder)
    # 文件路径（与脚本同目录）
    PATH_TO_BOOKS = "books.csv"
    # Execute the task
    # 执行任务
    books_data = read_books_csv(PATH_TO_BOOKS)
    if books_data:
        get_top20_popular(books_data)