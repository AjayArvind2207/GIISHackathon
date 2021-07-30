from flask import Flask
from flask import render_template, request, jsonify
from flask import session
import time
import requests

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'WEEB'

@app.route("/")
def login():
    return render_template("./index.html")

@app.route("/temperature", methods = ['POST'])
def get_temperature():
    temp = request.form["temperature"]
    # or however login works
    user = request.form["user"]
    _id = 0
    print(temp)
    return jsonify({'id': _id, 'time': time.time()})
    #Stored in firebase --> can


@app.route("/dailypuzzle")
#Get the daily puzzle in the form of 
def getLink():
    import random
    import requests 
    import bs4
    number = str(random.randint(1,100))
    link='https://www.google.com/search?q='+'geeksforgeeks puzzle '+number
    response=requests.get(link)
    
    ls=[]
    links=[]
    try:
        soup=bs4.BeautifulSoup(response.text,features="html.parser")
        
        for tag in soup.find_all('a'):
            ls.append(tag.get('href'))
        
        for link in ls:
            if(link.startswith('/url?q=https://www.geeksforgeeks.org/puzzle-'+number)==True):
                end=0
                index=37
                for c in link[37:]:
                    if c=='/':
                        end=index
                        break
                    index+=1
                links.append(link[7:end])
                break

        print(links)
        return links
    
    except:
        print('Error')
        return ['No Links Found!!']
        raise()



@app.route('/weather')
def weather() -> None:
    '''This fetches the weather data'''
    api_key = 'a6280859274843c64f27cccd1059ba8b'
    city_id = '1880252'
    url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'
    data = requests.get(url).text
    return jsonify(data)




if __name__ == '__main__':  
    app.run()


#@app.route("/entertainment")  #Courses + books + news 



#3@app.route("/emergency")