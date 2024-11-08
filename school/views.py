from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import bookresult
teachernames = ['usman']
teacherpasswords = ['1234']
studentnames = ['basheer']
studentpasswords = ['5678']
dic = {}
def percentagefind(percentage):
    if percentage <= 100 and percentage >= 90:
        lettergrage = 'A+'
    elif percentage < 90 and percentage >= 72:
        lettergrage = 'A'
    elif percentage < 72 and percentage >= 65:
        lettergrage = 'B+'
    elif percentage < 65 and percentage >= 60:
        lettergrage = 'B'
    elif percentage < 60 and percentage >= 50:
        lettergrage = 'C'
    else:
        lettergrage = 'FAIL'
    return lettergrage


# Create your views here.
def index(request):
    return render(request, 'index.html')

def studentsignin(request):
    studentname = request.POST.get('studentname')
    studentpassword = request.POST.get('studentpassword')
    print(studentname, studentpassword)
    indexes = index(request)
    if request.method == 'POST':
        if studentname in studentnames:
            nameindexs = studentnames.index(studentname)
            if studentpassword == studentpasswords[nameindexs]:
                return redirect('studentportal')
            else:
                return HttpResponse('Your password is not correct!')
        else:
            return HttpResponse("You'r Name or Password is wrong Please try again.")
    dict = {'studentname' : studentname, 'studentpassword' : studentpassword, 'index' : indexes}
    return render(request, 'studentsignin.html', dict)

def studentsignup(request):
    global teachernames
    global teacherpasswords
    teachernames = ['usman']
    teacherpasswords = ['1234']
    studentsignupname = request.POST.get('studentsignupname')
    studentsignuppassword = request.POST.get('studentsignuppassword')
    studentnames.append(studentsignupname)
    studentpasswords.append(studentsignuppassword)
    if request.method == 'POST':
        return redirect('studentsignin')
    return render(request, 'studentsignup.html')

def teachersignup(request):
    global teachernames
    global teacherpasswords
    teachernames = ['usman']
    teacherpasswords = ['1234']
    teachersignupname = request.POST.get('teachersignupname')
    teachersignuppassword = request.POST.get('teachersignuppassword')
    teachernames.append(teachersignupname)
    teacherpasswords.append(teachersignuppassword)
    if request.method == 'POST':
        return redirect('teachersignin')
    return render(request, 'teachersignup.html')

def teachersignin(request):
    teachername = request.POST.get('teachername', 'Error')
    teacherpassword = request.POST.get('teacherpassword', 'Error')
    if request.method == 'POST':
        if teachername in teachernames:
            nameindex = teachernames.index(teachername)
            if teacherpassword == teacherpasswords[nameindex]:
                return redirect('teacherportal')
            else:
                return HttpResponse('Your password is not correct!')
        else:
            return HttpResponse("You'r Name or Password is wrong Please try again.")
    dic = {'teachername' : teachername, 'teacherpassword' : teacherpassword}
    return render(request, 'teachersignin.html', dic)

def studentportal(request):
    # prod = bookresult.objects.all()
    # dic = {'prod' : prod}
    return render(request, 'studentportal.html', dic)

