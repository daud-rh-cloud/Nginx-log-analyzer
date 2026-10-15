from Analyzers import Analyzer
from Parsers import Parser

class Reporter:


    def __init__(self, parserOBJ :Parser, analyzerOBJ :Analyzer):
        self.analyzerOBJ = analyzerOBJ 
        self.parserOBJ = parserOBJ
         


    def report_Everything(self): 
        print ("=== logsentry report: sample.log ===")
        print  (f"TOTAL Logs counted : {self.parserOBJ.count_line} Line ") 
        print  ("                          "
                "                           "
                "                          "
                "                          ") 
                       
               
                                 
                                
        print ("Status codes:")
        self.analyzerOBJ.status_codes()
        self.analyzerOBJ.calculateErrorRate()
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )
        



        print ("Top IPs:")
        self.analyzerOBJ.popular_ip()
        print  ("                          "
                "                           "
        
                "                          "
                "                          "
                )



        
        self.analyzerOBJ.total_bytes_sent()

                        
        print ("Top paths:")
        self.analyzerOBJ.top_path()  
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )

        print ("Requests per hour:")
        self.analyzerOBJ.request_perHour()
        print  ("                          "
                "                           "
                "                          "
                "                          "
                )

        

        print ("WARNING:")
        print ("rejected.log:")
        for bad in self.parserOBJ.rejected_line:
            print (bad )