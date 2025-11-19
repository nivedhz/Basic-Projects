import os
import shutil

filetypes = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico", ".webp", ".tiff"],
    "video": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".m4v"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff"],
    "document": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".odt"],
    "archive": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"],
    "code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".php", ".rb", ".go"],
    "executable": [".exe", ".msi", ".app", ".deb", ".sh", ".bat", ".cmd"],
    "michellanious": [".msix", ".VSIXPackage"]
}

directory = r"C:\Users\nived\Downloads"

def main():
    store_files()



def check_files() -> str:
    all_files = []
    splitted_name = None
    joined_name =   None

    for files in os.listdir(directory):
        full_path = os.path.join(directory, files)

        if os.path.isdir(full_path):
            continue
        else:
            splitted_name = os.path.splitext(files)
            joined_name = os.path.join(directory, files)
            all_files.append({"splitted" :splitted_name, "joined": joined_name})
    return all_files
    

def store_files():
    checked_files = check_files()
    for files in checked_files:
        ext = files["splitted"][1]
        if ext in filetypes["image"]:
            try:
                os.makedirs(directory + r"\Images", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Images"))
                print(f"Moved {files['splitted'][0]} into Images folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["archive"]:
            try:
                os.makedirs(directory + r"\Archives", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Archives"))
                print(f"Moved {files['splitted'][0]} into Archives folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["audio"]:
            try:
                os.makedirs(directory + r"\Audios", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Audios"))
                print(f"Moved {files['splitted'][0]} into Audios folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["code"]:
            try:
                os.makedirs(directory + r"\Codes", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Codes"))
                print(f"Moved {files['splitted'][0]} into Codes Folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["document"]:
            try:
                os.makedirs(directory + r"\Documents", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Documents"))
                print(f"Moved {files['splitted'][0]} into Documents folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["executable"]:
            try:
                os.makedirs(directory + r"\Executables", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Executables"))
                print(f"Moved {files['splitted'][0]} into Executables folder")
            except FileExistsError:
                print("File already exists")

        elif ext in filetypes["video"]:
            try:
                os.makedirs(directory + r"\Videos", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Videos"))
                print(f"Moved {files['splitted'][0]} into Videos folder")
            except FileExistsError:
                print("File already exists")

        else:
            try:
                os.makedirs(directory + r"\Michellanious", exist_ok=True)
                shutil.move(files["joined"], os.path.join(directory, "Michellanious"))
                print(f"Moved {files['splitted'][0]} into Michellanious folder")
            except FileExistsError:
                print("File already exists")
                
main()