from django.shortcuts import render, HttpResponse


from waybackurls import waybackurls
import json
import requests
import exurl
import nmap


from .models import Redirect,Xss,Xsspayload,Lfi,Lfipayload,Domain,SubdomainTakeover,Hstpayload


# Create your views here.


def network(request):
    if request.method=='POST':
        domain= request.POST['domain']
        nmScan=nmap.PortScanner()
        nmScan.scan(domain)
        dict={}
        Host=[]
        for host in nmScan.all_hosts():
            Host.append(nmScan[host].hostname()) 
            for proto in nmScan[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
        
                lport = nmScan[host][proto].keys()
                dict1={}
                for port in lport:
                    dict1[port]=nmScan[host][proto][port]['state']
                dict[host]=dict1
       
        print(dict)
        data={'dict':dict,'Host':Host}
        
        return render(request, 'network.html',data) 
        

    return render(request, 'network.html') 

def home(request):
    alldomain=Domain.objects.all()
    context={'alldomain':alldomain}
    print(alldomain)
    return render(request, 'home.html',context) 
def scan_xss(dom):
    with open(dom+"-waybackurls.json", "r") as read_file:
            urls = json.load(read_file)
            d = Domain()
            d.domain=dom
            d.save()

            payloads=Xsspayload.objects.all()
            
            for url in urls:

                for payload in payloads:
                
                    ex_urls=exurl.split_url(url[0],str(payload))
                    

                    for ex_url in ex_urls:
                        print(ex_url)
                        try:
                            req = requests.get(ex_url)
                        
                        except:
                            continue

                        if payload in req:
                            print("xss vulnerablitiy found")
                            domn=Domain.objects.filter(domain=dom)
                            bug=Xss()
                            bug.Xssid=domn[0]
                            bug.xssurl=ex_url
                            bug.save()
                            
                        else:
                            print("secure")
                            


def scan_lfi(dom):
    with open(dom+"-waybackurls.json", "r") as read_file:
            urls = json.load(read_file)
        

            payloads=Lfipayload.objects.all()
            
            for url in urls:

                for payload in payloads:
                
                    ex_urls=exurl.split_url(url[0],str(payload))
                    

                    for ex_url in ex_urls:
                        print(ex_url)
                        try:
                            req = requests.get(ex_url)
                        
                        except:
                            continue

                        if "root:x:" in req:
                            print("lfi vulnerablitiy found")
                            domn=Domain.objects.filter(domain=dom)
                            bug=Lfi()
                            bug.Lfiid=domn[0]
                            bug.lfiurl=ex_url
                            bug.save()
                            
                        else:
                            print("secure")
                            
                            
def scan_redirect(dom):
    with open(dom+"-waybackurls.json", "r") as read_file:
            urls = json.load(read_file)
            

            payloads=Lfipayload.objects.all()
            
            for url in urls:

                
                
                ex_urls=exurl.split_url(url[0],"https://www.evil.com")
                

                for ex_url in ex_urls:
                    print(ex_url)
                    try:
                        req = requests.get(ex_url)
                    
                    except:
                        continue

                    if "evil.com" in req:
                        print("redirection vulnerablitiy found")
                        domn=Domain.objects.filter(domain=dom)
                        bug=Redirect()
                        bug.Redirectid=domn[0]
                        bug.redirecturl=ex_url
                        bug.save()
                        
                    else:
                        print("secure") 
                                                      

def scan_hst(dom):
    with open(dom+"-waybackurls.json", "r") as read_file:
            urls = json.load(read_file)
            d = Domain()
            d.domain=dom
            d.save()

            payloads=Hstpayload.objects.all()
            
            for url in urls:

                for payload in payloads:
                
                    ex_urls=exurl.split_url(url[0],str(payload))
                    

                    for ex_url in ex_urls:
                        print(ex_url)
                        try:
                            req = requests.get(ex_url)
                        
                        except:
                            continue

                        if payload in req:
                            print("HST vulnerablitiy found")
                            domn=Domain.objects.filter(domain=dom)
                            bug=SubdomainTakeover()
                            bug.Stid=domn[0]
                            bug.Sturl=ex_url
                            bug.save()
                            
                        else:
                            print("secure")
    
def scan(request):
    if request.method=='POST':
        domain= request.POST['domain']
        waybackurls(domain, False)
        scan_xss(domain)
        scan_lfi(domain)
        scan_redirect(domain)
        scan_hst(domain)

    alldomain=Domain.objects.all()
    context={'alldomain':alldomain}
    print(alldomain)
        
            

    


    return render(request, 'home.html',context) 

def showdetail(request):

    if request.method=='GET':
        domain=request.GET['domain']
        d=Domain.objects.filter(domain=domain)
        x=Xss.objects.filter(Xssid=d[0])
        l=Lfi.objects.filter(Lfiid=d[0])
        r=Redirect.objects.filter(Redirectid=d[0])
        st=SubdomainTakeover.objects.filter(Stid=d[0])
        context={'domain':domain,'xss':x,'lfi':l,'redirect':r, 'hst':st}


    return render(request, 'detail.html',context) 

