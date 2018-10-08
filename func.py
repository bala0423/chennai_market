from colmn import column
from sklearn.externals import joblib
import numpy as np

def make_dictionary (charge_weight, pieces, agent_code):
    dictn = {}
    for i in column:
        dictn[i] = 0

    dictn['Pieces'] = pieces
    dictn['Chargewt'] = charge_weight
    agent = "agent_"+agent_code
    dictn[agent] = 1

    return dictn

def iterations(charge_weight, pieces, agent, weight_variability=10, piece_variability=5):

    weight_lower = charge_weight - weight_variability
    weight_higher = charge_weight + weight_variability + 1
    piece_lower = pieces - piece_variability
    piece_higher = pieces + piece_variability + 1

    if weight_lower < 0 :
        weight_lower = 0

    if piece_lower < 0:
        piece_lower = 1

    piece_range = range(piece_lower, piece_higher)
    weight_range = range(weight_lower, weight_higher)
    iterations = [[i, j, k] for i in weight_range for j in piece_range for k in [agent]]

    return iterations


#def make_x_list(Pieces,Chargewt,agent_code):

def predict

val_v = iterations(2,2,'agent_KINGSMAN')

input = []
for element in val_v:

    charge_weight, pieces, agent = element
    dict = make_dictionary(10,5,'VELTABBS')
    input.append(list(dict.values()))


model = joblib.load('prediction_with_ChargeWeight_pieces_and_agents.pkl')

#print(input)
p_predict = model.predict(np.array(input))



#print(val_v)

print(p_predict.mean())
