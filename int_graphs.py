#%%
import pandas as pd
import altair as alt
#%%
inf_prob = (.99, .5, .01) #inf_prob const TODO: input the infection probability here
end_inf_prob = (0.5, 1) #end_inf_prob const TODO: input the end infection probability here
grey_nodes = 0 #number of dead nodes TODO: change this number based on scenario
#%%
data = pd.read_csv('/Users/victortu/Desktop/NetLogo 6.2.2/NetLogo Projects/Netlogo Generated Files/Scenario1_d1.csv')

df = data[['[run number]', 'end-infection-prob', 'infection-prob', 'count turtles with [removed?]','ticks']]

df['total turtles that died from spread'] = df['count turtles with [removed?]'] - grey_nodes

#%% i want to make an interactive graph, 3 graphs (reflecting each inf_prob) 2 lines per graph(reflecting each end_inf_prob)

def subset(df, inf_prob: float, end_inf_prob:float):

    subset = df.loc[(df['infection-prob'] == inf_prob) & (df['end-infection-prob'] == end_inf_prob)]

    return subset

#%%
sub_df_5 = subset(df, .99, .5)
sub_df_1 = subset(df, .99, 1)

#in this scenario, with an infection rates of ___ and an end infection rate ofs ___
#there was a total of ___ plants that died