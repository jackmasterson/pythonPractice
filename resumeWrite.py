#! /usr/bin/env python3
#resumeWrite.py - gather data and put into a JSON to be read in resumePrac.py
import pprint, subprocess

resInfo = {
		'Name': '',
		'Role': '',
		'Summary': '', 
		'Work':{}, 
		'Extra':{},
		'Email': '',
		'Phone': '', 
		'Edu':
			{
				'School': {},
				'Dates': {}, 
				'DegreeType': {}, 
				'DegreeField': {}, 
				'GPA': {}, 
				'Honors': {}
			}
	}

print('What is your professional name?')
name = input()
resInfo['Name'] = name

print('What is your current role? ie Web Developer, '+
	'Copywriter, Publicist, etc.')
role = input()
resInfo['Role'] = role

print('What is your email?')
email = input()
resInfo['Email'] = email

print('What is your phone number?')
phone = input()
resInfo['Phone'] = phone

print('Type a two-to-three sentence blurb about what you\'re doing '+
	' and what you\'re looking for')
summary = input()
resInfo['Summary'] = summary


print('Now tell us a little about your education.')
while True:
	print('What\'s the name of the school you went to?')
	school = input()
	resInfo['Edu']['School'] = school

	print('What years did you attend?')
	datesAtt = input()
	resInfo['Edu']['Dates'] = datesAtt

	print('Did you obtain a B.S., B.A., or something else? '+
		'If something else, please enter it.')
	degType = input()
	resInfo['Edu']['DegreeType'] = degType

	print('What field was your degree in?')
	degField = input()
	resInfo['Edu']['DegreeField'] = degField

	print('What was your GPA?')
	gpa = input()
	resInfo['Edu']['GPA'] = gpa

	print('Did you graudate with any honors (ie cum laude, magna cum laude '+
			', etc.)? If so, enter them.')
	honors = input()
	resInfo['Edu']['Honors'] = honors

	print('Enter \'done\' if finished, enter \'add\' to add more schooling.')
	ans = input()
	if ans == 'done':
		break
	elif ans == 'add':
		continue

while True:
	print('')

	print('Type \'Work\' to add Work Experience, '+
		'\'Extra\' to add Extracurricular info. Type \'done\' if finished entering all of it.')

	nextSect = input()

	if nextSect == 'done':
		break
	else:

		while True:

			print('Add the name of the company or organization to begin'+
				'; enter \'done\' to quit.')
			lastJob = input()
			
			if lastJob == 'done':
				break
			else:
				resInfo[nextSect][lastJob] = {'title': '', 'skills' : [], 'dates': ''}

				skills = resInfo[nextSect][lastJob]['skills']
				dates = resInfo[nextSect][lastJob]['dates']
				
				print('What did you learn there? Add skills one at '+
				'a time by hitting enter. Enter \'done\' when finished.')		

				while True:

					skill = input()
					if skill == 'done':
						break
					else:
						skills.append(skill)
					continue

				print('Months/Years worked there? Type done to finish')

				date = input()
				if date == 'done':
					break
				else:
					dates = date

				print('What was your title?')
				title = input()
				resInfo[nextSect][lastJob]['title'] = title
				



print('Writing Data File...')
resultFile = open('resumeData.py', 'w')
resultFile.write('allData = '+pprint.pformat(resInfo))
resultFile.close()
print('Done writing data file.')
subprocess.call('./resumePrac.py')




