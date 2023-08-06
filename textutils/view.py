from django.http import HttpResponse
from django.shortcuts import render

def fun(request):
    return render(request,"index.html")
def analyise(request):
    djtext=request.POST.get('text','default')
    removepun=request.POST.get('removepun','off')
    removextraspace=request.POST.get('removextraspace','off')
    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    capitalised=request.POST.get('capitalised','off')
    title=request.POST.get('title','off')
    swapcase=request.POST.get('swapcase','off')
    removenewline=request.POST.get('removenewline','off')
    puncuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    ## this is the way through which only one works at a time


    # if removepun=="on":
    #     ans=''
    #     n=len(djtext)
    #     i=0
    #     while i<n:
    #         if djtext[i] not in puncuation:
    #             ans+=djtext[i]
    #         elif djtext[i]=='.' and i==n-1:
    #             ans+=djtext[i]
    #         i+=1
    #     param={'perpose':'Remove Puncutation','AnalyisedText':ans}
    #     return render(request,'analysied.html',param)
    # elif uppercase=="on":
    #     param={'perpose':'Changed to UpperCase','AnalyisedText':djtext.upper()}
    #     return render(request,'analysied.html',param)
    # elif lowercase=="on":
    #     param={'perpose':'Changed to LowerCase','AnalyisedText':djtext.lower()}
    #     return render(request,'analysied.html',param)
    # elif capitalised=="on":
    #     param={'perpose':'Capitalised ','AnalyisedText':djtext.capitalize()}
    #     return render(request,'analysied.html',param)
    # elif title=="on":
    #     param={'perpose':'Titled ','AnalyisedText':djtext.title()}
    #     return render(request,'analysied.html',param)
    # elif swapcase=="on":
    #     param={'perpose':'Swaped Cases ','AnalyisedText':djtext.swapcase()}
    #     return render(request,'analysied.html',param)
    # elif removenewline=="on":
    #     ans=''
    #     for i in djtext:
    #         if i!='\n':
    #             ans+=i
    #     param={'perpose':'Remove new line ','AnalyisedText':ans}
    #     return render(request,'analysied.html',param)
    # else:
    #     return HttpResponse("Error")


    ## this is the way through which we can checked more than one checkbox and that works fine .....This is not the appropritate way to use ..
    count=0
    if removepun=="on":
        count+=1
        ans=''
        n=len(djtext)
        i=0
        while i<n:
            if djtext[i] not in puncuation:
                ans+=djtext[i]
            elif djtext[i]=='.' and i==n-1:
                ans+=djtext[i]
            i+=1
        djtext=ans
        param={'perpose':'Remove Puncutation','AnalyisedText':ans}
        # return render(request,'analysied.html',param)
        if removextraspace=="on":
            count+=1
            ans=''
            i=0
            n=len(djtext)
            while i<n-1:
                if djtext[i]==' ' and djtext[i+1]==' ':
                    pass
                else:
                    ans+=djtext[i]
                i+=1
            djtext=ans
            param={'perpose':'Removed extra Space','AnalyisedText':ans}
    if uppercase=="on":
        count+=1
        djtext=djtext.upper()
        param={'perpose':'Changed to UpperCase','AnalyisedText':djtext}
        # return render(request,'analysied.html',param)
    if lowercase=="on":
        count+=1
        djtext=djtext.lower()
        param={'perpose':'Changed to LowerCase','AnalyisedText':djtext}
        # return render(request,'analysied.html',param)
    if capitalised=="on":
        count+=1
        djtext=djtext.capitalize()
        param={'perpose':'Capitalised ','AnalyisedText':djtext}
        # return render(request,'analysied.html',param)
    if title=="on":
        count+=1
        djtext=djtext.title()
        param={'perpose':'Titled ','AnalyisedText':djtext}
        # return render(request,'analysied.html',param)
    if swapcase=="on":
        count+=1
        djtext=djtext.swapcase()
        param={'perpose':'Swaped Cases ','AnalyisedText':djtext}
        # return render(request,'analysied.html',param)
    if removenewline=="on":
        count+=1
        ans=''
        for i in djtext:
            # in network sending new line we use /r and /n both that's why we have to remove both
            if i!='\n' and i!='\r': 
                ans+=i
        djtext=ans
        param={'perpose':'Remove new line ','AnalyisedText':ans}
        # return render(request,'analysied.html',param)
    if count>1:
        param['perpose']='Selected Checked box operations have been applied.'
    if  removepun!="on" and removenewline!='on' and removextraspace!='on' and swapcase!='on' and title!="on" and capitalised!="on" and lowercase!="on" and uppercase!="on":
        return HttpResponse("Please choose any operations !")
    else:
        return render(request,'analysied.html',param)
        
    # 
