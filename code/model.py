import os

file_def = "../def-models/"
file_save = "../block/"

path = "../def-models"
files = os.listdir(path)

for file in files:
    with open(f"{file_def}{file}", encoding="cp932") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace("particle:",)
    data_lines = data_lines.replace('"textures": {','"textures": {\n        "particle": "blocks/bed_head_top",')

    # 同じファイル名で保存
    with open(f"{file_save}{file}", mode="w", encoding="cp932") as f:
        f.write(data_lines)