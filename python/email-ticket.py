import base64
import os
import mimetypes
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set the path to your credentials file
CREDS_PATH = 'path/to/credentials.json'
TOKEN_PATH = 'path/to/token.json'

# The scope for the Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_message(sender, to, subject, message_text, file_path):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    main_type, sub_type = content_type.split('/', 1)
    with open(file_path, 'rb') as file:
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(file.read())

    filename = os.path.basename(file_path)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw_message}

def send_message(service, sender, to, subject, body, attachment_path=None):
    message = create_message(sender, to, subject, body, attachment_path)
    try:
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Message sent. Message Id: {sent_message['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        CREDS_PATH, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(TOKEN_PATH, 'w') as token:
        token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    sender = 'your.email@gmail.com'
    to = 'recipient.email@gmail.com'
    subject = 'Test Email with Attachment'
    body = 'This is the body of the email.'

    attachment_path = 'path/to/your/attachment.txt'

    send_message(service, sender, to, subject, body, attachment_path)

if __name__ == '__main__':
    main()

