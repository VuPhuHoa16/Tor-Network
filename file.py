#Import thư viện TorIpChanger để sử dụng Tor để thay đổi địa chỉ IP
from toripchanger import TorIpChanger

# Khởi tạo một đối tượng TorIpChanger
tor_ip_changer = TorIpChanger(tor_password='my_password', tor_port=9051,
                               local_http_proxy='127.0.0.1:8118')

# Thay đổi địa chỉ IP
tor_ip_changer.get_new_ip()

# Kiểm tra địa chỉ IP mới
print(tor_ip_changer.get_current_ip())