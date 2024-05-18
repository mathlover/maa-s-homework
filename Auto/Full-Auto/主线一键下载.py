import requests
import json
import re
from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置阈值(好评率和浏览量)(不满足条件则降低阈值，但最低不低于50% 0)
download_score_threshold = 80  # 好评率阈值
download_view_threshold = 1000  # 浏览量阈值
# 设置stage_name
tough = [10, 11, 12, 13, 14]
main = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resource_level = ["wk_toxic_5", "wk_armor_5", "wk_fly_5", "wk_kc_6", "wk_melee_6", "pro_a_1",
                  "pro_a_2", "pro_b_1", "pro_b_2", "pro_c_1", "pro_c_2", "pro_d_1", "pro_d_2"]
# 设置最大关卡数
max_level = {
    0: 11,
    1: 12,
    2: 10,
    3: 8,
    4: 10,
    5: 10,
    6: 14,
    7: 16,
    8: 17,
    9: 17,
    10: 15,
    11: 18,
    12: 18,
    13: 19,
    14: 19
}
max_hard_level = {
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 6,
    10: 3,
    11: 4,
    12: 4,
    13: 4,
    14: 4
}
max_sub_level = {
    2: 12,
    3: 7,
    4: 10,
    5: 9,
    6: 4,
    7: 2,
    9: 2
}
# 设置空列表
no_result = []
# 设置日期
date = datetime.now().strftime('%Y-%m-%d')


def makedir():
    os.makedirs(f'./download/往期剿灭', exist_ok=True)
    os.makedirs(f'./download/资源关', exist_ok=True)
    for _stage in max_level:
        os.makedirs(f'./download/主线/第{_stage}章', exist_ok=True)


def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)


def pad_zero(i):
    return str(i).zfill(2)


def build_dict(data, key: str):  # key为生成的字典的键
    _dict = {}
    for member in data:
        _key = member[key]
        if _key in _dict:
            _dict[_key].append(member)
        else:
            _dict[_key] = [member]
    return _dict


def build_sub_dict(data):  # key为章节整数
    _dict = {}
    for member in data:
        if 'obt/main/level_sub_' not in member['level_id']:  # 只处理sub关卡
            continue
        _key = get_sub_stage_info(member['stage_id'])
        if _key in _dict:
            _dict[_key].append(member)
        else:
            _dict[_key] = [member]
    return _dict


def get_level_data():
    url = 'https://prts.maa.plus/arknights/level'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []


def calculate_percent(item):
    like = item.get('like', 0)
    dislike = item.get('dislike', 0)
    total = like + dislike
    if total == 0:
        return 0
    else:
        return round(like / total * 100, 2)


def get_level_name(stage_id):  # 通过stage_id获取关卡名称
    return stage_dict.get(stage_id, [{}])[0].get('cat_three', '')


def get_stage_info(text):  # 返回第一个-前的整数
    match = re.search(r"(\d+)-", text)
    if match:
        return int(match.group(1))
    else:
        return None


def get_sub_stage_info(text):
    match = re.search(r"sub_(\d+)-", text)
    if match:
        return int(match.group(1))
    else:
        return None


def replace_special_char(text):
    return text.replace('/', '').replace('\\', '')


def generate_filename(name, data, mode):
    stage_name = get_level_name(name)
    _stage = get_stage_info(stage_name)
    opers = data.get('opers', [])
    groups = data.get('groups', [])
    names_parts = ['+'.join(oper.get('name', '') for oper in opers),
                   '+'.join(group.get('name', '') for group in groups)]
    names = '+'.join(part for part in names_parts if part)  # 只连接非空的部分
    names = replace_special_char(names)
    if len(names) > 220:
        names = "文件名过长不予显示"
    if mode == 1 or mode == 3:
        file_path = f'./download/主线/第{_stage}章/{stage_name}_{names}.json'
    elif mode == 2:
        file_path = f'./download/往期剿灭/{stage_name}_{names}.json'
    elif mode == 4:
        file_path = f'./download/资源关/{stage_name}_{names}.json'
    else:
        file_path = f'./download/{stage_name}_{names}.json'
    return file_path


