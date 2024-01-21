from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create GoogleDrive instance
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and automatically handles authentication.
drive = GoogleDrive(gauth)

# Local file path
local_file_path = "/tmp/client_upload_test.txt"

# Google Drive folder ID where you want to copy the file
folder_id = "1mynH5r2dt-xp7453yqguku0ddVJta8Dq"

# Create a GoogleDriveFile instance
file_to_upload = drive.CreateFile({'title': 'client_upload_test.txt', 'parents': [{'id': folder_id}]})

# Set content of the file
file_to_upload.SetContentFile(local_file_path)

# Upload the file
file_to_upload.Upload()

print("File uploaded to Google Drive.")
