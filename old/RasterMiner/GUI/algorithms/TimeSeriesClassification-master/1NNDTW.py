import numpy as np
#import math
import os
import psutil

import time
#from dtaidistance import dtw
#from tslearn.metrics import dtw_limited_warping_length
import sys

class OneNNDTW:
    """"""
    def __init__(self, inputTrainingFile, inputTestingFile):
        """Constructor for OneNNDTW"""
        self.training = np.loadtxt(inputTrainingFile, delimiter='\t')
        self.testing = np.loadtxt(inputTestingFile, delimiter='\t')

    def dtw(self, A, B):
        N = len(A)
        M = len(B)
        d = np.zeros((N, M))
        for n in range(N):
            for m in range(M):
                d[n][m]=(A[n]-B[m])**2
        D=np.zeros(d.shape)
        D[0][0]=d[0][0]
        for n in range(1,N):
            D[n][0]=d[n][0]+D[n-1][0]
        for m in range(1,M):
            D[0][m]=d[0][m]+D[0][m-1]
        for n in range(1,N):
            for m in range(1,M):
                D[n][m]=d[n][m]+min(D[n-1][m],D[n-1][m-1],D[n][m-1])
        return D[N-1][M-1]


    # training = np.loadtxt(sys.argv[1], delimiter='\t')
    # testing = np.loadtxt(sys.argv[2],  delimiter='\t')
    def run(self):
        num_rows_test, num_columns_test = self.testing.shape
        num_rows_train, num_columns_train = self.training.shape
        training_noclass=self.training[:,1:]
        testing_noclass=self.testing[:,1:]

        predicted_label = None
        correct = 0
        start_time = time.time()
        for i in range(num_rows_test):
            #print(i)
            least_distance = float('inf')
            for j in range(num_rows_train):
                dist = self.dtw(testing_noclass[i], training_noclass[j])
                if dist < least_distance:
                    predicted_label = self.training[j][0]
                    least_distance = dist
            if predicted_label == self.testing[i][0]:
                correct = correct + 1


        accuracy = (correct/num_rows_test) * 100
        print("Datasetname:",sys.argv[1])
        print("Total Accuracy of oneNNDTW is:", accuracy)

        print("Total Execution time oneNNDTW is:", time.time() - start_time)
        process = psutil.Process(os.getpid())
        memory = process.memory_full_info().uss
        memory_in_KB = memory / (1024)
        print("Total Memory of oneNNDTW inKB",memory_in_KB)  # in bytes

        #Windows = dtw.distance(testing[i], training[j])  # math.sqrt(squaring)
if __name__ == '__main__':
    obj = OneNNDTW(sys.argv[1], sys.argv[2])
    obj.run()
