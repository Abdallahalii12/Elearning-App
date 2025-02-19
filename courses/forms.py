from django import forms 
from .models import Course,Image,Text,Video,File,Module


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields =['__all__'] # gets all fields
        fields =['subject','title','overview','status']

class ModuleForm(forms.ModelForm):
    class Meta:
        model =Module
        fields=['course','title','description']


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields =['content']




class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields =['video']





class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['image']



class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields =['file']
















    


