from django.db import models
from django.utils.text import slugify

#General Model Class
class Blogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs")
    like = models.IntegerField()

    user_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class Social_Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    tiktok = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)

    def __str__(self):
        return "social media"

class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.role_name}"
     
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user")
    is_active = models.BooleanField(default=True)
    created_date = models.DateField()
    
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.username}"
        
#Places Model Class

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"
    
class Places(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    short_description = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1500, null=True)
    address = models.CharField(max_length=250, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    map_url = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_home = models.BooleanField(default=True, null=True)
    is_open = models.BooleanField(default=True, null=True)
    cover_img = models.ImageField(upload_to="places")
    created_date = models.DateField()
    slug = models.SlugField(null=True, unique=True, db_index=True, blank=True)
    instagram = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    facebook = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=50, null=True)
    opening_day = models.CharField(max_length=150, null=True)
    opening_time = models.CharField(max_length=150, null=True)
    closing_time = models.CharField(max_length=150, null=True)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"

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

    Places = models.ForeignKey(Places, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f"{self.Places.title}"

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(max_length=750)
    point = models.IntegerField()

    image = models.ImageField(upload_to="comments")
    Places = models.ForeignKey(Places, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f"{self.Places.title, self.comment}"

class Menu_Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.category_name}"    

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to="menu")

    Menu_Category = models.ForeignKey(Menu_Category, on_delete=models.CASCADE, null=True)
    Places = models.ForeignKey(Places, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.Places.title, self.food_name}"

class Table_Layout(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_no = models.CharField(max_length=50)
    number_of_chairs = models.CharField(max_length=50)

    Places = models.ForeignKey(Places, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f"{self.Places.title, self.table_no}"

class Rezervation(models.Model):
    id = models.BigAutoField(primary_key=True)
    booker = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=50)
    finish_time = models.DateTimeField(max_length=50)
    status = models.BooleanField(default=False)

    Table_Layout = models.ForeignKey(Table_Layout, on_delete=models.CASCADE, null=True)
    Places = models.ManyToManyField(Places)

    def __str__(self):
        return f"{self.Places.title, self.booker}"

class Place_Img(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to="place_images")
    
    Places = models.ForeignKey(Places, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return f"{self.Places.title, self.image}"
