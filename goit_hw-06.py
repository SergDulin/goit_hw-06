import sys
import os
from pathlib import Path


# Словник з категоріями файлів та їх розширеннями
CATEGORIES = {
    "Audio": [".mp3", ".aiff", ".wav", ".aac", ".flac"],
    "Documents": [".docx", ".doc", ".txt", ".pdf", ".xls", ".xlsx", ".pptx", ".rtf"],
    "Video": [".avi", ".mp4", ".mov", ".mkv", ".mpeg"],
    "Image": [".jpeg", ".png", ".pcd", ".jpg", ".svg", ".tiff", ".raw", ".gif", ".bmp"],
    "Archive": [".zip", ".7-zip", ".7zip", ".rar", ".gz", ".tar"],
    "Book": [".fb2", ".mobi"]
}

# Функція для нормалізації імені файлу
def normalize(name):
    
    return name

# Функція для переміщення файлу у відповідну категорію
def move_file(file: Path, root_dir: Path, category: str) -> None:
    

# Функція для визначення категорії файлу за його розширенням
def get_category(file: Path) -> str:
    

# Функція для сортування файлів у кореневій папці
def sort_folder(path: Path) -> None:
    

# Функція для видалення порожніх папок
def delete_empty_folders(path: Path) -> None:
    

# Функція для розпакування архівів
def unpack_archives(path: Path) -> None:
    

# Основна функція
def main():
   

# Точка входу
if __name__ == "__main__":
    
