# Aryan Shirbhate BS22B009
codon_table = {
    "ATA": "Ile", "ATC": "Ile", "ATT": "Ile", "ATG": "Met",
    "ACA": "Thr", "ACC": "Thr", "ACG": "Thr", "ACT": "Thr",
    "AAC": "Asn", "AAT": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGC": "Ser", "AGT": "Ser", "AGA": "Arg", "AGG": "Arg",
    "CTA": "Leu", "CTC": "Leu", "CTG": "Leu", "CTT": "Leu",
    "CCA": "Pro", "CCC": "Pro", "CCG": "Pro", "CCT": "Pro",
    "CAC": "His", "CAT": "His", "CAA": "Gln", "CAG": "Gln",
    "CGA": "Arg", "CGC": "Arg", "CGG": "Arg", "CGT": "Arg",
    "GTA": "Val", "GTC": "Val", "GTG": "Val", "GTT": "Val",
    "GCA": "Ala", "GCC": "Ala", "GCG": "Ala", "GCT": "Ala",
    "GAC": "Asp", "GAT": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGA": "Gly", "GGC": "Gly", "GGG": "Gly", "GGT": "Gly",
    "TCA": "Ser", "TCC": "Ser", "TCG": "Ser", "TCT": "Ser",
    "TTC": "Phe", "TTT": "Phe", "TTA": "Leu", "TTG": "Leu",
    "TAC": "Tyr", "TAT": "Tyr", "TAA": "Stop", "TAG": "Stop",
    "TGC": "Cys", "TGT": "Cys", "TGA": "Stop", "TGG": "Trp",
}

# Prompt the user to enter a DNA sequence
dna_seq = input("Enter a DNA sequence: ").upper()

# Get the reverse complement of the DNA sequence
rev_seq = dna_seq.translate(str.maketrans("ATCG", "TAGC"))[::-1]

# Initialize lists to store the six reading frames
frames = ["", "", "", "", "", ""]

# Perform translation on each of the three forward frames
for i in range(3):
    frame = dna_seq[i:]
    for j in range(0, len(frame), 3):
        codon = frame[j:j+3]
        if len(codon) == 3:
            frames[i] += codon_table[codon]

# Perform translation on each of the three reverse frames
for i in range(3):
    frame = rev_seq[i:]
    for j in range(0, len(frame), 3):
        codon = frame[j:j+3]
        if len(codon) == 3:
            frames[i+3] += codon_table[codon]

# Print the protein products in all six frames
for i in range(6):
    print(f"In frame {i+1} (after appropriate deletion) the protein sequence is: {frames[i]}")
