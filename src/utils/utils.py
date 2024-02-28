
# Modify the Transaction date column
def date_modify(x):
    val=int((x-int(x))*365)
    month_number=val//30
    day_number=val-month_number*30
    if day_number==0: day_number=1
    if month_number!=12: month_number+=1
    return f"{str(day_number).zfill(2)}-{str(month_number).zfill(2)}-{int(x)}"

# Split the data into train and test part
def data_split(df,test_size_percentage=0.25):
    test_size=int(df.shape[0]*test_size_percentage)
    test_data = df.sample(n=test_size, random_state=42)
    train_data = df[~df.isin(test_data)].dropna()
    return train_data, test_data

# Seperate the dependent and independent variables
def get_features_target(data, dependent_variable):
    X=data.drop(dependent_variable, axis=1)
    y=data[dependent_variable]
    return X, y
       

