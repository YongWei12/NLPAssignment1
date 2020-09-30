'''
Script for extracting text from pdf,
then storing extracted text into txt files of the same name.
Note that txt files still need to be cleaned manually.
'''
from pdfminer.high_level import extract_text
import os


# make sure we are in the right directory
os.chdir(os.path.dirname(os.path.dirname(__file__)))
print(f'current dir: {os.getcwd()}')

# source directory structure:
# data_pdf/
# ----psychology/
# ----sigbovik/
source_dir_path = os.path.join(os.getcwd(), 'data_pdf/')

# destination directory structure:
# data_txt/
# ----psychology/
# ----sigbovik/
dest_dir_path = os.path.join(os.getcwd(), 'data_txt/')

for subdir in os.listdir(source_dir_path):
    source_subdir_path = os.path.join(source_dir_path, subdir)
    dest_subdir_path = os.path.join(dest_dir_path, subdir)

    # make sure directory exists before wirting to it
    os.makedirs(dest_subdir_path, exist_ok=True)

    for pdf in os.listdir(source_subdir_path):
        if not pdf.endswith('.pdf'):  # make sure we are actually dealing with pdfs
            continue

        print(f'working on {pdf}')

        pdf_path = os.path.join(source_subdir_path, pdf)
        txt_path = os.path.join(dest_subdir_path, pdf.replace('.pdf', '.txt'))

        text = extract_text(pdf_path)

        with open(txt_path, mode='w') as txt_file:
            txt_file.write(text)

print('done')
