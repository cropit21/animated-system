import os
import requests
import subprocess

# URL GitHub untuk folder kode
repo_url = 'https://github.com/cropit21/animated-system/raw/main/project/'

# Nama file yang akan diunduh
files = ['upload_code.py', 'output_name_code.py', 'run_faceswap_code.py']

# Membuat folder untuk menyimpan file kode
os.makedirs('/content/code', exist_ok=True)

# Mengunduh file dari GitHub
for file_name in files:
    url = repo_url + file_name
    response = requests.get(url)
    with open(f'/content/code/{file_name}', 'wb') as file:
        file.write(response.content)

print("Files downloaded:")
print(os.listdir('/content/code'))

# Menyiapkan folder sementara dan hasil
os.makedirs('/content/temp', exist_ok=True)
os.makedirs('/content/hasil', exist_ok=True)

# Menjalankan file unduhan
script_paths = [
    '/content/code/upload_code.py',
    '/content/code/output_name_code.py',
    '/content/roop/run.py'  # Menjalankan run.py yang sudah ada di /content/roop
]

for script_path in script_paths:
    print(f"Running {script_path}...")
    subprocess.run(['python3', script_path], check=True)

print("All scripts have been executed.")
