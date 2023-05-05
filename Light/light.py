import json
import pandas as pd
from sklearn.cluster import KMeans
import datetime
from time import strftime, localtime

# Open file
with open('light.json', 'r') as f:
    # Load the contents of the file into a list
    dataList = json.load(f)
# parsing the list into a dictionary that fit dataframe
data = {
    'timeon': [],
    'state': []
}

for item in dataList:
    timeon = item['timeon']
    res = strftime('%Y-%m-%d %H:%M:%S', localtime(timeon))
    data['timeon'] += [res]
    data['state'] += [item['state']]
df = pd.DataFrame(data)
bias = -14000
# Filter out and keep only the "1" state
df['state'] = pd.to_numeric(df['state'])
df = df[df['state'] == 1].reset_index(drop=True)
print(df)
# Cutting date out of datetime, than parsing time into int of seconds
df['timeon'] = pd.to_datetime(df['timeon'], format='%Y-%m-%d %H:%M:%S')
df['time'] = df['timeon'].apply(lambda x: pd.to_datetime(x).time())
df['time'] = df['time'].apply(lambda x: int(x.hour * 3600 + x.minute * 60 + x.second + bias))
print(df)
# Extract the feature
x_train_df = df.loc[:, ['time']].copy()
x_train = x_train_df.values
x_train = x_train.reshape(-1,1)
print(x_train)
# Fit a KMeans clustering model and extract the clusters
kmeans = KMeans(n_clusters=3, random_state=0).fit(x_train)
ans = kmeans.cluster_centers_.tolist()
ans = [] + ans[0] + ans[1] + ans[2]
print(ans)
# Parsing number into time and print the final ans
for i in range(len(ans)): 
    ans[i] = int(ans[i])
    hours, remainder = divmod(ans[i], 3600)
    minutes, seconds = divmod(remainder, 60)
    ans[i] = datetime.time(hours, minutes, seconds).strftime('%H:%M:%S')
print(ans)