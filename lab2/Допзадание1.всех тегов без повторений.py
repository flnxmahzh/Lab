import csv
from typing import List, Dict


def read_books_csv(path_to_file: str) -> List[Dict]:
    """
    Reads a CSV file with books, handles encodings for Russian text
    读取包含书籍信息的CSV文件，处理俄语文本的编码问题
    """
    books = []
    encodings = ['cp1251', 'utf-8']  # Main encodings for Russian CSV files
                                     # 俄语CSV文件的主要编码格式
    for enc in encodings:
        try:
            with open(path_to_file, 'r', encoding=enc, newline='') as f:
                reader = csv.DictReader(f, delimiter=';')
                # Check if the genre field exists
                # 检查是否存在"书籍类型"字段
                if "Жанр книги" not in reader.fieldnames:
                    continue
                for row in reader:
                    books.append(row)
                print(f"✅ Successfully read {len(books)} records (encoding: {enc})")
                return books
        except UnicodeDecodeError:
            continue
    print("❌ Error: failed to read books.csv file")
    return books


def output_unique_genres(books: List[Dict]) -> List[str]:
    """
    Extracts and prints all unique genres (tags) from the 'Жанр книги' field
    从'Жанр книги'（书籍类型）字段中提取并打印所有唯一的类型（标签）
    """
    genres_set = set()  # Use a set to automatically remove duplicates
                       # 使用集合自动去除重复项
    for book in books:
        genre_str = book.get("Жанр книги", "").strip()  # Get the genre string
                                                       # 获取类型字符串
        if not genre_str:
            continue  # Skip empty values
                      # 跳过空值
        # Split genres (often separated by #)
        # 分割类型（通常用#分隔）
        genres = [g.strip() for g in genre_str.split("#") if g.strip()]
        for g in genres:
            genres_set.add(g)  # Add to set (duplicates are removed)
                               # 添加到集合（重复项会被自动移除）
    # Convert set to a sorted list
    # 将集合转换为排序后的列表
    unique_genres = sorted(list(genres_set))
    # Print results
    # 打印结果
    print(f"\n🏷️ All unique genres (tags) in the library:")
    print(f"Number of unique genres: {len(unique_genres)}")
    for number, genre in enumerate(unique_genres, 1):
        print(f"{number}. {genre}")
    return unique_genres


if __name__ == "__main__":
    # Path to the file (in the same folder)
    # 文件路径（与脚本同目录）
    PATH_TO_BOOKS = "books.csv"
    # Execute the task
    # 执行任务
    books_data = read_books_csv(PATH_TO_BOOKS)
    if books_data:
        output_unique_genres(books_data)