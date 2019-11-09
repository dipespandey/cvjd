from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # # Call the Drive v3 API
    # results = service.files().list(
    #     pageSize=1000, fields="nextPageToken, files(id, name)").execute()
    # items = results.get('files', [])
    # all_files = []
    # if not items:
    #     print('No files found.')
    # else:
    #     print('Files:')
    #     for item in items:
    #         print(u'{0} ({1})'.format(item['name'], item['id']))
    #         all_files.append((item['name'], item['id']))
    
    # return all_files
    page_token = None
    all_files = []
    while True:
        response = service.files().list(pageSize=1000,q="'184b0EFkuuI1nbeXQZACxQEcJlwzzPyvh' in parents",pageToken = page_token, fields="nextPageToken, files(id, name)").execute()
        items = response.get('files', [])
        if not items:
            print('No files found')
        else:
            for item in items:
                # print('Found file: %s (%s)' % (item['name'], item['id']))
                all_files.append((item['name'], item['id']))
            all_files = list(set(all_files))
            print(len(all_files))            
            page_token = response.get('nextPageToken', None)
            print('next page token', page_token)
        if page_token is None:
            break
    return all_files

if __name__ == '__main__':
    all_files = main()
