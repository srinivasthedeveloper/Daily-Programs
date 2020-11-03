hour,minute=input().split(":")
hour,minute=int(hour),int(minute)
while 1:
    hour+=minute//60
    hour%=24
    minute%=60
    newHour,newMin=str(hour),str(minute)
    time='0'*(2-len(newHour))+newHour+":"+'0'*(2-len(newMin))+newMin
    if time==time[::-1]:
        print(time)
        break
    minute+=1
