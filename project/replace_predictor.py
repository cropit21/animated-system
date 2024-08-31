import os
import hashlib
from IPython.display import display, HTML, clear_output
import time

# URL dari file predictor.py yang baru di GitHub
url = 'https://raw.githubusercontent.com/cropit21/animated-chainsaw/main/predictor.py'

# Path file tujuan
destination_path = '/content/roop/roop/predictor.py'

# Fungsi untuk menghitung hash dari file (untuk memastikan file sudah terganti)
def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Fungsi untuk menggantikan file predictor.py dengan yang baru
def replace_predictor():
    # Tampilkan pesan sementara saat proses download
    display(HTML("""
    <div style=\"display: flex; justify-content: center; align-items: center; height: 100vh;\">
        <h2 style=\"font-size: 24px; color: #555;\">Mengunduh dan menggantikan file predictor.py...</h2>
    </div>
    """))

    # Beri jeda sejenak untuk memberi waktu animasi tampil
    time.sleep(2)

    # Hitung hash dari file predictor.py yang lama
    old_file_hash = calculate_file_hash(destination_path)
    
    # Unduh file predictor.py yang baru dari GitHub
    os.system(f'wget -O {destination_path} {url}')
    
    # Hitung hash dari file predictor.py yang baru
    new_file_hash = calculate_file_hash(destination_path)
    
    # Hapus output sebelumnya
    clear_output()

    # Tentukan pesan akhir dan warnanya
    message, color = ("File predictor.py berhasil diganti!", "#4CAF50") if new_file_hash != old_file_hash else ("File predictor.py tidak diganti, sudah sesuai.", "#FF5722")
    
    # Tampilkan pesan akhir dengan animasi CSS yang interaktif, ukuran kontainer disesuaikan
    display(HTML(f"""
    <div style=\"display: flex; justify-content: center; align-items: center; height: 50vh;\">
        <h2 class=\"animated-message\" style=\"text-align: center; font-size: 24px; color: {color};\">
            {message}
        </h2>
    </div>
    <style>
    .animated-message {{
        position: relative;
        animation: fadeInUp 1s ease-in-out, pulse 1.5s infinite;
    }}
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    </style>
    """))

# Tampilkan tombol konfirmasi sebelum memulai pengunduhan
display(HTML("""
<div style=\"display: flex; justify-content: center; align-items: center; height: 50vh;\">
    <div style=\"text-align: center;\">
        <h2>Konfirmasi untuk Mengganti File predictor.py</h2>
        <button id=\"download-btn\" class=\"btn\" style=\"background-color: #ddd; border: none; color: black; padding: 16px 32px; font-size: 16px; transition: 0.3s;\">
            Mulai Pengunduhan
        </button>
        <style>
        .btn:hover {{ background-color: #3e8e41; color: white; cursor: pointer; }}
        </style>
    </div>
</div>
<script>
document.getElementById('download-btn').onclick = function() {{
    google.colab.kernel.invokeFunction('notebook.replacePredictor', [], {});
}};
</script>
"""))

from google.colab import output
output.register_callback('notebook.replacePredictor', replace_predictor)
