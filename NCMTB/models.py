from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
   



class TrailArticle(models.Model):
    """Represents a trail article on NC MTB"""



# Trail Meta Information
  
    Trail_Name = models.CharField(max_length=200, help_text="Trail Location Name")
    
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title e.g. NCMTB.com/url-friendly-slug")

    trail_short_card_description = models.TextField(blank=True, null=True, help_text="Short trail description for cards")
    
    Trail_Landing_Desc = models.CharField(max_length=500, help_text="Landing Page Description")

    Trail_Difficulty_Range = models.CharField(max_length=50, help_text="Enter difficulty range") 
    
    Trail_Distance = models.CharField(max_length=100, help_text="Total Trail Mileage")

    e_bikes_allowed = models.CharField(blank=True, null=True, max_length=50, help_text="Yes or No") 
    
    Trail_Tags = models.CharField(max_length=200, blank=True, null=True, help_text="Justin to add MANY TO MANY Model relationship for tag selection.")

    Maintained_By = models.CharField(max_length=200, blank=True, null=True, help_text="Justin to add Tarheel and other auto logo image SVGs.")

# Location and Map API Coordinates

    Trail_Address = models.CharField(max_length=300, blank=True, null=True, help_text="Physical address to show on page.'")

    Latitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")
    
    Longitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")
    
    Main_Features_Trails = models.TextField(blank=True,null=True, help_text="Enter the main trails and features at location e.g. Mountain Creek Hub, Loop, Jumps, Pump Track.")
    

   
# DB Metadata

    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

# Media
    
    Title_Trail_Image = models.ImageField(upload_to='trail_photos', blank=True)

    Trail_Map_Image = models.ImageField(upload_to='trail_photos', blank=True)

    Trail_Introduction_Description = models.TextField(blank=True, help_text="Introductory description of the trail.")
    
    Overview_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    First_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="1st Trail/Section Leading Image")
    First_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    First_Trail_Section_Title = models.CharField(max_length=100, null=True, help_text="Sub-trail name")
    First_Trail_Section_Difficulty = models.CharField(max_length=20, null=True, help_text="Sub-trail difficulty")
    First_Trail_Section_Distance = models.CharField(max_length=20, null=True, help_text="Sub-trail distance")
    First_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="1st Trail/Section Description")
    
    Second_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="2nd Trail/Section Leading Image")
    Second_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Second_Trail_Section_Title = models.CharField(max_length=100, null=True, help_text="Sub-trail name")
    Second_Trail_Section_Difficulty = models.CharField(max_length=20, null=True, help_text="Sub-trail difficulty")
    Second_Trail_Section_Distance = models.CharField(max_length=20, null=True, help_text="Sub-trail distance")
    Second_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="2nd Trail/Section Description")
    
    Third_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="3rd Trail/Section Leading Image")
    Third_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Third_Trail_Section_Title = models.CharField(max_length=100, null=True, help_text="Sub-trail name")
    Third_Trail_Section_Difficulty = models.CharField(max_length=20, null=True, help_text="Sub-trail difficulty")
    Third_Trail_Section_Distance = models.CharField(max_length=20, null=True, help_text="Sub-trail distance")
    Third_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="3rd Trail/Section Description")

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Trail Article"

    def __str__(self):
        return f"{self.Trail_Name}"

    def get_absolute_url(self):
        # This tells Django how to calculate the URL for an instance
        return reverse('trail_detail', kwargs={'slug': self.slug})
    
    def get_trailtype_color(self):
        """Returns a specific brand color based on the meal type."""
        colors = {
            'Advanced': '#BC6C25',    # Terracotta/Peach
            'Beginner': '#D4A373', # Gold/Mustard
            'Dessert': '#2A9D8F',   # Teal/Aqua
            'Intermediate': '#264653',     # Deep Dark Blue
        }
        return colors.get(self.Trail_Difficulty, '#FF7F50') # Default to orange if not found

    def get_content_blocks(self):
        """Groups trail sections into dictionaries for clean template rendering."""
        blocks = [
            
            {
                "title": self.First_Trail_Section_Title,
                "difficulty": self.First_Trail_Section_Difficulty,
                "distance": self.First_Trail_Section_Distance,
                "image": self.First_Trail_Section_Image,
                "video": self.First_Trail_Video,
                "desc": self.First_Trail_Section_Desc,
            },
            {
                "title": self.Second_Trail_Section_Title,
                "difficulty": self.Second_Trail_Section_Difficulty,
                "distance": self.Second_Trail_Section_Distance,
                "image": self.Second_Trail_Section_Image,
                "video": self.Second_Trail_Video,
                "desc": self.Second_Trail_Section_Desc,
            },
            {
                "title": self.Third_Trail_Section_Title,
                "difficulty": self.Third_Trail_Section_Difficulty,
                "distance": self.Third_Trail_Section_Distance,
                "image": self.Third_Trail_Section_Image,
                "video": self.Third_Trail_Video,
                "desc": self.Third_Trail_Section_Desc,
            },
        ]

        # Only return blocks that have at least a title or a description
        return [b for b in blocks if b['title'] or b['desc']]
    
# Article Comments

class Comment(models.Model):
    post = models.ForeignKey(TrailArticle, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True
    )
    
    def __str__(self):
        return f"{self.post.Trail_Name} - {self.parent} - {self.name} - {self.body}"
    