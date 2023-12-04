from Bio import Entrez

# Always tell NCBI who you are
Entrez.email = "your.email@example.com"

def get_nucleotide_sequence(refseq_id):
    handle = Entrez.efetch(db="nucleotide", id=refseq_id, rettype="fasta", retmode="text")
    sequence_data = handle.read()
    handle.close()
    return sequence_data

# Example usage
sequence = get_nucleotide_sequence("NM_001301357")
print(sequence)