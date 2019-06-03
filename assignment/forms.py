from django import forms
import datetime
class NameForm(forms.Form):
	investment = forms.CharField(label='Investment Amount', max_length=100, required=True)
	date = forms.DateField(input_formats=['%d-%b-%Y','%d-%m-%Y','%m/%d/%y','%d/%m/%y','%b-%d-%Y'],required=True)
	date2 = forms.DateField(input_formats=['%d-%b-%Y','%d-%m-%Y','%m/%d/%y','%d/%m/%y','%b-%d-%Y'],required=True)

	#choicelist = tuple(ch)
	#fHouse = forms.ChoiceField(choices=[])

	#fHouse = forms.ChoiceField(label="Fund House",choices=[])
	#def __init__(self,ch=None,*args,**kwargs):
	#	super(NameForm,self).__init__(*args,**kwargs)
	#	if ch:
	#		print (ch)
	#		self.fields['fHouse'].choices=[(str(k)) for k in enumerate(ch)]	
