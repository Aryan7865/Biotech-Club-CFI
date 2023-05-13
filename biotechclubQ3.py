#Aryan Shirbhate BS22B009
# Codon table
codontable = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W"
}

def translate(dnaseq):
    proteinseq = ['', '', '', '', '', '']
    for i in range(3):
        for j in range(i, len(dnaseq)-2, 3):
            codon = dnaseq[j:j+3]
            aa = codontable.get(codon, 'X')
            proteinseq[i] += aa
        
    revcomp = reversecomplement(dnaseq)
    for i in range(3):
        for j in range(i, len(revcomp)-2, 3):
            codon = revcomp[j:j+3]
            aa = codontable.get(codon, 'X')
            proteinseq[i+3] += aa
            
    return proteinseq

def reversecomplement(dnaseq):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    revcomp = ''.join([complement.get(base, 'N') for base in reversed(dnaseq)])
    return revcomp

# Example usage
dnaseq = 'ATTTCCAG'
proteinseq = translate(dnaseq)

for i, seq in enumerate(proteinseq):
    print(f"In reading frame {i+1}: {seq}")
