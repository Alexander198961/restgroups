class MyGroupType:
    myGroupList =[]
    myId = ""
    def setMyId(self,myId):
        self.myId = myId
    def getMyId(self):
        return self.myId    
      
    def addMyGroupList(self,group):
        self.myGroupList.append(group) 
    def getMyGroupList(self):
        return  self.myGroupList   
      