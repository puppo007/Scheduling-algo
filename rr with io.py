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
count=0
n=int(raw_input("Enter Total Number of Processes: "))
for i in range(n):
    print "Process",i+1
    name.append(raw_input("Enter Name of Process: "))
    arival.append(int(raw_input("Enter Arival Time: ")))
    burst.append(int(raw_input("Enter Burst Time: ")))
    temp.append(burst[i])

quantum=int(raw_input("Enter Quantum Time : "))
io=int(raw_input("Enter IO Interrupt Time: " ))
qwait=int(raw_input("Enter Waiting time in Queue: "))
quat=[]
wtime=[]
IO=[]
for i in range(n):
    quat.append(quantum)
    wtime.append(0)
    IO.append(io)
flag=1
time=arival[0]
while remain!=n:
    if temp[index]<=quat[index] and temp[index]>0 and quat[index]<=IO[index] and time>=wtime[index]:
        time+=temp[index]
        temp[index]=0
        flag=1
        if temp[index]==0:
            quat[index]=0
        if quat[index]==0:
            quat[index]=quantum
        chart.append(name[index])
        comp.append(time)
    elif temp[index]>0 and time>=wtime[index]:
        if quat[index]!=quantum:
            temp[index]-=quat[index]
            time+=quat[index]
        else:
            temp[index]-=IO[index]
            time+=IO[index]
        if quat[index]>IO[index] :
            quat[index]-=IO[index]
        else:
            IO[index]-=quat[index]
            quat[index]=0
        if temp[index]==0:
            comp.append(time)
            quat[index]=0
        if quat[index]==0:
            quat[index]=quantum
        if count==1:
            IO[index]=0
            count=0
        if IO[index]==0:
            IO[index]=io
        if IO[index]!=io:
            wtime[index]=wtime[index]
            count=1
        else:
            wtime[index]=time+qwait    
        chart.append(name[index])
    else:
        time=time+1
    if temp[index]<=0 and flag==1:
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


        
        
        
        



