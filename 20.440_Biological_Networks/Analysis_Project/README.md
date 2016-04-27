# Rosalind Bioinformatics #

### Description
---
20.440 Biological Networks Final Project
Francis Lee
Rob Wilson

This analysis pipeline is designed to evaluate 
Resources:
MCAM

### Workflow
---
***Preprocessing***

1.) Download BioAssay dataset from PubChem as CSV.
2.) Convert SMILES to fingerprints

Fingerprint Parameters
1.) Type (Murcko Fragments, Daylight Fingerprints, Morgan(extended-connectively) Fingerprints
2.) Radius (2, 3, 4, 5)
4.) Size (1024-bit, 4096-bit)

***Evaluate Distance***

Distance Parameters
1.) Tanimoto Coefficient
2.) Euclidean
3.) Manhattan

*** Cluster Function ***

Cluster Type
1.) K-Medoid/K-means
2.) Agglomerative Hierarchical

Cluster Parameters
1.) K size
2.) 

*** Test Statistic ***

*** Confirmation Rate ***
Parameters
1.) Type (TopX, Data-driven)

