#Import thư viện TorIpChanger để sử dụng Tor để thay đổi địa chỉ IP
from toripchanger import TorIpChanger

'''Tạo đối tượng TorIpChanger với reuse_threshold=0, 
có nghĩa là tạo một địa chỉ IP mới cho mỗi yêu cầu'''
tor_ip_changer_0 = TorIpChanger(reuse_threshold=0)

#Lấy địa chỉ IP mới từ Tor
current_ip = tor_ip_changer_0.get_new_ip()

'''Tạo đối tượng TorIpChanger với 
local_http_proxy='127.0.0.1:8888', có nghĩa là 
sử dụng proxy HTTP ở localhost cổng 8888 để kết nối đến Tor'''
tor_ip_changer_1 = TorIpChanger(local_http_proxy='127.0.0.1:8888')

#Lấy địa chỉ IP mới từ Tor
current_ip = tor_ip_changer_1.get_new_ip()

'''Tạo đối tượng TorIpChanger với tor_address="localhost" 
và reuse_threshold=5, có nghĩa là sử dụng cổng mặc định của Tor 
ở localhost và sử dụng cùng một địa chỉ IP cho tối đa 5 yêu cầu'''
tor_ip_changer_5 = TorIpChanger(tor_address="localhost",
                                 reuse_threshold=5)

#Lấy địa chỉ IP mới từ Tor
current_ip = tor_ip_changer_5.get_new_ip()