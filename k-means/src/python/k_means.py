import random
import math
import sys
import threading


class Kmeans(threading.Thread):
    def __init__(self,datas,num_of_cluster,num_of_steps,object):
        threading.Thread.__init__(self)
        self.datas = datas
        self.num_of_cluster = num_of_cluster
        self.num_of_steps = num_of_steps
        self.object = object

    def run(self):
        self.core()

    def initialization(self):
        return random.sample(list(self.datas.values()), self.num_of_cluster)

    def core(self):
        centroids = self.initialization()

        i=0
        while True:
            print(i," step : ",centroids)
        
            cluster = {}
            for centroid in centroids:
                cluster[tuple(centroid)]=[]

            for data in self.datas.items():
                min = sys.maxsize
                for centroid in centroids:
                    if min > self.distance(data[1], centroid):
                        min = self.distance(data[1], centroid)
                        which_cluster = tuple(centroid)

                cluster[which_cluster].append(data)

            next_centroids = []
            for (_, each) in cluster.items():
                next_centroids.append( self.average(each) )


            result_data = self.convert_data_from(cluster)
            
            if centroids != next_centroids and i < self.num_of_steps:
                #continue condition
                self.object.core_intermediate(result_data, centroids)
                centroids = next_centroids
            else:
                #exit condition                
                self.save_Cluster(cluster,self.datas)
                self.object.core_result(result_data)
                return
                
            i=i+1



    def save_Cluster(self,cluster,datas):
        i=1
        for key in cluster.keys():
            fout = open(str(self.num_of_cluster)+"_"+str(i)+".dat","w")

            for each in cluster[key]:                
                coorvalue = each[0]
                fout.write(str(datas[coorvalue][0])+" "+str(datas[coorvalue][1])+" "+str(datas[coorvalue][2])+"\n")

            fout.write("\n")
            i=i+1
        fout.close()


           


    @staticmethod
    def distance(point1, point2):
        return math.sqrt(math.pow(point1[0] - point2[0],2) + math.pow(point1[1]-point2[1],2) + math.pow(point1[2]-point2[2],2))
    
    @staticmethod
    def convert_data_from(result_cluster):
        datas = {}
        for centroids in result_cluster.keys():
            for each in result_cluster[centroids]:
                datas[each[0]] = centroids
        return datas

    @staticmethod
    def average(items):
        sumx=0; sumy=0; sumz=0;
        for item in items:
            x,y,z,_ = item[1]
            sumx += x
            sumy += y
            sumz += z

        return [int(sumx/len(items)),int(sumy/len(items)),int(sumz/len(items)),255]









