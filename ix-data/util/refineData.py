import pandas as pd
import matplotlib.pyplot as plt
from multiprocessing import Manager, Process
import os
import json
from datetime import datetime
import seaborn as sns
import matplotlib.ticker as ticker
import pickle
from util.events import markEvents
    



def getDataFromParsedFile(file,data):
    

    with open(file,"r") as fileObject:
        jsonData = json.load(fileObject)
        nameSplitted = file.split("_")
        try:
            date = nameSplitted[1]+'T'+nameSplitted[2].split('.mrt')[0]
        except:
            print("Exception out of bounds name/date")
            print(file)
            return
        dateTime = datetime.strptime(date, '%Y-%m-%dT%Hh%Mm') 
        data.append([
            dateTime,
            jsonData["members"]["countv4"],
            jsonData["members"]["countv42nd"],
            jsonData["members"]["countv4both"],
            jsonData["reachableASes"]["countv4"],
            jsonData["reachableASes"]["countv42nd"],
            jsonData["reachableASes"]["countv4both"],
            jsonData["prefixes"]["countv4"],
            jsonData["prefixes"]["countv42nd"],
            jsonData["prefixes"]["countv4both"],
            jsonData["pathSize"]["v4"] if len(jsonData["pathSize"]["v4"]) > 0 else [0],
            jsonData["avgPathSize"]["v4"],
            jsonData["avgPathSize"]["v42nd"],
            jsonData["avgPathSize"]["v4both"],
            jsonData["routes"]["v4"],
            jsonData["routes"]["v42nd"],
            jsonData["routes"]["v4both"],
        ])

def makeAvgPathPlot(df,graphFolder,checkforRS):
    print("Making Average Path Plot")
    pallet = {'Average Path v4 Both':'#2ca02c', 'Average Path v4 R1': '#08519c', 'Average Path v4 R2':'#eb6e34'}
    plt.rcParams.update({'font.size': 22})
    df_plot2 = df.melt(id_vars='Day', value_vars=['Average Path v4 R1', 'Average Path v4 R2', 'Average Path v4 Both'], var_name='Type', value_name='Average Path Size')
    print(df_plot2)
    box = sns.boxplot(x='Day', y='Average Path Size', hue='Type', data=df_plot2,palette=pallet)
    plt.xticks(rotation=45)
    plt.xlabel('Date', fontsize=30)
    plt.ylabel('Average Path Size', fontsize=30)
    plt.grid()
    if checkforRS == 1:
        title =  ' RS Only'
        rs =  'RSOnly'
        offset = 1.96
        plt.ylim(bottom=1.95)
    elif checkforRS == 2:
        title = ' Excluding RS'
        rs = 'NotRS'
        offset = 3.2
    else:
        title = ''
        rs = ''
        offset = 3.0
    plt.title('Average Path Size for v4'+title, fontsize=30)
    plt.figure(figsize=(20,10))
    box.figure.set_size_inches(20,10)
    box.xaxis.set_major_locator(ticker.LinearLocator(10))
    markEvents(box,offset,1)
    

    fig = box.get_figure()
    fig.savefig(graphFolder+"/MediaCaminhos"+rs+".png",bbox_inches = "tight") 
    fig.savefig(graphFolder+"/MediaCaminhos"+rs+".pdf",bbox_inches = "tight") 
    print("Done Making Average Path Plot")


def makev4PrefixesRoutesPlot(df: pd.DataFrame,graphFolder,checkforRS):
    print("Making Prefix and Routes Plot for IPv4")
    fig, ax = plt.subplots()
    cycler = plt.cycler(linestyle=['-', '-', '-', '--', '--', '--'],
                    color=['#08519c', '#eb6e34', '#2ca02c','#08519c', '#eb6e34', '#2ca02c'],
    )
    plt.rcParams.update({'font.size': 22})
    ax.set_prop_cycle(cycler)
    df_plot2 = df.plot(ax=ax,x='Date',figsize=(20,10), y=['Prefixes v4 Both'],
                    ylabel=['Prefixes v4 Both'], 
                    fontsize=22)
    plt.ylim(bottom=0)
    plt.xlim("2024-04-16","2024-10-02")
    plt.xticks(rotation=45)
    df_plot2.xaxis.set_major_locator(ticker.LinearLocator(10))
    if checkforRS == 1:
        title =  ' RS Only'
        rs =  'RSOnly'
        offset = -3000
    elif checkforRS == 2:
        title = ' Excluding RS'
        rs = 'NotRS'
        offset = -30000
    else:
        title = ''
        rs = ''
        offset = -30000
    markEvents(df_plot2,offset)
    plt.grid()
    plt.xlabel('Date', fontsize=30)
    plt.ylabel('Quantity', fontsize=30)
    plt.title('Prefixes v4'+title, fontsize=30)
    plt.savefig(graphFolder+'/PrefixosvRotasv4'+rs+'.png',bbox_inches = "tight")
    plt.savefig(graphFolder+'/PrefixosvRotasv4'+rs+'.pdf',bbox_inches = "tight")
    print("Done Prefix and Routes Plot for IPv4")


