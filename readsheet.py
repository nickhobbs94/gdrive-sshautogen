#!/usr/bin/python3
import gspread
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
		if key['Allow RPi'] == 'TRUE':
			print(key['Key'])
