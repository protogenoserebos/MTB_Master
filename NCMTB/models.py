from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models import Avg
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill




class TrailArticle(models.Model):
    """Represents a trail article on NC MTB"""



# Trail Meta Information
  
    Trail_Name = models.CharField(max_length=200, help_text="Trail Location Name e.g. Whitewater Center")

    Order_Priority = models.IntegerField(null=True, blank=True, help_text="Priority of Trail that dictates where it is displayed on the home screen. 1 being first, etc.")

    Loc_Priority = models.IntegerField(null=True, blank=True, help_text="Priority of Trail that dictates where it is displayed on the home screen. 1 being first, etc.")

    Beginner_Priority = models.IntegerField(null=True, blank=True, help_text="Priority of Trail that dictates whether it's beginner friendly.")

    Family_Priority = models.IntegerField(null=True, blank=True, help_text="Priority of Trail that dictates whether it's beginner friendly.")

    Bike_Park_Priority = models.IntegerField(null=True, blank=True, help_text="Priority of Trail that dictates whether its a bike park.")

    Trail_Card_Logo = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Image that shows up on card on landing page tile. Typically a trail logo ex: Airline Logo.")
    
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title e.g. NCMTB.com/url-friendly-slug")

    trail_short_card_description = models.TextField(blank=True, null=True, help_text="Add individual lines about key features that will show up on the card as a bulleted list (for each separate line).")

    Trail_Landing_Desc = models.CharField(max_length=500, help_text="Trail Description that appears on the Trail page as an opening statement.")

    Main_Features_Trails = models.TextField(blank=True,null=True, help_text="Enter the main trails and features on individual line e.g. Mountain Creek Hub, Loop, Jumps, Pump Track. Each line will be a bulleted list.")
    
    Trail_Map_Image = models.ImageField(upload_to='trail_photos', blank=True, null=True, help_text="The trail map is displayed on the trail page under Trails tab.")

    Trail_Map_Thumbnail = ImageSpecField(source='Trail_Map_Image', processors=[ResizeToFill(400, 250)], format='JPEG', options={'quality': 70})
    
    Trail_Website = models.URLField()

    Trail_Address = models.CharField(max_length=300, blank=True, null=True, help_text="Physical address of the trail to show on page.'")

    Latitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")
    
    Longitude = models.DecimalField(max_digits=50, decimal_places=20, null=True, blank=True, help_text="For weather API and Google Maps API... goto Google Maps, drop pin at location, right-click and copy coords..")

    date_added = models.DateField(auto_now_add=True)


    Feature_Spotlight_1 = models.ImageField(upload_to='trail_photos', blank=True, null=True, help_text="This image is a feature spotlight.")

    Feature_Spotlight_1_Desc = models.CharField(max_length=500, blank=True, null=True, help_text="Trail Description that appears on the Trail page as an opening statement.")

    Feature_Spotlight_2 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is a feature spotlight.")

    Feature_Spotlight_2_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trail Description that appears on the Trail page as an opening statement.")

    Feature_Spotlight_3 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is a feature spotlight.")

    Feature_Spotlight_3_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trail Description that appears on the Trail page as an opening statement.")

    Feature_Spotlight_4 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is a feature spotlight.")

    Feature_Spotlight_4_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trail Description that appears on the Trail page as an opening statement.")
    
    
    Approach_img_1 = models.ImageField(upload_to='trail_photos', blank=True, null=True, help_text="This image is an approach to the trail head.")

    Approach_img_1_Desc = models.CharField(max_length=500, blank=True, null=True, help_text="Trailhead approach description.")
                                           
    Approach_img_2 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is an approach to the trail head.")

    Approach_img_2_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trailhead approach description.")

    Approach_img_3 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is an approach to the trail head.")

    Approach_img_3_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trailhead approach description.")

    Approach_img_4 = models.ImageField(upload_to='trail_photos', blank=True, null=True,  help_text="This image is an approach to the trail head.")

    Approach_img_4_Desc = models.CharField(max_length=500, blank=True, null=True,  help_text="Trailhead approach description.")
    
   

    
    First_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    First_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    First_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    First_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
  
    
   
    Second_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Second_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Second_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Second_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")

    
    
    Third_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
   
    Third_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Third_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Third_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Fourth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Fourth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Fourth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Fourth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Fifth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
   
    Fifth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Fifth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Fifth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
  

    Sixth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
   
    Sixth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Sixth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Sixth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Seventh_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
   
    Seventh_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Seventh_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Seventh_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Eigth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Eigth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Eigth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Eigth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Ninth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Ninth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Ninth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Ninth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
   

    Tenth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")

    Tenth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Tenth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Tenth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
  

    Eleventh_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Eleventh_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Eleventh_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Eleventh_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")


    Twelfth_Trail_Section_Title = models.CharField(blank=True, max_length=100, null=True, help_text="Trail Name")
    
    Twelfth_Trail_Section_Desc = models.TextField(blank=True, null=True, help_text="Trail Description")
    Twelfth_Trail_Section_Image = models.ImageField(upload_to='trail_photos', null=True, blank=True, help_text="Trail Image")
    Twelfth_Trail_Video = models.TextField(blank=True, null=True, help_text="YouTube Embed Code")
  

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
    
    def get_feature_spotlights(self):
        """Returns a list of dictionaries for each non-empty spotlight."""
        spotlights = []
        for i in range(1, 5):
            img = getattr(self, f'Feature_Spotlight_{i}')
            desc = getattr(self, f'Feature_Spotlight_{i}_Desc')
            if img:
                spotlights.append({'image': img, 'desc': desc})
        return spotlights
    
    def get_approach_img(self):
        """Returns a list of dictionaries for each non-empty spotlight."""
        approach = []
        for i in range(1, 5):
            img = getattr(self, f'Approach_img_{i}')
            desc = getattr(self, f'Approach_img_{i}_Desc')
            if img:
                approach.append({'image': img, 'desc': desc})
        return approach


    def get_content_blocks(self):
        """Groups trail sections into dictionaries for clean template rendering."""
        blocks = [
            
            {
                "title": self.First_Trail_Section_Title,

                "image": self.First_Trail_Section_Image,
                "video": self.First_Trail_Video,
             
                "desc": self.First_Trail_Section_Desc,
            },
            {
                "title": self.Second_Trail_Section_Title,

                "image": self.Second_Trail_Section_Image,
                "video": self.Second_Trail_Video,
                "desc": self.Second_Trail_Section_Desc,
            },
            {
                "title": self.Third_Trail_Section_Title,
      
                "image": self.Third_Trail_Section_Image,
                "video": self.Third_Trail_Video,
                "desc": self.Third_Trail_Section_Desc,
            },
            {
                "title": self.Fourth_Trail_Section_Title,

                "image": self.Fourth_Trail_Section_Image,
                "video": self.Fourth_Trail_Video,
                "desc": self.Fourth_Trail_Section_Desc,
            },
            {
                "title": self.Fifth_Trail_Section_Title,
      
                "image": self.Fifth_Trail_Section_Image,
                "video": self.Fifth_Trail_Video,
                "desc": self.Fifth_Trail_Section_Desc,
            },
            {
                "title": self.Sixth_Trail_Section_Title,
      
                "image": self.Sixth_Trail_Section_Image,
                "video": self.Sixth_Trail_Video,
                "desc": self.Sixth_Trail_Section_Desc,
            },
            {
                "title": self.Seventh_Trail_Section_Title,

                "image": self.Seventh_Trail_Section_Image,
                "video": self.Seventh_Trail_Video,
                "desc": self.Seventh_Trail_Section_Desc,
            },
            {
                "title": self.Eigth_Trail_Section_Title,

                "image": self.Eigth_Trail_Section_Image,
                "video": self.Eigth_Trail_Video,
                "desc": self.Eigth_Trail_Section_Desc,
            },
            {
                "title": self.Ninth_Trail_Section_Title,
 
                "image": self.Ninth_Trail_Section_Image,
                "video": self.Ninth_Trail_Video,
                "desc": self.Ninth_Trail_Section_Desc,
            },
            {
                "title": self.Tenth_Trail_Section_Title,

                "image": self.Tenth_Trail_Section_Image,
                "video": self.Tenth_Trail_Video,
                "desc": self.Tenth_Trail_Section_Desc,
            },
{
                "title": self.Eleventh_Trail_Section_Title,

                "image": self.Eleventh_Trail_Section_Image,
                "video": self.Eleventh_Trail_Video,
                "desc": self.Eleventh_Trail_Section_Desc,
            },
            {
                "title": self.Twelfth_Trail_Section_Title,
   
                "image": self.Twelfth_Trail_Section_Image,
                "video": self.Twelfth_Trail_Video,
                "desc": self.Twelfth_Trail_Section_Desc,
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
    