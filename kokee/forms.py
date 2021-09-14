from django import  forms
from kokee.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'contents']

        labels = {
            'subject': '제목',
            'contents': '내용',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['contents']

        labels = {
            'contents': '답변내용',
        }
"""       widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'row': 10}),
        }
"""