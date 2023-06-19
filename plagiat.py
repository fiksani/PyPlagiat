import json
import os
import sys
import PyPDF2

from algorithms import calculate_similarity


# check if any arguments of path file
if len(sys.argv) < 2:
    print("Please provide a path to the submitted document.")
    exit(1)

# Path to the folder containing the PDF files in the internal database
folder_path = os.path.join(os.getcwd(), 'internal_database')

# Create a list to store the preprocessed text and metadata
documents = []

# check if any documents.json file or any option argument --rebuild
if not os.path.exists('database.json') or '--rebuild' in sys.argv:
    # Iterate over the PDF files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
                # Preprocess the text (clean, lowercase, etc.) if necessary
                documents.append({'text': text, 'file_name': file_name})

    # cache documents to file
    with open('database.json', 'w') as file:
        json.dump(documents, file)
else:
    # load documents from file
    with open('database.json', 'r') as file:
        documents = json.load(file)

# Compare the submitted document against the stored documents Get from args
submitted_document = sys.argv[1]
threshold = 0.6
with open(submitted_document, 'rb') as file:
    submitted_text = ''
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        submitted_text += page.extract_text()
    # Preprocess the submitted text (clean, lowercase, etc.) if necessary

    # Compare the submitted text against each stored document
    for document in documents:
        similarity_score = calculate_similarity(submitted_text, document['text'])
        if similarity_score > threshold:
            print(f"Plagiarism detected in submitted document {submitted_document}. "
                  f"Similarity score: {similarity_score:.2f}. "
                  f"Matched with document: {document['file_name']}.")
            exit(0)
        else:
            print(f"No plagiarism detected in submitted document {submitted_document} compared to {document['file_name']}. "
                  f"Similarity score: {similarity_score:.2f}.")