def addnewstd(request):  
    if request.method == 'POST':  
        rollno = request.POST.get('rollno')  # Default value for rollno  
        regno = request.POST.get('regno')  
        sname = request.POST.get('stdname')  # Ensure that 'stdname' is the correct key used in the form  
        fname = request.POST.get('fname')  
        session = request.POST.get('session')  
        semester = request.POST.get('semester') 

        courdecode = request.POST.get('courdecode')  
        crhours = request.POST.get('crhours')
        name = request.POST.get('name', 'Chemistry')  
        tmark = int(request.POST.get('tmark', 200))
        omark = int(request.POST.get('omark', 150))
        percentage = (omark / tmark * 100) if tmark > 0 else 0  
        lettergrage = percentagefind(percentage)

        courdecode1 = request.POST.get('courdecode1')  
        crhours1 = request.POST.get('crhours1')
        name1 = request.POST.get('name1', 'Chemistry')  
        tmark1 = int(request.POST.get('tmark1', 200))
        omark1 = int(request.POST.get('omark1', 150))
        percentage1 = (omark1 / tmark1 * 100) if tmark1 > 0 else 0  
        lettergrage1 = percentagefind(percentage1)

        courdecode2 = request.POST.get('courdecode2')  
        crhours2 = request.POST.get('crhours2')
        name2 = request.POST.get('name2', 'Chemistry')  
        tmark2 = int(request.POST.get('tm3rk2', 200))
        omark2 = int(request.POST.get('omark2', 150))
        percentage2 = (omark2 / tmark2 * 100) if tmark2 > 0 else 0  
        lettergrage2 = percentagefind(percentage2)

        courdecode3 = request.POST.get('courdecode3')  
        crhours3 = request.POST.get('crhours3')
        name3 = request.POST.get('name3', 'Chemistry')  
        tmark3 = int(request.POST.get('tmark3', 200))
        omark3 = int(request.POST.get('omark3', 150))
        percentage3 = (omark3 / tmark3 * 100) if tmark3 > 0 else 0  
        lettergrage3 = percentagefind(percentage3)

        courdecode4 = request.POST.get('courdecode4')  
        crhours4 = request.POST.get('crhours4')
        name4 = request.POST.get('name4', 'Chemistry')  
        tmark4 = int(request.POST.get('tmark4', 200))
        omark4 = int(request.POST.get('omark4', 150))
        percentage4 = (omark4 / tmark4 * 100) if tmark4 > 0 else 0  
        lettergrage4 = percentagefind(percentage4)

        courdecode5 = request.POST.get('courdecode5')  
        crhours5 = request.POST.get('crhours5')
        name5 = request.POST.get('name5', 'Chemistry')  
        tmark5 = int(request.POST.get('tmark5', 200))
        omark5 = int(request.POST.get('omark5', 150))
        percentage5 = (omark5 / tmark5 * 100) if tmark5 > 0 else 0  
        lettergrage5 = percentagefind(percentage5)
        
        gpa = (omark / tmark * 4.0)
        remarks = 'Promoted'
        bookresults = bookresult(  
            rollno = rollno,
            regno=regno,   
            sname=sname,   
            fname=fname,   
            session=session,   
            semester=semester,  
            
            courdecode=courdecode,  
            crhours=crhours,   
            lettergrage=lettergrage,   
            bname=name,   
            tmark=tmark, 
            omark=omark,   
            percentage=percentage,

            courdecode1=courdecode1,  
            crhours1=crhours1,   
            lettergrage1=lettergrage1,   
            bname1=name1,   
            tmark1=tmark1, 
            omark1=omark1,   
            percentage1=percentage1,

            courdecode2=courdecode2,  
            crhours2=crhours2,   
            lettergrage2=lettergrage2,   
            bname2=name2,   
            tmark2=tmark2, 
            omark2=omark2,   
            percentage2=percentage2,

            courdecode3=courdecode3,  
            crhours3=crhours3,   
            lettergrage3=lettergrage3,   
            bname3=name3,   
            tmark3=tmark3, 
            omark3=omark3,   
            percentage3=percentage3,

            courdecode4=courdecode4,  
            crhours4=crhours4,   
            lettergrage4=lettergrage4,   
            bname4=name4,   
            tmark4=tmark4, 
            omark4=omark4,   
            percentage4=percentage4,

            courdecode5=courdecode5,  
            crhours5=crhours5,   
            lettergrage5=lettergrage5,   
            bname5=name5,   
            tmark5=tmark5, 
            omark5=omark5,   
            percentage5=percentage5,

            gpa = gpa, 
            remarks = remarks
        )  
        bookresults.save()  # Save the instance  

        return redirect('teacherportal')  # Adjust to your success URL 
    

    return render(request, 'addnewstd.html')

