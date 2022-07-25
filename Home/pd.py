import pandas as pd


# df = pd.read_csv('data.csv')
# print(df.to_string())
mydataset = {
    'car': ["BMW", 'Volvo', 'Ford'],
    'Passings': [3, 7,2]
}

my_var = pd.DataFrame(mydataset)