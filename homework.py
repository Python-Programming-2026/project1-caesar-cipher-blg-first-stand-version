# 凯撒密码 + qwer可视化
import matplotlib.pyplot as plt
text = input("请输入要加密的文本：")
shift = int(input("请输入加密偏移量："))
encrypted_text = ""
# 存储字母位置数据
original_positions = []  # 原文字母的位置
encrypted_positions = []  # 加密后字母的位置
original_chars = []  # 存储原文的字母
# 加密+收集可视化数据
for char in text:
    if char.isalpha():
        # 记录原文字母和位置
        original_chars.append(char)
        if char.isupper():
            original_pos = ord(char) - ord('A')
            new_pos = (original_pos + shift) % 26
            new_char = chr(new_pos + ord('A'))
        else:
            original_pos = ord(char) - ord('a')
            new_pos = (original_pos + shift) % 26
            new_char = chr(new_pos + ord('a'))
        # 收集位置数据
        original_positions.append(original_pos)
        encrypted_positions.append(new_pos)
        encrypted_text += new_char
    else:
        encrypted_text += char
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 创建图表
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# 子图1：原文字母位置
ax1.bar(original_chars, original_positions, color='lightblue')
ax1.set_title(f'原文字母位置（A=0, B=1...Z=25）')
ax1.set_ylim(0, 25)
# 子图2：加密后字母位置
ax2.bar(original_chars, encrypted_positions, color='coral')
ax2.set_title(f'加密后字母位置（偏移量={shift}）')
ax2.set_ylabel('字母位置数值')
ax2.set_ylim(0, 25)
# 标题
plt.suptitle(f'凯撒密码移位可视化 | 原文：{text} | 加密后：{encrypted_text}', fontsize=14)
plt.tight_layout()
plt.show()
print(f"\n加密后的文本：{encrypted_text}")