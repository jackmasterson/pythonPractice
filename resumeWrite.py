#! /usr/bin/env python3
#resumeWrite.py - gather data and put into a JSON to be read in resumePrac.py
resInfo = {'Summary':{}, 'Work':{}, 'Extra':{}, 'Edu':{}}
print(resInfo)


while True:
	print('')

	print('Type \'Work\' to add Work Experience. Type '+
		'\'Extra\' to add Extracurriculars. ' +
		'Type \'done\' if finished entering both '+
		'work and extracurricular info.')

	nextSect = input()

	if nextSect == 'done':
		break
	else:

		while True:

			print('Add your next most recent item name, enter '+
				'\'done\' to quit.')
			lastJob = input()
			
			
			
			if lastJob == 'done':
				break
			else:
				resInfo[nextSect][lastJob] = {'skills' : [], 'dates': []}

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

				print('Months/Years worked there? done to finish')

				
				date = input()
				if date == 'done':
					break
				else:
					dates.append(date)
				

print('Type a two-to-three sentence blurb about what you\'re doing '+
	' and what you\'re looking for')

summary = input()

resInfo['Summary'] = [summary]

print(resInfo)
		



