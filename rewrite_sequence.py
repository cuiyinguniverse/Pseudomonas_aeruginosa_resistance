import os
protein_names = ['gyrA','gyrB','nfxB','mexR']
for i in protein_names:
    with open("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}.tsv".format(i.strip()),"w") as F:
        for dirs in os.listdir("/edisk2/yangh22/protein/ncbi_dataset/data"):
            with open("/edisk2/yangh22/protein/ncbi_dataset/data/{}/{}.blastp".format(dirs,i.strip()),"r") as f:
                for j in f.readlines():
                    F.write(dirs + '\t' + j)

#

import csv

protein_names = ['gyrA','gyrB','nfxB','mexR']
for i in protein_names:
    header = ['reference_genome_id','Query_accession_{}'.format(i.strip()),'Target_accession_{}'.format(i.strip()), \
              'Sequence_identity_{}'.format(i.strip()),'Length_{}'.format(i.strip()),'Mismatches_{}'.format(i.strip()),'Gap_openings_{}'.format(i.strip()), \
                'Query_start_{}'.format(i.strip()),'Query_end_{}'.format(i.strip()),'Target_start_{}'.format(i.strip()),'Target_end_{}'.format(i.strip()), \
                    'E_value_{}'.format(i.strip()),'Bit_score_{}'.format(i.strip())]
    with open("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}.csv".format(i.strip()),"w",encoding = 'utf-8',newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        with open("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}.tsv".format(i.strip()),"r") as F:
            list = [line.split() for line in F.readlines()]            
            writer.writerows(list)
#

import pandas as pd

protein_names = ['gyrA','gyrB','nfxB','mexR']
for i in protein_names:
    data = pd.read_csv("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}.csv".format(i.strip()))
    j = []
    for index,row in data.iterrows():
        if row['Sequence_identity_{}'.format(i.strip())] < 100:
            j.append(row['reference_genome_id'])
    j_df = pd.DataFrame(j,columns=['reference_genome_id'])
    j_df.to_csv("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}_mutation.csv".format(i.strip()),index=False)

#

from Bio import SeqIO
j = 0
protein_names = ['gyrA','gyrB','nfxB','mexR']
for k in protein_names:
    with open("/edisk2/yangh22/yxq_works/protein/complete_genome_level/{}.csv".format(k.strip()),"r") as H ,open("/edisk2/yangh22/{}.faa".format(k.strip()),"r") as f:
        source = SeqIO.read(f,"fasta")
        for i in H.readlines()[:]:
            file_input = r"/edisk2/yangh22/protein/ncbi_dataset/data/{}/{}.blastp".format(i.strip(),k.strip())
            file_fasta = r"/edisk2/yangh22/protein/ncbi_dataset/data/{}/protein.faa".format(i.strip())
            with open(file_input,"r") as h:
                target_id = h.readlines()[0].split("\t")[1]
                for fa in SeqIO.parse(file_fasta,"fasta"):
                    if fa.id == target_id:
                        my_records = []
                        my_records.append(source)
                        fa.id = i.strip() + "|"+ fa.id
                        my_records.append(fa)
                        j += 1
                        SeqIO.write(my_records, r"/edisk2/yangh22/protein/ncbi_dataset/data/{}/{}.fasta".format(i.strip(),k.strip()),"fasta")