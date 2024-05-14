import subprocess

# Command untuk menjalankan skrip Python pertama
command1 = "python download_CMEM_T.py"
# Command untuk menjalankan skrip Python kedua
command2 = "python download_CMEM_S.py"
# Command untuk menjalankan skrip Python ketiga
command3 = "python download_CMEM_Chl.py"

# Jalankan skrip pertama dan kirimkan input "y"
process1 = subprocess.Popen(command1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output1, error1 = process1.communicate(input="y\n")

# Jalankan skrip kedua dan kirimkan input "y"
process2 = subprocess.Popen(command2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output2, error2 = process2.communicate(input="y\n")

# Jalankan skrip ketiga dan kirimkan input "y"
process3 = subprocess.Popen(command3, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output3, error3 = process3.communicate(input="y\n")

# Cek output atau error jika diperlukan
print("Output 1:", output1)
print("Error 1:", error1)

print("Output 2:", output2)
print("Error 2:", error2)

print("Output 3:", output3)
print("Error 3:", error3)
