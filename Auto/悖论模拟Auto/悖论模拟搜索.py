import requests
from bs4 import BeautifulSoup


def calculate_percent(item):
    like = item.get('like', 0)
    dislike = item.get('dislike', 0)
    total = like + dislike
    if total == 0:
        return 0
    else:
        return round(like / total * 100, 2)


def code_output(percent, id):
    if percent < 80:
        return f"*maa://{id} ({percent})"
    else:
        return f"maa://{id} ({percent})"


def search(keyword):
    url = f"https://prts.maa.plus/copilot/query?desc=true&limit=15&page=1&order_by=hot&level_keyword={keyword}"
    _headers = {
        "Origin": "https://prts.plus",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }

    _response = requests.get(url, headers=_headers)

    if _response.status_code == 200:
        data = _response.json()
        total = data['data'].get('total', 0)
        if total > 0:
            ids = []
            for item in data['data']['data']:
                percent = calculate_percent(item)
                if percent > 50:
                    ids.append(code_output(percent, item['id']))
                else:
                    continue
            return len(ids), ', '.join(ids)
        else:
            return 0, "None"
    else:
        return 0, "None"


# 读取关键字文件
keywords_file = './keywords.txt'
output_file = './output.txt'
file_path2 = "./output2.txt"
output_lines = []
with open(keywords_file, 'r', encoding='utf-8') as f:
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in f:
            # 如果是空行，保留空行并继续下一行的处理
            if not line.strip():
                output_lines.append(line)
                continue
            keyword = line.strip()
            id_count, str_ids = search(keyword)
            output_lines.append(f"{keyword}\t{id_count}\t{str_ids}\n")
            print(f"{keyword}\t{id_count}\t{str_ids}\n")
        output.writelines(output_lines)

print("输出完成！")


# 解析HTML并提取角色名
def extract_character_names(html_content):
    _character_names = set()
    soup = BeautifulSoup(html_content, 'html.parser')
    prop_cells = soup.find_all('div', class_='smw-table-cell smwprops')
    for cell in prop_cells:
        _name = cell.find('a').text.strip()
        _character_names.add(_name)
    return _character_names


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}
params = {
    'title': '属性:悖论模拟对象',
    'limit': '500',
    'offset': '0',
    'filter': '',
}
response = requests.get('https://prts.wiki/index.php', params=params, headers=headers)
# 提取HTML中的角色名
character_names = extract_character_names(response.text)
# 处理txt文件
with open(output_file, 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
# 处理每一行
output_lines = []
for line in lines:
    # 如果是空行，保留空行并继续下一行的处理
    if not line.strip():
        output_lines.append(line)
        continue
    parts = line.split('\t')
    name = parts[0]
    if name in character_names:
        output_lines.append(line)
    else:
        # 如果角色名不存在，将后面两个内容都变为"-"
        output_lines.append(name + '\t-\t-\n')
# 写入处理后的内容到新的txt文件中
with open(file_path2, 'w', encoding='utf-8') as output_file:
    output_file.writelines(output_lines)
print("输出完成！")