def teacherportal(request):
    prod = bookresult.objects.all()
    if request.method=='POST':
        searchtext = request.POST.get('searchbox')
        prod = prod.filter(sname__icontains = searchtext)
        request.session.modified = True
        # return redirect('teacherportal')
    dic = {'prod' : prod}
    return render(request, 'teacherportal.html', dic)

def studentresultcard(request):
    return render(request, 'studentresultcard.html')

def changeresult(request, rollno):
    produ = bookresult.objects.filter(rollno=rollno)
    dicti = {'bookresult':produ[0]}
    if request.method == 'POST':
        crollno = request.POST.get('crollno')
        cregno = request.POST.get('cregno')
        csname = request.POST.get('csname')
        cfname = request.POST.get('cfname')
        csession = request.POST.get('csession')
        csemester = request.POST.get('csemester')

        ccourdecode = request.POST.get('ccourdecode')
        cbnames = request.POST.get('cbname')
        ccrhours = request.POST.get('ccrhours')
        ctmark = request.POST.get('ctmark')
        comark = request.POST.get('comark')
        cpercentage = (int(comark) / int(ctmark) * 100)
        clettergrade = percentagefind(cpercentage)

        ccourdecode1 = request.POST.get('ccourdecode1')
        cbnames1 = request.POST.get('cbname1')
        ccrhours1 = request.POST.get('ccrhours1')
        ctmark1 = request.POST.get('ctmark1')
        comark1 = request.POST.get('comark1')
        cpercentage1 = (int(comark1) / int(ctmark1) * 100)
        clettergrade1 = percentagefind(cpercentage1)

        ccourdecode2 = request.POST.get('ccourdecode2')
        cbnames2 = request.POST.get('cbname2')
        ccrhours2 = request.POST.get('ccrhours2')
        ctmark2 = request.POST.get('ctmark2')
        comark2 = request.POST.get('comark2')
        cpercentage2 = (int(comark2) / int(ctmark2) * 100)
        clettergrade2 = percentagefind(cpercentage2)

        ccourdecode3 = request.POST.get('ccourdecode3')
        cbnames3 = request.POST.get('cbname3')
        ccrhours3 = request.POST.get('ccrhours3')
        ctmark3 = request.POST.get('ctmark3')
        comark3 = request.POST.get('comark3')
        cpercentage3 = (int(comark3) / int(ctmark3) * 100)
        clettergrade3 = percentagefind(cpercentage3)

        ccourdecode4 = request.POST.get('ccourdecode4')
        cbnames4 = request.POST.get('cbname4')
        ccrhours4 = request.POST.get('ccrhours4')
        ctmark4 = request.POST.get('ctmark4')
        comark4 = request.POST.get('comark4')
        cpercentage4 = (int(comark4) / int(ctmark4) * 100)
        clettergrade4 = percentagefind(cpercentage4)

        ccourdecode5 = request.POST.get('ccourdecode5')
        cbnames5 = request.POST.get('cbname5')
        ccrhours5 = request.POST.get('ccrhours5')
        ctmark5 = request.POST.get('ctmark5')
        comark5 = request.POST.get('comark5')
        cpercentage5 = (int(comark5) / int(ctmark5) * 100)
        clettergrade5 = percentagefind(cpercentage5)

        bookresult.objects.all()
        bookresult.objects.filter(rollno = rollno).update(rollno=crollno)
        bookresult.objects.filter(rollno = rollno).update(regno=cregno)
        bookresult.objects.filter(rollno = rollno).update(sname=csname)
        bookresult.objects.filter(rollno = rollno).update(fname=cfname)
        bookresult.objects.filter(rollno = rollno).update(session=csession)
        bookresult.objects.filter(rollno = rollno).update(semester=csemester)

        bookresult.objects.filter(rollno = rollno).update(courdecode=ccourdecode)
        bookresult.objects.filter(rollno = rollno).update(bname=cbnames)
        bookresult.objects.filter(rollno = rollno).update(crhours=ccrhours)
        bookresult.objects.filter(rollno = rollno).update(tmark=ctmark)
        bookresult.objects.filter(rollno = rollno).update(omark=comark)
        bookresult.objects.filter(rollno = rollno).update(percentage=cpercentage)
        bookresult.objects.filter(rollno = rollno).update(lettergrage=clettergrade)

        bookresult.objects.filter(rollno = rollno).update(courdecode1=ccourdecode1)
        bookresult.objects.filter(rollno = rollno).update(bname1=cbnames1)
        bookresult.objects.filter(rollno = rollno).update(crhours1=ccrhours1)
        bookresult.objects.filter(rollno = rollno).update(tmark1=ctmark1)
        bookresult.objects.filter(rollno = rollno).update(omark1=comark1)
        bookresult.objects.filter(rollno = rollno).update(percentage1=cpercentage1)
        bookresult.objects.filter(rollno = rollno).update(lettergrage1=clettergrade1)

        bookresult.objects.filter(rollno = rollno).update(courdecode2=ccourdecode2)
        bookresult.objects.filter(rollno = rollno).update(bname2=cbnames2)
        bookresult.objects.filter(rollno = rollno).update(crhours2=ccrhours2)
        bookresult.objects.filter(rollno = rollno).update(tmark2=ctmark2)
        bookresult.objects.filter(rollno = rollno).update(omark2=comark2)
        bookresult.objects.filter(rollno = rollno).update(percentage2=cpercentage2)
        bookresult.objects.filter(rollno = rollno).update(lettergrage2=clettergrade2)

        bookresult.objects.filter(rollno = rollno).update(courdecode3=ccourdecode3)
        bookresult.objects.filter(rollno = rollno).update(bname3=cbnames3)
        bookresult.objects.filter(rollno = rollno).update(crhours3=ccrhours3)
        bookresult.objects.filter(rollno = rollno).update(tmark3=ctmark3)
        bookresult.objects.filter(rollno = rollno).update(omark3=comark3)
        bookresult.objects.filter(rollno = rollno).update(percentage3=cpercentage3)
        bookresult.objects.filter(rollno = rollno).update(lettergrage3=clettergrade3)

        bookresult.objects.filter(rollno = rollno).update(courdecode4=ccourdecode4)
        bookresult.objects.filter(rollno = rollno).update(bname4=cbnames4)
        bookresult.objects.filter(rollno = rollno).update(crhours4=ccrhours4)
        bookresult.objects.filter(rollno = rollno).update(tmark4=ctmark4)
        bookresult.objects.filter(rollno = rollno).update(omark4=comark4)
        bookresult.objects.filter(rollno = rollno).update(percentage4=cpercentage4)
        bookresult.objects.filter(rollno = rollno).update(lettergrage4=clettergrade4)

        bookresult.objects.filter(rollno = rollno).update(courdecode5=ccourdecode5)
        bookresult.objects.filter(rollno = rollno).update(bname5=cbnames5)
        bookresult.objects.filter(rollno = rollno).update(crhours5=ccrhours5)
        bookresult.objects.filter(rollno = rollno).update(tmark5=ctmark5)
        bookresult.objects.filter(rollno = rollno).update(omark5=comark5)
        bookresult.objects.filter(rollno = rollno).update(percentage5=cpercentage5)
        bookresult.objects.filter(rollno = rollno).update(lettergrage5=clettergrade5)

        return redirect('teacherportal')
    return render(request, 'changeresult.html', dicti)


def viewresult(request, rollno):
    produ = bookresult.objects.filter(rollno=rollno)
    sdata = {'bookresult':produ[0]}

    return render(request, 'viewresult.html', sdata)