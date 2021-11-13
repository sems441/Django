from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, Link


class MembershipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('is_main'):
                count += 1
        if count != 1:
            raise ValidationError('Главный тег должен быть лишь один')
        return super().clean()


class MembershipInline(admin.TabularInline):
    model = Link
    extra = 1
    formset = MembershipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
