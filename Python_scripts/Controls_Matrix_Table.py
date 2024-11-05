#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Import necessary libraries
from datetime import datetime
start = datetime.now()


# In[2]:

# Record the start time of the script
import os
bucket = os.getenv("WORKSPACE_BUCKET")
bucket


# In[3]:

# Retrieve the workspace bucket environment variable
import hail as hl
# Initialize Hail with the specified default reference genome
hl.init(default_reference='GRCh38', idempotent=True)


# In[4]:

# Retrieve the path to the matrix table from the environment variable
mt_wgs_path = os.getenv("WGS_ACAF_THRESHOLD_MULTI_HAIL_PATH")
mt_wgs_path


# In[5]:

# Read the matrix table from the specified path
mt = hl.read_matrix_table(mt_wgs_path)


# In[6]:

# Count the number of entries (rows) in the matrix table
mt.count()


# In[7]:

# Define the path to the file containing the controls person_id list
flagged_samples = "gs://fc-secure-e8c07dee-29f2-4c12-a27b-56054fc762ef/control_sample_id.txt"


# In[8]:

# Use gsutil to print the first three lines of the flagged samples file
get_ipython().system('gsutil -u $$GOOGLE_PROJECT cat $flagged_samples | head -n 3')


# In[9]:

# Import the flagged samples as a Hail table, using "person_id" as the key
sample_to_keep = hl.import_table(flagged_samples, key="person_id")


# In[10]:

# Filter the matrix table to only include columns (samples) that are in the flagged samples
mt = mt.semi_join_cols(sample_to_keep)


# In[11]:

# Count the number of entries in the filtered matrix table
mt.count()


# In[12]:

# Filter the matrix table to retain only SNP rows (Single Nucleotide Polymorphisms)
mt = mt.filter_rows(hl.is_snp(mt.alleles[0], mt.alleles[1]))


# In[13]:

# Count the number of entries again after filtering for SNPs
mt.count()


# In[14]:

# Define the output path for PLINK format data in the workspace bucket
out_path = f'{bucket}/data/test_plink_controls'


# In[15]:

# Export the filtered matrix table to PLINK format, specifying the individual IDs
hl.export_plink(mt, out_path, ind_id = mt.s)


# In[16]:

# Record the stop time of the script
stop = datetime.now()
# Calculate and print the total time taken to run the script
total_time = str(stop - start)
total_time







