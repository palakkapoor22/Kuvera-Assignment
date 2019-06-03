from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
			investment=float( form.cleaned_data['investment'])
			date= form.cleaned_data['date']
			date_purchase=date.strftime('%d-%b-%Y')
			date2= form.cleaned_data['date2']
			date_sell=date2.strftime('%d-%b-%Y')
			limit_date=datetime.strptime('01-04-2015', '%d-%m-%Y')
			lt=limit_date.strftime('%d-%b-%Y')
			if date_purchase > date_sell:
				raise ValueError("The purchase date cannot be after selling date!")
			if date_purchase < lt:
				raise ValueError("The purchase date cannot be less than 01-04-2015!")
			fh = request.POST['fund_house']
			nav1=0
			nav2=0
			file = open('/home/iiitg/kuvera/kuvera/assignment/nav.txt')
			for line in file:
				fields = line.strip().split(';')
				if fields[1]==fh and fields[7]==date_purchase:
					nav1=float(fields[4])
				if fields[1]==fh and fields[7]==date_sell:
					nav2=float(fields[4])	
			if nav1 and nav2 :
				units=investment/nav1
				investment_amount=units*nav2	
			else:
				print("nav error")		
				raise ValueError("NAV data not available for the given date!") 
#			print("dt",date_purchase,"date sell",date_sell,"inv",investment,"fh",fh,"nav",nav1,"un",units,"n2",nav2,"ia",investment_amount)
			result={'date_purchase':date_purchase , 'date_sell':date_sell , 'investment':investment, 'nav1':nav1 ,'nav2':nav2, 'amount':round(investment_amount,3)}			
			file.close()
			return render(request, 'result.html',{"res":result})
		else:
			print ("not valid")
			raise ValueError("Valid input not provided!") 
    # if a GET (or any other method) we'll create a blank form
	else:
		file = open('/home/iiitg/kuvera/kuvera/assignment/nav.txt')
		fund_house=[]
		#fund_hous={1:'abc',2:'qrs'}
		for line in file:
			fields = line.strip().split(';')
			#print line
			fHouse=fields[1] 
			#nav=fields[4] 
			#dt=fields[7]
			if fHouse not in fund_house:
				fund_house.append(fHouse)
		form = NameForm()
		file.close()
		return render(request, 'template.html',{"form":form,"fund_house":fund_house})
	
	raise ValueError("Invalid Request!") 
	return HttpResponseRedirect('error')
	
