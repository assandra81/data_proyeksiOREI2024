@echo off

rem Tentukan path ke file yang akan diunggah
set file_path=C:\MATLAB\OREI_Indramayu2024\data_proyeksi\data_proyeksiOREI2024\cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m_thetao_108.00E-111.00E_7.00S-3.50S_0.49m_2024-05-14-2024-05-17.nc

rem Salin file ke repositori GitHub
copy "%file_path%" "C:\MATLAB\OREI_Indramayu2024\data_proyeksi\data_proyeksiOREI2024\"

rem Pindah ke direktori repositori GitHub
cd /D "C:\MATLAB\OREI_Indramayu2024\data_proyeksi\data_proyeksiOREI2024\"

rem Tambahkan file ke repositori menggunakan Git
git add .

rem Buat commit
git commit -m "tes_suhu.nc"

rem Lakukan push ke repositori
git push