import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def markEvents(plot: plt):
    events = [
        ("2024-04-27","First Storm","red",'1st'),
        ("2024-05-02","Taquari Reaches\n 30 meters","cyan",'2nd'),
        ("2024-05-03","Guaiba Reaches\n 4.77 meters","magenta",'3rd'),
        ("2024-05-04","Guaiba Reaches\n 5 meters","purple",'4th'),
        ("2024-05-05","Guaiba Reaches\n 5.3 meters","brown",'5th'),
    ]

    for event in events:
        plot.axvline(x=event[0],color=event[2],linestyle='dotted', label=event[1], linewidth=3)
        plot.legend(bbox_to_anchor = (1.0, 1), loc = 'upper left')

def circuitsPlot(file,graphFolder,startDateCutoff,endDateCutoff):
    print("Making Circuits Plot")
    df = pd.read_csv(file, delimiter=';')
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True).dt.date 

    plt.rcParams.update({'font.size': 22})
    df['Number of fault circuits per day'] = (df['Number of fault circuits per day']/132)*100 #number of faults to percentage considering the total number of circuits

    df_plot2 = df.plot(x='Data',figsize=(20,10), y=['Number of fault circuits per day'],ylabel=['Number of fault circuits per day'], )
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100.0))
    plt.ylim(bottom=0)
    plt.xlim(pd.Timestamp(startDateCutoff), pd.Timestamp(endDateCutoff))
    plt.xticks(rotation=45)
    df_plot2.xaxis.set_major_locator(ticker.LinearLocator(10))


    markEvents(df_plot2)
    plt.grid()
    plt.xlabel('Date', fontsize=30)
    plt.ylabel('Percentage', fontsize=30)
    plt.title('Unavailable Circuits', fontsize=30)
    plt.savefig(graphFolder+'/Fault Circuits.png',bbox_inches = "tight")
    plt.savefig(graphFolder+'/Fault Circuits.pdf',bbox_inches = "tight")
    print("Done")

if __name__ == '__main__':
    circuitsPlot('quedas_enchente.csv',".",'2024-04-21','2024-06-30')