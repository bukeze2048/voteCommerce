from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Contestant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='contestant_images')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100)
    votes = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class BallotBox(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    contestants = models.ManyToManyField(Contestant, through='Vote')

    def __str__(self):
        return self.session_id

class Vote(models.Model):
    ballot_box = models.ForeignKey(BallotBox, on_delete=models.CASCADE)
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.contestant} - {self.vote_count} votes"