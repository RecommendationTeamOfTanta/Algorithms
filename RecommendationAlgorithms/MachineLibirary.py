
def	split_data(data,prob):
#split data into fractions [prob, 1 - prob]"""
    results = [],[]
    for	row	in	data:
        results[0 if random.random() < prob else 1].append(row)
    return results


#split to train and test
def	train_test_split(x,y,test_pct):
    #pair corresponding values
    data = zip(x,y)				
    #split the data set of pairs
    train,test = split_data(data,1 - test_pct)		
    #magical un-zip trick
    x_train,y_train = zip(*train)						
    x_test,y_test = zip(*test)
    return x_train,x_test,y_train,y_test