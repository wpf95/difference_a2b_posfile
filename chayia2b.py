import sys

fo1=open(sys.argv[1],"r")
fo2=open(sys.argv[2],"r")
diff_1=open(sys.argv[3],"w")
diff_2=open(sys.argv[4],"w")
samefile=open(sys.argv[5],"w")

list3=[]
list4=[]
for line1 in fo1:
    line1 = line1.strip().split()
    list1 = line1[0]+"_"+line1[1]
    list3.append(list1)

for line2 in fo2:
    line2 = line2.strip().split()
    list2 = line2[0]+"_"+line2[1]
    list4.append(list2)

diff_a=set(list3).difference(set(list4))
diff_b=set(list4).difference(set(list3))
diff_same=set(list3).intersection(set(list4))
for i in diff_a:
    diff_1.write(i.split("_")[0]+"\t"+i.split("_")[1]+"\n")
for j in diff_b:
    diff_2.write(j.split("_")[0]+"\t"+j.split("_")[1]+"\n")
for z in diff_same:
    diff_2.write(z.split("_")[0] + "\t" + z.split("_")[1] + "\n")

