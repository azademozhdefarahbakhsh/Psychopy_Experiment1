import pandas as pd

def save_data(responses, filename='data/results.csv'):
    df = pd.DataFrame(responses, columns=['Trial', 'Response'])
    df.to_csv(filename, index=False, sep=';')
