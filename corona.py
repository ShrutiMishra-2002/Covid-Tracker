import json
from tkinter import*
import requests
from datetime import*

def getCovidData():
    api="https://disease.sh/v3/covid-19/all"
    json_data= requests.get(api).json()
    total_cases = str(json_data ['cases'])
    total_deaths = str(json_data ['deaths'])
    today_cases = str(json_data ['todayCases'])
    today_deaths = str(json_data ['todayDeaths'])
    today_recovered = str(json_data ['todayRecovered'])
    updated_at = json_data ['updated']
    date = datetime.fromtimestamp(updated_at/1e3)
    label1.config(text="Total Cases:"+total_cases+"\n"+"Total Deaths:"+total_deaths+"\n"+"Todaycases:"+today_cases+"\n"+"Today Death:"
    +today_deaths+"\n"+"Today Recovered:"+today_recovered+"\n")
    label2.config(text=date)


    #control backlslash
    # d=json_data.json()
    # print(d)
root= Tk()

# root.geometry("1200x1000")
root.geometry("1200x800")
# widthxheight
# root.maxsize(600,800)
root.maxsize(1200,800)
root.title("Covid Tracker App")
f= ("poppins", 15,"bold")
# to give background colour we use root.config(bg='colour')
# we can give colour to background by giving bg colour for labels , labels have individual colour
top=Label(root,text="****COVID TRACKER APP****",font=f,bg='green',fg='black')
top.pack(pady=10)

button=Button(root, font= f, text="load", command=getCovidData,padx=48)
button.pack(pady=10)
label1=Label(root, font=f,bg='green',fg='red')
label1.pack(pady=10)
label2=Label(root, font=f,bg='green',fg='black')
label2.pack()
photo = PhotoImage(file="mask.png")
photo_label = Label(image=photo , height=500 , width=500 ,bg='green')
photo_label.pack()
root.configure(bg='green')

root.mainloop()