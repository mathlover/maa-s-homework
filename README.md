# 中文版本

## 公告

**作业站已经恢复正常运作。如果您需要更多的作业，请前往作业站下载。**  
**请注意，本仓库仅收录部分作业。**  

作业站地址：<https://prts.plus>  
创建作业：<https://prts.plus/create>

## 自动下载

自动下载的Python程序位于 `Auto\Full-Auto` 目录。

- `作业搜索.py`: 批量搜索各种关卡  

### Auto\Full-Auto\CI

- `主线一键下载.py`: 自动搜索主线关卡（包括H关和S关）、剿灭作战、资源关
- `悖论模拟模组任务搜索.py`: 自动搜索悖论模拟和模组任务关卡
- `module.py`: 自动生成全部模组任务
- `活动一键下载.py`: 自动判断当前开启活动并下载
- `excel.py`: 自动生成excel文件

### CI

[daily_download.yml](https://github.com/ntgmc/maa-s-homework/blob/master/.github/workflows/daily_download.yml)  
此工作流程每日自动执行以下程序：

- [`主线一键下载.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E4%B8%BB%E7%BA%BF%E4%B8%80%E9%94%AE%E4%B8%8B%E8%BD%BD.py)
- [`悖论模拟模组任务搜索.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E6%82%96%E8%AE%BA%E6%A8%A1%E6%8B%9F%E6%A8%A1%E7%BB%84%E4%BB%BB%E5%8A%A1%E6%90%9C%E7%B4%A2.py)
- [`module.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/module.py)
- [`主线.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/%E4%B8%BB%E7%BA%BF.py)
- [`活动一键下载.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E6%B4%BB%E5%8A%A8%E4%B8%80%E9%94%AE%E4%B8%8B%E8%BD%BD.py)
- [`ALL.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/ALL.py)
- [`excel.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/excel.py)

生成 `json`, `zip` 文件并创建 Pull Request。

## 命名规则

`【下载看这里】合集下载`中压缩包命名规则：`[文件夹]-[文件数量].zip`  
`悖论模拟`中json文件命名规则：`[干员名] - [评分] - [作业站id].json`  
`模组任务`中json文件命名规则：`[干员名] - [任务关卡] - [评分] - [作业站id].json`  

## 活动收录规则

当前活动中收录的作业须同时满足以下条件：  

- 好评率 >= 80% (好评率：好评数/总评数)
- 浏览量 >= 1000

注: 对于作者 `萨拉托加` 的作业，将会显示其名于文件名中。  

## 版权声明

所有本仓库内的作业 `json` 文件均由 [MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights) 软件生成，具体生成方式，请参考 [Github链接](https://github.com/MaaAssistantArknights/MaaAssistantArknights) 和 [作业站创建作业](https://prts.plus/create)  
此仓库仅供本人存放之用，因此更新可能会不及时，请您理解。  
如果您需要借存或备份文件，请提交PR（[Pull Request](https://github.com/ntgmc/maa-s-homework/pulls)），我们欢迎您的贡献。建议在PR中留下您的联系方式以便进一步沟通。  
如果您有任何建议或意见，请随时与我联系。我们乐意听取您的反馈！  

# English Version

## Announcement

**The Homework Station is now back to normal operation. If you need more homework, please visit the Homework Station to download.**  
**Please note that this repository only includes a part of the homework.**  

- Homework Station: <https://prts.plus>  
- Create Homework: <https://prts.plus/create>

## Automatic Download

The automatic download Python scripts are located in `Auto\Full-Auto` directory.

- `作业搜索.py`: For users to use, batch search various levels.

### Auto\Full-Auto\CI

- `主线一键下载.py`: Automatically search for mainline stages (including H and S stages), Annihilation stages, and resource stages.
- `悖论模拟模组任务搜索.py`: Automatically search for Contingency Contract and module tasks.
- `module.py`: Automatically generate all module tasks.
- `活动一键下载.py`: Automatically determine the currently open event and download.
- `excel.py`: Automatically generate excel files.

### CI

[daily_download.yml](https://github.com/ntgmc/maa-s-homework/blob/master/.github/workflows/daily_download.yml)  
This workflow automatically executes the following programs daily: 

- [`主线一键下载.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E4%B8%BB%E7%BA%BF%E4%B8%80%E9%94%AE%E4%B8%8B%E8%BD%BD.py)
- [`悖论模拟模组任务搜索.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E6%82%96%E8%AE%BA%E6%A8%A1%E6%8B%9F%E6%A8%A1%E7%BB%84%E4%BB%BB%E5%8A%A1%E6%90%9C%E7%B4%A2.py)
- [`module.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/module.py)
- [`主线.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/%E4%B8%BB%E7%BA%BF.py)
- [`活动一键下载.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/%E6%B4%BB%E5%8A%A8%E4%B8%80%E9%94%AE%E4%B8%8B%E8%BD%BD.py)
- [`ALL.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/ALL.py)
- [`excel.py`](https://github.com/ntgmc/maa-s-homework/blob/master/Auto/Full-Auto/CI/excel.py)

then generates JSON files, and creates Pull Requests.

## Naming Rules

- `【下载看这里】合集下载` compressed package naming rule: `[Folder]-[Number of Files].zip`  
- `悖论模拟` JSON file naming rule: `[Operator Name] - [Rating] - [Homework Station ID].json`  
- `模组任务` JSON file naming rule: `[Operator Name] - [Task Level] - [Rating] - [Homework Station ID].json`  

## Activity Inclusion Rules
 
The assignments included in the current activity must meet all of the following conditions:  
 
- Rate >= 80% (Rate: number of positive reviews/total number of reviews)
- Views >= 1000
 
Note: For the assignment of author `萨拉托加` , their name will be displayed in the file name.  

## Copyright Statement

All howework `json` files in this repository are generated by the [MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights) software. For the specific generation method, please refer to the [Github-link](https://github.com/MaaAssistantArknights/MaaAssistantArknights) and [Create Homework on Homework Station](https://prts.plus/create).  
This repository is only for storing for myself, so updates may not be timely. Your understanding is appreciated.  
If you need to borrow or backup files, feel free to submit a PR ([Pull Request](https://github.com/ntgmc/maa-s-homework/pulls)). Your contribution is welcome. It is recommended to leave your contact information in the PR for further communication.  
If you have any suggestions or comments, please feel free to contact me. We are happy to hear your feedback!
