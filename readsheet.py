#!/usr/bin/python3
import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

def getKeys():
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('homenetwork_secret.json', scope)
	client = gspread.authorize(creds)

	sheet = client.open('Home Network').worksheet('SSH Keys')

	keys = sheet.get_all_records()
	return keys

if __name__ == "__main__":
	allKeys = getKeys()
	for key in allKeys:
		if len(sys.argv) == 1:
			print(key['Key'])
		elif key[sys.argv[1]] == 'TRUE':
			print(key['Key'])
