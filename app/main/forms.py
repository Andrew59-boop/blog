from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField
from wtforms.validators import Required,Email,EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('UPDATE')

class BlogForm(FlaskForm):
    title = StringField('Blog Title',validators = [Required()])
    blog = TextAreaField('Write your Blog.',validators = [Required()])
    submit = SubmitField('POST')

class CommentForm(FlaskForm):
    description = TextAreaField('Add a comment.',validators = [Required()])
    submit = SubmitField('COMMENT')