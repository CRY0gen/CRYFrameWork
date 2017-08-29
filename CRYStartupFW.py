"""
TODO:
    3.Add Application updater (will control in https://raw.github.com/CRY0gen/%appname%/version.dat)
    4.Add FrameWork Updater (will control in https://raw.github.com/CRY0gen/CRYFrameWork/version.dat)
"""
#!/usr/bin/env python
#coding=utf-8

import threading
import time
import libs.clear
import libs.CRYLog as CRYLog
import random ##Used only for random Sentecies


print("Booting up the FrameWork...")

clear=libs.clear.clear
CRLOG=CRYLog.CRYLog("./CRYData/CRYlogs")
printc=CRLOG.CRYprint
logc=CRLOG.CRYlog
logc("Loading phase stared a few moments before",CRYLog.deb)


class CRYFrameWork(threading.Thread):
    def __init__(self ,appname="null",version="null",isStartup=1):
        threading.Thread.__init__(self)
        self.result=None
        self.canStartProgram=0x00001010
        self.ncanStartProgram=0x00001011
        self.giveControlToApp=0x00001012
        self.isStartup=isStartup
        self.outp_lock=0
        self.isEnd=0
        self._FW_version="1.0.3d"
        self._appname=self.setAppName()
        if not self.checkAppName(self._appname):
                printc("[!]Warining: File APP.nam is missing from \"/AppData/\".\nPlease use AppUpdater specifiing the app name or simply create the file using nano or pico or something like this giving the appname.")
                exit()
        self._version=self.setAppVer()
        self._helppagedef="""
    <command>           <function>
     h                   Shows this help page
"""
        logc("###DEBUG INFO###", CRYLog.warn)
        logc("	CRYFrameWork Version:" + str(self._FW_version),CRYLog.deb)
        logc("	App Name:" + str(self._version), CRYLog.deb)
        logc("	App Version:" + str(self._appname), CRYLog.deb)
        logc("###DEBUG INFO END###\n", CRYLog.warn)
        logc("Booting has finished", CRYLog.warn)

    def setIsStartup(self,isStartup):
        self.isStartup=0
    def setAppName(self):
        AppName=None
        try:
                appnmf=open("./AppData/App.nam","r")
        except:
                logc("Could not open file App.nam in ./AppData/",CRYLog.err)
        try:
                logc("Reading App Name...",CRYLog.deb)
                AppName=appnmf.read()
                logc("[ DONE ]",CRYLog.deb)
        except:
                logc("[ FAILURE ]",CRYLog.warn)
        return AppName
    def checkAppName(self,data):
        if data==None:
                return False
        return True
    def setAppVer(self):
        Version=None
        try:
                versf=open("./AppData/App.ver","r")
        except:
                logc("Could not open file App.ver in ./AppData/", CRYLog.err)
        try:
                logc("Reading App Version...",CRYLog.deb)
                Version=versf.read()
                logc("[ DONE ]", CRYLog.deb)
        except:
                logc("[ FAILURE ]", CRYLog.warn)
        return Version
    def CRYStartupFW(self,first_input="Start the program?(yes/no):",showHelpPage=1):
        __help_page__=self._helppagedef
        self.outp_lock=1
        _startup_template_=""" by CRY0g3n.
    FrameWork v. """ + self._FW_version + """
    Free to use/modify, just give me credits.
    The illegal use of my creations aren't my responsibility, but is user's one.


         __          _...._     
      _cC''Cc_     .&ç''''%&.  \\y$.     .R0/
     cP     'cc    5R     Md^   .2y     y2.
    CR             RR    I:'     \\45   5vc
    C$             sR_  .Ta       v$v.vRv
    CR             C14c$3d         °cG3°
     cR     _cc    Y£   Jcv         xNc
     'Cp.pC'&"     R3    'vd        bC<  <Softwares&FrameWorks>
       "''''       t5     1LI       nRn
"""
        final_template="    "
        final_template+=self._appname+" v "+self._version+_startup_template_+self._helppagedef
    
        if self.isStartup==1:
            printc(final_template)
            loop=1
            while loop==1:
                start=input(first_input)
                if start=="yes" or start=="YES" or start=="Yes" or start=="y" or start=="Y":
                    printc("[*]Booting program setup...")
                    self.outp_lock=0
                    self.isEnd=1
                    self.result = self.canStartProgram
                    return 1
                elif start=="no":
                    printc("[*]Exiting the framework...")
                    self.outp_lock=0
                    self.isEnd=1
                    self.result = self.ncanStartProgram
                    return 1
                else:
                    printc("Answer is not correct, retry..")
        else:
            printc("[*]Printing help page...\n\n\n"+final_template)
            self.outp_lock=0
            self.isEnd=1
            self.result = self.giveControlToApp
            return 1
    def run(self):
        self.outp_lock = 1
        inittime=time.time()
        _date=time.localtime(inittime)
        date=str(_date.tm_mday)+"/"+str(_date.tm_mon)+"/"+str(_date.tm_year)+" "+str(_date.tm_hour)+":"+str(_date.tm_min)+":"+str(_date.tm_sec)
        printc("[*]Starting time: " + date)
        self.outp_lock = 0
        threading.Thread(target=self.CRYStartupFW).start()
        print(self.isEnd)
        while self.isEnd == 0:
            pass
        print("Self.isend:"+str(self.isEnd))
        finishtime=time.time()
        wrktime=finishtime-inittime
        print(self.outp_lock)
        while self.outp_lock==1:
            pass
        print(self.outp_lock)
        self.outp_lock=1
        _date=time.localtime(finishtime)
        date=str(_date.tm_mday)+"/"+str(_date.tm_mon)+"/"+str(_date.tm_year)+" "+str(_date.tm_hour)+":"+str(_date.tm_min)+":"+str(_date.tm_sec)
        printc("[*]End Time: "+date)
        printc("[*]WorkTime: "+str(wrktime) + "[s]")
        logc("FrameWork ended with " + str(hex(self.result)),CRYLog.deb)
        return self.result

