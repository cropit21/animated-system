import ipywidgets as widgets
from IPython.display import display, clear_output

# Widget untuk upload source image
source_upload = widgets.FileUpload(accept='image/*', multiple=False)
source_label = widgets.Label("Upload Source Image:")
source_vbox = widgets.VBox([source_label, source_upload])

# Widget untuk upload multiple target images
target_upload = widgets.FileUpload(accept='image/*', multiple=True)
target_label = widgets.Label("Upload Target Images:")
target_vbox = widgets.VBox([target_label, target_upload])

# Output widget untuk menampilkan hasil
output = widgets.Output()

# Fungsi untuk menampilkan opsi output name setelah file di-upload
def on_files_uploaded(change):
    if source_upload.value and target_upload.value:
        output_name_box.layout.display = 'flex'
        confirm_button.layout.display = 'flex'
    with output:
        clear_output()
        print("Files uploaded. Please enter and confirm the output file name.")

# Menghubungkan fungsi dengan widget upload
source_upload.observe(on_files_uploaded, names='value')
target_upload.observe(on_files_uploaded, names='value')

# Menampilkan widget upload
display(source_vbox, target_vbox)
