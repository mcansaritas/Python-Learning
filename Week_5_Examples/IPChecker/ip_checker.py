def ipchecker (x):
    ip_address = x
    empyty_element = ""
    dot_counter = x.count(".")
    ip_address_separator = x.split(".")
    for x in range(4):
        if dot_counter < 3:
            print("This can't be an IP address. Because there isn't 3 '.' between octets.")
            break
        else :
            if ip_address_separator [x] == empyty_element:
                print("This can't be an IP address.")
                break
            elif (ip_address_separator[x].isdigit() == False):
                print("This can't be an IP address. It is not digit")
            elif int(ip_address_separator[x]) > 255:
                print("This is not an IP address. Octet can't be bigger than 255")
                break
            elif int(ip_address_separator[x]) <= 255 and x == 3 :
                print("This is an IP address.")
                break
            else :
                continue
    return ip_address