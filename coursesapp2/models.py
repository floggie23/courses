from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Course's name should be at least 5 characters"
        if len(postData['desc']) < 5:
            errors["desc"] = "Description should be at least 5 characters"
        return errors
class Description(models.Model):
    desc = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=45)
    desc = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="course"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.TextField()
    commentss = models.ForeignKey(Course, related_name = 'comments', on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True) 
    def __repr__(self):
           return f"<Movie object: {self.comment} ({self.id})>"

