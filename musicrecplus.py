#Robert Brandl
#I pledge my honor that I have abided by the Stevens Honor System.
from cs115 import *
import sys

iFile = 'musicrecplus.txt'

def loadUsers(File):
    '''loads the users and preferences stored in File and returns a dictionary with user names mapped to a list of artists'''
    try:
        file = open(File, 'r')
    except:
        file = open(File, 'w+')
    userDict = {}
    for line in file:
        [userName, artists] = line.strip().split(':')
        if userName not in userDict: 
            artists = artists.title()
            artistList = artists.split(',')
            artistList.sort()
            for i in range(len(artistList)):
                artistList[i] = artistList[i].strip()
            userDict[userName] = artistList
    file.close()
    return userDict

def main():
    '''main function which handles basic setup'''
    userDict = loadUsers(iFile)
    name = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n')
    uPrefs = []
    if name not in userDict: uPrefs = enterPref(name, userDict)
    else: uPrefs = userDict[name]
    uPrefs = menu(name, uPrefs, userDict)
    savePrefs(name,uPrefs,userDict,iFile)

def menu(name, prefs, udict):
    '''outputs the menu of options'''
    choices = 'Enter a letter to choose an option :\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit'
    option = input(choices + "\n")
    changePref = False
    while option != 'q':
        if option == 'e': prefs = enterPref(name,udict)
        elif option == 'r': getRec(name,prefs,udict)
        elif option == 'p': mostPopular(name,udict,prefs) 
        elif option == 'h': howPopular(name,udict,prefs) 
        elif option == 'm': mostLikes(name,prefs,udict)
        option = input(choices + '\n')
    return prefs

def enterPref(userName, udict):
    '''allows the user to enter their artist preferences'''
    prefs = []
    nextPref = input('Enter an artist that you like ( Enter to finish ):\n')
    nextPref.title()
    while nextPref != '':
        if nextPref not in prefs:
            prefs.append(nextPref.strip().title())
        nextPref = input('Enter an artist that you like ( Enter to finish ):\n')
        nextPref.title()
    prefs.sort()
    if userName in udict:
        udict[userName] = prefs
    return prefs

def getRec(userName,prefs,udict):
    '''gets recommendations for the user based on their prefs against udict'''
    bestUser = findBestUser(userName,prefs,udict)
    if bestUser == '': print("No recommendations available at this time.")
    else:
        recs = drop(prefs,udict[bestUser])
        for artist in recs:
            print(artist)
            
def findBestUser(currUser,prefs,udict):
    '''finds the user whose artist list is most similar to user'''
    bestUser = ''
    bestScore = 0
    for user in udict.keys():
        if str(user)[-1] != '?':
            score = numMatches(prefs, udict[user])
            if score > bestScore and currUser != user and drop(prefs,udict[user]) != []:
                bestScore = score
                bestUser = user
    return bestUser

def numMatches(list1,list2):
    '''returns the number of elements that match between 2 sorted lists'''
    matches = 0
    i = 0
    j = 0
    while i<len(list1) and j<len(list2):
        if list1[i]==list2[j]:
            matches +=1
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
    return matches
    
def drop(list1, list2):
    '''returns a new list that contains only elements in list2 that were not in list1'''
    list3 = []
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i]==list2[j]:
            i+=1
            j+=1
        elif list1[i]<list2[j]:
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    while j < len(list2):
        list3.append(list2[j])
        j+=1
    list3.sort()
    return list3

def pop(name,udict,prefs): 
    '''returns a list of list containing the most popular artists and their likes'''
    listAll = []
    for user in udict:
        if str(user)[-1] != '?':
            listAll = listAll + udict[user]
    if name not in udict:
        listAll = listAll + prefs
    listAll.sort()
    countF,countS,countT, currC = 0,0,0,0
    popArtF,popArtS,popArtT,art = '','','',''
    while listAll != []:
        if listAll[0] == art: currC+=1
        elif len(listAll) == 1:
            currC = 1
            prevA,art = art,listAll[0]
            if currC > countF:
                countF,countS,countT = currC, countF,countS
                popArtF,popArtS,popArtT = art,popArtF,popArtS
            elif currC > countS:
                countS,countT = currC,countS
                popArtS,popArtT = art,popArtS
            elif currC > countT:
                countT = currC
                popArtT = art
            art = prevA
        if listAll[0] != art:
            if currC > countF:
                countF,countS,countT = currC, countF,countS
                popArtF,popArtS,popArtT = art,popArtF,popArtS
            elif currC > countS:
                countS,countT = currC,countS
                popArtS,popArtT = art,popArtS
            elif currC > countT:
                countT = currC
                popArtT = art
            if countS > countF:
                countF,countS = countS,countF
                popArtF,popArtS=popArtS,popArtF
            if countT > countF:
                countF,countT = countT,countF
                popArtF,popArtT=popArtT,popArtF
            if countT > countS:
                countT,countS = countS,countT
                popArtT,popArtS=popArtS,popArtT
            art = listAll[0]
            currC = 1
        listAll = listAll[1:]
    if countF == countS and countF == countT:
        l = [popArtF,popArtS,popArtT]
        l.sort()
        popArtF,popArtS,popArtT=l[0],l[1],l[2]
    elif countF == countS:
        l = [popArtF,popArtS]
        l.sort()
        popArtF,popArtS=l[0],l[1]
    elif countF == countT:
        l = [popArtF,popArtT]
        l.sort()
        popArtF,popArtT=l[0],l[1]
    elif countS == countT:
        l = [popArtS,popArtT]
        l.sort()
        popArtS,popArtT=l[0],l[1]
    return [[popArtF,countF],[popArtS,countS],[popArtT,countT]]

def mostPopular(name,udict,prefs):
    '''prints the 3 most popular artists'''
    listP = pop(name,udict,prefs)
    if listP[0][1] > 0: print(listP[0][0])
    if listP[1][1] >0: print(listP[1][0])
    if listP[2][1]>0: print(listP[2][0])
    if listP[0][1] == 0 and listP[1][1] == 0 and listP[2][1] == 0: print('Sorry, no artists found.')
        

def howPopular(name,udict,prefs):
    '''prints the number of likes the most popular artist recieved'''
    listP = pop(name,udict,prefs)
    if listP[0][1] > 0: print(listP[0][1])
    elif listP[1][1] >0: print(listP[1][1])
    elif listP[2][1]>0: print(listP[2][1])
    if listP[0][1] == 0 and listP[1][1] == 0 and listP[2][1] == 0: print('Sorry, no artists found.')
        
    
def mostLikes(name,prefs, udict):
    '''prints out the user name with the most likes (artists)'''
    most = 0
    mname = ''
    for user in udict:
        if str(user)[-1] != '?':
            if len(udict[user]) > most:
                most = len(udict[user])
                mname = str(user)
    if name[-1] != '?' and len(prefs) > most:
        most = len(prefs)
        mname = name
    if most == 0: print('Sorry, no user found')
    else: print(mname)
    
def savePrefs(name, prefs, udict, File):
    '''saves the user preferences to this file'''
    udict[name] = prefs
    file = open(File, 'w')
    for user in udict:
        save = str(user) + ':' + ','.join(udict[user]) + '\n'
        file.write(save)
    file.close()

#runs program automatically
#if __name__ == '__main__': main()
