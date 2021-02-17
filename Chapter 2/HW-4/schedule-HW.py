import os
import time
import schedule
import requests
import pygame

cdPath = str("C:\\Users\\User\\Desktop\\schedule-HW")
os.system("cls")        # Windows

# Change the directory to where the .py file & the .txt file located first to make this work
def getAutoCode():
    filePath = "{}\\authCode.txt".format(cdPath)
    with open(filePath) as file:
        return file.readline()

def getJsonFromURL(url):
    return requests.get(url).json()

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={}".format(getAutoCode())

class TodaysWeatherInfo:
    def __init__(self, jsonData):
        self.jsonData = jsonData

    def __getCorrespondingInfo(self, infoName):
        weatherElements = self.jsonData["weatherElement"]
        for weatherElement in weatherElements:
            name = weatherElement["elementName"]
            if (name == infoName):
                return weatherElement
    
    def getLocationName(self):
        return self.jsonData["locationName"]
    
    def getStartEndTime(self):
        startTime = self.jsonData["weatherElement"][0]["time"][0]["startTime"]
        endTime = self.jsonData["weatherElement"][0]["time"][0]["endTime"]

        return startTime, endTime
    
    def getTemperature(self):
        minT_Info = self.__getCorrespondingInfo("MinT")["time"][0]["parameter"]

        minT = minT_Info["parameterName"]
        minT_Unit = minT_Info["parameterUnit"]
        if (str(minT_Unit).upper() == "C"):
            minT_Unit = "°C"

        maxT_Info = self.__getCorrespondingInfo("MaxT")["time"][0]["parameter"]

        maxT = maxT_Info["parameterName"]
        maxT_Unit = maxT_Info["parameterUnit"]
        if (str(maxT_Unit).upper() == "C"):
            maxT_Unit = "°C"
        
        # return "Lowest temperature: {}{}. Highest temperature: {}{}".format(minT, minT_Unit, maxT, maxT_Unit)
        return "最低溫度: {}{}. 最高溫度: {}{}".format(minT, minT_Unit, maxT, maxT_Unit)
    
    def getStatus(self):
        return self.__getCorrespondingInfo("Wx")["time"][0]["parameter"]["parameterName"]

    def getRemind(self):
        return self.__getCorrespondingInfo("CI")["time"][0]["parameter"]["parameterName"]


# Start of weather report part

def weatherReport():
    locationRecords = getJsonFromURL(url)["records"]["location"]

    for record in locationRecords:
        info = TodaysWeatherInfo(record)

        locationName = info.getLocationName()
        startTime, endTime = info.getStartEndTime()

        print("[{}] {}，{}".format(locationName, info.getStatus(), info.getRemind()))
        print(info.getTemperature())        # This has been formatted in the function when returning.
        # print("日期：{} ~ {}".format(startTime, endTime))       # Needed?
        print("")       # Sep

# End of weather part.

# This will work as an alarm clock

def playMP3(mp3FileName):
    duration = 60 * 3 + 40      # Play the song for how many seconds
    mp3FilePath = "{}\\{}".format(cdPath, mp3FileName)      # Build the path to the .mp3 file

    pygame.mixer.init()
    pygame.mixer.music.load(mp3FilePath)
    pygame.mixer.music.set_volume(0.055)    # Volume control

    pygame.mixer.music.play()
    time.sleep(duration)            # This will wait until the player finished playing the .mp3 file
    pygame.mixer.music.stop()

# End of MP3 Player part

def goodMoring():
    mp3FileName = "Guns N Roses - My Michelle.mp3"
    weatherReport()
    print("--------------------")
    print("早安！現在是早上八點。以上是今天的天氣預報。")
    print("現在會播放：{}".format(mp3FileName))
    print("Have a nice day!")
    print("--------------------")
    # playMP3(mp3FileName)

goodMoring()      # Test run


""" schedule.every().day.at("08:00").do(goodMoring)

while True:
    schedule.run_pending()
    time.sleep(24 * 60 * 60)        # 1 day
 """

# Output:

""" 
[嘉義縣] 晴時多雲，寒冷
最低溫度: 14°C. 最高溫度: 15°C   

[新北市] 晴時多雲，稍有寒意      
最低溫度: 17°C. 最高溫度: 19°C   

[嘉義市] 晴時多雲，寒冷至稍有寒意
最低溫度: 14°C. 最高溫度: 16°C   

[新竹縣] 晴時多雲，寒冷至稍有寒意
最低溫度: 15°C. 最高溫度: 18°C   

[新竹市] 晴時多雲，寒冷至稍有寒意
最低溫度: 15°C. 最高溫度: 18°C

[臺北市] 晴時多雲，稍有寒意
最低溫度: 17°C. 最高溫度: 18°C

[臺南市] 晴時多雲，寒冷至稍有寒意
最低溫度: 15°C. 最高溫度: 17°C

[宜蘭縣] 晴時多雲，稍有寒意
最低溫度: 16°C. 最高溫度: 17°C

[苗栗縣] 晴時多雲，寒冷
最低溫度: 13°C. 最高溫度: 15°C

[雲林縣] 晴時多雲，寒冷
最低溫度: 14°C. 最高溫度: 15°C

[花蓮縣] 多雲時晴，稍有寒意
最低溫度: 17°C. 最高溫度: 18°C

[臺中市] 晴時多雲，寒冷至稍有寒意
最低溫度: 15°C. 最高溫度: 17°C

[臺東縣] 晴時多雲，稍有寒意
最低溫度: 18°C. 最高溫度: 19°C

[桃園市] 晴時多雲，稍有寒意
最低溫度: 16°C. 最高溫度: 18°C

[南投縣] 晴時多雲，寒冷至稍有寒意
最低溫度: 14°C. 最高溫度: 16°C

[高雄市] 晴時多雲，稍有寒意
最低溫度: 18°C. 最高溫度: 20°C

[金門縣] 晴時多雲，寒冷
最低溫度: 15°C. 最高溫度: 15°C

[屏東縣] 晴時多雲，稍有寒意
最低溫度: 16°C. 最高溫度: 18°C

[基隆市] 晴時多雲，稍有寒意
最低溫度: 17°C. 最高溫度: 18°C

[澎湖縣] 晴時多雲，稍有寒意
最低溫度: 16°C. 最高溫度: 17°C

[彰化縣] 晴時多雲，寒冷至稍有寒意
最低溫度: 14°C. 最高溫度: 16°C

[連江縣] 晴時多雲，寒冷
最低溫度: 12°C. 最高溫度: 13°C

--------------------
早安！現在是早上八點。以上是今天的天氣預報。
現在會播放：Guns N Roses - My Michelle.mp3
Have a nice day!
-------------------- 
"""