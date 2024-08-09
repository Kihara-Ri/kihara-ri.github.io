import os

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if not (
              (line.strip().startswith("updated:")) | 
              (line.strip().startswith("categories:")) | 
              (line.strip().startswith("description:")) | 
              (line.strip().startswith("keywords:")) | 
              (line.strip().startswith("top_img:")) | 
              (line.strip().startswith("cover:")) | 
              (line.strip().startswith("copyright:")) | 
              (line.strip().startswith("mathjax:")) | 
              (line.strip().startswith("swiper_index:")) | 
              (line.strip().startswith("abbrlink:")) | 
              (line.strip().startswith("main_color:"))
                    ):
                file.write(line)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)
                print(f"Processed file: {file_path}")

if __name__ == "__main__":
    process_directory(os.getcwd())
    print("Processing completed.")

