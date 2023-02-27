from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    image= models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField()
    
class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

class Places(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    map_url = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    cover_img = models.CharField(max_length=150)
    created_date = models.DateField()
    slug = models.CharField(max_length=150)

class Places_Features(models.Model):
    id = models.BigAutoField(primary_key=True)
    wifi = models.BooleanField(default=False)
    smoking_allowed = models.BooleanField(default=False)
    bike_parking = models.BooleanField(default=False)
    street_parking = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    wheelchair_wc = models.BooleanField(default=False)
    wheelchair_ramp = models.BooleanField(default=False)
    wheelchair_accesible = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    quide_line = models.BooleanField(default=False)
    vegan_option = models.BooleanField(default=False)
    for_kids = models.BooleanField(default=False)
    outdoor_seating = models.BooleanField(default=False)
    offers_delivery = models.BooleanField(default=False)
    takes_rezervations = models.BooleanField(default=False)

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(max_length=750)
    point = models.IntegerField()

    user_id = models.CharField(max_length=100)

class Comment_Img(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=150)

    comments_id = models.CharField(max_length=100)

class Place_Img(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=150)

    place_id = models.CharField(max_length=100)

class Open_Times(models.Model):
    id = models.BigAutoField(primary_key=True)
    opening_day = models.CharField(max_length=150)
    opening_time = models.DateTimeField(max_length=150)
    closing_time = models.DateTimeField(max_length=150)

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=150)

    place_id = models.CharField(max_length=100)
    category_id = models.CharField(max_length=100)

class Menu_Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=150)

class Place_SocialMedia(models.Model):
    id = models.BigAutoField(primary_key=True)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    place_id = models.CharField(max_length=100)

class Table_Layout(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_no = models.CharField(max_length=50)
    number_of_chairs = models.CharField(max_length=50)

    place_id = models.CharField(max_length=100)


class Rezervation(models.Model):
    id = models.BigAutoField(primary_key=True)
    booker = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=50)
    day = models.DateTimeField(max_length=50)

    place_id = models.CharField(max_length=100)
    table_id = models.CharField(max_length=100)

class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    slug = models.CharField(max_length=100)
    image = models.CharField(max_length=150)
    like = models.IntegerField()

    user_id = models.CharField(max_length=100)

class Social_Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)