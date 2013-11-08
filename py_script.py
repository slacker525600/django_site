from mlarble import settings
from django.core.management  import setup_environ
setup_environ(settings)
from mlarble import models
#now I can run tests

models.test_add_artists()

def add_artist_list():
  aArtists = Artist.objects.all()
  nCount = len(aArtists)
  # going to try something crazy here, 
  # create csv file with list of artists to add, 
  fFile = open('artists_to_add.csv' , 'r')
  asLines = fFile.readlines()
  fFile.close()
  if(len(asLines) == 0)
    #could throw error here, but ... not where Im at in implementation
    print('length of artists_to_add.csv = 0 does not contain header row')
    return
  asFieldNames = asLines[0].split(',')
  for sLine in asLines[1:]:
    asFields = sLine.split(',')
    if len(asFields) != len(asFieldNames):
      print('improperly formatted line, field count does not match')
      #print(asFields,'\n' ,asFieldNames)
      continue
    #first check if artists in db, 
    #as opposed to using an enum and then messing things up when fields change ... 
    sName = asFields[asFieldNames.find('full_name')]
    aaFound = Artist.objects.filter(full_name__exact=sName)
    if len(aFound) != 0:
      print('appears ' + sLine + ' has already been added, matched: ')
      for aFound in aaFound:
        print(aFound)
    else:
      #then add them, 
      dDict = {}
      for nFieldOn in range(0, len(asFieldNames) - 1):
        if len(asFieldNames[nFieldOn]) != 0 and asFieldNames[nFieldOn] != 'full_name':
          dDict[asFieldNames[nFieldOn] = asFields[nFieldOn]
      models.add_artist(sName, **dDict)
      if len(Artist.objects.all()) == nCount +1:
        nCount += 1
      else:
        print('insert failed')
        return


