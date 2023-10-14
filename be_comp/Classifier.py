import pickle

filename = "finalized_class_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

result = loaded_model.predict([[2.9587, 88.21,69.13, 0.021, 1.72, 10.02]])
print(result)

def classify(input): 
    # Convert the dictionary values to a list
    data_list = list(input.values())
    # Print the resulting list
    print(data_list)
    flag = loaded_model.predict([data_list])
    print(flag)
    return "Upward" if flag == 1 else "Downward"