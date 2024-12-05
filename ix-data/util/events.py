import matplotlib.pyplot as plt


def markEvents(plot: plt, offset=0, seaborn = 0):
    events = [
        ("2024-04-27","First Storm","red",'1st'),
        ("2024-05-02","Taquari Reaches\n 30 meters","cyan",'2nd'),
        ("2024-05-03","Guaíba Reaches\n 4.77 meters","magenta",'3rd'),
        ("2024-05-04","Guaíba Reaches\n 5 meters","purple",'4th'),
        ("2024-05-05","Guaíba Reaches\n 5.35 meters","brown",'5th'),
        # ("2024-05-05","Guaíba level \nfell below the \nflooding level","gold",'6th'),
        # ("2024-06-07","Guaíba River \nreturns to its \nbanks","purple",'7th'),
    ]
    xmin, xmax, ymin, ymax = plot.axis()
    for event in events:
        # plot.axvline(x=event[0],color='black',linestyle='dotted', label=event[1])
        plot.axvline(x=event[0],color=event[2],linestyle='dotted', label=event[1], linewidth=3)
        plot.legend(bbox_to_anchor = (1.0, 1), loc = 'upper left')
        # plot.text(event[0],ymax/2+offset if seaborn == 0 else offset,event[1],rotation=90,rotation_mode="anchor")
        # plot.annotate(text=event[1], xy=(event[0],offset),arrowprops=dict(facecolor='black', shrink=0.05))