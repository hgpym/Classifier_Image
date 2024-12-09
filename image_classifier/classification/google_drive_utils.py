from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(file_path, file_name):
    # Настройка аутентификации
    credentials = ...  # Добавьте код для аутентификации
    drive_service = build('drive', 'v3', credentials=credentials)
    media = MediaFileUpload(file_path)
    drive_service.files().create(
        body={'name': file_name},
        media_body=media
    ).execute()
