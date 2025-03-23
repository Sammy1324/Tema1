class IP_decomposing:
    def __init__(self, ip):
        self.ip = ip
        
    def split_ip(self):
        ip = self.ip.split(".")
        return ip
    
    def list_to_bin(self):
        ip = self.split_ip()
        ip_bin = []
        for i in ip:
            ip_bin.append(bin(int(i))[2:].zfill(8))
        return ip_bin