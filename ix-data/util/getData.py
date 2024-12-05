import json
from multiprocessing import Process
import os
import geoip2.database
import geoip2.models
import geoip2.errors
import ipaddress
import urllib.request
import statistics
from numpy import nan


def parseFiles(folder,outputFolder,checkforRS,aspp,shortestBetweenMembers):
    print("Parsing Data")
    processList = []
    for file in os.listdir(folder):
        p = Process(target=getFileData, args=(folder+'/'+file,outputFolder,checkforRS,aspp,shortestBetweenMembers), daemon=False)
        processList.append(p)
        p.start()
        if len(processList) >= 8:
            for process in processList:
                process.join()
                processList.remove(process)
                
    for process in processList:
        process.join()
    print("Done Parsing Data")
    


def getFileData(mrt,outputFolder,checkforRS,aspp,shortestBetweenMembers):
    

    #Path Size for each member, for each route server and considering both route servers
    pathSizesV4 = dict()
    pathSizesV42nd = dict()
    pathSizesV4both = dict()

    #Path Size independent of AS, for each route server and considering both route servers
    pathSizesAllR1 = list()
    pathSizesAllR2 = list()
    pathSizesAllBoth = list()

    #Prefixes present in each Route Server
    prefixesV4 = set()
    prefixesV42nd = set()

    #Members in each Route Server
    membersV42nd = set()
    membersV4 = set()

    #Reachable ASes in each Route Server
    reachableASesV42nd = set()
    reachableASesV4 = set()


    dictOfShortestPathsBetweenMembers = dict() #Shortest path between a member and a origin/reachable AS
    verifiedASes = {} #Verified ASes in RS
    if checkforRS != 0:
        reader=geoip2.database.Reader('./GeoLite2-City_20240301/GeoLite2-City.mmdb')
        with open('ASesConsideredinRSorNot.json','r') as output:
            verifiedASes = json.load(output)
    with open(mrt,'r') as file:
        for line in file:
            data = line.split('|')
            prefix = data[1]
            path = data[2]
            pathData = path.split(' ')
            member = pathData[0]
            reachable = pathData[-1]
            if aspp:
                pathSize = len(list(set(pathData)))
            else:
                pathSize = len(pathData)
            if shortestBetweenMembers:
                try:
                    if dictOfShortestPathsBetweenMembers[str(member)+str(reachable)] > pathSize:
                        dictOfShortestPathsBetweenMembers[str(member)+str(reachable)]=pathSize
                except:
                    dictOfShortestPathsBetweenMembers.update({str(member)+str(reachable):pathSize})

            if checkforRS != 0:
                try:
                    addressObject = ipaddress.ip_network(prefix)
                except:
                    print("Error in file",mrt)
                presentInVerifiedASes = ''
                try:
                    maxMindQueryReachable = reader.city(addressObject.broadcast_address).subdivisions[0].iso_code
                except Exception as e:
                    maxMindQueryReachable = ''
                try:
                    if verifiedASes[member] == 1:
                        presentInVerifiedASes = 'RS'
                except:
                    pass
                try:
                    if verifiedASes[reachable] == 1:
                        presentInVerifiedASes = 'RS'
                except:
                    pass
                if (maxMindQueryReachable != 'RS' and presentInVerifiedASes != 'RS') and checkforRS == 1: #Only count in RS, either through maxMind DB or defined list
                    continue
                if (maxMindQueryReachable == 'RS' or presentInVerifiedASes == 'RS') and checkforRS == 2: #Exclude any in RS
                    continue
            routeServer = data[-3].split(" ")[0]
            if '.' in prefix and routeServer == "177.52.38.253": #Route server 1
                membersV4.add(member)
                reachableASesV4.add(reachable)
                pathSizesAllR1.append(pathSize)
                try:
                    pathSizesV4[str(member)].append(pathSize)
                except KeyError:
                    pathSizesV4.update({str(member):list()})
                    pathSizesV4[str(member)].append(pathSize)
                prefixesV4.add(prefix)
            elif '.' in prefix and routeServer == "177.52.38.254": #Route server 2
                membersV42nd.add(member)
                reachableASesV42nd.add(reachable)
                pathSizesAllR2.append(pathSize)
                try:
                    pathSizesV42nd[str(member)].append(pathSize)
                except KeyError:
                    pathSizesV42nd.update({str(member):list()})
                    pathSizesV42nd[str(member)].append(pathSize)
                prefixesV42nd.add(prefix)
            pathSizesAllBoth.append(pathSize)
            try:
                pathSizesV4both[str(member)].append(pathSize)
            except KeyError:
                pathSizesV4both.update({str(member):list()})
                pathSizesV4both[str(member)].append(pathSize)
    if checkforRS != 0:
        reader.close()
    pathSizesTotal = []
    for key, value in pathSizesV4both.items():
        pathSizesTotal.append((
            statistics.median(value),
            statistics.median(pathSizesV4[key] if key in pathSizesV4 else [nan]),
            statistics.median(pathSizesV42nd[key] if key in pathSizesV42nd else [nan])
            ))

    membersBoth = membersV42nd.union(membersV4)
    reachableBoth = reachableASesV42nd.union(reachableASesV4)
    prefixesBoth = prefixesV42nd.union(prefixesV4)

    if shortestBetweenMembers:
        sumOfShortestPaths = 0
        for key, value in dictOfShortestPathsBetweenMembers.items():
            sumOfShortestPaths+=value
        avgOfShortestPath = sumOfShortestPaths/len(dictOfShortestPathsBetweenMembers) if len(dictOfShortestPathsBetweenMembers) > 0 else nan
        avgpath = avgOfShortestPath
    else:
        avgpath = (sum(pathSizesAllR1)/len(pathSizesAllR1)) if len(pathSizesAllR1) > 0 else nan
    toWrite = {
        "members":{
            "v4": list(membersV4),
            "v42nd": list(membersV42nd),
            "v4both": list(membersBoth),
            "countv4":len(membersV4),
            "countv42nd":len(membersV42nd),
            "countv4both":len(membersBoth),
        },
        "reachableASes":{
            "v4": list(reachableASesV4),
            "v42nd": list(reachableASesV42nd),
            "v4both": list(reachableBoth),
            "countv4":len(reachableASesV4),
            "countv42nd":len(reachableASesV42nd),
            "countv4both":len(reachableBoth),
        },
        "prefixes":{
            "v4": list(prefixesV4),
            "v42nd": list(prefixesV42nd),
            "v4both": list(prefixesBoth),
            "countv4":len(prefixesV4),
            "countv42nd":len(prefixesV42nd),
            "countv4both":len(prefixesBoth),
        },
        "pathSize":{
            "v4": pathSizesTotal,
        },
        "routes":{
            "v4": len(pathSizesAllR1),
            "v42nd": len(pathSizesAllR2),
            "v4both": len(pathSizesAllBoth),
        },
        "avgPathSize":{
            "v4": avgpath,
            "v42nd": (sum(pathSizesAllR2)/len(pathSizesAllR2)) if len(pathSizesAllR2) > 0 else nan,
            "v4both": (sum(pathSizesAllBoth)/len(pathSizesAllBoth)) if len(pathSizesAllBoth) > 0 else nan,
        }
    }
    if checkforRS == 1:
        rs =  'RSOnlyPrefix'
    elif checkforRS == 2:
        rs = 'NotRS'
    else:
        rs = ''
    with open(outputFolder+'/'+mrt[:-3].split('/')[-1]+rs+'-parsed.json','w+') as output:
        json.dump(toWrite,output)