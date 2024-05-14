from github import Github

# Mengganti 'username', 'password', dan 'repository_name' dengan informasi Anda
username = 'assandra81'
password = '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'
repository_name = 'data_proyeksiOREI2024'

# Membuat objek GitHub dengan kredensial
g = Github(username, password)

# Mendapatkan repositori yang ingin Anda unggah file-nya
repo = g.get_user().get_repo(repository_name)

# Menentukan path ke file yang ingin Anda unggah
file_path = 'C:/MATLAB/OREI_Indramayu2024/data_proyeksi/data_proyeksiOREI2024/cmems_mod_glo_bgc-bio_anfc_0.25deg_P1D-m_nppv_108.00E-111.00E_7.00S-3.50S_0.49m_2024-05-14-2024-05-17_(1).nc'

# Membaca konten file
with open(file_path, 'r') as file:
    content = file.read()

# Menentukan nama file di repositori GitHub
file_name = 'kloro.nc'

# Membuat atau mengunggah file ke repositori GitHub
repo.create_file(file_name, "Commit message", content)