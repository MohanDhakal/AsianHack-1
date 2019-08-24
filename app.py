from flask import Flask, render_template, request, jsonify
from inference import get_cash_name, get_cuisine_name
from commons import get_tensor
from conversion import converter
app = Flask(__name__)


cash_values = [
    {
        "NepaliValue": "5",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },

    {
        "NepaliValue": "10",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },

    {
        "NepaliValue": "20",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },

    {
        "NepaliValue": "50",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },

    {
        "NepaliValue": "100",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },
        {
        "NepaliValue": "500",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },
        {
        "NepaliValue": "1000",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Lorem Ipsum at Jorem Ipsum",
            "2": "Single Life Rocks",
            "3": "Hello World, we welcome you"
        }
    },
]

@app.route("/")
def index():
    return render_template("base.html")

@app.route('/check/cash/', methods = ['GET', 'POST'])
def upload_file():

    results = []

    if request.method == 'GET':
        return render_template('upload_file_cash.html')
    if request.method == 'POST':
        if "file" not in request.files:
            print("File not uploaded.")
            return
        preferred_currency = request.form["PreferredCurrency"]
        file = request.files['file']
        image = file.read()
        tensor = get_tensor(image_bytes=image)
        category, cash, output = get_cash_name(image_bytes=image)
        converted_value = converter.convert(int(cash), "NPR", preferred_currency)
        for the_cash_value in cash_values:
            if the_cash_value["NepaliValue"] == cash:
                the_cash_value["ConvertedValue"] = converted_value
                results.append(the_cash_value)
                
        return jsonify(results)
        #return render_template('result_file.html', cash = cash, output = output)


cuisines = [
    {
        "cuisine_name": "Selroti",
        "description":"Sel roti (Nepali: सेल रोटी) is a traditional homemade, sweet, ring-shaped rice bread/doughnut originating from the Nepal. It is mostly prepared during Dashain and Tihar, widely celebrated Hindu festivals in Nepal and Sikkim and Darjeeling.",
        "ingredients": "",
        "food_type": "Veg"
    },
    {
        "cuisine_name": "Yomari",
        "description": "Yomari, also called Yamari, is a delicacy of the Newar community in Nepal. It is a steamed dumpling that consists of an external covering of rice flour and an inner content of sweet substances such as chaku. ",
        "ingredients": "",
        "food_type": ""
    }
]

@app.route('/check/cuisine/', methods = ['GET', 'POST'])
def upload_file_cuisine():
    results = []

    if request.method == 'GET':
        return render_template('upload_file.html')
    if request.method == 'POST':
        if "file" not in request.files:
            print("File not uploaded.")
            return
        file = request.files['file']
        image = file.read()
        tensor = get_tensor(image_bytes=image)
        category, cuisine, output = get_cuisine_name(image_bytes=image)
        print(get_tensor(image_bytes=image))

        for the_cuisine in cuisines:
            if the_cuisine["cuisine_name"] == cuisine:
                results.append(the_cuisine)

        return jsonify(results)
        # return render_template('result_file.html', cuisine = cuisine, output = output)

if __name__ == "__main__":
    app.run()

