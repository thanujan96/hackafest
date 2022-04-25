import csv
from fileinput import filename
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from bioWeb.mlModelClass import MlModelClass
from django.contrib.auth import login
from .forms import CreateUserForm, UpdateUserForm
from .models import Collection, User
from .models import CSVFile
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "bioweb/indexnew.html")


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, form.errors)
    form = CreateUserForm()
    return render(request, "bioweb/register.html", {"form": form})


def profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your profile has been updated !")
            return redirect("/profile")
        messages.error(request, form.errors)
    form = UpdateUserForm(instance=request.user)
    return render(request, "bioweb/profile.html", {"form": form})


def collections(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")

        if id == "":
            coll = Collection(collectionName=name, userId=request.user)
            coll.save()
            return redirect("Collections")

        coll = Collection.objects.filter(id=request.POST.get("id")).update(
            collectionName=name
        )
        return redirect("Collections")
        # coll.update(collectionName=request.POST.get('name'))
    coll = Collection.objects.filter(userId=request.user.id)
    return render(request, "bioweb/collections.html", {"collection": coll})


def collDelete(request, id):
    coll = Collection.objects.get(id=id)
    coll.delete()
    return redirect("Collections")


# csv view


def csvView(request, id):
    url = "/csvviews/" + str(id)
    collectionNo = id
    if request.method == "POST":
        try:
            id = request.FILES
            myfile = request.FILES["myfile"]
            fileType = request.POST.get("filetype")
            print(fileType)
            df = pd.read_csv(myfile, sep="\t")
            df.to_csv("bioWeb/csvFiles/" + myfile.name.split(".")[0] + ".csv", sep=",")
            collectionInstance = Collection.objects.get(id=collectionNo)
            newFile = CSVFile(
                fileName=myfile.name.split(".")[0],
                collectionId=collectionInstance,
                csvFile="bioWeb/csvFiles/" + myfile.name.split(".")[0] + ".csv",
                fileType=fileType,
            )
            newFile.save()
            return redirect(url)
        except:
            id = request.POST.get("id")
            name = request.POST.get("name")
            csvUpdate = CSVFile.objects.filter(id=request.POST.get("id")).update(
                fileName=name
            )
            return redirect(url)
        # coll.update(collectionName=request.POST.get('name'))
    # print(id)
    userIdFormColl = Collection.objects.get(id=collectionNo).userId
    if str(request.user.username) == str(userIdFormColl):
        csvfiles = CSVFile.objects.filter(collectionId=collectionNo)
        # print(csvfiles[0].fileName)
        return render(request, "bioweb/csvviews.html", {"csvviews": csvfiles})
        pass
    return redirect("Collections")


def csvDelete(request, id):
    url = request.META.get("HTTP_REFERER")
    csv = CSVFile.objects.get(id=id)
    csv.delete()
    return redirect(url)


def readCSV(request, id):
    print("readCSV call aakuthu")
    try:
        csvFile = CSVFile.objects.get(id=id)
    except:
        return redirect("/collections/")
    coll = csvFile.collectionId
    userIdformColl = Collection.objects.get(id=coll.id).userId.id
    if request.user.id == userIdformColl:
        csvFileName = csvFile.csvFile
        df = pd.read_csv(csvFileName)
        # print(df)
        feature = MlModelClass(df, labelDf, metaDf)
        tablesHead = df.columns
        if request.method == "POST" and request.POST.get("csvsort") == "Filter":
            endRow = int(request.POST.get("endRow"))
            startRow = int(request.POST.get("startRow"))
            selectValue = request.POST.get("sortview")
            if selectValue != "None":
                df1 = df.sort_values(selectValue)
            if df1.shape[0] > 100:
                df1 = df1.head(100)
            df1 = df1.iloc[int(startRow) : int(endRow) + 1]
            data = df1.to_html()
            context = {
                "csvfiledata": data,
                "tablesHead": tablesHead,
                "maxRow": df.shape[0] - 1,
                "totalRows": df.shape[0],
                "CSVid": id,
            }
            return render(request, "bioweb/readcsv.html", context)
        if df.shape[0] > 100:
            df1 = df.head(100)
        else:
            df1 = df
        data = df1.to_html()
        context = {
            "csvfiledata": data,
            "tablesHead": tablesHead,
            "totalRows": df.shape[0],
            "maxRow": df.shape[0] - 1,
            "CSVid": id,
        }
        return render(request, "bioweb/readcsv.html", context)
    return redirect(request.META.get("HTTP_REFERER"))


def sortcsv(request):
    id = request.META.get("HTTP_REFERER").split("/")[-1]
    start = request.POST.get("startRow")
    end = request.POST.get("endRow")
    import datetime

    print(datetime.datetime.now())
    return render(
        request,
        "bioweb/elements/csvreadsort.html",
        {"time": datetime.datetime.now(), "CSVid": id},
    )


def selectedrow(request):
    id = request.META.get("HTTP_REFERER").split("/")[-1]
    csvFile = CSVFile.objects.get(id=id)
    csvFileName = csvFile.csvFile
    df = pd.read_csv(csvFileName)
    tablesHead = df.columns
    endRow = int(request.POST.get("endRow"))
    startRow = int(request.POST.get("startRow"))
    selectValue = request.POST.get("sortview")
    noOfRows = request.POST.get("noOfRow", False)

    df1 = df.iloc[int(startRow) : int(endRow) + 1]
    if selectValue != "None":
        df1 = df1.sort_values(selectValue)
    if noOfRows != "0":
        df1 = df1.head(int(noOfRows))
    else:
        df1 = df1.head(int(20))

    data = df1.to_html()
    x = 2
    # context={
    #     "csvfiledata": data,
    #     'tablesHead': tablesHead,
    #     'maxRow': df.shape[0]-1,
    #     'totalRows': df.shape[0]
    # }
    return HttpResponse(data)
    # print("hello")
    start = request.POST.get("startRow")
    end = request.POST.get("endRow")
    return HttpResponse("selected rows: " + str(int(end) - int(start) + 1))


def summa(request):
    # print("hello")
    import datetime

    return HttpResponse("Time :" + str(datetime.datetime.now()))


# data visualizer


def visualizer1(request):
    id = request.META.get("HTTP_REFERER").split("/")[-1]
    csvFile = CSVFile.objects.get(id=id)
    coll = csvFile.collectionId
    csvFileName = csvFile.csvFile
    df = pd.read_csv(csvFileName)
    userIdformColl = Collection.objects.get(id=coll.id).userId.id
    try:
        endRow = int(request.POST.get("endRow"))
        startRow = int(request.POST.get("startRow"))
    except:
        pass
    yAxis = request.POST.get("yaxis")
    xAxis = request.POST.get("xaxis")
    noOfRows = request.POST.get("noOfRow", False)
    chartType = request.POST.get("charttype", "line")
    tablesHead = df.columns
    # df1 = df.iloc[int(startRow):int(endRow)+1]
    df1 = df
    if noOfRows:
        df1 = df1.head(int(noOfRows))
    if yAxis != "None":
        selectColumn = df1[yAxis]
    else:
        selectColumn = df1.value
    if xAxis != "None":
        selectedLabel = list(df1[xAxis])
        selectedLabel.sort()
    else:
        selectedLabel = [i for i in range(len(list(selectColumn)))]
    print(selectedLabel)
    if request.user.id == userIdformColl:
        data = {
            # 'tablesHead': tablesHead,
            "charttype": chartType,
            "value": list(selectColumn),
            "label": selectedLabel,
            "title": yAxis + " VS " + xAxis,
        }
        return render(request, "bioweb/visualizer.html", data)


def getBoxChartValue(microName, featureCSVFile, labelCSVFile):
    print(featureCSVFile, labelCSVFile)

    feature_data = pd.read_csv(featureCSVFile)
    lable_data = pd.read_csv(labelCSVFile)

    row = feature_data["Unnamed: 0"].tolist().index(microName)
    featureSelectedMicro = feature_data.iloc[row]
    # concatannated_data = pd.concat(
    #     [feature_data.iloc[2], lable_data.iloc[1]], axis=1)
    featureSelectedMicro = featureSelectedMicro.to_frame()
    featureSelectedMicro["result"] = ["NaN"] + list(lable_data.iloc[1])

    pos = featureSelectedMicro.loc[featureSelectedMicro["result"] == "1", [True, False]]
    neg = featureSelectedMicro.loc[
        featureSelectedMicro["result"] == "-1", [True, False]
    ]
    return list(pos[row]), list(neg[row])
    pass


def visualizer(request, id):
    print("Visuvalizer funtion called")
    csvFile = CSVFile.objects.get(id=id)

    coll = csvFile.collectionId
    csvFiles = CSVFile.objects.filter(collectionId=coll)
    for csv in csvFiles:
        if csv.fileType == "Feature":
            featureCSVFile = csv.csvFile
        elif csv.fileType == "Label":
            labelCSVFile = csv.csvFile
    yAxis = request.POST.get("yaxis", "UNMAPPED")

    posValue, negValue = feature.getBoxChartValue(yAxis)
    # print(posValue,"\n\n",negValue)
    csvFileName = csvFile.csvFile
    df = pd.read_csv(csvFileName)
    userIdformColl = Collection.objects.get(id=coll.id).userId.id
    # print(list(df[['Unnamed: 0']]))

    data = {
        "tablesHead": df["Unnamed: 0"].tolist(),
        # "tablesHead":[1,2,4],
        "charttype": "boxplot",
        "posValue": posValue,
        "negValue": negValue,
        "label": [1],
        "csvId": id,
    }
    return render(request, "bioweb/boxchart.html", data)


# htmx functions
def boxchart(request, id):
    print("box chart sort call akkuthu")
    csvFile = CSVFile.objects.get(id=id)

    coll = csvFile.collectionId
    csvFiles = CSVFile.objects.filter(collectionId=coll)
    for csv in csvFiles:
        if csv.fileType == "Feature":
            featureCSVFile = csv.csvFile
        elif csv.fileType == "Label":
            labelCSVFile = csv.csvFile
    try:
        yAxis = request.POST.get("yaxis")
    except:
        yAxis = ""
    posValue, negValue = getBoxChartValue(yAxis, featureCSVFile, labelCSVFile)

    csvFileName = csvFile.csvFile
    df = pd.read_csv(csvFileName)
    userIdformColl = Collection.objects.get(id=coll.id).userId.id
    # print(list(df[['Unnamed: 0']]))

    print(yAxis)
    data = {
        "tablesHead": df["Unnamed: 0"].tolist(),
        # "tablesHead":[1,2,4],
        "charttype": "boxplot",
        "posValue": posValue,
        "negValue": negValue,
        "label": [1],
    }
    return render(request, "bioweb/elements/boxchart.html", data)
