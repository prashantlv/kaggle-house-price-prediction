
def process_data(data):
    columns = list(data)
    for c in columns:
        if data[c].dtype == 'O':
            data[c].fillna('Missing', inplace = True)
        else:
            data[c].fillna(value=data[c].mode, inplace = True) 
    print("All null value removed.")
    return data            

def set_index(data, index):
    print("Index set to ID ")
    return data.set_index(index,inplace = True)


if __name__ == '__main__' :
    pass    
