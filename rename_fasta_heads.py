from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

input_handle=open(sys.argv[1],'r')
dates_handle=open(sys.argv[2],'r')
output_handle=open(sys.argv[1]+'.dates','w')

records=SeqIO.parse(input_handle,'fasta')

id_dict={}
new_records=[]


for line in dates_handle.readlines():
	line=line.split()
	id_dict[line[0].strip()]=line[1].strip()


for record in records:
	if record.id.strip() in id_dict:
		new_id=id_dict[record.id.strip()]
		new_record=SeqRecord(record.seq, id=new_id, name='', description='')
	new_records.append(new_record)


SeqIO.write(new_records,output_handle,'fasta')

input_handle.close()
output_handle.close()
dates_handle.close()
