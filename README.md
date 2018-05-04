# Machine learning Standards (Coding, Document structure etc.)
This repository is created to set coding standards and folder structure for any Machine learning usecase.

## 1. Coding standards
	1. filename: predict_ad_revenue.R or predict_ad_revenue.py
	2. variblename: avgClicks
	3. constantname: kConstantName
	4. functionname: CalculateAvgClicks
	5. In R: use <- not =
	6. Function definitions should first list arguments without default values, followed by those with default values.
	7. Function documentation:
		CalculateSampleCovariance <- function(x, y, verbose = TRUE) {
			# Computes the sample covariance between two vectors.
			#
			# Args:
			#   x: One of two vectors whose sample covariance is to be calculated.
			#   y: The other vector. x and y must have the same length, greater than one,
			#      with no missing values.
			#   verbose: If TRUE, prints sample covariance; if not, not. Default is TRUE.
			#
			# Returns:
			#   The sample covariance between x and y.
			do_something <- some_value
	8. At the end of the code specify TODO(username): Explicit description of action to be taken
	9. In R: Errors should be raised using stop().
  
## 2. Code Metadata
### For R
```
# # Author 		: 	Kartheek Palepu
# # Copyright 	: 	TEAM_NAME
# # Version 	: 	1.0
# # Maintainer 	: 	Kartheek Palepu
# # Email 		: 	YOUR@EMAILID.COM
# # Status 		: 	Development
# # Date		:	26-APR-2018

"Module documentation goes here
   and here
   and ...
"
```
### For Python
```
#!/usr/bin/env python
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
```

## 3. Folder Structure
To follow the folder structure mentioned below run the "python create_ds_structure.py path" with path as command line argument
```
├── LICENSE
├── README.md             <- The top-level README for developers using this project.
├── data
│   ├── external          <- Data from third party sources.
│   ├── interim           <- Intermediate data that has been transformed.
│   ├── processed         <- The final, canonical data sets for modeling.
│   ├── raw               <- The original, immutable data dump.
│   └── deprecated
│
├── docs
|	├── documents
|	├── presentations
|	└── deprecated
│
├── models
|	└── deprecated      
│
├── notebooks
│   ├── data              <- Scripts to download or generate or process data
│   ├── features          <- Scripts to turn raw data into features for modeling
│   │   └── build_features.ipynb
│   ├── models            <- Scripts to train models and then use trained models to make predictions
│   │   ├── train_model.py
│   │   └── predict_model.ipynb
│   ├── visualization     <- Scripts to create exploratory and results oriented visualizations
│   |   ├── explore.ipynb
│   |   └── visualize.ipynb
│   └── deprecated
│
├── references            <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
|	├── presentations
|	├── figures       <- Generated graphics and figures to be used in reporting
|	├── dashboards     
│   	└── deprecated
│
├── requirements.txt
│
├── src                   <- Source code for use in this project.
│   ├── data              <- Scripts to download or generate or process data
│   ├── features          <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   ├── models            <- Scripts to train models and then use trained models to make predictions
│   │   ├── train_model.py
│   │   └── predict_model.py
│   ├── visualization     <- Scripts to create exploratory and results oriented visualizations
│   |   ├── explore.py
│   |   └── visualize.py
│   └── deprecated
│
├── cache                 <- This can be used to store .rda files or .pkl files or .npy files
|
├── config                <- This can be used to store configurations
│   └── global.dcf
|
├── logs                  <- This can be used to store logs (data wise)
|
└── meeting               <- This can be used to store minutes of the meeting, reports, presentations (date wise)
```
