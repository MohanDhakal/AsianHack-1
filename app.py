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
            "1": "Visit Central Zoo, Patan.",
            "2": "MoMo at New Everest MoMo Center, Thamel.",
            "3": "Try Chatamari and other Nepwari Cuisine at Kirtipur."
        }
    },
        {
        "NepaliValue": "500",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Buy handicrafts at thamel.",
            "2": "Visit Nepal Aviation Museum at Sinamangal.",
            "3": "Try Chatamari and other Nepwari Cuisine at Kirtipur."
        }
    },
        {
        "NepaliValue": "1000",
        "ConvertedValue": "",
        "what_can_i_buy": {
            "1": "Buy Cake with Ur Koseli",
            "2": "Buy Bhojpuri Khukuri at Thamel Khukhuri House",
            "3": "10 Plates MoMo at New Everest MoMo Center, Thamel"
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
        preferred_currency = "USD"
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
        "ingredients": "It is made of rice flour with adding customized flavours. A semi-liquid rice flour dough is usually prepared by adding milk, water, cooking oil, sugar, ghee, butter, cardamom, cloves, bananas and other flavours of personal choice.The ingredients are mixed well by stirring. Once the semi liquid dough is ready, it is deep fried in boiling oil or ghee. ",
        "food_type": "Veg"
    },
    {
        "cuisine_name": "Yomari",
        "description": "Yomari, also called Yamari, is a delicacy of the Newar community in Nepal. It is a steamed dumpling that consists of an external covering of rice flour and an inner content of sweet substances such as chaku. ",
        "ingredients": " A yomari is a confection of rice flour (from the new harvest) dough shaped like fish and filled with brown cane sugar and sesame seeds, which is then steamed. This delicacy is the chief item on the menu during the post-harvest celebration of Yomari Punhi.",
        "food_type": "Mostly Veg"
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

