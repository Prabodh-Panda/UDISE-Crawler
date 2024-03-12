import crawler

input_str = input("Enter the list of pincode separated by comma: ")
pincodes = input_str.split(",")

base_pincode = pincodes[0]
pincode_range = pincodes[1:]

crawler.initiate_crawl(base_pincode)
crawler.crawl_range(pincode_range)