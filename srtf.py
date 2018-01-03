wsum=0
tsum=0
name=[]
nname=[]
arival=[]
narival=[]
burst=[]
nburst=[]
turn=[]
wait=[]
temp=[]
index=0
chart=[]
com=[]
n=int(raw_input("Enter Total Number of Processes: "))
for i in range(n):
    print "Process",i+1
    name.append(raw_input("Enter Name of Process: "))
    arival.append(int(raw_input("Enter Arival Time: ")))
    burst.append(int(raw_input("Enter Burst Time: ")))
    temp.append(burst[i])
    index=i

temp.append(9999)
time=0
remain=0
while remain!=n:
    small=index+1
    i=0
    while i<n:
            if arival[i]<=time and temp[i]<temp[small] and temp[i]>0:
                small=i
            i+=1 
    temp[small]=temp[small]-1
    chart.append(name[small])
    if temp[small]==0:
        remain=remain+1
        finish=time+1
        wait.append(finish-arival[small]-burst[small])
        turn.append(finish-arival[small])
        wsum=wsum+finish-arival[small]-burst[small]
        tsum=tsum+finish-arival[small]
        nname.append(name[small])
        narival.append(arival[small])
        nburst.append(burst[small])
        com.append(finish)
    time=time+1

print "Name     Arival Time     Burst Time     Completition Time     Waiting Time     Turnaround Time"
for l  in range(n):
    print nname[l],"\t\t",narival[l],"\t\t",nburst[l],"\t\t",com[l],"\t\t",wait[l],"\t\t",turn[l],"\t"

print "\n\n\t\t\tGantt Chart\n\t\t\t-----------"
for i in range(len(chart)):
    print chart[i],"--",


avg=float(wsum)/n
avg1=float(tsum)/n
print "\nAverage Waiting Time : ",avg
print "Average Turnaround Time : ",avg1

