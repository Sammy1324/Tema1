from IP_decomposition import IP_decomposing

ip = "11000000.10101000.01111011.10000100"

def main():
    ip_obj = IP_decomposing(ip)
    for i in ip_obj.list_to_bin():
        print(i)
        
if __name__ == "__main__":
    main()