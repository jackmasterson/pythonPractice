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

		if typed == 'Work':
			workHeader = doc.add_heading('Work Experience:', 2)
	
		elif typed == 'Extra':
			workHeader = doc.add_heading('Extracurriculars:', 2)
	

		orgs = list(data[typed].keys())

		for org in orgs:

			skills = data[typed][org]['skills']
			dates = data[typed][org]['dates']
			title = data[typed][org]['title']
	
			newOrg = doc.add_paragraph()
			newOrg.add_run(org).bold = True
			newOrg.style = 'NoSpacing'
			newOrg.add_run('\t\t\t\t\t\t' + dates[0]).italic = True
			
			for skill in skills:
				newList = doc.add_paragraph(skill, style='ListBullet2')

	education()

def education():

	doc.add_heading('Education:', 2)
	
	edu = data['Edu']
	school = data['Edu']['School']
	eduHead = doc.add_paragraph()
	eduHead.add_run(school)
	eduHead.style = 'Normal'
	eduHead.runs[0].bold = True

	dates = edu['Dates']

	eduHead.add_run('\t\t\t\t\t\t\t\t' + dates).italic = True

	deg = edu['DegreeType']
	eduHead.runs[1].add_break()
	eduHead.add_run(deg)
	
	degIn = edu['DegreeField']
	eduHead.add_run(', ' + degIn)
	honors = edu['Honors']

	if honors == '':
		eduHead.add_run('')
	else:
		eduHead.add_run('\t\t\t\t\t\t\t\t\t' + '[' + honors + 
			']').italic = True
	
	gpa = edu['GPA']
	eduHead.runs[4].add_break()
	if gpa == '':
		eduHead.add_run()
	else:
		eduHead.add_run('GPA: ' + gpa)
			



	
greeting()
doc.save('resumeTemplate.docx')

print('Okay, all set. Open it up!')