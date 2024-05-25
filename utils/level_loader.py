def load_level_data( path : str )->list[str]:
    data = []
    with open(path,'r') as file:
        lines = file.readlines()
        for line in lines:
            processed_line = line.replace(' ','').replace('\n','')
            data.append( processed_line )
    return data