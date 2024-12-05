import os
import subprocess

def unpackMRTs(folder, outputFolder):
    running = []
    print("Unpacking MRTs")
    for file in os.listdir(folder):
        command = 'bgpscanner '+folder+'/'+file+' > '+outputFolder+'/'+file+'.txt'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        running.append(process)
        if len(running) >= 16:
            for process in running:
                process.wait()
                running.remove(process)
    for process in running:
        process.wait()
    print("Done Unpacking")
    