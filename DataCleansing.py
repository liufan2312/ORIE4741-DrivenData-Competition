import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


training_set = pd.read_csv("Training Set.csv")
training_label = pd.read_csv("Training Set Labels.csv")
all_data = pd.merge(training_set, training_label, how="left", on="id")
print(all_data.shape)
all_data.head()


feature_list = ['amount_tsh', 'date_recorded', 'funder', 'gps_height', 'installer', 'longitude', 'latitude', 'basin',
 'subvillage', 'region', 'region_code', 'district_code', 'lga', 'ward', 'population', 'public_meeting', 'scheme_management',
 'permit', 'construction_year', 'extraction_type_group', 'extraction_type_class', 'management', 'payment_type', 'water_quality',
 'quantity', 'source_type', 'source_class', 'waterpoint_type', 'status_group']

all_data = all_data[feature_list]
print(all_data.shape)
all_data.head()

# ### "amount_tsh" - total static head (amount water available to waterpoint)

# In[21]:

all_data["amount_tsh"].describe()


# In[57]:

plt.hist(all_data["amount_tsh"], 100)
plt.show()
#print(all_data[all_data["amount_tsh"] > 50000].shape)


# There is obivous outliers, we should remove those.

# ### "date_recorded" - the date the row was entered

# In[16]:

print(all_data["date_recorded"].describe())
print("Number of empty cells: ", all_data["date_recorded"].isnull().sum())


# ### "funder" - who funded the we

# In[26]:

print(all_data["funder"].describe())
print("Number of empty cells: ", all_data["funder"].isnull().sum())


# ### "gps_height" - altitude of the well

# In[29]:

print(all_data["gps_height"].describe())
print("Number of empty cells: ", all_data["gps_height"].isnull().sum())


# In[30]:

plt.hist(all_data["gps_height"], 100)
plt.show()


# Tanzania's elevation extremes: 0m - 5895m (according to Wikipedia), **does that mean those with gps_height < 0 are wrong?**

# ### "installer" - organization that installed the well

# In[31]:

print(all_data["installer"].describe())
print("Number of empty cells: ", all_data["installer"].isnull().sum())


# ### "longitude"

# In[33]:

print(all_data["longitude"].describe())
print("Number of empty cells: ", all_data["longitude"].isnull().sum())


# In[36]:

plt.hist(all_data["longitude"], 50)
plt.show()


# Remove obvious outliers

# ### "latitude"

# In[38]:

print(all_data["latitude"].describe())
print("Number of empty cells: ", all_data["latitude"].isnull().sum())


# In[39]:

plt.hist(all_data["latitude"], 50)
plt.show()


# ### "basin" - geographic water basin

# In[40]:

print(all_data["basin"].describe())
print("Number of empty cells: ", all_data["basin"].isnull().sum())


# In[46]:

group = all_data.groupby(["basin"]).size().sort_values(ascending=False)
group_name = group.index.tolist()
ind = np.arange(len(group_name))

width = 0.5

plt.bar(ind, group, width)

plt.ylabel("Count")
plt.xticks(ind + width/2., group_name)
plt.xlim(-0.5, len(group_name))
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# ### "subvillage" - geographic location

# In[47]:

print(all_data["subvillage"].describe())
print("Number of empty cells: ", all_data["subvillage"].isnull().sum())


# ### "region" - geographic location

# In[48]:

print(all_data["region"].describe())
print("Number of empty cells: ", all_data["region"].isnull().sum())


# In[49]:

group = all_data.groupby(["region"]).size().sort_values(ascending=False)
group_name = group.index.tolist()
ind = np.arange(len(group_name))

width = 0.5

plt.bar(ind, group, width)

plt.ylabel("Count")
plt.xticks(ind + width/2., group_name)
plt.xlim(-0.5, len(group_name))
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# ### "region_code" - geographic location (coded)

# In[50]:

print(all_data["region_code"].describe())
print("Number of empty cells: ", all_data["region_code"].isnull().sum())


# We should treat region code as object.

# ### "lga" - geographic location

# In[52]:

print(all_data["lga"].describe())
print("Number of empty cells: ", all_data["lga"].isnull().sum())


# ### "ward" - geographic location

