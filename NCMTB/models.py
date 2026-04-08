from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models import Avg




class TrailArticle(models.Model):
    """Represents a trail article on NC MTB"""



# Trail Meta Information
  
    Trail_Name = models.CharField(max_length=200, help_text="Trail Location Name e.g. Whitewater Center")

    Order_Priority = models.IntegerField(help_text="Priority of Trail that dictates where it is displayed on the home screen. 1 being first, etc.")

    Trail_Card_Logo = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Image that shows up on card on landing page tile. Typically a trail logo ex: Airline Logo.")
    
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title e.g. NCMTB.com/url-friendly-slug")

    trail_short_card_description = models.TextField(blank=True, null=True, help_text="Add individual lines about key features that will show up on the card as a bulleted list (for each separate line).")
    
    Trail_Map_Image = models.ImageField(upload_to='trail_photos', blank=True, help_text="The trail map is displayed on the trail page under Trails tab.")
    
    Trail_Website = models.URLField()

    Trail_Address = models.CharField(max_length=300, blank=True, null=True, help_text="Physical address of the trail to show on page.'")

    Latitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")
    
    Longitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")

    date_added = models.DateField(auto_now_add=True)

    date_updated = models.DateField(auto_now=True)
    
    Title_Trail_Image = models.ImageField(upload_to='trail_photos', help_text="This image appears on the Trail page as an opening image. This should be an action shot and eye-catcher e.g. Flight Deck at Airline.")

    Trail_Landing_Desc = models.CharField(max_length=500, help_text="Trail Description that appears on the Trail page as an opening statement.")


    Main_Features_Trails = models.TextField(blank=True,null=True, help_text="Enter the main trails and features on individual line e.g. Mountain Creek Hub, Loop, Jumps, Pump Track. Each line will be a bulleted list.")

    
    Overview_Trail_Video = models.TextField(blank=True, null=True, help_text="Overview video of the trails at the location. This is a YouTube Embed Code.")

    
    First_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    First_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    First_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    First_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    First_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    First_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    First_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    
   
    Second_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Second_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Second_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Second_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Second_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Second_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Second_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    
    
    Third_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Third_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Third_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Third_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Third_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Third_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Third_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Fourth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Fourth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Fourth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Fourth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Fourth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Fourth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Fourth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Fifth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Fifth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Fifth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Fifth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Fifth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Fifth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Fifth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Sixth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Sixth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Sixth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Sixth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Sixth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Sixth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Sixth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Seventh_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Seventh_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Seventh_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Seventh_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Seventh_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Seventh_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Seventh_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Eigth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Eigth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Eigth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Eigth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Eigth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Eigth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Eigth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Ninth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Ninth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Ninth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Ninth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Ninth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Ninth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Ninth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    Tenth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    Tenth_Trail_Section_Difficulty = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Difficulty")
    Tenth_Trail_Section_Distance = models.CharField(blank=True, max_length=20, null=True, help_text="Trail Distance")
    Tenth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Tenth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Tenth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
    Tenth_Trail_Short = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    class Meta:
        ordering = ['Order_Priority']
        verbose_name = "Trail Article"

    def __str__(self):
        return f"{self.Trail_Name}"

    def get_absolute_url(self):
        # This tells Django how to calculate the URL for an instance
        return reverse('trail_detail', kwargs={'slug': self.slug})
    
    @property
    def average_rating(self):
        # Calculates avg of the 'rating' field from related 'comments'
        avg = self.comments.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0

    @property
    def review_count(self):
        return self.comments.count()
    
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
                "short": self.First_Trail_Short,
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
            {
                "title": self.Fourth_Trail_Section_Title,
                "difficulty": self.Fourth_Trail_Section_Difficulty,
                "distance": self.Fourth_Trail_Section_Distance,
                "image": self.Fourth_Trail_Section_Image,
                "video": self.Fourth_Trail_Video,
                "desc": self.Fourth_Trail_Section_Desc,
            },
            {
                "title": self.Fifth_Trail_Section_Title,
                "difficulty": self.Fifth_Trail_Section_Difficulty,
                "distance": self.Fifth_Trail_Section_Distance,
                "image": self.Fifth_Trail_Section_Image,
                "video": self.Fifth_Trail_Video,
                "desc": self.Fifth_Trail_Section_Desc,
            },
            {
                "title": self.Sixth_Trail_Section_Title,
                "difficulty": self.Sixth_Trail_Section_Difficulty,
                "distance": self.Sixth_Trail_Section_Distance,
                "image": self.Sixth_Trail_Section_Image,
                "video": self.Sixth_Trail_Video,
                "desc": self.Sixth_Trail_Section_Desc,
            },
            {
                "title": self.Seventh_Trail_Section_Title,
                "difficulty": self.Seventh_Trail_Section_Difficulty,
                "distance": self.Seventh_Trail_Section_Distance,
                "image": self.Seventh_Trail_Section_Image,
                "video": self.Seventh_Trail_Video,
                "desc": self.Seventh_Trail_Section_Desc,
            },
            {
                "title": self.Eigth_Trail_Section_Title,
                "difficulty": self.Eigth_Trail_Section_Difficulty,
                "distance": self.Eigth_Trail_Section_Distance,
                "image": self.Eigth_Trail_Section_Image,
                "video": self.Eigth_Trail_Video,
                "desc": self.Eigth_Trail_Section_Desc,
            },
            {
                "title": self.Ninth_Trail_Section_Title,
                "difficulty": self.Ninth_Trail_Section_Difficulty,
                "distance": self.Ninth_Trail_Section_Distance,
                "image": self.Ninth_Trail_Section_Image,
                "video": self.Ninth_Trail_Video,
                "desc": self.Ninth_Trail_Section_Desc,
            },
            {
                "title": self.Tenth_Trail_Section_Title,
                "difficulty": self.Tenth_Trail_Section_Difficulty,
                "distance": self.Tenth_Trail_Section_Distance,
                "image": self.Tenth_Trail_Section_Image,
                "video": self.Tenth_Trail_Video,
                "desc": self.Tenth_Trail_Section_Desc,
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
    