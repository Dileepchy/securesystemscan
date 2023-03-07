# Django-scanner

The django system helps in scanning web vulnerabilitieslike xss, lfi and redirection with the help of exurl, waybackurls tools. The user can add the xss and lfi payloads in django backend for scanning the bugs. Likewise, it stores the bug in backend.
directory listing
The system takes the domain as input , uses waybackurls to get the urls. Then the payloads are fetched from database and with the help of exurl, the payloads are used in url and requested.

1 if payload is retured as response itself, the xss is detected
2 if "root:x:" or content of passwd file, is returned as response itself, the lfi is detected
3 if evil.com or content of evil.com webpage is returned, open redirection is detected

After detection, the issues are saved in database. 
Different payloads can be added to database to be used in scanning xss and lfi.

The django system also help in scanning networks. It helps to know the open ports with the help of nmap tool.

The system takes input and feeds the input to python-nmap tool to get the active network along with the ports status.


# Installation
1. pip3 install -r requirements.txt
2. Run the django server
