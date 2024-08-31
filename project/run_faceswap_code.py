import ipywidgets as widgets
from IPython.display import display, clear_output
import subprocess
import os
import shutil

# Menyiapkan folder sementara dan hasil
os.makedirs('/content/temp', exist_ok=True)
os.makedirs('/content/hasil', exist_ok=True)

# Output widget untuk menampilkan hasil
output = widgets.Output()

# Fungsi untuk menjalankan FaceSwap
def on_run_button_clicked(b):
    global output_name
    with output:
        clear_output()
        if not source_upload.value or not target_upload.value:
            print("Please upload both source image and target images.")
            return
        if not output_name:
            print("Please confirm the output file name.")
            return
        
        # Save uploaded source file
        source_filename = list(source_upload.value.keys())[0]
        source_path = f"/content/temp/{source_filename}"
        
        with open(source_path, 'wb') as file:
            file.write(source_upload.value[source_filename]['content'])
        
        # Save uploaded target files
        target_filenames = [name for name in target_upload.value.keys()]
        for filename in target_filenames:
            target_path = f"/content/temp/{filename}"
            with open(target_path, 'wb') as file:
                file.write(target_upload.value[filename]['content'])
        
        # Run FaceSwap
        target_files = " ".join([f"/content/temp/{name}" for name in target_filenames])
        command = f"python run.py -s \"{source_path}\" -t {target_files} -o \"/content/hasil/{output_name}.png\" --keep-frames --keep-fps --temp-frame-quality 1 --output-video-quality 1 --execution-provider cpu --frame-processor face_swapper face_enhancer"
        subprocess.run(command, shell=True)
        
        # Hapus folder sementara
        shutil.rmtree('/content/temp')
        
        # Menampilkan notifikasi selesai
        print("Processing complete. Output saved as:", f"/content/hasil/{output_name}.png")
        clear_output(wait=True)
        print("Selesai")

# Menghubungkan fungsi dengan tombol run
run_button.on_click(on_run_button_clicked)

# Menampilkan tombol run FaceSwap
display(run_button, output)
