
import os

# 画像があるフォルダ
folder = "./images"
files = sorted(os.listdir(folder))

# 拡張子を確認しつつ連番でリネーム
for i, filename in enumerate(files):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        new_name = f"photo{str(i+1).zfill(3)}.jpg"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        print(f"{filename} → {new_name}")
