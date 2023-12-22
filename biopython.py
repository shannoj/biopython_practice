from Bio import SeqIO

def find_max_gc_content(file_name, file_format):
    max_sequence_id = None
    max_gc_content = 0

    for record in SeqIO.parse(file_name, file_format):
        sequence = str(record.seq)
        sequence_id = record.id
        gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence)
        if gc_content > max_gc_content:
            max_sequence_id = sequence_id
            max_gc_content = gc_content

    print(max_sequence_id)
    print(max_gc_content)

find_max_gc_content("gene.fna", "fasta")