def search(keyword, path_mode=1, filter_mode=0):
    url = f"https://prts.maa.plus/copilot/query?page=1&limit=15&levelKeyword={keyword}&desc=true&orderBy=views"
    _headers = {
        "Origin": "https://prts.plus",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    _response = requests.get(url, headers=_headers)
    if _response.ok:
        filter_data(_response.json(), keyword, path_mode, filter_mode)
    else:
        print(f"请求 {keyword} 失败")


def filter_data(data, keyword, path_mode, filter_mode):
    global no_result
    total = data['data'].get('total', 0)
    if total > 0:
        download_amount = 0
        if filter_mode == 0:
            score_threshold = download_score_threshold
            view_threshold = download_view_threshold
        else:
            score_threshold = 80
            view_threshold = -1  # 保证只搜索一次
        while not download_amount:
            for item in data['data']['data']:
                percent = calculate_percent(item)
                view = item.get('views', 0)
                if percent >= score_threshold and view >= view_threshold:
                    content = json.loads(item['content'])
                    file_path = generate_filename(keyword, content, path_mode)
                    content['doc'][
                        'details'] = f"统计日期：{date}\n好评率：{percent}%  浏览量：{view}\n来源：{item['uploader']}  ID：{item['id']}\n" + \
                                     content['doc']['details']
                    print(f"{file_path} {percent}% {view} 成功下载")
                    write_to_file(file_path, content)
                    download_amount += 1
            if not download_amount:
                if score_threshold > 50:
                    score_threshold -= 5
                else:
                    view_threshold -= 200
                if view_threshold < 0:
                    print(f"{keyword} 无符合50% 0的数据 不再重试")
                    no_result.append(keyword)
                    break
                print(f"{keyword} 无符合条件的数据，降低阈值为{score_threshold}% {view_threshold}重试")
    else:
        print(f"{keyword} 无数据")


def tough_stage_search(_stage):
    for level in range(1, max_level.get(_stage, 0) + 1):
        search(f"tough_{pad_zero(_stage)}-{pad_zero(level)}")


def main_stage_search(_stage):
    for level in range(1, max_level.get(_stage, 0) + 1):
        search(f"main_{pad_zero(_stage)}-{pad_zero(level)}")


def hard_stage_search(_stage):
    for level in range(1, max_hard_level.get(_stage, 0) + 1):
        search(f"hard_{pad_zero(_stage)}-{pad_zero(level)}")


def sub_stage_search(_stage):
    for member in sub_dict.get(_stage, []):
        search(f"{member['stage_id']}", 3)


def camp_stage_search():
    for level in range(1, 4):
        search(f"camp_{pad_zero(level)}", 2)
    for level in range(1, len(cat_one_dict.get('剿灭作战', [])) - 2):
        search(f"camp_r_{pad_zero(level)}", 2)


def resource_stage_search():
    for level in resource_level:
        search(level, 4, 1)


makedir()
level_data = get_level_data()
stage_dict = build_dict(level_data, 'stage_id')
sub_dict = build_sub_dict(level_data)
cat_one_dict = build_dict(level_data, 'cat_one')
now = datetime.now().timestamp()
# 创建一个线程池
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    # 添加任务到线程池
    for stage in tough:
        futures.append(executor.submit(tough_stage_search, stage))
    for stage in main:
        futures.append(executor.submit(main_stage_search, stage))
    for stage in max_hard_level:
        futures.append(executor.submit(hard_stage_search, stage))
    for stage in max_sub_level:
        futures.append(executor.submit(sub_stage_search, stage))
    futures.append(executor.submit(camp_stage_search))
    futures.append(executor.submit(resource_stage_search))

    # 等待所有任务完成
    for future in as_completed(futures):
        try:
            future.result()
        except Exception as e:
            print(f"Task generated an exception: {e}")
last = datetime.now().timestamp()
print(f"搜索完毕，共耗时 {round(last - now, 2)} s.\n")
print('No_result: ', no_result)
