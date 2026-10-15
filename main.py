from Parsers import Parser 
from Analyzers import Analyzer 
from Report import Reporter 
import os 
import sys 
import datetime 
import gzip

# path = "/var/log/nginx/"
path = sys.argv[1]  

output_path = None
Orrginal_stdout = sys.stdout



File_and_TimeMap = {}                ##Only to Store the [fd : timestamp]
file_obj_list = []                  ## store the fileobject to keep the fd alive 


##SORT OLDEST TO NEWEST
if os.path.isdir(path):                                                             ##cheak if the argumant is a  directory 
     for file in os.listdir(path):   
          full_path = os.path.join(path, file)     
          motifytime = os.path.getmtime(full_path)                                    
          timestamp = str(datetime.datetime.fromtimestamp(motifytime))              ##Get&filter linuxtime--> Normal Timestamp
          
          #-->  #--> Cheak if the file is a (.gzip)
          file_name_list = os.path.splitext(file)                                     # retuns a Touple with (name, .ex)-->  comma (,) unpacks the the touple 

          
          if ".gz" in file_name_list: 
               gzipfile_file_obj = gzip.open(full_path,"rb")
               file_obj_list.append(gzipfile_file_obj)  # ---> keeping the FD alive 

               File_and_TimeMap [full_path] = [gzipfile_file_obj.fileno(), timestamp]      ## HashMap += (filename : [Fd,timestamp] ) 

          else:                                                               
               file_obj = open(full_path,"r")                                            
               file_obj_list.append(file_obj)   # --->keeping the FD alive                                  

               File_and_TimeMap [full_path] = [file_obj.fileno(), timestamp]              ## HashMap += (filename : [Fd,timestamp] ) 

     
     def demofunc(filemap_touple):
          return filemap_touple[1][1]                                           ### Funtion thats return the timestamp from List of touple()
     
     sortedbytime = sorted(File_and_TimeMap.items(), key=demofunc )             ## sorting by timestamps and fd's stil remained as int  





                                                         
## Open() EACH ONE AND GIVE THEM TO PARSER AND ANALYSER 

     New_ouput_file_counter = 0 
     for element in sortedbytime:                                           ##Take int( fd:) from sortedlist -->  
          fd = element[1][0]                                                # open() New file_obj with the active fd nummer--> parse them each 
          full_path  = element [0]

          if ".gz" in full_path: 
               f = gzip.open (full_path, "rt")

          else :
               f = open (full_path,"r") 

          try:
               parser = Parser (f) 
               analyzer = Analyzer (parser.CombinedFormatParser())
               reporter = Reporter (parser,analyzer)






## OUTPUT -> SET THE RIGHT FD POINTER, CREATE SEPARATE OUTPUT FILES FOR EACH LOG FILE --> AND REPORT THEM () 
## ---> only accept Folder also as a output Paths 

               now = datetime.datetime.now().strftime("%a %d %b %Y, %I:%M")
               
               if len(sys.argv) > 2:    
                    output_path = sys.argv[2]                                     # Just to cheak if any value even exist --> IF YES POINT the Stdout to that FILE -->  !    
                    file :str = f"analyzed.log.{New_ouput_file_counter}.{now}"                        # Create New File Each time and Join them  with the folder path                          
                    output_path = os.path.join (output_path,file)         
                    with open (output_path,"w") as out: 
                     sys.stdout = out                                             # Replaciing the orginal Stdout fileobejct -- > to New one
                     reporter.report_Everything() 
                     sys.stdout = Orrginal_stdout
                     New_ouput_file_counter += 1                                   # bring back the stdout to orgnial File object
                                                                             
               else :
                    reporter.report_Everything()

          except: 
               print ("Not a access.Logfile or can be a Permission Error! ")

          






## IF THE SOURCE LOG PATH IS A SPECEFIC ONE FILE  ---> Output also to a singel file /folder/file   

 
else:   

      #--> Cheak if the file is a (.gzip)  
     filename = os.path.basename(path)                           # abstruct the the file name from full pathname 
     if ".gz" in filename: 
          f = gzip.open(path, "r") 
     else : 
          f =  open (path, "r") 
     
     try:
          parser = Parser(f)
          analyzer = Analyzer (parser.CombinedFormatParser())
          reporter = Reporter(parser,analyzer)

          if len(sys.argv) > 2:                                   # Just to cheak if any value even exist --> IF YES POINT the Stdout to that FILE -->  ! 
               output_path = sys.argv[2]
               with open (output_path,"w") as out: 
                    sys.stdout = out     
                    reporter.report_Everything()                  # Replaciing the orginal Stdout fileobejct  -- > to New one
                    sys.stdout = Orrginal_stdout  
          else :    
              reporter.report_Everything()     
     except:
          print ("File not found or permission error")
          

f.close()
 


