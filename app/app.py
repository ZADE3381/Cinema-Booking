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
        editCell("static/test.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
                 changeToExcelCoords(keys[data_to_excelIteration])[1], "B")
        data_to_excelIteration = data_to_excelIteration + 1


def basketTimerCheck(rawData, timer):
    time.sleep(timer)
    data = json.loads(rawData)
    basketTimerCheckIteration = 0
    while basketTimerCheckIteration < len(data.keys()):
        keys = list(data.keys())
        if checkCell("static/test.xlsx", changeToExcelCoords(keys[basketTimerCheckIteration])[0],
                     changeToExcelCoords(keys[basketTimerCheckIteration])[1], "B"):
            editCell("static/test.xlsx", changeToExcelCoords(keys[basketTimerCheckIteration])[0],
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
        editCell("static/test.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
                 changeToExcelCoords(keys[data_to_excelIteration])[1], data[keys[data_to_excelIteration]])
        data_to_excelIteration = data_to_excelIteration + 1


def removeBasketFromExcel(rawData):
    data = json.loads(rawData)
    data_to_excelIteration = 0
    while data_to_excelIteration < len(data.keys()):
        keys = list(data.keys())
        editCell("static/test.xlsx", changeToExcelCoords(keys[data_to_excelIteration])[0],
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
    # thread = threading.Thread(target=editCell, args=("test.xlsx", 4, 2, "C"))
    # thread.start()
    return render_template("grid.html", allSeats=getAllSeatsFormatted("static/test.xlsx"))


@app.route('/book')
def book():
    data_to_excel(request.args.get('data'))
    return "booked"


@app.route('/basket')
def basket():
    if checkIfBooked("static/test.xlsx", request.args.get('data')):
        return "Failed (Seat Has Already Been Booked)"
    else:
        basket_to_excel(request.args.get('data'))
        threading.Thread(target=basketTimerCheck, args=[request.args.get('data'), 15]).start()
        return render_template("basket.html", data=request.args.get('data'))


@app.route('/basketfail')
def basketfail():
    return render_template("basketfail.html")


if __name__ == '__main__':
    app.run()
