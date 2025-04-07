from abc import ABC, abstractmethod

class Report(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        pass

        
class DetailedReport(Report):
    def generate(self):
        return f"Detailed Report: {self.data}"


class CompactReport(Report):  
    def generate(self):
        return f"Compact Report: {self.data}"
         

class SummaryReport(Report):  
    def generate(self):
        return f"Summary Report: {self.data}"
         

# Example Usage
reports = [
    DetailedReport("Detailed Report Text..."), 
    CompactReport("Compact Report Text.."), 
    SummaryReport("Sumary Report Text..")
]

for report in reports:
    print(report.generate())