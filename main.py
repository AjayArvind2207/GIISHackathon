from flask import Flask, render_template, jsonify


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def login():
    return render_template("login_page.html")

@app.route("/temperature", methods = ['POST'])
def get_temperature():
    temp = requests.form("temperature")
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

if __name__ == '__main__':  
    app.run()


#@app.route("/entertainment")  #Courses + books + news 



#3@app.route("/emergency")