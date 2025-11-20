from django import forms
from . import models
from captcha.fields import CaptchaField



class DateInput(forms.DateInput):
	input_type = 'date'


class ReadForm(forms.ModelForm):
	class Meta:
		model= models.Read
		fields = ['title', 'rating', 'review', 'date']
		widgets = {'date' : DateInput(), }

	def __init__(self, *args, **kwargs):
		super(ReadForm, self).__init__(*args, **kwargs)
		self.fields['title'].label="Book Title"
		self.fields['rating'].label="Book Rating (1-5)"
		self.fields['review'].label="Book Review"
		self.fields['date'].label="Finished Date"

class TBRForm(forms.ModelForm):
	class Meta:
		model= models.TBR
		fields = ['title', 'author', 'description']

	def __init__(self, *args, **kwargs):
		super(TBRForm, self).__init__(*args, **kwargs)
		self.fields['title'].label="Book Title"
		self.fields['author'].label="Book Author"
		self.fields['description'].label="Book Description"

class AskForm(forms.ModelForm):
	class Meta:
		model= models.Ask
		fields = ['title', 'description', 'triggers']

	def __init__(self, *args, **kwargs):
		super(AskForm, self).__init__(*args, **kwargs)
		self.fields['title'].label="Subject Title"
		self.fields['description'].label="What Kind Of Book I'm Looking For"
		self.fields['triggers'].label="Stuff I Don't Want"

class RecForm(forms.ModelForm):
	class Meta:
		model= models.Rec
		fields = ['title', 'author', 'description']

	def __init__(self, *args, **kwargs):
		super(RecForm, self).__init__(*args, **kwargs)
		self.fields['title'].label="Book Title"
		self.fields['author'].label="Book Author"
		self.fields['description'].label="Book Description"
		# self.fields['comment'].label="Leave a Comment"

# class DiaryForm(forms.ModelForm):
# 	class Meta:
# 		model= models.Diary
# 		fields = ['budget', 'weight', 'note', 'ddate']
# 		widgets = {'ddate' : DateInput(), }

# 	def __init__(self, *args, **kwargs):
# 		super(DiaryForm, self).__init__(*args, **kwargs)
# 		self.fields['budget'].label="今日花費"
# 		self.fields['weight'].label="今日體重"
# 		self.fields['note'].label="日記內容"
# 		self.fields['ddate'].label="日期"

# class ProfileForm(forms.ModelForm):
# 	class Meta:
# 		model= models.Profile
# 		fields = ['height', 'male', 'website']

# 	def __init__(self, *args, **kwargs):
# 		super(ProfileForm, self).__init__(*args, **kwargs)
# 		self.fields['height'].label="身高(cm)"
# 		self.fields['male'].label="是男生嗎"
# 		self.fields['website'].label="個人網站"


class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=10)
	password = forms.CharField(label='Password', widget=forms.PasswordInput())
	captcha = CaptchaField()


# class ContactForm(forms.ModelForm):
# 	class Meta:
# 		model = models.Contact
# 		fields = ['user_name', 'user_city', 'user_school', 'user_email', 'user_message']
# 	def __init__(self, *args, **kwargs):
# 		super(ContactForm, self).__init__(*args, **kwargs)
# 		self.fields['user_name'].label='姓名'
# 		self.fields['user_city'].label='城市'
# 		self.fields['user_school'].label='在學'
# 		self.fields['user_email'].label='E-mail'
# 		self.fields['user_message'].label='意見'


# class PostForm(forms.ModelForm):
# 	captcha = CaptchaField()
# 	class Meta:
# 		model = models.Post
# 		fields = ['mood', 'nickname', 'message', 'del_pass']
# 	def __init__(self, *args, **kwargs):
# 		super(PostForm, self).__init__(*args, **kwargs)
# 		self.fields['mood'].label='心情'
# 		self.fields['nickname'].label='暱稱'
# 		self.fields['message'].label='留言'
# 		self.fields['del_pass'].label='密碼'
# 		self.fields['captcha'].label='不是機器人'