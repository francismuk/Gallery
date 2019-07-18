from django.db import models
import datetime as dt


# Create your models here.
class Location(models.Model):
    image_location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.image_location
    
class Category(models.Model):
    photo_category = models.CharField(max_length=50)
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    def update_category(self):
        self.update_category()
    
    @classmethod
    def get_all_categories(cls):
        all_categories = Category.objects.all()
        return all_categories
    
    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update_image()
        
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
        
    @classmethod
    def get_image_by_id(id):
        my_image = Image.objects.get(id=id)
    
    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(search_category=search_category)
        return images_category

    @classmethod
    def filter_by_location(cls, filter_location):
        images_location = Image.objects.filter(location__id=filter_location)
        return images_location   
        
    def __str__(self):
        return self.name