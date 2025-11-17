from strelka import strelka

class TestScan(strelka.Scanner):
    def scan(self, data, file, options):
        self.event["helllllllllllllllllllllllllllllllloooooooooooooooooooooooooo"] = len(data)
