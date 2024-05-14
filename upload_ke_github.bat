@echo off

rem Tentukan path ke file yang akan diunggah
set file_path=C:\KERJA\PRIMA\Kegiatan_Riset\2024\OREI2024\SAL2014_2023_OREI2024.nc

rem Salin file ke repositori GitHub
copy "%file_path%" "C:\MATLAB\OREI_Indramayu2024\data_proyeksi\data_proyeksiOREI2024\"

rem Pindah ke direktori repositori GitHub
cd /D "C:\MATLAB\OREI_Indramayu2024\data_proyeksi\data_proyeksiOREI2024\"

rem Tambahkan file ke repositori menggunakan Git
git add .

rem Buat commit
git commit -m "tes_sal.nc"

rem Lakukan push ke repositori
git push