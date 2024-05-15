from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autentikasi dengan Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Proses autentikasi menggunakan web browser lokal

# Buat koneksi ke Google Drive
drive = GoogleDrive(gauth)

# Path file yang akan diunggah
file_path = "C:/path/to/your/file.txt"

# Buat metadata file
file_metadata = {'title': 'file.txt'}

# Unggah file
file = drive.CreateFile(file_metadata)
file.SetContentFile(file_path)
file.Upload()
print('File berhasil diunggah: %s' % file['title'])