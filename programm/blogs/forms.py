from .models import Articles, Visitors, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, IntegerField, ImageField
from django.core.exceptions import ValidationError



class ArticlesForm(ModelForm):
    class Meta:
        model  = Articles
        fields = ['titl', 'shorttitle', 'content', 'issued', 'image']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Название статьи'}),
            "shorttitle": TextInput(attrs = {'placeholder':'Главное о главном'}),
            "content": Textarea(attrs = {'placeholder':'Основная информация'}),
            "issued": DateTimeInput(attrs = {'placeholder':'Дата публикации'})
           
            
        }
        
class VisitorsForm(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarone','content', 'email', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
        }
    def clean_time(self):
    
        title = self.cleaned_data['title']
        surname = self.cleaned_data['surname']
        time = self.cleaned_data['time']
        
        
        if title == surname:
            raise ValidationError('error means')
        if time[0] =='4' or time[0] =='5' or time[0] =='6' or time[0] =='7' or time[0] =='8' or time[0] =='9' :
            raise ValidationError('error means')
        if time[9] =='6' or time[9] =='7'or time[9] =='8' or time[9] =='9':
            raise ValidationError('error means')
        if time[6] !='1':
            raise ValidationError('error means')     
        if time[10] !='0':
            raise ValidationError('error means')
        if time[7]=='9':
            raise ValidationError('error means')
        if time[4] =='0':
            raise ValidationError('error means')
        if time[2] !='/':
            raise ValidationError('error means')
        if time[5] !=' ':
            raise ValidationError('error means')
        if time[8] !=':':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='2' or time[0] =='3' and time[1]=='3' or time[0] =='3' and time[1]=='4' or time[0] =='3' and time[1]=='5':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='6' or time[0] =='3' and time[1]=='7' or  time[0] =='3' and time[1]=='8' or time[0] =='3' and time[1]=='9':
            raise ValidationError('error means')
        if time[3] =='2' or time[3] =='3' or time[3] =='4' or time[3] =='5' or time[3] =='6' or time[3] =='7' or time[3] =='8' or time[3] =='9':
            raise ValidationError('error means')
        
       
        return time
    
    
    
        
       
        
class VisitorsForm01(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvartwo','content', 'email',  'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
           
           
           
        }
    def clean_time(self):
        
    
        title = self.cleaned_data['title']
        surname = self.cleaned_data['surname']
        time = self.cleaned_data['time']
        
        
        if title == surname:
            raise ValidationError('error means')
        if time[0] =='4' or time[0] =='5' or time[0] =='6' or time[0] =='7' or time[0] =='8' or time[0] =='9' :
            raise ValidationError('error means')
        if time[9] =='6' or time[9] =='7'or time[9] =='8' or time[9] =='9':
            raise ValidationError('error means')
        if time[6] !='1':
            raise ValidationError('error means')     
        if time[10] !='0':
            raise ValidationError('error means')
        if time[7]=='9':
            raise ValidationError('error means')
        if time[4] =='0':
            raise ValidationError('error means')
        if time[2] !='/':
            raise ValidationError('error means')
        if time[5] !=' ':
            raise ValidationError('error means')
        if time[8] !=':':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='2' or time[0] =='3' and time[1]=='3' or time[0] =='3' and time[1]=='4' or time[0] =='3' and time[1]=='5':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='6' or time[0] =='3' and time[1]=='7' or  time[0] =='3' and time[1]=='8' or time[0] =='3' and time[1]=='9':
            raise ValidationError('error means')
        if time[3] =='2' or time[3] =='3' or time[3] =='4' or time[3] =='5' or time[3] =='6' or time[3] =='7' or time[3] =='8' or time[3] =='9':
            raise ValidationError('error means')
        
       
        return time
        
