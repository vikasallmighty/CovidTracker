from django.shortcuts import render,redirect, HttpResponse
import requests
import json
from datetime import datetime
now = datetime.now()

def district():
    api="https://api.covid19india.org/v2/state_district_wise.json"
    api2 = "https://api.covid19tracker.in/data/static/data.min.json"
    s=(requests.get(api)).text
    s2=(requests.get(api2)).text
    data=json.loads(s)
    data2=json.loads(s2)
    statelist = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh",
                 "Chattisgarh",
                 "Delhi", "Dadar and Nagar Havelli", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
                 "Jammu and Kashmir", "jharkhand", "Karnataka", "Kerala", "Ladakh", "Madhya Pradesh",
                 "Maharashtra",
                 "Manipur", "Meghalya", "Mizoram", "Nagaland", "Orissa", "Punjab", "Pondicherry", "Rajastha", "Sikkim",
                 "Tamil Nadu",
                 "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal", "Total"]
    statecode = ["an", "ap", "ar", "as", "br", "ch", "ct", "dl", "dn", "ga", "gj", "hr", "hp", "jk", "jh", "ka",
                 "kl", "la",
                 "mp", "mh", "mn", "ml", "mz", "nl", "or", "pb", "py", "rj", "sk", "tn", "tg", "tr", "ut", "up", "wb"
        , "tt"]
    dict = {}
    for i in range(len(statecode)):

        l = data2[statecode[i].upper()]
        dict[statelist[i]] = l
    return dict
def stateWise(request):
    dict = district()
    vaccinated = dict['Total']['total']['vaccinated1'] +  dict['Total']['total']['vaccinated2']
    date = dict['Total']['meta']['last_updated']
    params = {
        "ss": district(),
        "v": vaccinated,
        "date":date
    }
    return render(request, 'state.html', params)


def DistrictWise(request):
    parms = {

        "data1": district(),
    }

    return render(request, 'home.html', parms)

