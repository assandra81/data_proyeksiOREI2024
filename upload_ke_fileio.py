import os
import requests

# Token API File.io (ganti dengan token API Anda)
api_token = 'Z55TX6Y.095KZ5V-EPJ4SKG-M9FEV1X-AS7Y31W'

# Mendapatkan daftar file NetCDF dalam folder lokal
local_folder = 'C:/MATLAB/OREI_Indramayu2024/data_proyeksi/data_proyeksiOREI2024'
file_list = [file for file in os.listdir(local_folder) if file.endswith('.nc')]

# Mengunggah setiap file NetCDF ke akun File.io Anda
for filename in file_list:
    local_file_path = os.path.join(local_folder, filename)
    with open(local_file_path, 'rb') as file:
        response = requests.post('https://file.io/?token=' + api_token, files={'file': file})
    download_url = response.json()['link']
    print(f"File '{filename}' berhasil diunggah. URL: {download_url}")