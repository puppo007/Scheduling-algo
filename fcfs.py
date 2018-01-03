wsum=0
tsum=0
name=[]
arival=[]
burst=[]
turn=[]
wait=[]
start=[]
chart=[]
com=[]
n=int(raw_input("Enter Total Number of Processes: "))
for i in range(n):
    print "Process",i+1
    name.append(raw_input("Enter Name of Process: "))
    arival.append(int(raw_input("Enter Arival Time: ")))
    burst.append(int(raw_input("Enter Burst Time: ")))

for j in range(n):
    if j==0:
        start.append(arival[j])
    else:    
        start.append(start[j-1]+burst[j-1])
    wait.append(start[j]-arival[j])
    wsum=wsum+wait[j]
    ftime=start[j]+burst[j]
    turn.append(ftime-arival[j])
    tsum=tsum+turn[j]
    chart.append(name[j])
    com.append(ftime)

print "Name     Arival Time     Burst Time     Completition Time     Waiting Time     Turnaround Time"
for l  in range(n):
    print name[l],"\t\t",arival[l],"\t\t",burst[l],"\t\t",com[l],"\t\t",wait[l],"\t\t",turn[l],"\t"

print "\n\n\t\t\tGantt Chart\n\t\t\t-----------"
for i in range(len(chart)):
    print chart[i],"--",


avg=float(wsum)/n
avg1=float(tsum)/n
print "\nAverage Waiting Time : ",avg
print "Average Turnaround Time : ",avg1


    

    
