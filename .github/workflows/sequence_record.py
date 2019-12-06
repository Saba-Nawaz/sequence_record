from Bio import SeqIO
for s in SeqIO.parse("fasta.fasta","fasta"):
    print(s.seq)
acount = 0
ccount = 0
tcount = 0
gcount = 0
for n in s:
    if n=="A":
        acount = acount+1
    elif n=="T":
            tcount=tcount+1
    elif n=="G":
            gcount=gcount+1
    elif n=="C":
            ccount=ccount+1
print(str(acount))
print(str(tcount))
print(str(gcount))
print(str(ccount))