# In[53]:

print(all_data["ward"].describe())
print("Number of empty cells: ", all_data["ward"].isnull().sum())


# ### "population" - population around the well

# In[54]:

print(all_data["population"].describe())
print("Number of empty cells: ", all_data["population"].isnull().sum())


# In[61]:

plt.hist(all_data["population"], 200)
plt.show()


# In[68]:

#a = all_data[all_data["population"] == 0]
#a.groupby(["status_group"]).size()


# We should remove the obvious outliers. And why so many 0 population?!

# ### "public_meeting" - True/False

# In[58]:

print(all_data["public_meeting"].describe())
print("Number of empty cells: ", all_data["public_meeting"].isnull().sum())


# ### "scheme_management" - who operates the waterpoint

# In[59]:

print(all_data["scheme_management"].describe())
print("Number of empty cells: ", all_data["scheme_management"].isnull().sum())


# ### "permit" - if the waterpoint is permitted

# In[60]:

print(all_data["permit"].describe())
print("Number of empty cells: ", all_data["permit"].isnull().sum())


# ### "construction_year" - year the waterpoint was constructed

# In[69]:

print(all_data["construction_year"].describe())
print("Number of empty cells: ", all_data["construction_year"].isnull().sum())


# In[72]:

# Check how many different years
print(all_data[all_data["construction_year"] != 0]["construction_year"].describe())


# We should treat this as categorical data

# ### "extraction_type_group" - the kind of extraction the waterpoint uses

# In[73]:

print(all_data["extraction_type_group"].describe())
print("Number of empty cells: ", all_data["extraction_type_group"].isnull().sum())


# ### "extraction_type_class" - the kind of extraction the waterpoint uses

# In[74]:

print(all_data["extraction_type_class"].describe())
print("Number of empty cells: ", all_data["extraction_type_class"].isnull().sum())


# In[75]:

group = all_data.groupby(["extraction_type_class"]).size().sort_values(ascending=False)
group_name = group.index.tolist()
ind = np.arange(len(group_name))

width = 0.5

plt.bar(ind, group, width)

plt.ylabel("Count")
plt.xticks(ind + width/2., group_name)
plt.xlim(-0.5, len(group_name))
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# ### "management" - how the waterpoint is managed

# In[76]:

print(all_data["management"].describe())
print("Number of empty cells: ", all_data["management"].isnull().sum())


# In[77]:

group = all_data.groupby(["management"]).size().sort_values(ascending=False)
group_name = group.index.tolist()
ind = np.arange(len(group_name))

width = 0.5

plt.bar(ind, group, width)

plt.ylabel("Count")
plt.xticks(ind + width/2., group_name)
plt.xlim(-0.5, len(group_name))
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# We probably need some cleansing for this column as well, combine unknown with other maybe?

# ### "payment_type" - what the water costs

# In[78]:

print(all_data["payment_type"].describe())
print("Number of empty cells: ", all_data["payment_type"].isnull().sum())


# In[79]:

group = all_data.groupby(["payment_type"]).size().sort_values(ascending=False)
group_name = group.index.tolist()
ind = np.arange(len(group_name))

width = 0.5

plt.bar(ind, group, width)

plt.ylabel("Count")
plt.xticks(ind + width/2., group_name)
plt.xlim(-0.5, len(group_name))
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# ### "water_quality" - the quality of the water

# In[80]:

print(all_data["water_quality"].describe())
print("Number of empty cells: ", all_data["water_quality"].isnull().sum())


# ### "quantity" - the quantity of the water

# In[81]:

print(all_data["quantity"].describe())
print("Number of empty cells: ", all_data["quantity"].isnull().sum())


# ### "source_type" - the source of the water

# In[82]:

print(all_data["source_type"].describe())
print("Number of empty cells: ", all_data["source_type"].isnull().sum())


# ### "source_class" - the source of the water

# In[83]:

print(all_data["source_class"].describe())
print("Number of empty cells: ", all_data["source_class"].isnull().sum())


# ### "waterpoint_type" - the kind of waterpoint

# In[84]:

print(all_data["waterpoint_type"].describe())
print("Number of empty cells: ", all_data["waterpoint_type"].isnull().sum())


# In[ ]:
