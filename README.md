# Pseudomonas aeruginosa resistance
It was used to calculate the prevalence of combinations of mutations associated with fluoroquinolone antibiotic resistance in clinical and environmental strains of Pseudomonas aeruginosa.

Pseudomonas aeruginosa is an important conditional pathogen, which often causes long-term infection in patients with low immune function. 
Fluoroquinolone antibiotics have long been widely used in the treatment of clinical infection caused by Pseudomonas aeruginosa. 
Our laboratory evolution shows that Pseudomonas aeruginosa PAO1 can quickly select highly resistant mutants with multiple mutations under different levels of fleroxacin exposure. 
The mutant combination of DNA gyrase (gyrA/gyrB) and efflux pump negative regulator (nfxB/mexR) leads to high drug resistance. 
Here, we downloaded the corresponding protein sequences of the complete genome assembly level of Pseudomonas aeruginosa from the NCBI database, taking the GyrA, GyrB, NfxB and MexR amino acid sequences of Pseudomonas aeruginosa PAO1 as reference sequences, using Diamond blastp for homologous alignment (identity > 50%, coverage > 80%, E-value=1E-5). According to the annotation information in the NCBI database, these sequences are classified by source: clinical and non-clinical. 
The mutated amino acid sequences of GyrA, GyrB, NfxB and MexR were compared with their corresponding reference amino acid sequences by clustalw2. The mutated sites and amino acid residues were calculated by Python script, and the results were counted according to clinical and non-clinical classification. At the same time, a series of 2 × 2 contingency tables were obtained. 
Fisher's exact test these contingency tables for visualization and other analysis.

Citation:Efflux pump-related mutations dictate the multi-step evolution of high-level resistance to fluoroquinolone in Pseudomonas aeruginosa.

Requirement:

    • Diamond v2.0.15.153
    • clustalw2 

Step 1 Genome download using linux shell scripts

• 1.1 Run the following script to download the protein sequences of Pseudomonas aeruginosa from the NCBI database(https://www.ncbi.nlm.nih.gov/). Only complete genomes are downloaded and included for downstream analysis.

    bash download.sh

• 1.2 Run the following script to unzip the protein sequence file of Pseudomonas aeruginosa.

    bash decompression.sh

Step 2 Data processing using Jupyter Notebook and linux shell scripts

• 2.1 Run the Jupyter Notebook script blastp.ipynb to compare the homology of the unzipped protein fasta format file.

• 2.2 Rewriting each mutated gyrA, gyrB, nfxB and mexR amino acid sequence and its corresponding reference sequence to the corresponding file directory in fasta format using the Jupyter Notebook script, rewrite_sequence.ipynb. Using clustalw2 for double sequence alignment.

    bash clustalw2.sh

• 2.3 According to the sequence alignment results of clustalw2, the mutation sites and amino acid residues were calculated by using Jupyter Notebook script calculate_mutation_sites.ipynb.

• 2.4 The results of mutation sites and amino acid residues calculated by Jupyter Notebook script in step 2.3 are counted according to clinical and non-clinical, and the sequences without mutation are classified and counted according to clinical and non-clinical, so as to obtain a series of 2×2 contingency tables.

Step 3 Data visualization and statistics

• 3.1 According to the data in these 2 × 2 contingency tables, the frequency of functional loss mutations and their combinations of DNA gyrase (gyrA/gyrB) and efflux pump negative regulatory factor (nfxB/mexR) were calculated, indicating whether these types of mutations are widespread in evolution.

These series of 2 × 2 contingency tables were performed by Fisher's exact test respectively to determine whether the functional loss mutations of DNA gyrase (gyrA/gyrB) and efflux pump negative regulatory factor (nfxB/mexR) and their combinations were significantly enriched in clinical according to P-value.

