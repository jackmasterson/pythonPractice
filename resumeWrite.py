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

			print('Add your next most recent item name.')
			lastJob = input()
			
			
			
			if lastJob == 'done':
				break
			else:
				resInfo[nextSect][lastJob] = {}
				continue
print(resInfo)
		



