from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['gender', 'birth_date', 'birth_hour', 'birth_location_city', 'birth_location_province', 'birth_location_country', 'degree', 'happiness_level', 'ext1', 'ext2', 'ext3', 'ext4', 'ext5', 'ext6', 'ext7', 'ext8', 'ext9', 'ext10', 'est1', 'est2', 'est3', 'est4', 'est5', 'est6', 'est7', 'est8', 'est9', 'est10', 'agr1', 'agr2', 'agr3', 'agr4', 'agr5', 'agr6', 'agr7', 'agr8', 'agr9', 'agr10', 'csn1', 'csn2', 'csn3', 'csn4', 'csn5', 'csn6', 'csn7', 'csn8', 'csn9', 'csn10', 'opn1', 'opn2', 'opn3', 'opn4', 'opn5', 'opn6', 'opn7', 'opn8', 'opn9', 'opn10']

    def save(self, commit=True):
        person = super().save(commit=False)
        person.gender = self.cleaned_data['gender']
        person.birth_date = self.cleaned_data['birth_date']
        person.birth_hour = self.cleaned_data['birth_hour']
        person.birth_location_city = self.cleaned_data['birth_location_city']
        person.birth_location_province = self.cleaned_data['birth_location_province']
        person.birth_location_country = self.cleaned_data['birth_location_country']
        person.degree = self.cleaned_data['degree']
        person.happiness_level = self.cleaned_data['happiness_level']
        person.ext1 = self.cleaned_data['ext1']
        person.ext2 = self.cleaned_data['ext2']
        person.ext3 = self.cleaned_data['ext3']
        person.ext4 = self.cleaned_data['ext4']
        person.ext5 = self.cleaned_data['ext5']
        person.ext6 = self.cleaned_data['ext6']
        person.ext7 = self.cleaned_data['ext7']
        person.ext8 = self.cleaned_data['ext8']
        person.ext9 = self.cleaned_data['ext9']
        person.ext10 = self.cleaned_data['ext10']
        person.est1 = self.cleaned_data['est1']
        person.est2 = self.cleaned_data['est2']
        person.est3 = self.cleaned_data['est3']
        person.est4 = self.cleaned_data['est4']
        person.est5 = self.cleaned_data['est5']
        person.est6 = self.cleaned_data['est6']
        person.est7 = self.cleaned_data['est7']
        person.est8 = self.cleaned_data['est8']
        person.est9 = self.cleaned_data['est9']
        person.est10 = self.cleaned_data['est10']
        person.agr1 = self.cleaned_data['agr1']
        person.agr2 = self.cleaned_data['agr2']
        person.agr3 = self.cleaned_data['agr3']
        person.agr4 = self.cleaned_data['agr4']
        person.agr5 = self.cleaned_data['agr5']
        person.agr6 = self.cleaned_data['agr6']
        person.agr7 = self.cleaned_data['agr7']
        person.agr8 = self.cleaned_data['agr8']
        person.agr9 = self.cleaned_data['agr9']
        person.agr10 = self.cleaned_data['agr10']
        person.csn1 = self.cleaned_data['csn1']
        person.csn2 = self.cleaned_data['csn2']
        person.csn3 = self.cleaned_data['csn3']
        person.csn4 = self.cleaned_data['csn4']
        person.csn5 = self.cleaned_data['csn5']
        person.csn6 = self.cleaned_data['csn6']
        person.csn7 = self.cleaned_data['csn7']
        person.csn8 = self.cleaned_data['csn8']
        person.csn9 = self.cleaned_data['csn9']
        person.csn10 = self.cleaned_data['csn10']
        person.opn1 = self.cleaned_data['opn1']
        person.opn2 = self.cleaned_data['opn2']
        person.opn3 = self.cleaned_data['opn3']
        person.opn4 = self.cleaned_data['opn4']
        person.opn5 = self.cleaned_data['opn5']
        person.opn6 = self.cleaned_data['opn6']
        person.opn7 = self.cleaned_data['opn7']
        person.opn8 = self.cleaned_data['opn8']
        person.opn9 = self.cleaned_data['opn9']
        person.opn10 = self.cleaned_data['opn10']
        
        if commit:
            person.save()
            
        return person
