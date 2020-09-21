# ID : 571367416044-uva9mnh75n5r36nc5tn5oia0csctts5f.apps.googleusercontent.com
# Secret : C0t96oDCYFiRbgB15rUDNOlQ

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try: 
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()	

if not creds or creds.invalid:
	print("make storage data files")
	flow = client.flow_from_clientsecrets('client_secret.json',SCOPES)
	creeds = tools.run_flow(flow,store,flags) \
		if flags else tools.run(flow, store)

DRIVE  = build('drive', 'v3', http = creds.authorize(Http()))

def upload(file):
	
	file_name = file
	metadata = {'name' : file_name,
				'mimeType': None
				}
	res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
	if res:
		print('Uploaded "%s" (%s)') % (file_name, res['mimeType'])