class VisitorsForm02(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarthree','content', 'email', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
             
       
        
            
        }
    def clean_time(self):
        
    
        title = self.cleaned_data['title']
        surname = self.cleaned_data['surname']
        time = self.cleaned_data['time']
        
        
        if title == surname:
            raise ValidationError('error means')
        if time[0] =='4' or time[0] =='5' or time[0] =='6' or time[0] =='7' or time[0] =='8' or time[0] =='9' :
            raise ValidationError('error means')
        if time[9] =='6' or time[9] =='7'or time[9] =='8' or time[9] =='9':
            raise ValidationError('error means')
        if time[6] !='1':
            raise ValidationError('error means')     
        if time[10] !='0':
            raise ValidationError('error means')
        if time[7]=='9':
            raise ValidationError('error means')
        if time[4] =='0':
            raise ValidationError('error means')
        if time[2] !='/':
            raise ValidationError('error means')
        if time[5] !=' ':
            raise ValidationError('error means')
        if time[8] !=':':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='2' or time[0] =='3' and time[1]=='3' or time[0] =='3' and time[1]=='4' or time[0] =='3' and time[1]=='5':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='6' or time[0] =='3' and time[1]=='7' or  time[0] =='3' and time[1]=='8' or time[0] =='3' and time[1]=='9':
            raise ValidationError('error means')
        if time[3] =='2' or time[3] =='3' or time[3] =='4' or time[3] =='5' or time[3] =='6' or time[3] =='7' or time[3] =='8' or time[3] =='9':
            raise ValidationError('error means')
        
       
        return time
        
class VisitorsForm03(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarfour','content', 'email', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
           
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
           
          
            
        }
    def clean_time(self):
        
    
        title = self.cleaned_data['title']
        surname = self.cleaned_data['surname']
        time = self.cleaned_data['time']
        
        
        if title == surname:
            raise ValidationError('error means')
        if time[0] =='4' or time[0] =='5' or time[0] =='6' or time[0] =='7' or time[0] =='8' or time[0] =='9' :
            raise ValidationError('error means')
        if time[9] =='6' or time[9] =='7'or time[9] =='8' or time[9] =='9':
            raise ValidationError('error means')
        if time[6] !='1':
            raise ValidationError('error means')     
        if time[10] !='0':
            raise ValidationError('error means')
        if time[7]=='9':
            raise ValidationError('error means')
        if time[4] =='0':
            raise ValidationError('error means')
        if time[2] !='/':
            raise ValidationError('error means')
        if time[5] !=' ':
            raise ValidationError('error means')
        if time[8] !=':':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='2' or time[0] =='3' and time[1]=='3' or time[0] =='3' and time[1]=='4' or time[0] =='3' and time[1]=='5':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='6' or time[0] =='3' and time[1]=='7' or  time[0] =='3' and time[1]=='8' or time[0] =='3' and time[1]=='9':
            raise ValidationError('error means')
        if time[3] =='2' or time[3] =='3' or time[3] =='4' or time[3] =='5' or time[3] =='6' or time[3] =='7' or time[3] =='8' or time[3] =='9':
            raise ValidationError('error means')
        return time
    
class VisitorsForm04(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarfive','content', 'email', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
        
            
        }
    def clean_time(self):
        
    
        title = self.cleaned_data['title']
        surname = self.cleaned_data['surname']
        time = self.cleaned_data['time']
        
        
        if title == surname:
            raise ValidationError('error means')
        if time[0] =='4' or time[0] =='5' or time[0] =='6' or time[0] =='7' or time[0] =='8' or time[0] =='9' :
            raise ValidationError('error means')
        if time[9] =='6' or time[9] =='7'or time[9] =='8' or time[9] =='9':
            raise ValidationError('error means')
        if time[6] !='1':
            raise ValidationError('error means')     
        if time[10] !='0':
            raise ValidationError('error means')
        if time[7]=='9':
            raise ValidationError('error means')
        if time[4] =='0':
            raise ValidationError('error means')
        if time[2] !='/':
            raise ValidationError('error means')
        if time[5] !=' ':
            raise ValidationError('error means')
        if time[8] !=':':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='2' or time[0] =='3' and time[1]=='3' or time[0] =='3' and time[1]=='4' or time[0] =='3' and time[1]=='5':
            raise ValidationError('error means')
        if time[0] =='3' and time[1]=='6' or time[0] =='3' and time[1]=='7' or  time[0] =='3' and time[1]=='8' or time[0] =='3' and time[1]=='9':
            raise ValidationError('error means')
        if time[3] =='2' or time[3] =='3' or time[3] =='4' or time[3] =='5' or time[3] =='6' or time[3] =='7' or time[3] =='8' or time[3] =='9':
            raise ValidationError('error means')
        
       
        return time
    
class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'surname', 'content', 'choice']
        widgets = {
            "name": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Ваш отзыв', 'class': 'form-control'})
            
        
            
        }