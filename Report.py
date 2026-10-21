from Analyzers import Analyzer
from Parsers import Parser

class Reporter:


    def __init__(self, parserOBJ :Parser, analyzerOBJ :Analyzer):
        self.analyzerOBJ = analyzerOBJ 
        self.parserOBJ = parserOBJ
         
    def report_FILES_FromAndTO_time(self):
        return self.analyzerOBJ.getFromAndTO_timestamp()
         
    

        

    def report_Everything(self): 
        return { "TOTAL Logs counted" : self.parserOBJ.count_line, 
                 "Status codes" : self.analyzerOBJ.status_codes(), 
                 "Error rates" : self.analyzerOBJ.calculateErrorRate(),
                 "Top_IPs" : self.analyzerOBJ.popular_ip(),
                 "Total Bytes Sent" : self.analyzerOBJ.total_bytes_sent(),
                 "Top paths" : self.analyzerOBJ.top_path(),
                 "Requests per hour" : self.analyzerOBJ.request_perHour(),
                 "Rejected" : self.parserOBJ.rejected_line}