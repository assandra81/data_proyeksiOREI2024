import os
import shutil

# Path folder tempat Anda ingin menyimpan file
folder_path = "C:/MATLAB/OREI_Indramayu2024/data_proyeksi/data_proyeksiOREI2024"


# Fungsi untuk menghapus file lama
def remove_old_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and not file.endswith((".bat", ".py")):
            os.remove(file_path)

# Fungsi untuk mengecek jika ada file baru
def check_for_new_file(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        if not file.endswith((".bat", ".py")):
            print(f"File baru ditemukan: {file}")
            return True
    return False

if __name__ == "__main__":
    # Cek jika ada file baru
    if check_for_new_file(folder_path):
        # Jika ada, hapus file lama
        remove_old_files(folder_path)
