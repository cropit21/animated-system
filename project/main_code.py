import os
import requests
import subprocess
import ipywidgets as widgets
from IPython.display import display

# URL GitHub untuk folder kode
repo_url = 'https://github.com/username/repository-name/raw/main/folder-name/'

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

# Menampilkan file yang diunduh
print("Files downloaded:")
print(os.listdir('/content/code'))

# Menyiapkan folder sementara dan hasil
os.makedirs('/content/temp', exist_ok=True)
os.makedirs('/content/hasil', exist_ok=True)

# Menjalankan file kode secara berurutan
script_paths = [
    '/content/code/upload_code.py',
    '/content/code/output_name_code.py',
    '/content/code/run_faceswap_code.py'
]

for script_path in script_paths:
    print(f"Running {script_path}...")
    subprocess.run(['python', script_path], check=True)

# Notifikasi selesai
print("All scripts have been executed successfully.")

# Menampilkan widget untuk memastikan semuanya berjalan
with widgets.Output() as output:
    display(widgets.Label("All scripts have been executed successfully."))
