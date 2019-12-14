import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %matplotlib inline

from sklearn.cluster import KMeans, SpectralClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score

class Cluster:
    def __init__(self):
        pass
    def sendCoordandTeam(self,lat_long,n_teams):
        self.lat_long = lat_long
        self.n_teams = n_teams
        self.df = pd.DataFrame(lat_long,columns=['lat','long'])
    def getAllCoordinates(self):
        return self.lat_long
    def fit(self):
        self.km = KMeans(n_clusters=self.n_teams, max_iter=100)
        self.km.fit(self.df)
    def getCentroids(self):
        centroids = self.km.cluster_centers_
#         print(centroids)
        return centroids
    def getClasses(self):
        return self.km.labels_