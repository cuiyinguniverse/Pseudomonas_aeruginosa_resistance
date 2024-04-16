#According to the sequence alignment results of clustalw2, calculating amino acid mutation sites, and writing to a comma-separated values format file.

from Bio import AlignIO
import pandas as pd

def mutation_site(i):
    zidian = {}
    with open("/edisk2/yangh22/lm.csv","r") as g:
        contents = g.readlines()
        x = contents[0].replace("\n","").strip()
        y = contents[1].strip()
        file_aln = "/edisk2/yangh22/protein/ncbi_dataset/data/{}/gyrA.aln".format(i.strip())
        align = AlignIO.read(file_aln,"clustal")
        a = align[0].id
        b = align[1].id
        c = align[0].seq
        d = align[1].seq
        zidian[a] = b
        zipped = zip(c,d)
        lj = []
        lk = []
        j = 0
        for k in zipped:
            j += 1
            if k[0] != k[1]:
                lj.append(j)
                lk.append(k)
                zidian[x] = lj
                zidian[y] = lk
    return zidian

if __name__ == '__main__' :
    j = pd.DataFrame() 
    q = 0 
    with open("/edisk2/yangh22/yxq_works/protein/complete_genome_level/gyrA_mutation.csv","r") as f:
        m = f.readlines()
        for i in f.readlines():
            r = mutation_site(i)
            df = pd.DataFrame([r])
            q += 1    
            if q <= len(m):
                df = pd.concat([j,df], axis=0, join='outer', ignore_index=False)
                df.to_csv("/edisk2/yangh22/yxq_works/protein/complete_genome_level/gyrA_mutation_site.csv",mode="a",index=False,header=False)
