#! /usr/bin/env python3
#resumeWrite.py - gather data and put into a JSON to be read in resumePrac.py
resInfo = {'Work':{}, 'Extra':{}}
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
				resInfo[nextSect][lastJob] = {'skills' : []}

				skills = resInfo[nextSect][lastJob]['skills']
				
				print('What did you learn there? Add skills one at '+
				'a time by hitting enter. Enter \'done\' when finished.')		

				while True:

					skill = input()
					if skill == 'done':
						break
					else:
						skills.append(skill)
				print(skills)

				continue
print(resInfo)
		



