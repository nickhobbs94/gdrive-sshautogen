#!/usr/bin/python3
import gspread
import sys
from oauth2client.service_account import ServiceAccountCredentials

# connect to the google sheet and get the contents of the SSH Keys sheet
def getKeys():
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('homenetwork_secret.json', scope)
	client = gspread.authorize(creds)

	sheet = client.open('Home Network').worksheet('SSH Keys')

	keys = sheet.get_all_records()
	return keys

# generate authorized_keys file from column name
def genAuthKeys(colName=""):
	allKeys = getKeys()
	for key in allKeys:
		if colName == "":
			print(key['Key'])
		elif key[colName] == 'TRUE':
			print(key['Key'])

if __name__ == "__main__":
	if len(sys.argv) == 1:
		genAuthKeys()
	else:
		genAuthKeys(sys.argv[1])
