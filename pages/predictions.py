# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#mport joblib
#from joblib import load
import numpy as np
import pandas as pd
from app import app

occupation = ['Machine-op-inspct', 'Farming-fishing', 'Protective-serv',
       'Prof-specialty', 'Other-service', 'Craft-repair', 'Adm-clerical',
       'Exec-managerial', 'Tech-support', 'Sales', 'Priv-house-serv',
       'Transport-moving', 'Handlers-cleaners', 'Armed-Forces']

education = ['Preschool','Elementary','Junior High','High School',
        'Professional School','Some College','Associates VoTech',
        'Associates College','Bachelors','Masters','Doctorate','Prof College']

maritalstatus = ['Never-married','Married-Civilian-Spouse','Widowed',
        'Divorced','Separated','Married-pouse-absent','Married-ArmedForces-spouse']
race = ['Black', 'White', 'Asian-Pac-Islander', 'Other',
       'Amer-Indian-Eskimo']
       
style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Here we are.  Use the drop down menu and slides to change values and predict whether that person
            would be Male or Female.  Then try out your stats and see if the prediction was correct.  Fill out 
            the form and let me know how if it got it right.  I look forward to seeing how it went.

    
    """), 

    html.Div([
        dcc.Markdown('###### Age'), 
        dcc.Slider(
            id='age', 
            min=15,
            max=90,
            step=1,
            value=25, 
            marks={n: f'{n/1:.0f}' for n in range(15,90,10)} 
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Highest Education'), 
        dcc.Dropdown(
            id='education', 
            options=[{'label': purpose, 'value': purpose} for purpose in education], 
            value=education[0]
        ),
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Marital Status'), 
        dcc.Dropdown(
           id='maritalstatus', 
            options=[{'label': purpose, 'value': purpose} for purpose in maritalstatus], 
            value=maritalstatus[0]
        ),  
    ], style=style),

    html.Div([
        dcc.Markdown('###### Occupation'), 
        dcc.Dropdown(
            id='occupation', 
            options=[{'label': purpose, 'value': purpose} for purpose in occupation], 
            value=occupation[0]
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('###### Race'), 
        dcc.Dropdown(
            id='race', 
            options=[{'label': purpose, 'value': purpose} for purpose in race], 
            value=race[0]
        )
    ], style=style),

    dcc.Markdown('### Prediction'), 
    html.Div(id='prediction-content', style={'marginBottom': '5em'}), 

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('annual-income', 'value'),
     Input('credit-score', 'value'),
     Input('loan-amount', 'value'),
     Input('loan-purpose', 'value'),
     Input('monthly-debts', 'value')])
def predict(annual_income, credit_score, loan_amount, loan_purpose, monthly_debts):

    df = pd.DataFrame(
        columns=['Annual Income', 'Credit Score', 'Loan Amount', 'Loan Purpose', 'Monthly Debts'], 
        data=[[annual_income, credit_score, loan_amount, loan_purpose, monthly_debts]]
    )

    #pipeline = load('model/pipeline.joblib')
    #y_pred_log = pipeline.predict(df)
    #y_pred = np.expm1(y_pred_log)[0]

    #return f'Interest rate for 36 month loan: {y_pred:.2f}%'