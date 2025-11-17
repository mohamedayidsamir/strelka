from strelka import strelka

class TestScan(StrelkaScanner):
    def scan(self, data, file, options):
        self.event["helllllllllllllllllllllllllllllllloooooooooooooooooooooooooo"] = len(data)
