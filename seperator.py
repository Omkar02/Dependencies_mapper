import pandas as pd


df = pd.read_csv('modified.csv',
                 index_col='script_name',
                 header=0,
                 names=['what', 'script_name', 'Date', 'Time', 'status', 'id'])


df['Date'] = pd.to_datetime(df['Date']).dt.date
df['Time'] = pd.to_datetime(df['Time']).dt.time
# print(df.groupby(['script_name', 'id'])['Time'].agg({'Start':[min], 'Finish':[max]}))
df.groupby(['script_name', 'id'])['Time'].agg(Start=('min'), Finish=('max')).to_csv(r'export_dataframe.csv', index='script', header=True)

# script_name,id,Start,Finish
# job1,4job1,02:41:11,03:01:11

fig = ff.create_gantt(df.groupby(['script_name', 'id'])['Time'].agg(Start=('min'), Finish=('max')),
                      colors=False,
                      index_col='script_name',
                      title='Daily Schedule',
                      show_colorbar=True,
                      bar_width=0.1,
                      showgrid_x=True,
                      showgrid_y=True,
                      group_tasks=True)
'''-------------------------------------------------------------------------------------------------------'''
# import plotly.figure_factory as ff

# import pandas as pd
# df = [dict(Task="11", Start='2020-02-17 00:00:00', Finish='2020-02-17 02:01:11', Resource='j1'),
#       dict(Task="11", Start='2020-02-17 02:41:11', Finish='2020-02-17 03:01:11', Resource='j1'),
#       dict(Task="21", Start='2020-02-17 02:21:11', Finish='2020-02-17 02:51:11', Resource='j2'),
#       dict(Task="31", Start='2020-02-17 02:31:11', Finish='2020-02-17 02:59:11', Resource='j3')]

# colors = dict(j1='rgb(46, 137, 205)',
#               j2='rgb(114, 44, 121)',
#               j3='rgb(198, 47, 105)',
#               )

# # fig = ff.create_gantt(df, colors=colors, index_col='Task', title='Daily Schedule',
# #                       show_colorbar=True, bar_width=0.1, showgrid_x=True, showgrid_y=True,group_task= True)

# fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule', show_colorbar=True, bar_width=0.1, showgrid_x=True, showgrid_y=True,
#                       group_tasks=True)
# fig.show()
