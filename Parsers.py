from Models import LogEntry
import datetime  

class Parser: 

    def __init__(self, f :open):
        self.f = f  
        self.log_lines = []
        self.filtered_lines = []
        self.rejected_line = [] 
        self.cheaked_lines  = []
        self.count_line = 0 
        self.obj_entryList = []

    def CombinedFormatParser (self):
        for line in self.f: 
            self.log_lines.append(line)
        

        for line in self.log_lines:
            self.count_line += 1 
            if (len (line.split('"'))) == 7:
                self.cheaked_lines.append(line)
            else:
                self.rejected_line.append(f"Line: {self.count_line} contains more or less then 7 postional value ")


        for line in self.cheaked_lines:
            self.filtered_lines.append(line.split())
            


        for line in self.filtered_lines: 
            rem_timebraket =  line[3].strip("[")        # Remove --> [
 
            try: # remove unvalid time (strptime()--> only filter valid times)
             timestamp = datetime.datetime.strptime(rem_timebraket,  '%d/%b/%Y:%H:%M:%S' ) 
             
             logobj = LogEntry (ip=line[0],timestamp=timestamp,method=line[5],path=line[6],protocol=line[7],status=line [8],bytes_sent=line[9],user_agent=line[11])
            except (ValueError):
             self.rejected_line.append((f"Line : {"--"} got rejected because of invalid Timestamp"))
             continue
           
            self.obj_entryList.append(logobj)



        return self.obj_entryList  
        
