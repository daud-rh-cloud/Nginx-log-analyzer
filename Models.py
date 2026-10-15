class LogEntry:

    def __init__(self,ip,timestamp,method,path,protocol,status,bytes_sent,user_agent):
        self.ip = ip 
        self.timestamp = timestamp
        self.method = method
        self.path = path 
        self.protocol = protocol 
        self.status =  status
        self.bytes_sent = int (bytes_sent ) 
        self.user_agent = user_agent






    def __str__(self):
        return f"Logentry:- IP:- {self.ip} TIME:- {self.timestamp} {self.method} {self.path} {self.protocol} {self.status} {self.bytes_sent} {self.user_agent}" 