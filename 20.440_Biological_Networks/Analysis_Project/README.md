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

- Download BioAssay dataset from PubChem as CSV.
- Convert SMILES to fingerprints

Fingerprint Parameters
- Type (Murcko Fragments, Daylight Fingerprints, Morgan(extended-connectively) Fingerprints
- Radius (2, 3, 4, 5)
- Size (1024-bit, 4096-bit)

***Evaluate Distance***

Distance Parameters
- Tanimoto Coefficient
- Euclidean
- Manhattan

*** Cluster Function ***

Cluster Type
- K-Medoid/K-means
- Agglomerative Hierarchical

Cluster Parameters
- K size
- 

*** Test Statistic ***

*** Confirmation Rate ***
Parameters
- Type (TopX, Data-driven)

