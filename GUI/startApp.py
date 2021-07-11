import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from GUI import kmeans
import elbowKmeans
import elbowKmeansPl
import dbscan
import fuzzc
import spectralClustering
import meanShift
from GUI import kmeans
inputRasterFolder=''
outputFolder = ''


def UploadAction1(event=None):
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    print('Selected:', filename)
    inputRasterFolder = filename
    return inputRasterFolder

def UploadAction2(event=None):
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    print('Selected:', filename)
    outputFolder = filename
    return outputFolder


def main():

    def judgeAlg():
        root.destroy()
        target = v2.get()
        if target == 'k-means/k-means++':
            kmeans.kmeansGUI().Main()
        elif target == 'elbow-kmeans':
            elbowKmeans.main()
        elif target == 'elbow-kmeans++':
            elbowKmeansPl.main()
        elif target == 'DBscan':
            dbscan.main()
        elif target == 'fuzzCMeans':
            fuzzc.main()
        elif target == 'meanShift':
            meanShift.main()
        elif target == 'spectral Clustering':
            spectralClustering.main()

    def elbowAlgSelected():
        selectBtn1.state(['pressed'])
        selectBtn2.state(['!pressed'])
    def simpleAlgSelected():
        selectBtn1.state(['!pressed'])
        selectBtn2.state(['pressed'])

    root = tk.Tk()
    root.title("rasterMiner: Discovering Knowledge Hidden in Raster Images")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Convert Raster Files to CSV File')
    tabControl.add(tab2, text='Pattern Mining')
    tabControl.add(tab3, text='Clustering')
    tabControl.add(tab4, text='Classification')
    tabControl.add(tab5, text='Prediction')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab1, text='Select the folder containing raster files:').grid(column=0, row=0, padx=30, pady=30,sticky = 'W')
    ttk.Label(tab1, text='Enter the file extension of the raster files:').grid(column=0, row=1, padx=30, pady=30,sticky = 'W')
    ttk.Label(tab1, text='Select output folder:').grid(column=0, row=2, padx=30, pady=30,sticky = 'W')
    ttk.Label(tab1, text='Type of Append').grid(column=0, row=3, padx=30, pady=30, sticky='W')
    ttk.Label(tab3, text='Select algorithm',font=("Arial", 20)).place(relx=0,rely=0,relwidth=1,relheight=0.125)

    # make textbox
    inputrasterFolderName = tk.StringVar()
    outputFolderName = tk.StringVar()
    e1 = tk.Entry(tab1,textvariable=inputrasterFolderName)
    e2 = tk.Entry(tab1)
    e3 = tk.Entry(tab1,textvariable=outputFolderName)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)


    button1 = tk.Button(tab1, text='Browse', command=lambda: inputrasterFolderName.set(UploadAction1()))
    button1.grid(row=0,column=2)
    button2 = tk.Button(tab1, text='Browse',command=lambda: outputFolderName.set(UploadAction2()))
    button2.grid(row=2,column=2)
    submit = tk.Button(tab1,text='submit')
    submit.grid(row=4,column=0)

    #button3 = tk.Button(tab3, text='submit', command=)

    Type = ['None', 'Horizontal', 'Vertical']
    v1 = tk.StringVar()
    cb = ttk.Combobox(tab1, textvariable=v1,values=Type,state='readonly')
    cb.grid(column=1, row=3, padx=30, pady=30, sticky='W')
    cb.set(Type[0])
    Algorithms = {'elbowAlg':["elbow-kmeans", "elbow-kmeans++"], 'simpleAlg': ["k-means/k-means++", "DBscan", "Spectral Clustering", "MeanShift","fuzzyCMeans" ]}

    #v2 = tk.StringVar()
    selectBtn1 = ttk.Button(tab3,text='elbowAlg',padding=(10),command=elbowAlgSelected)
    selectBtn1.bind('<1>', lambda e: cb2.config(values=Algorithms['elbowAlg']))
    selectBtn2 = ttk.Button(tab3,text='simpleAlg',padding=(10),command=simpleAlgSelected)
    selectBtn2.bind('<1>', lambda e: cb2.config(values=Algorithms['simpleAlg']))
    selectBtn1.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.125)
    selectBtn2.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.125)
    #selectBtn1.grid(row=1,column=1,sticky='W')
    #selectBtn2.grid(row=1,column=2,sticky='W')
    #cb1 = ttk.Combobox(tab3, textvariable=v2,values=list(Algorithms.keys()),state='readonly')
    #cb1.grid(column=1, row=0, padx=30, pady=30, sticky='W')
    # cb1.bind(
    #      '<<ComboboxSelected>>',
    #      lambda e: cb2.config(values=Algorithms[v2.get()]))
    v2 = tk.StringVar()
    cb2 = ttk.Combobox(tab3,textvariable=v2,values=list(Algorithms.values()),state='readonly')
    cb2.place(relx=0.25,rely=0.5,relwidth=0.5)
    #print(str(v2.get))
    submit = ttk.Button(tab3,text='submit',command=judgeAlg)
    submit.place(relx=0.378,rely=0.7,relwidth=0.25,relheight=0.125)
    # ttk.Label(tab2, text='Input csv file:').grid(column=0, row=0, padx=30, pady=30)
    root.mainloop()

if __name__ == '__main__':
    main()
