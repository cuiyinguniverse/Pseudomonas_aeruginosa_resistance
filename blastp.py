#diamond makedatabase

import os
for dirs in os.listdir("/edisk2/yangh22/protein/ncbi_dataset/data"):
    mdb = r"diamond makedb --in /edisk2/yangh22/protein/ncbi_dataset/data/{}/*.faa --db /edisk2/yangh22/protein/ncbi_dataset/data/{}/prot_database".format(dirs,dirs)
    os.system(mdb)

#diamond blastp

for dirs in os.listdir("/edisk2/yangh22/protein/ncbi_dataset/data"):
    blastp = r"/data/anaconda3/envs/diamond/bin/diamond blastp --query ./GyrA.faa --db /edisk2/yangh22/protein/ncbi_dataset/data/{}/prot_database.dmnd --out /edisk2/yangh22/protein/ncbi_dataset/data/{}/GyrA.blastp --query-cover 80 --id 0 --outfmt 6 --evalue 1e-5 -k 1".format(dirs,dirs)
    os.system(blastp)
