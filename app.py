import pickle
from flask import Flask, request, render_template


app = Flask(__name__)

model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def html():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        year = int(request.form['year'])

        km_driven = int(request.form['km_driven'])

        fuel_type = request.form['fuel_type']

        if fuel_type == 'Petrol':
            fuel_Diesel = 0
            fuel_Electric = 0
            fuel_LPG = 0
            fuel_Petrol = 1
        elif fuel_type == 'Diesel':
            fuel_Diesel = 1
            fuel_Electric = 0
            fuel_LPG = 0
            fuel_Petrol = 0
        elif fuel_type == 'Electric':
            fuel_Diesel = 0
            fuel_Electric = 1
            fuel_LPG = 0
            fuel_Petrol = 0
        elif fuel_type == 'LPG':
            fuel_Diesel = 0
            fuel_Electric = 0
            fuel_LPG = 1
            fuel_Petrol = 0
        else :
            fuel_Diesel = 0
            fuel_Electric = 0
            fuel_LPG = 0
            fuel_Petrol = 0

        seller_type = request.form['seller_type']

        if seller_type == 'Individual':
            seller_type_Individual = 1
            seller_type_Trustmark_Dealer = 0
        elif seller_type == 'Trustmark':
            seller_type_Individual = 0
            seller_type_Trustmark_Dealer = 1
        else:
            seller_type_Individual = 0
            seller_type_Trustmark_Dealer = 0

        transmission = request.form['transmission']

        if transmission == 'Manual':
            transmission_Manual = 1
        else:
            transmission_Manual = 0

        owner = request.form['owner']

        if owner == 'Second':
            owner_Fourth_and_Above_Owner = 0
            owner_Second_Owner = 1
            owner_Test_Drive_Car = 0
            owner_Third_Owner = 0
        elif owner == 'Third':
            owner_Fourth_and_Above_Owner = 0
            owner_Second_Owner = 0
            owner_Test_Drive_Car = 0
            owner_Third_Owner = 1
        elif owner == 'Fourth':
            owner_Fourth_and_Above_Owner = 1
            owner_Second_Owner = 0
            owner_Test_Drive_Car = 0
            owner_Third_Owner = 0
        elif owner == 'Test':
            owner_Fourth_and_Above_Owner = 0
            owner_Second_Owner = 0
            owner_Test_Drive_Car = 1
            owner_Third_Owner = 0
        else :
            owner_Fourth_and_Above_Owner = 0
            owner_Second_Owner = 0
            owner_Test_Drive_Car = 0
            owner_Third_Owner = 0

        age_of_car = 2021 - year

        prediction = model.predict([[km_driven, age_of_car, fuel_Diesel, fuel_Electric, fuel_LPG,
                                     fuel_Petrol, seller_type_Individual, seller_type_Trustmark_Dealer,
                                     transmission_Manual, owner_Fourth_and_Above_Owner, owner_Second_Owner,
                                     owner_Test_Drive_Car, owner_Third_Owner]])

        output = round(prediction[0], 2)
        prediction_text = "You can sell your car at {}".format(output)
        return render_template('index.html', prediction_text=prediction_text)
    else :
        return "sorry"


if __name__ == '__main__':
    app.run(debug=True)
