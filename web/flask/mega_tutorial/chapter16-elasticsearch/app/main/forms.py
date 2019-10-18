from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_babel import lazy_gettext as  _l
from flask import request


import sys
sys.path.append('../..')
from app.models import User


class SearchForm(FlaskForm):
    q = StringField('搜索', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args

        if 'csrf_enabled' not in kwargs:
            """
            表单默认添加了CSRF保护，包含一个CSRF标记，该标记通过模板中的form.hidden_​​tag()构造添加到表单中。
            为了使搜索表单运作，CSRF需要被禁用，所以我将csrf_enabled设置为False
            """
            kwargs['csrf_enabled'] = False

        super(SearchForm, self).__init__(*args, **kwargs)


class EditProfileForm(FlaskForm):
    """
    个人资料编辑
    """
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class PostForm(FlaskForm):
    """
    发布post
    """
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('提交')
