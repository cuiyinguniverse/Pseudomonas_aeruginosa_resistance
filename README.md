# Pseudomonas aeruginosa resistance
It was used to calculate the prevalence of combinations of mutations associated with fluoroquinolone antibiotic resistance in clinical and environmental strains of Pseudomonas aeruginosa.

Pseudomonas aeruginosa is an important opportunistic pathogen that usually causes long-term infection in immunocompromised patients. Fluoroquinolone antibiotics have been widely used in clinical practice for a long time to treat infections caused by Pseudomonas aeruginosa. We show through laboratory evolution that Pseudomonas aeruginosa PAO1 exposed to different levels of fleroxacin can rapidly select for highly resistant mutants carrying multi-step mutations. The combination of mutations in DNA gyrase (gyrA/gyrB) and negative regulator of the efflux pump (nfxB/mexR) results in high resistance. Here, we downloaded the protein sequences corresponding to the complete genome assembly level of Pseudomonas aeruginosa from the NCBI database. The amino acid sequences of GyrA, GyrB, NfxB and MexR of Pseudomonas aeruginosa PAO1 were used as reference sequences. Diamond blastp was used for homology alignment (identity>50%, coverage>80%, E-value=1E-5). The sequences were classified according to the source: clinical and non-clinical according to the annotation information in the NCBI database. The mutated amino acid sequences of GyrA, GyrB, NfxB and MexR were compared with their corresponding reference amino acid sequences by clustalw2. The Python script was used to calculate the mutation sites and amino acid residues, and the results were classified. The classification results were then subjected to Fisher's exact test for visualization and other analyses.

Citation:Efflux pump-related mutations dictate the multi-step evolution of high-level resistance to fluoroquinolone in Pseudomonas aeruginosa.

Requirement:

    • Diamond v2.0.15.153
    • clustalw2 

Step 1 Genome download using Ubuntu/linux scripts

• 1.1 Run the following script to download the protein sequences of Pseudomonas aeruginosa from the NCBI database(https://www.ncbi.nlm.nih.gov/). Only complete genomes are downloaded and included for downstream analysis.

    bash download.sh

• 1.2 Run the following script to unzip the protein sequence file of Pseudomonas aeruginosa.

    bash decompression.sh

Step 2 Data processing using Python and Ubuntu/linux scripts

• 2.1 Run the following Python script to compare the homology of the unzipped protein fasta format file.

    python blastp.py
or
    nohup python blastp.py &

• 2.2 Rewriting each mutated gyrA, gyrB, nfxB and mexR amino acid sequence and its corresponding reference sequence to the corresponding file directory in fasta format using the Python script, rewrite_sequence.py. Use clustalw2 for double sequence alignment.

    bash clustalw2.sh

• 2.3 According to the sequence alignment results of clustalw2, the mutation sites and amino acid residues were calculated by using Python script.

    python calculate_mutation_sites.py 
or
    nohup python calculate_mutation_sites.py &

• 2.4 The results of mutation sites and amino acid residues calculated by Python script in step 2.3 are counted according to clinical and non-clinical, and the sequences without mutation are classified and counted according to clinical and non-clinical, so as to obtain a 2X2 contingency table.

Step 3 Data visualization and statistics

