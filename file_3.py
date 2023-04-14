# Import thư viện urllib.request để thực hiện các yêu cầu mạng
import urllib.request 

# Import thư viện time để sử dụng hàm sleep() để chờ đợi
import time 

# Import module Signal từ thư viện stem, dùng để kích hoạt Tor controller
from stem import Signal  

# Import module Controller từ thư viện stem.control để kết nối và điều khiển Tor
from stem.control import Controller  


# Định nghĩa hàm request để thực hiện yêu cầu HTTP thông qua proxy
def request(url): 
    def _set_urlproxy():  # Định nghĩa hàm _set_urlproxy để cấu hình proxy cho urllib.request
        proxy_support = urllib.request.ProxyHandler({"http": "http://127.0.0.1:8118"})
        # Tạo một đối tượng proxy_support với thông số "http": "http://127.0.0.1:8118"
        opener = urllib.request.build_opener(proxy_support)  # Tạo một đối tượng opener bằng cách sử dụng proxy_support
        urllib.request.install_opener(opener)  # Cài đặt opener làm opener mặc định cho toàn bộ chương trình

    _set_urlproxy()  # Gọi hàm _set_urlproxy() để cấu hình proxy cho urllib.request

    headers = {'User-Agent': 'Mozilla/5.0'}  # Tạo một đối tượng headers chứa thông tin về User-Agent
    req = urllib.request.Request(url, headers=headers)  # Tạo một đối tượng yêu cầu Request với thông tin url và headers
    return urllib.request.urlopen(req).read()  # Thực hiện yêu cầu và trả về nội dung trang web

newIP = "0.0.0.0"  # Khởi tạo newIP với giá trị "0.0.0.0"
oldIP = "0.0.0.0"  # Khởi tạo oldIP với giá trị "0.0.0.0"

for i in range(5):  # Lặp lại 5 lần
    if newIP == "0.0.0.0":  # Nếu newIP vẫn là "0.0.0.0"
        newIP = request("http://icanhazip.com/")  # Thực hiện yêu cầu để lấy địa chỉ IP
    else:  # Nếu newIP đã được cập nhật
        oldIP = newIP  # Gán giá trị của newIP cho oldIP
        newIP = request("http://icanhazip.com/")  # Thực hiện yêu cầu để lấy địa chỉ IP mới
    print("newIP: %s" % newIP)  # In ra địa chỉ IP mới

seconds = 0  # Khởi tạo biến seconds với giá trị 0

while oldIP == newIP:  # Lặp lại cho đến khi địa chỉ IP mới khác với địa chỉ IP cũ
    time.sleep(2)  # Dừng chương trình trong 2 giây
    seconds += 2  # Tăng giá trị của biến seconds lên 2
    newIP = request("http://icanhazip.com/")  # Thực hiện yêu cầu để lấy địa chỉ IP mới
    print("%d seconds elapsed awaiting a different IP address." % seconds)  # In ra số giây đã trôi qua
    print("")
    print("newIP: %s" % newIP)  # In ra địa chỉ IP mới
