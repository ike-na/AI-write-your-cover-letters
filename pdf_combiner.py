import os
from PyPDF2 import PdfMerger

folder_path = 'training'
output_filename = 'combined.pdf'
output_path = os.path.join(folder_path, output_filename)


if os.path.exists(output_path):
    user_choice = input(f"'{output_filename}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
    if user_choice == 'y':


        try:
            os.remove(output_path)
            print(f"Deleted existing '{output_filename}'.")
        except Exception as e:
            print(f"Error deleting '{output_filename}': {e}")
            exit()

        pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(pdf)

        with open(output_path, 'wb') as output_file:
            merger.write(output_file)

        print(f'Combined PDF saved as {output_path}')

    if user_choice == 'n':
        print("Exiting without combining PDFs.")
        exit()

    elif user_choice != 'y' and user_choice != 'n':
        print("Invalid input. Exiting without combining PDFs.")
        exit()


else:
    pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f'Combined PDF saved as {output_path}')
