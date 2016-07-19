#! /usr/bin/env python3
# - trying to get this information to the localhost to be
# used on the front end
#import requests


allData = {'Edu': {'Dates': '2009 - 2013',
         'DegreeField': 'English',
         'DegreeType': 'B.S.',
         'GPA': '3.646',
         'Honors': 'cum laude',
         'School': 'Boston College'},
 'Email': 'jackmasterson5@gmail.com',
 'Extra': {'Sea Girt Recreation': {'dates': ['jun - july'],
                                   'skills': ['Maintain order with children',
                                              'Ensure sports equipment was '
                                              'ready-to-use each day',
                                              'Cooperate with needs of '
                                              'parents'],
                                   'title': 'Counselor'},
           'Sloan Kettering': {'dates': ['jul-aug'],
                               'skills': ['Ensure ER is clean and ready for '
                                          'use',
                                          'Maintain patient comfort while '
                                          'administering care',
                                          'Detail operation to accompanying '
                                          'family members'],
                               'title': 'Volunteer'}},
 'Name': 'Jack C Masterson',
 'Phone': '(908)433-0178',
 'Role': 'Web Developer',
 'Summary': 'Web developer with a passion for problem solving, thinking '
            'critically, and getting the job done. Looking to learn more about '
            'the tech side of business.',
 'Work': {'Shawmut Design and Construction': {'dates': ['sept - oct'],
                                              'skills': ['Copyedit internal '
                                                         'documents',
                                                         'Copywrite external '
                                                         'marketing materials '
                                                         'sent to prospective '
                                                         'clients',
                                                         'Initiate rewrite of '
                                                         'Business Development '
                                                         'marketing template'],
                                              'title': 'Junior Marketing '
                                                       'Coordinator'},
          'Workman': {'dates': ['dec - nov'],
                      'skills': ['Compose press releases highlighting '
                                 'attribtues of titles',
                                 'Engage with media outlets to increase book '
                                 'publicity',
                                 'Ensure authors remained in the loop on '
                                 'publicity efforts'],
                      'title': 'Publicity and Marketing Assistant'}}}

#url='http://localhost:3000'
#r = requests.post(url, data=allData)

#r = requests.get('http://jack-masterson.com')

#print(r.text)






