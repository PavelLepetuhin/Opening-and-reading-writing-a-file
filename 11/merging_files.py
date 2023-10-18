import os


folder_path = os.path.join(os.path.dirname(__file__))


files= []
extension = ".txt"

for root, dirs, file in os.walk(folder_path):
    for f in file:
        if f.endswith(extension):
            files.append(f)


file_contents = []


for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)


sorted_files = sorted(files, key=lambda x: file_contents[files.index(x)].count("\n"))


result_path = os.path.join(folder_path, "result.txt")
with open(result_path, "w", encoding="utf-8") as result_file:
    for file_name in sorted_files:
        content = file_contents[files.index(file_name)]
        backslash = "\n"
        result_file.write(f"\n{file_name}\n")
        result_file.write(f"строк: {content.count(backslash) + 1}\n")
        result_file.write(content)