import xml.etree.ElementTree as ET
from typing import Dict


def parse_xml_average_value(file_path: str) -> Dict:
    """
    Parses an XML file with currency information, extracts Value indicators, and calculates their average
    解析包含货币信息的XML文件，提取Value指标并计算其平均值
    """
    value_list = []  # List to store numeric values of Value indicators (用于存储Value指标的数值)

    try:
        # Parse the XML file (解析XML文件)
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Traverse all <Valute> tags (遍历所有<Valute>标签)
        for currency in root.findall("Valute"):
            # Extract Value (numeric indicator, handle comma as decimal separator)
            # 提取Value（数值指标，处理逗号作为小数点的情况）
            value_elem = currency.find("Value")
            if value_elem is not None and value_elem.text.strip():
                value_str = value_elem.text.strip()
                # Replace comma with dot to handle decimal numbers (替换逗号为点以处理小数)
                value_str = value_str.replace(',', '.')
                try:
                    value = float(value_str)
                    value_list.append(value)
                except ValueError:
                    print(f"⚠️ Value '{value_elem.text}' is not a valid number")  # ⚠️ Value不是有效的数字

        # Calculate average if there are valid values (如果有有效数值则计算平均值)
        average = None
        if value_list:
            average = sum(value_list) / len(value_list)

        # Output results to console (将结果输出到控制台)
        print(f"\n Result of parsing currency.xml:")  #  解析currency.xml的结果：
        print(f"List of Value indicators (count: {len(value_list)}): {value_list}")  # Value指标列表（数量：{...}）：{...}
        print(
            f"Average of Value indicators: {average:.2f}" if average is not None else "No valid Value indicators to calculate average")
        # Value指标的平均值：{...}（若无可用于计算平均值的有效Value指标则提示）

    except Exception as e:
        print(f"❌ XML parsing error: {str(e)}")  # ❌ XML解析错误：{...}

    return {"value_list": value_list, "average": average}


if __name__ == "__main__":
    XML_PATH = "currency.xml"  # Path to the XML file (XML文件路径)
    parse_xml_average_value(XML_PATH)  # Results are printed to console（结果输出到控制台）