def makev4MembersReachablePlot(df,graphFolder,checkforRS):
    print("Making Members and Reachable ASes Plot for IPv4")
    fig, ax = plt.subplots()
    cycler = plt.cycler(linestyle=['-', '-', '-', '--', '--', '--'],
                    color=['#08519c', '#eb6e34', '#2ca02c','#08519c', '#eb6e34', '#2ca02c'],
    )
    plt.rcParams.update({'font.size': 22})

    ax.set_prop_cycle(cycler)
    df_plot2 = df.plot(ax=ax,x='Date',figsize=(20,10), y=['Members v4 R1', 'Members v4 R2', 'Members v4 Both', 'Reachable v4 R1', 'Reachable v4 R2', 'Reachable v4 Both'],
                       ylabel=['Members v4 Route Server 1', 'Members v4 Route Server 2', 'Members v4 Both', 'Reachable v4 Route Server 1', 'Reachable v4 Route Server 2', 'Reachable v4 Both'],
                       fontsize=22)


    plt.ylim(bottom=0)
    plt.xlim("2024-04-16","2024-05-25")
    plt.xticks(rotation=45)
    df_plot2.xaxis.set_major_locator(ticker.LinearLocator(10))
    plt.xlabel('Date', fontsize=30)
    plt.ylabel('Number of ASes', fontsize=30)
    if checkforRS == 1:
        title =  ' RS Only'
        rs =  'RSOnly'
        offset = -380
    elif checkforRS == 2:
        title = ' Excluding RS'
        rs = 'NotRS'
        offset = -500
    else:
        title = ''
        rs = ''
        offset = -500
    markEvents(df_plot2,offset)
    plt.grid()
    plt.title('Members and Reachable ASes v4'+title, fontsize=30)
    plt.savefig(graphFolder+'/MembrosAlcancaveisv4'+rs+'.png',bbox_inches = "tight")
    plt.savefig(graphFolder+'/MembrosAlcancaveisv4'+rs+'.pdf',bbox_inches = "tight")
    print("Done Members and Reachable ASes Plot for IPv4")


def makeDataframeSingleProcess(folder,graphFolder,checkforRS):
    print("Loading Parsed Data")
    mp = Manager()
    data = mp.list()
    for file in os.listdir(folder):
        if checkforRS == 2 and 'NotRS' not in file:
            continue
        if checkforRS == 1 and 'RSOnly' not in file:
            continue
        if checkforRS == 0 and 'RS' in file:
            continue
        getDataFromParsedFile(folder+'/'+file,data)
    print("Done Loading Parsed Data")
    print("Making DataFrame")
    df = pd.DataFrame(list(data), columns=[
        'Date',
        'Members v4 R1',
        'Members v4 R2',
        'Members v4 Both',
        'Reachable v4 R1',
        'Reachable v4 R2',
        'Reachable v4 Both',
        'Prefixes v4 R1',
        'Prefixes v4 R2',
        'Prefixes v4 Both',
        'Paths v4 All',
        'Average Path v4 R1',
        'Average Path v4 R2',
        'Average Path v4 Both',
        'Routes v4 R1',
        'Routes v4 R2',
        'Routes v4 Both',
        ])
    df['Date'] = pd.to_datetime(df['Date'])
    df["Day"] = df["Date"].dt.strftime("%Y-%m-%d")
    df.sort_values(by='Date', inplace=True)

    graphProcess = []
    graphs = [
        makeAvgPathPlot,
        makev4PrefixesRoutesPlot,
        makev4MembersReachablePlot,

    ]
    for graph in graphs:
        p = Process(target=graph, args=(df,graphFolder,checkforRS))
        graphProcess.append(p)
        p.start()

    for process in graphProcess:
        process.join()



