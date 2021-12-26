import speedtest

test = speedtest.Speedtest()

print("Loading servers list ...")
test.get_servers() # get list of servers
print("Choosing the best and appropriate server ...")
best = test.get_best_server() #choose the best server

print(f"Founded: {best['host']} Location: {best['country']}")

print("Download mb/s ...")
download_result = test.download()

print("Upload mb/s ...")
upload_result = test.upload()
ping_result = test.results.ping

print("Chosen list and server:")

print(f"Download {download_result / 1024 / 1024:.2f}") # a simple mathematic to transform the bite counting
print(f"Upload {upload_result / 1024 / 1024:.2f}")
print(f"Ping {ping_result:.2f}")