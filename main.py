from flask import Flask, url_for , render_template
import http_request
import model
import mail

app = Flask(__name__)

@app.route("/")
def home():
    prediction = model.get_prediction()
    

    # prediction = "high"
    if(prediction[0]=="nil"):
        
        return render_template("index.html",content = "Nil Chances of fire",temp=prediction[1],wind_speed=prediction[2],precip=prediction[3],humidity=prediction[4])

    elif(prediction[0]=="Mild"):
        return render_template("index.html",content = "Low Chances of fire",temp=prediction[1],wind_speed=prediction[2],precip=prediction[3],humidity=prediction[4])

    elif(prediction[0]=="Good"):
        mail.send_mail()
        return render_template("index.html",content = "Good chances of fire",temp=prediction[1],wind_speed=prediction[2],precip=prediction[3],humidity=prediction[4]) 

    else:
        mail.send_mail()
        return render_template("index.html",content = "High chances of fire",temp=prediction[1],wind_speed=prediction[2],precip=prediction[3],humidity=prediction[4]) 

if __name__ == "__main__":
    app.run()

