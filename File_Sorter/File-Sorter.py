# Create a dict that contains file types and extensions of that file type.
# Check for the files in the fixed downloads folder.
# Construct a for loop for iterating over every file in that folder.
# Split the filename and extensions of that folder.
# Check if the extension matches the file type and extensions dict.
# Store the files into the matching folder and if there is no folder for the given extension, create a new folder.

'''
Imports:
--From the os library:-
----listdir - Lists every file and directories in a folder.
----path - I don't need path but I need the path.join function, it joines two things, and I also need the path.isdir function which checks if the path is a folder or not.
----makedirs - It makes directories or folders inside a given folder, we use makedirs instead of makedir to not get an error when the file already exists.

--From the shutil Library:-
----move - To move the files into the respective folders safely.
'''
from os import listdir, path, makedirs
from shutil import move

# Declared a variable containing keyword and list inside a dict.
filetypes = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico", ".webp", ".tiff"],
    "video": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".m4v"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".aiff"],
    "document": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".odt"],
    "archive": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso"],
    "code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".php", ".rb", ".go"],
    "executable": [".exe", ".msi", ".app", ".deb", ".sh", ".bat", ".cmd"],
}

# The common name that my directory has so I declared it as a global variable.
directory = r"C:\Users\nived\Downloads"

# main function which just calls the store_files function and does nothing else.
# I did not implement the store_files() function here coz i might need to call that function in other files.
def main():
    store_files()


# A check_files function to check every folder or file inside the given "Downloads" folder and storing it as splitted (filename, extension) and joined (filename + extension) and return the joined name, splitted name inside a dict inside a list.
def check_files() -> str:
    # A variable of a list which will be used to store the dicts of joined and splitted files that are not folders.
    all_files = []
    # Declaring the splitted_name and joined_name variables before the for loop because else it will just rewrite itself in every for loop iteration.
    splitted_name = None
    joined_name =   None

    # A loop that gives every file and folder inside the given directory.
    for files in listdir(directory):
        # The full_path is the same as the joined name, but it only contains the joined name of the current iterating file or folder.
        full_path = path.join(directory, files)

        # If the full_path is considered as a directory or a folder, then skip.
        if path.isdir(full_path):
            continue

        # Else if the path is a file,
        else:
            # Give the splitted and joined names of the files and append them onto the above declared empty list as a dict.
            splitted_name = path.splitext(files)
            joined_name = path.join(directory, files)
            all_files.append({"splitted" :splitted_name, "joined": joined_name})
    # The return function is in the check_files function so that the value doesn't re-write itself in every iteration.
    return all_files
    

# A function that stores files inside their respective folder.
def store_files():
    # Implement the check_files() function inside this function
    checked_files = check_files()

    # A for loop that checks for files inside the return of check_files() function, and the joined filename is stored as a variable named "ext".
    for files in checked_files:
        ext = files["splitted"][1]

        # A line of if and elif statements which state the filetypes stated in the filetypes dict.
        # This if function condition deals with the filetype "image".
        if ext in filetypes["image"]:
            # To avoid errors we use try and except,
            try:
                # makedirs function instead of makedir function to get rid of FileExistsError,
                # Makes a directory or a folder to store the file inside the respective folder,
                # It stores the directory with \Filetype added to create a new folder in the given directory named the respective filetype.
                makedirs(directory + r"\Images", exist_ok=True)
                # Moves the file which is the joined_filename to the joined path of given directory and the filetype name.
                move(files["joined"], path.join(directory, "Images"))
                # Print statement to indicate which function moved where.
                print(f"Moved {files['splitted'][0]} into Images folder")
            # If accidentally there is a FileExistsError even when using makedirs function print the given statement.
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "archive".
        elif ext in filetypes["archive"]:
            try:
                makedirs(directory + r"\Archives", exist_ok=True)
                move(files["joined"], path.join(directory, "Archives"))
                print(f"Moved {files['splitted'][0]} into Archives folder")
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "audio".
        elif ext in filetypes["audio"]:
            try:
                makedirs(directory + r"\Audios", exist_ok=True)
                move(files["joined"], path.join(directory, "Audios"))
                print(f"Moved {files['splitted'][0]} into Audios folder")
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "code".
        elif ext in filetypes["code"]:
            try:
                makedirs(directory + r"\Codes", exist_ok=True)
                move(files["joined"], path.join(directory, "Codes"))
                print(f"Moved {files['splitted'][0]} into Codes Folder")
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "document".
        elif ext in filetypes["document"]:
            try:
                makedirs(directory + r"\Documents", exist_ok=True)
                move(files["joined"], path.join(directory, "Documents"))
                print(f"Moved {files['splitted'][0]} into Documents folder")
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "executable".
        elif ext in filetypes["executable"]:
            try:
                makedirs(directory + r"\Executables", exist_ok=True)
                move(files["joined"], path.join(directory, "Executables"))
                print(f"Moved {files['splitted'][0]} into Executables folder")
            except FileExistsError:
                print("File already exists")

        # This elif function condition deals with the filetype "video".
        elif ext in filetypes["video"]:
            try:
                makedirs(directory + r"\Videos", exist_ok=True)
                move(files["joined"], path.join(directory, "Videos"))
                print(f"Moved {files['splitted'][0]} into Videos folder")
            except FileExistsError:
                print("File already exists")

        # If there is no match in all these filetypes then save the file into a miscellanious folder.
        else:
            try:
                makedirs(directory + r"\Michellanious", exist_ok=True)
                move(files["joined"], path.join(directory, "Michellanious"))
                print(f"Moved {files['splitted'][0]} into Michellanious folder")
            except FileExistsError:
                print("File already exists")

# An amazing convention to use in every code if you do not want to execute the code with every impport usage as well.
if __name__ == "__main__":
    main()