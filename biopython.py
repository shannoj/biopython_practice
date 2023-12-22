from Bio import SeqIO

for record in SeqIO.parse("/Users/jamesshannon/Desktop/AMY2A_datasets/ncbi_dataset/data/gene.fna", "fasta"):
    print(record.id)