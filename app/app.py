import os
import json
import time
from flask import Flask, render_template, request
import threading
from app.dataToCoords import *
from app.excelEditor import editCell, getAllSeats, checkCell
import datetime

dt = datetime.datetime.now()
app = Flask(__name__)

def basket_to_excel(rawData):
    data = json.loads(rawData)
    data_to_excelIteration = 0
    while data_to_excelIteration < len(data.keys()):
        keys = list(data.keys())
        editCell("app/static/booking.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
                 changeToExcelCoords(keys[data_to_excelIteration])[1], "B")
        data_to_excelIteration = data_to_excelIteration + 1


def basketTimerCheck(rawData, timer):
    time.sleep(timer)
    data = json.loads(rawData)
    basketTimerCheckIteration = 0
    while basketTimerCheckIteration < len(data.keys()):
        keys = list(data.keys())
        if checkCell("app/static/booking.xlsx", changeToExcelCoords(keys[basketTimerCheckIteration])[0],
                     changeToExcelCoords(keys[basketTimerCheckIteration])[1], "B"):
            editCell("app/static/booking.xlsx", changeToExcelCoords(keys[basketTimerCheckIteration])[0],
                     changeToExcelCoords(keys[basketTimerCheckIteration])[1], "")
        basketTimerCheckIteration = basketTimerCheckIteration + 1


def getAllSeatsFormatted(file):
    allSeatsRaw = getAllSeats(file)
    allSeats = []
    for x in allSeatsRaw:
        allSeats.append(changeFromCoords(x))
    return allSeats


def data_to_excel(rawData):
    data = json.loads(rawData)
    data_to_excelIteration = 0
    while data_to_excelIteration < len(data.keys()):
        keys = list(data.keys())
        editCell("app/static/booking.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
                 changeToExcelCoords(keys[data_to_excelIteration])[1], data[keys[data_to_excelIteration]])
        data_to_excelIteration = data_to_excelIteration + 1


def removeBasketFromExcel(rawData):
    data = json.loads(rawData)
    data_to_excelIteration = 0
    while data_to_excelIteration < len(data.keys()):
        keys = list(data.keys())
        editCell("app/static/booking.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
                 changeToExcelCoords(keys[data_to_excelIteration])[1], "")
        data_to_excelIteration = data_to_excelIteration + 1


def checkIfBooked(file, data):
    isBooked = False
    for x in range(0, len(list(json.loads(data).keys()))):
        if list(json.loads(data).keys())[x] in getAllSeatsFormatted(file):
            isBooked = True
    if isBooked:
        return True
    else:
        return False


@app.route('/')
def home():
    tryTimer = 0
    while tryTimer < 30:
        try:
            # thread = threading.Thread(target=editCell, args=("booking.xlsx", 4, 2, "C"))
            # thread.start()
            return render_template("grid.html", allSeats=getAllSeatsFormatted("app/static/booking.xlsx"))
        except:
            tryTimer += 1
            time.sleep(0.3)

    return render_template("basketfail.html", reasonText="There Was An Error, Please Refresh The Page!")


@app.route('/book')
def book():
    tryTimer = 0
    while tryTimer < 30:
        try:
            data_to_excel(request.args.get('data'))
            return render_template("book.html")
        except:
            tryTimer += 1
            time.sleep(0.3)

    return render_template("basketfail.html", reasonText="There Was An Error, Please Refresh The Page!")


@app.route('/basket', methods=["GET"])
def basket():
    tryTimer = 0
    while tryTimer < 30:
        try:
            if checkIfBooked("app/static/booking.xlsx", request.args.get('data')):
                return "Failed (Seat Has Already Been Booked)"
            elif request.args.get('data') == "{}":
                return render_template("basketfail.html", reasonText="You Must Pick A Seat!")
            else:
                threading.Thread(target=basketTimerCheck, args=[request.args.get('data'), 15]).start()
                basket_to_excel(request.args.get('data'))
                return render_template("basket.html", data=request.args.get('data'))
        except:
            tryTimer += 1
            time.sleep(0.3)

    return render_template("basketfail.html", reasonText="There Was An Error, Please Refresh The Page!")


@app.route('/basketfail')
def basketfail():
    tryTimer = 0
    while tryTimer < 30:
        try:
            if request.args.get('reason') == "timeout":
                return render_template("basketfail.html", reasonText="You Ran Out Of Time!")
            elif request.args.get('reason') == "cancelled":
                data = json.loads(request.args.get('data'))
                dataTimerCheckIteration = 0
                while dataTimerCheckIteration < len(data.keys()):
                    keys = list(data.keys())
                    if checkCell("app/static/booking.xlsx", changeToExcelCoords(keys[dataTimerCheckIteration])[0],
                                 changeToExcelCoords(keys[dataTimerCheckIteration])[1], "B"):
                        editCell("app/static/booking.xlsx", changeToExcelCoords(keys[dataTimerCheckIteration])[0],
                                 changeToExcelCoords(keys[dataTimerCheckIteration])[1], "")
                    dataTimerCheckIteration = dataTimerCheckIteration + 1
                return render_template("basketfail.html", reasonText="Your Seats Have Been Cancelled!")
        except:
            tryTimer += 1
            time.sleep(0.3)

    return render_template("basketfail.html", reasonText="There Was An Error, Please Refresh The Page!")


@app.route('/developer')
def developer():
    return render_template("developer.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(".\\app\\static\\booking.xlsx")
        return render_template("upload.html")


if __name__ == '__main__':
    app.run()
