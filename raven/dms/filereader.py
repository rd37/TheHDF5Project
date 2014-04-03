import json

class FileReader:
  def __init__(self):
    print 'creating a file reader';

  def gethandle(self,filename):
    json_data=open(filename).read()
    data=json.loads(json_data)
    return data

  def check(self,str1,str2):
    if str1 == str2 :
      print 'equals'
    else:
      print 'not equals'
