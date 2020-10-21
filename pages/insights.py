# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
           When I began working with my dataset the original prediction was to tell if 
           someone was making more or less than 50K as their annual income.  With only a 
           little time to work with the data the challenge was to use the information to 
           predict something new so I thought insight into whether the values indicated 
           a Male of Female would be an interesting Machine Learning model.  I was more 
           more shocked that the accuracy was pretty good for the information that was 
           fed to the model.  I did a few work arounds and made new features that allowed 
           the data submissions to read each other in a more cohessive manner.  I found the
           best model was working with the XGBClassifier.  It gave me the best scores off the
           bat with my training and validation sets and worked great on my Test set as well.


            """
        ),

    ],
)

layout = dbc.Row([column1])

column2 = dbc.Col(
    [
       
    ])