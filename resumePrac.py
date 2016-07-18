#! /usr/bin/env python3
# wordPrac.py - write a Resume-template generator

import docx, resumeData
from docx.shared import Pt

doc = docx.Document()
data = resumeData.allData

def greeting():
	print('Formatting...')

	nameRole()

def nameRole():
	
	name = data['Name']
	nameHead = doc.add_paragraph(name, 'Title')
	nameHead.alignment = 0
	nameHead.runs[0].font.size = Pt(25)

	role = data['Role']
	nameHead.add_run(' '+role).italic = True
	doc.paragraphs[0].runs[1].style = "SubtitleChar"
	
	email = data['Email']
	contactSect = doc.add_paragraph(email, 'NoSpacing')
	contactSect.alignment = 1

	phone = data['Phone']
	contactSect.add_run('  |  ' + phone)

	summary()

def summary():

	summary = data['Summary']

	doc.add_heading('Summary:', 2)
	summaryInfo = doc.add_paragraph()
	summaryInfo.add_run(summary)
	summaryInfo.runs[0].style = 'SubtleEmphasis'
	
	typeIt()

def typeIt():

	types = ['Work', 'Extra']
	for typed in types:
		#print(typed)
		#print(data[typed])

		if typed == 'Work':
			workHeader = doc.add_heading('Work Experience:', 2)
			workHead = doc.add_paragraph()
		elif typed == 'Extra':
			workHeader = doc.add_heading('Extracurriculars:', 2)
			workHead = doc.add_paragraph()

		orgs = list(data[typed].keys())
		#print(orgs)
		for org in orgs:
		#	print(org)
		#	print(data[typed][org])
			skills = data[typed][org]['skills']
			dates = data[typed][org]['dates']
			title = data[typed][org]['title']

			#print(skills)
			#print(dates)
			#print(title)


			workHead.add_run(org)
			workHead.runs[0].bold = True

			workHead.add_run('\t\t\t' + dates).italic = True
			workHead.style = 'NoSpacing'

			for skill in skills:
				print(skill)
				listed = doc.add_paragraph(skill, style='ListBullet2')
		
		

			



	
greeting()
#nameRole()
#typeIt()
#education()
#contact()



doc.save('resumeTemplate.docx')