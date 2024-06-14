import PyPDF2
import os

def pdf_to_txt(pdf_path, txt_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text() or ""
                text += page_text + "\n\n\n"

        with open(txt_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        print(f"Text successfully extracted and saved to '{txt_path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = 'training'
pdf_filename = 'combined.pdf'  # Replace with your PDF file name
txt_filename = 'output.txt'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)    

if not os.path.exists(os.path.join(folder_path, pdf_filename)):
    print(f"PDF file '{pdf_filename}' not found in '{folder_path}'.")
    exit()

if os.path.exists(os.path.join(folder_path, txt_filename)):
    print(f"Text file '{txt_filename}' already exists in '{folder_path}'.")
    choice = input("Do you want to overwrite it? (y/n)")
    if choice.lower() == 'y':
        try:
            os.remove(os.path.join(folder_path, txt_filename))
            print(f"Deleted existing '{txt_filename}'.")
        except Exception as e:
            print(f"Error deleting '{txt_filename}': {e}")
            exit()
    elif choice.lower() == 'n':
        print("Exiting without overwriting text file.")
        exit()
    else:
        print("Invalid input. Exiting without overwriting text file.")
        exit()
        
pdf_path = os.path.join(folder_path, pdf_filename)
txt_path = os.path.join(folder_path, txt_filename)

pdf_to_txt(pdf_path, txt_path)
