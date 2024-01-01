# -*- coding: utf-8 -*-
"""
File:swap.py
Author:ezgameworkplace
Date:2023/12/4
"""
import os

# 替换文件夹中文件有“A”就替换成“B”
def replace_A_with_B_in_filenames(folder_path, str1, str2):
    # 遍历文件夹中的所有文件和子文件夹
    for filename in os.listdir(folder_path):
        # 检查文件名中是否包含"A"
        if str1 in filename:
            # 构造新的文件名，将"A"替换为"B"
            new_filename = filename.replace(str1, str2)
            # 构造完整的旧文件路径和新文件路径
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == '__main__':

    # 使用示例
    folder_path = r''  # 替换为你的文件夹路径
    replace_A_with_B_in_filenames(folder_path, "", "")
