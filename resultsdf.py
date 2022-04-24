#%% packages
import pandas as pd
import statistics as s

#%%
inf_prob = (.99, .5, .01) #inf_prob const TODO: input the infection probability here
end_inf_prob = (0.5, 1) #end_inf_prob const TODO: input the end infection probability here
grey_nodes = 50 #number of dead nodes TODO: change this number based on scenario
#%% reading csv file
data = pd.read_csv('/Users/victortu/Desktop/NetLogo 6.2.2/NetLogo Projects/Netlogo Generated Files/Scenario3_d2.csv')

#%% only keep specific columns
df = data[['[run number]', 'end-infection-prob', 'infection-prob', 'count turtles with [removed?]','ticks']]

#%% creating total turtles that died from spread column
df['total turtles that died from spread'] = df['count turtles with [removed?]'] - grey_nodes

#%% finding average duration
def avg_dur(df, inf_prob: tuple, end_inf_prob: tuple):

    subset1 = df.loc[(df['infection-prob'] == inf_prob[0]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset2 = df.loc[(df['infection-prob'] == inf_prob[0]) & (df['end-infection-prob'] == end_inf_prob[1])]

    subset3 = df.loc[(df['infection-prob'] == inf_prob[1]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset4 = df.loc[(df['infection-prob'] == inf_prob[1]) & (df['end-infection-prob'] == end_inf_prob[1])]

    subset5 = df.loc[(df['infection-prob'] == inf_prob[2]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset6 = df.loc[(df['infection-prob'] == inf_prob[2]) & (df['end-infection-prob'] == end_inf_prob[1])]

    avg_dur = (s.mean(subset1['ticks']),
               s.mean(subset2['ticks']),
               s.mean(subset3['ticks']),
               s.mean(subset4['ticks']),
               s.mean(subset5['ticks']),
               s.mean(subset6['ticks']))

    return avg_dur

#%% finding st. deviation of ticks
def st_dev(df):

    st_dev = s.stdev(df['ticks'])

    return st_dev

#%% finding mean removed column
def mean_removed(df, inf_prob: tuple, end_inf_prob: tuple):

    subset1 = df.loc[(df['infection-prob'] == inf_prob[0]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset2 = df.loc[(df['infection-prob'] == inf_prob[0]) & (df['end-infection-prob'] == end_inf_prob[1])]

    subset3 = df.loc[(df['infection-prob'] == inf_prob[1]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset4 = df.loc[(df['infection-prob'] == inf_prob[1]) & (df['end-infection-prob'] == end_inf_prob[1])]

    subset5 = df.loc[(df['infection-prob'] == inf_prob[2]) & (df['end-infection-prob'] == end_inf_prob[0])]

    subset6 = df.loc[(df['infection-prob'] == inf_prob[2]) & (df['end-infection-prob'] == end_inf_prob[1])]

    mean_removed = (s.mean(subset1['total turtles that died from spread']),
                    s.mean(subset2['total turtles that died from spread']),
                    s.mean(subset3['total turtles that died from spread']),
                    s.mean(subset4['total turtles that died from spread']),
                    s.mean(subset5['total turtles that died from spread']),
                    s.mean(subset6['total turtles that died from spread']))

    return mean_removed

#%% finding standard deviation of all removed turtles
def std_removed(df):

    std_removed = s.stdev(df['total turtles that died from spread'])

    return std_removed

#%% generating the results dataframe
def resultsdf(df, inf_prob: tuple, end_inf_prob: tuple):

    ip  = (inf_prob[0],inf_prob[0],inf_prob[1],inf_prob[1],inf_prob[2],inf_prob[2])
    eip = (end_inf_prob[0],end_inf_prob[1],end_inf_prob[0],end_inf_prob[1],end_inf_prob[0],end_inf_prob[1])

    results = {'infection probability': ip,
               'end infection probability': eip,
               'mean duration': avg_dur(df, inf_prob, end_inf_prob),
               'st. deviation of ticks': st_dev(df),
               'mean removed': mean_removed(df, inf_prob, end_inf_prob),
               'st. deviation of removed turtles': std_removed(df)

    }

    resultsdf = pd.DataFrame(results)

    return resultsdf

#%% exporting results dataframe to a csv file
def export_csv(df, inf_prob, end_inf_prob, filename):
    res_df = resultsdf(df, inf_prob, end_inf_prob)

    res_df.to_csv(f'/Users/victortu/Desktop/NetLogo 6.2.2/NetLogo Projects/Results Files/{filename}.csv', index = False)

#%%
export_csv(df, inf_prob, end_inf_prob, 'scenario3_d2_results')