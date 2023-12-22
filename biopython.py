from Bio import SeqIO

for record in SeqIO.parse("gene.fna", "fasta"):
    print(record.id)
