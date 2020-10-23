# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
#from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Gender Calculated Insights

            What if you had some insights into a persons life and you could use it to find out if the
            individual was a Male of Female.  This app is little fun setup where you can change your
            values and make a prediction whether or not this information believes the person would be 
            Male of Female.  When you are done working with the prediction portion of the model I'd love
            to hear feedback, please click the google symbol to be redirected to a google form to fill in
            your specific data and let me know it your prediction was correct with your real life values.
           
           Feel free to toggle Male and Female and hover over the dots to get a feel for the 
           data and when your all set click the link below to make some predictions and submit your results.
           
            """
        ),
        dcc.Link(dbc.Button('Lets Predict', color='btn btn-info'), href='/predictions')
    ],
    md=4,
)
gender_prop = pd.read_csv('https://raw.githubusercontent.com/VPDeb/Build-Gender-Bias-Insight-App/master/pages/testdata.csv')
df = px.data.iris()
fig = px.scatter(gender_prop, x="occupation", y="native-country",color="gender-F/1-M/0",
                size='age', hover_data=['education'],labels={'gender-F/1-M/0':'Male/Female','education':'Education',
                                                                 'age':'Age','native-country':'Native Country','occupation':'Occupation'},
                title='Gender Bias Insights',width=800, height=700)
fig.update_layout(legend = dict(bgcolor ='gray'),paper_bgcolor="black",plot_bgcolor='black')

column2 = dbc.Col(
   [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
