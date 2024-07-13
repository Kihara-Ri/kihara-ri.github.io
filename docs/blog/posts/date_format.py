import os
import re

def process_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding = 'utf-8') as file:
        for line in lines:
            match = re.match(r"^date: '(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}'$", line.strip())
            if match:
                new_line = f"date: {match.group(1)}\n"
                file.write(new_line)
            else:
                file.write(line)

def process_dir(dir):
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)
                print(f"Processed file: {file_path}")

if __name__ == "__main__":
    dir = os.getcwd()
    process_dir(dir)
    print("Proces completed.")
