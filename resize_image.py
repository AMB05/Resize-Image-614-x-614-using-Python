from PIL import Image
import os

# Direktori tempat gambar-gambar berada
input_directory = 'Dataset Ikan Kembung'
output_directory = 'Dataset_Ikan_Kembung_RS'

# Membuat direktori output jika belum ada
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Ukuran gambar yang diinginkan
new_size = (614, 614)

# Iterasi untuk setiap file di direktori input
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')):
        img_path = os.path.join(input_directory, filename)
        img = Image.open(img_path)
        
        # Resize gambar menggunakan LANCZOS (pengganti ANTIALIAS)
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Simpan gambar hasil resize ke direktori output
        img_resized.save(os.path.join(output_directory, filename))

print("Resize selesai untuk semua gambar.")
