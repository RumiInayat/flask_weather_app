
from flask import Flask as fl  ,  render_template, request
import requests , json
 
app = fl(__name__)


@app.route("/", methods=['GET' , 'POST'])
def home():
    if request.method == "POST":
        with open('config.json', 'r') as c:
            parms = json.load(c)['details']

        api_key = parms['api_key']
        base_url=parms['url']
        city = request.form.get('city')
        url = f"{base_url}{api_key}&q={city}"
      
       
        response = requests.get(url)
        weather_data = response.json()

        
        try:
        
            country = weather_data['location']['country']
            region = weather_data['location']['region']
            temp_c = weather_data['current']['temp_c']
            temp_f = weather_data['current']['temp_f']
            condition = weather_data['current']['condition']['text']
            wind = weather_data['current']['wind_kph']
            humidity = weather_data['current']['humidity']
            cloud = weather_data['current']['cloud']
            icon = weather_data['current']['condition']['icon']

        

        except KeyError:
            return render_template('index.html',error="Invalid City, Please Check City Name.", city_error=True)
       

        return render_template('index.html', temp_c=temp_c,temp_f=temp_f, condition=condition, region=region ,city=city, country=country,humidity=humidity, cloud=cloud, wind=wind,   icon=icon, show_data=True)
    
    return render_template('index.html',  show_data=False)



@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact",methods=['GET' , 'POST'] )
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()