if __name__=='__main__':
    tests=[0,0]
    printc("FrameWork startup Test!!!!!")
    cry=CRYFrameWork()
    printc("Starting Test 1...")
    watchdog=cry.run()
    printc("WatchDog Result:"+str(hex(watchdog)))
    printc("END test!!!")
    if watchdog==cry.canStartProgram:
        printc("1° test gone WELL")
        tests[0]+=1
    elif watchdog==cry.ncanStartProgram:
        printc("1° test gone WELL, exiting framework by user...")
        tests[0]+=1
    else:
        printc("1° test gone WRONG",log=False)
        logc("First Error gone wrong, waiting for User input...", CRYLog.err)
        tests[0]+=-1
        choose=input("Keep doing the 2° test?(yes/no):")
        if choose=="no":
            printc("Exiting testing phase...BYE!")
            exit
    logc("User is going too start second test...",CRYLog.warn)
    printc("Starting test 2...")
    cry.setIsStartup(0)
    printc(str(cry.isStartup))
    watchdog=cry.run()
    printc("WatchDog Result:"+str(hex(watchdog)))
    if watchdog==cry.giveControlToApp:
        printc("2° test gone WELL")
        tests[1]+=1
    else:
        printc("2° test gone WRONG", log=False)
        logc("Second Error gone Wrong", CRYLog.err)
        tests[1]+=-1
    printc("Resumee':\n   1°Test: ")
    if tests[0]==1:
        printc("PASS")
    else:
        printc("FAIL")
    print("   2°Test: ",)
    if tests[1]==1:
        printc("PASS")
    else:
        printc("FAIL")
    if tests[0]+tests[1]==2:
        printc("All the tests gone well, FrameWork can work now :)\n BYE!")
        exit
    else:
        printc("Email me at raulradu2000@yahoo.it: subject FrameWork Startup Error,then write witch test gone wrong, and the version of the framework ")
        
        
