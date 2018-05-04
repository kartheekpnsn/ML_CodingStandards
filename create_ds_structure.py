import os
import sys
from shutil import copyfile

path = sys.argv[1]
copyfile('folder_structure.txt', path + "\\folder_structure.txt")
os.chdir(path)

files = ['README.md', 'requirements.txt', 'src/features/build_features.py', 'src/models/train_model.py', 'src/models/predict_model.py', 'src/visualization/explore.py', 'src/visualization/visualize.py', 'config/global.dcf', 'notebooks/models/train_model.ipynb', 'notebooks/models/predict_model.ipynb', 'notebooks/visualization/explore.ipynb', 'notebooks/visualization/visualize.ipynb']
folders = ['data', 'data/external', 'data/interim', 'data/processed', 'data/raw', 'data/deprecated', 'docs', 'docs/documents', 'docs/presentations', 'docs/deprecated', 'models', 'models/deprecated', 'notebooks', 'notebooks/data', 'notebooks/features', 'notebooks/models', 'notebooks/visualization', 'notebooks/deprecated', 'references', 'reports', 'reports/presentations', 'reports/figures', 'reports/dashboards', 'reports/deprecated', 'src', 'src/data', 'src/features', 'src/models', 'src/visualization', 'src/deprecated', 'cache', 'config', 'logs', 'meeting']

code_header = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author 		: 	Kartheek Palepu
Copyright 	: 	TEAM_NAME
Version 	: 	1.0
Maintainer 	: 	Kartheek Palepu
Email 		: 	YOUR@EMAILID.COM
Status 		: 	Development
Date		: 	26-APR-2018
"""

"""Module documentation goes here
   and here
   and ...
"""
'''


for eachFolder in folders:
	if not os.path.exists(eachFolder):
		os.makedirs(eachFolder)

for eachFile in files:
	open(eachFile, 'a').close()

header_files = ['src/features/build_features.py', 'src/models/train_model.py', 'src/models/predict_model.py', 'src/visualization/explore.py', 'src/visualization/visualize.py']
for eachFile in header_files:
	fileObject = open(eachFile, 'w')
	fileObject.write(code_header)
	fileObject.close()
