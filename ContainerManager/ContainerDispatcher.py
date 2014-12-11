import ConfigParser
from encodings.punycode import selective_find
import shutil

__author__ = 'root'
import Container
import subprocess

class ContainerDispatcher:
#
    def __init__(self):
        self.container_list=[]      #saved as a file at container_root_path
        self.num_containers = 0
        self.container_root_path = ''    #get from config file
        self.hackademic_root_path = ''   #get from config file

        self.getConfig()
        self.getContainerList()



    def getConfig(self):

        #open config file
        conf = open("container.conf",)

        #read config into configparser
        configparser = ConfigParser.ConfigParser()

        return



    # def setConfig(self):
    #
    #     conf = open("container.conf",'w')
    #     configparser = ConfigParser.ConfigParser()
    #     return


    def saveContainerList(self):

        containerlist_file = open('containerlist.txt','w')

        #save containerlist to file
        #if file does not exist make one
        return


    def getContainerList(self):

        containerlistfile = open("containerlist.txt",'r');


        #load containerlist from file
        #check if folder exists if not remove the container from list
        return





    def createContainer(self,name,ram):

        #create new folder at  container_root_path for new container
        src = self.hackadmic_root_path + '/master'
        dst = self.container_root_path + '/' + name    #replace some_id with random id for new container
        shutil.copytree(src,dst)

        #add to container list
        temp = Container(some_id,dst)
        self.container_list.append(temp)


        #create container using virt-install
        subprocess.call("virt-install -connect lxc:// --name ",name," --ram ",ram," --filesystem ",self.container_root_path,"/",name,"")


        #save changes to container_file
        return


    def getFreeContainer(self):
        #return a container that is not being used




    def startall(self):
        for i in self.container_list:
            i.startContainer();



