# AllOfUs VTE Study

This repository contains the code used for my thesis project, which aims to determine genetic variants associated with Venous Thromboembolism (VTE) in African Americans.

## Contents

The repository includes several scripts written in R, Unix, and Python:

### R Scripts

The R scripts include the following functionalities:
- **Welchs_t_test.Rmd**: Code for analyzing non-genomic risk factors for VTE.
- **Sex_at_birth.Rmd**: Code to determine the sex of individuals in the study.
- **age.Rmd**: Code to determine the age of individuals in the study.
- **Demographic Information**: Code for combining the demographic information of individuals.
- **covariate_file_setup.Rmd**: Code for setting up the covariate file.
- **post_gwas.Rmd**: Code for performing post-GWAS analyses.

### Unix Scripts

The Unix scripts include:
- **Cases_plink_files_setup.txt**: Script to download case PLINK files from Google Cloud Storage and update sex information.
- **Controls_plink_files_setup.txt**: Script to download control PLINK files from Google Cloud Storage and update sex information.
- **merging_cases_and_controls.txt**: Script to merge case and control genotyping data, including further quality control steps.
- **logistic_regression.txt**: Script to run PCA of ancestry and perform the logistic regression model.

### Python Scripts

The Python scripts provide:
- **Cases_Matrix_Table.py**: Extraction of genomic data using Hail Matrix Tables for cases into Google Cloud Storage.
- **Controls_Matrix_Table.py**: Extraction of genomic data using Hail Matrix Tables for controls into Google Cloud Storage.

## Getting Started

To get started with this repository, ensure you have the necessary tools installed for R, Unix, and Python, and follow the instructions provided in the respective script files.

## Acknowledgements

Thank you for your interest in my research! Please feel free to reach out if you have any questions or feedback.
