import os

# File organizer

print(" ===== File Organizer Automation. =====")
target_path = r"C:\Users\LENOVO\Downloads"

file_type = {
    'Images' : ['.jpg','.png','.jpeg'],
    'Videos' : ['.mp4','.mvk'],
    'Documents' : ['.pdf','.txt','.docx','.xlsx'],
    'Audio' : ['.mp3','.wav'],
    'Presentations' : ['.ppt', '.pptx']
}

for file in os.listdir(target_path):
    file_path = os.path.join(target_path,file)
    
    if os.path.isfile(file_path):
        _,extension = os.path.splitext(file)
        
    for folder_name,extensions in file_type.items():
        if extension.lower() in extensions:
            subfolder_path = os.path.join(target_path,folder_name)
            
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
            
            os.rename(file_path,os.path.join(subfolder_path,file))
            
print("File Organize Successfully.")




# import os

# downloads_path = r"C:\Users\LENOVO\Downloads"
# document_path = os.path.join(downloads_path,"Documents")
# presentation_path = os.path.join(downloads_path,"Presentations")

# if not os.path.exists(presentation_path):
#     os.makedirs(presentation_path)
    
# if os.path.exists(document_path):
#     for file in os.listdir(document_path):
#         file_path = os.path.join(document_path,file)
        
#         if os.path.isfile(file_path):
#             _,extension = os.path.splitext(file)
            
#             if extension.lower() in ['.ppt','.pptx']:
#                 destination_path = downloads_path
                
#                 os.rename(file_path,destination_path)

# print("SuccessFully Extract PPT files")




# import os

# downloads_path = r"C:\Users\LENOVO\Downloads"

# # सिर्फ उन फोल्डर्स के नाम जहाँ PPT फाइलें हो सकती हैं
# folders_to_check = ['Presentations', 'Documents']

# for folder_name in folders_to_check:
#     folder_path = os.path.join(downloads_path, folder_name)
    
#     # चेक करें कि फोल्डर कंप्यूटर में मौजूद है या नहीं
#     if os.path.exists(folder_path):
#         for file in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file)
            
#             if os.path.isfile(file_path):
#                 _, extension = os.path.splitext(file)
                
#                 # सिर्फ .ppt और .pptx फाइलों को ही बाहर निकालें
#                 if extension.lower() in ['.ppt', '.pptx']:
#                     destination_path = os.path.join(downloads_path, file)
                    
#                     # फाइल को मुख्य Downloads फोल्डर में वापस भेजें
#                     os.rename(file_path, destination_path)
#                     print(f"Moved Back to Downloads: {file}")

# print("\nSuccessfully moved only PPT and PPTX files back to Downloads!")
