[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fPQK30A4)
# 凯撒密码可视化实现
本项目是基于Python语法实现的凯撒密码加密工具，支持大小写字母的加密，并增加了字母移位可视化功能。
## 1.凯撒密码原理
凯撒密码是一种经典的替换加密技术，通过将字母按照指定的偏移量进行移位实现加密（如 A+3=D，z+1=a），解密则是加密的逆过程。
本项目支持：
- 大小写字母的加密与解密
- 字母移位可视化（柱状图）
## 2.运行环境
- PyCharm
- python3.6+
- 第三方库：matplotlib
## 3.程序部署与运行
### 3.1 前置环境准备
1. 安装Python环境：确保电脑已安装Python 3.6及以上版本（推荐3.8/3.9）；
2. 安装PyCharm：下载并安装PyCharm，官网地址：https://www.jetbrains.com/pycharm/。
### 3.2 项目部署操作
1. 新建项目：打开PyCharm，点击「New Project」，选择项目保存路径，确认Python解释器为已安装的版本，点击「Create」；
2. 导入代码：在新建的项目中，右键点击项目名称 → 「New」→ 「Python File」，命名为`caesar_cipher.py`（可自定义），将凯撒密码代码复制到该文件中并保存；
3. 安装依赖（仅可视化版本需要）：
   - 打开PyCharm底部的「Terminal」终端；
   - 输入命令 `pip install matplotlib` 并回车，等待依赖安装完成。
### 3.3 运行程序
1. 直接运行：点击PyCharm右上角的绿色「Run」按钮（或右键代码文件 → 「Run 'caesar_cipher'」）；
2. 交互操作：根据控制台提示，依次输入要加密或解密的文本、偏移量，程序自动输出加密或解密的结果（可视化版本会额外弹出图表窗口）；
3. 验证结果：输入示例（如文本「Hello World!」、偏移量3），查看输出是否为「Khoor Zruog!」，确认程序运行正常。
### 3.4 常见问题解决
1. 提示「pip不是内部命令」：打开Python安装目录，将「Scripts」文件夹路径添加到系统环境变量，或在终端使用 `python -m pip install matplotlib` 替代；
2. 可视化图表不显示：确认matplotlib安装成功，代码中已添加中文字体设置，重启PyCharm后重新运行；
3. 输入偏移量报错：确保输入的是整数（如3、5），避免输入字母/符号。
## 4.包含的课内知识点
- 变量的定义与赋值
- if else语句
- for循环
- ord() chr() 函数
- 列表
- %运算
## 5.演示视频

https://github.com/user-attachments/assets/11c104f9-8939-4559-9cc9-39a3e9389239
## 6.作者
王宇翔 2243415880  （同组成员：张忠泽 2244413901）
