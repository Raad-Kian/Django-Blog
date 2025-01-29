from django import  forms


from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'creator', 'genre', 'release_date', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Leave a comment...', 'rows': 4}),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) <1:
            raise forms.ValidationError("Comment must be at least 1 characters long.")
        if len(text) > 500:
            raise forms.ValidationError("Comment cannot exceed 500 characters.")
        return text