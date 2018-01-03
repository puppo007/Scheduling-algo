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
chart=[]
comp=[]
index=0
quantum=0
remain=0
n=int(raw_input("Enter Total Number of Processes: "))
for i in range(n):
    print "Process",i+1
    name.append(raw_input("Enter Name of Process: "))
    arival.append(int(raw_input("Enter Arival Time: ")))
    burst.append(int(raw_input("Enter Burst Time: ")))
    temp.append(burst[i])

quantum=int(raw_input("Enter Quantum Time : "))
time=arival[0]
while remain!=n:
    if temp[index]<=quantum and temp[index]>0:
        time=time+temp[index]
        temp[index]=0
        flag=1
        chart.append(name[index])
        comp.append(time)
    elif temp[index]>0:
        temp[index]=temp[index]-quantum
        time=time+quantum
        chart.append(name[index])
    if temp[index]==0 and flag==1:
        remain=remain+1
        wait.append(time-arival[index]-burst[index])
        turn.append(time-arival[index])
        wsum=wsum+time-arival[index]-burst[index]
        tsum=tsum+time-arival[index]
        flag=0
        nname.append(name[index])
        narival.append(arival[index])
        nburst.append(burst[index])
        
    if index==n-1:
        index=0
    #elif temp[index+1]<=time:
     #   index=index+1
    else:
        index=index+1

print "Name     Arival Time     Burst Time     Waiting Time     Turnaround Time    Completition Time"
for l  in range(n):
    print nname[l],"\t\t",narival[l],"\t\t",nburst[l],"\t\t",wait[l],"\t\t",turn[l],"\t\t",comp[l]

print "\n\n\t\t\tGantt Chart\n\t\t\t-----------"
for i in range(len(chart)):
    print chart[i],"--",


avg=float(wsum)/n
avg1=float(tsum)/n
print "\nAverage Waiting Time : ",avg
print "Average Turnaround Time : ",avg1

