import ipywidgets as widgets
from IPython.display import display, clear_output

# Widget untuk memasukkan nama file output (tampil setelah file di-upload)
output_name_input = widgets.Text(
    description='Output Name:',
    placeholder='Enter output file name without extension',
    layout=widgets.Layout(width='500px')  # Menetapkan lebar agar teks tidak terpotong
)
output_name_box = widgets.VBox([output_name_input])
output_name_box.layout.display = 'none'

# Tombol untuk mengonfirmasi nama file output (tampil setelah output name diisi)
confirm_button = widgets.Button(description="Confirm Output Name")
confirm_button.layout.display = 'none'

# Tombol untuk menjalankan FaceSwap (tampil setelah nama file output dikonfirmasi)
run_button = widgets.Button(description="Run FaceSwap")
run_button.layout.display = 'none'

# Output widget untuk menampilkan hasil
output = widgets.Output()

# Variable to store output name
output_name = None

# Fungsi untuk mengonfirmasi nama file output
def on_confirm_button_clicked(b):
    global output_name
    output_name = output_name_input.value
    with output:
        clear_output()
        if output_name:
            print(f"Output file name confirmed: {output_name}.png")
            run_button.layout.display = 'flex'

# Menghubungkan fungsi dengan tombol konfirmasi
confirm_button.on_click(on_confirm_button_clicked)

# Menampilkan widget untuk nama file output dan tombol konfirmasi
display(output_name_box, confirm_button)
