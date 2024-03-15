# Pseudomonas aeruginosa resistance
It was used to calculate the prevalence of combinations of mutations associated with fluoroquinolone antibiotic resistance in clinical and environmental strains of Pseudomonas aeruginosa.

Pseudomonas aeruginosa is an important opportunistic pathogen that usually causes long-term infection in immunocompromised patients. Fluoroquinolone antibiotics have been widely used in clinical practice for a long time to treat infections caused by Pseudomonas aeruginosa. We show through laboratory evolution that Pseudomonas aeruginosa PAO1 exposed to different levels of fleroxacin can rapidly select for highly resistant mutants carrying multistep mutations. The combination of mutations in DNA gyrase (gyrA/gyrB) and negative regulator of the efflux pump (nfxB/mexR) results in high resistance. Here, we downloaded the protein sequences corresponding to the complete genome assembly level of Pseudomonas aeruginosa from the NCBI database. The amino acid sequences of GyrA, GyrB, NfxB and MexR of Pseudomonas aeruginosa PAO1 were used as reference sequences. Diamond blastp was used for homology alignment (identity>50%, coverage>80%, E-value=1E-5). The sequences were classified according to the source: clinical and non-clinical according to the annotation information in the NCBI database. The mutated amino acid sequences of GyrA, GyrB, NfxB and MexR were compared with their corresponding reference amino acid sequences by clustalw2. The Python script was used to calculate the mutated sites and amino acid residues, and the results were classified. The classification results were then subjected to Fisher's exact test for visualization and other analyses.
