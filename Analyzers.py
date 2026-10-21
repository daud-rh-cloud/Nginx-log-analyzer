from Parsers import Parser
from Models import LogEntry
from datetime import datetime 

class Analyzer: 


    def __init__(self, obj_entryList :Parser):
        self.obj_entryList = obj_entryList
        self.time_list = []
        self.error_rate = 0 
   



    def status_codes (self):
        statuscodes_list = []
        for obj in self.obj_entryList: 
             statuscodes_list.append(obj.status) 

        
        counts = {}                                  
        for code in statuscodes_list: 
            if code in counts: 
                     counts[code] += 1
            else: 
                    counts[code] = 1 
    
#error rate count for 5xx 
        totalReq = 0  
        total5xx = 0 
        for i in counts.items():
             totalReq += i[1]          ##storing ammout of totalreq for later devide 
             if "5" in i[0]: 
                total5xx += i[1] 
                 
        try: 
            self.error_rate = total5xx / totalReq * 100  
     
        except(ZeroDivisionError):
            return None
            
            


        
        def demofunc(parameter_touple):
         return parameter_touple [1]
        result =dict (sorted (counts.items(), key=demofunc, reverse=True))


        return result 

        # list_of_statuscode = []            ## a list so we can return the value istead of prit ()
        # x = 0       
        # # print ("Status code / : ")
        # for STCODE, N  in result:
        #  list_of_statuscode.append (f"{STCODE:<18}{N}")     

        # return list_of_statuscode



         

    def calculateErrorRate(self): 
        return  self.error_rate   









    def popular_ip(self):
        ip_list = []
        for obj in self.obj_entryList: 
            ip_list.append(obj.ip) 

        counts = {}                                  
        for ip in ip_list:
            if ip in counts: 
                counts[ip] += 1
            else: 
                counts[ip] = 1  
                

        # NOTES --- ----- -------------------
        # the count.item makes each key:value to list of touple(key,value), and the sort need to know the sort key/value 
        # the ( key = ) is a parameter thats sort takes and expects a our own castom written funtion thats retuen the value 
        # that we want to sort with... 
        # it later passes the count.item as parametet to out castom funtion 
        # option -1 (wrtting the castom Funtion myself) //   --or Lambda 

        def my_sort(counts):
            return counts[1]
        
        result = dict(sorted (counts.items(), key= my_sort, reverse=True))

        return result


        # list_of_ip = []
        # x = 0 
        # for ip, N  in result :
        #  x += 1 
        #  list_of_ip.append(f"{ip:<18}{N}")
        #  if x == 4:
        #      break 

        # return list_of_ip

         
 






    def top_path (self):
        path_list :list = []
        for obj in self.obj_entryList:
           path_list.append(obj.method + "  " + obj.path) 
           

        counts = {}
        for path in path_list:
            path = path.lstrip('"')

            if path in counts: 
                counts[path] += 1 
            else : 
                counts[path] = 1 

        def demofunc(parameter_touple):
                return parameter_touple [1]

        result = sorted (counts.items(), key=demofunc, reverse=True)

        # print ("TOP PATHS / : ") /// Splited the Method and GET/ to print them with fixed space in btw 
        list_of_paths = []
        x = 0
        for thepath, Nummer  in result :                   
            x += 1 
            thepath = thepath.split()      
            list_of_paths.append(f"{thepath[0]:<6} {thepath[1]:<11} : {Nummer} ")
            if x == 4 :
                break 

        return list_of_paths











    def request_perHour(self):
        for obj in self.obj_entryList :
              self.time_list.append(obj.timestamp)

    
        splited_time = []
        for time in self.time_list:
            time  = str(time)
            splited_time.append (time.split(":"))

        
            
        DateHourMIn : str
        counts = {}
        for i in splited_time: 
            DateHourMIn = i [0]
            DateHourMIn = DateHourMIn.split()
            DateHourMIn = DateHourMIn[0] + " time:" +DateHourMIn[1]
            
            if DateHourMIn in counts :
                counts[DateHourMIn] += 1 
            else :
                 counts[DateHourMIn] = 1


        
        rev_counts = reversed(counts.items())   ## it will return iterator object (has __next__()) but wuith the item being in reversed 

        list_of_times = []
        for key,value in rev_counts: 
           list_of_times.append(f"{key:<16} : {value}")             
        
        return list_of_times



    def total_bytes_sent (self):
        totalbytes = 0 
        for obj in self.obj_entryList: 
            totalbytes += obj.bytes_sent 
        return (f"Total Bytes Sent: {totalbytes}")



    def getFromAndTO_timestamp (self):
        last_obj_nummer = len(self.obj_entryList)
        first_obj_time = self.obj_entryList[0].timestamp
        last_obj_time = self.obj_entryList[last_obj_nummer - 1].timestamp   ##the len() counted from 1 so we have to -1

      

        joined_time = f"{first_obj_time.strftime("%d-%b-%Y")}___{last_obj_time.strftime("%d-%b-%Y")}" 
        return joined_time



    # def rejected_lines (self):
    #     return (Parser.rejected_line) 
             
        
                