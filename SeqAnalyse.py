import Bio 
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

open_gap= -5
ext_gap= -1 
match= 2 
mismatch= -1 

querySeq = SeqIO.parse(open('QuerySeq.fasta'), 'fasta')
for fasta in querySeq:
  str(fasta.seq)

path_to_file = 'MTdb.fasta'   

align_results = open('results1.txt', mode ='w')
# Open file with "with" statement to avoid problems with access 
# to original file (in case computer hangs
# or there will be any other problem)
with open(path_to_file, mode='r') as handle:

    # Use Biopython's parse function to process individual
    # FASTA records (thus reducing memory footprint)
    for record in SeqIO.parse(handle, 'fasta'):

        # Extract individual parts of the FASTA record
        sequence = record.seq
        for a in pairwise2.align.globalms(sequence, fasta.seq, match, mismatch, open_gap, ext_gap): 
            align_results.write(format_alignment(*a)) 
            
             
                    
                    
             


    



       
