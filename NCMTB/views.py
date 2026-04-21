from django.shortcuts import render, redirect
from .models import TrailArticle, Comment
from django.views.generic import DetailView, ListView
from django.db.models import Avg
import requests, os
from django.conf import settings

# Home view (shows everything)
class TrailListView(ListView):
    model = TrailArticle
    template_name = 'NCMTB/home.html'
    context_object_name = 'trails'

    def get_queryset(self):
        sort_by = self.request.GET.get('sort', 'favorites')
        
        sort_mapping = {
            'favorites': 'Order_Priority',
            'location': 'Loc_Priority',
            'beginner': 'Beginner_Priority',
            'bikepark': 'Bike_Park_Priority',
            'roadtrip': 'Loc_Priority', # Reusing Loc_Priority or a specific field
        }
        
        target_field = sort_mapping.get(sort_by, 'Order_Priority')

        # Logic for "Road Trip": Sort descending (biggest values first)
        if sort_by == 'roadtrip':
            queryset = TrailArticle.objects.exclude(
                **{f"{target_field}__in": [0, None]}
            ).order_by(f"-{target_field}") # The '-' makes it descending
        else:
            # Standard ascending sort for others
            queryset = TrailArticle.objects.exclude(
                **{f"{target_field}__in": [0, None]}
            ).order_by(target_field)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', 'favorites')
        return context
    

    
def trail_list(request):
    # Get the sort parameter from the URL, default to 'favorites'
    sort_by = request.GET.get('sort', 'favorites')
    
    # Map the UI labels to your model fields
    sort_mapping = {
        'favorites': 'Order_Priority',
        'location': 'Loc_Priority',
        'beginner': 'Beginner_Priority',
        'bikepark': 'Bike_Park_Priority',
    }
    
    # Get the actual field name, defaulting to Order_Priority if key is invalid
    target_field = sort_mapping.get(sort_by, 'Order_Priority')
    
    # Filter: Exclude trails where the selected priority field is 0
    # Order: Ascending order based on that same field
    trails = TrailArticle.objects.exclude(**{f"{target_field}": 0}).order_by(target_field)
    
    return render(request, 'your_template.html', {
        'trails': trails,
        'current_sort': sort_by
    })

def category_view(request, trail_difficulty_type):
    # This filters trail difficulty based on the key
    trails = TrailArticle.objects.filter(Trail_Difficulty=trail_difficulty_type)
    
    # This maps the key to a nice human-readable title
    titles = {
        'Beginner': 'Beginner Trails',
        'Advanced': 'Advanced Trails',
        'Intermediate': 'Intermediate Trails',
        'Expert': 'Expert Trails',
    }
    
    context = {
        'trails': trails,
        'page_title': titles.get(trail_difficulty_type, 'Recipes')
    }
    return render(request, 'NCMTB/home.html', context)

# Filter Tags


def beginner_trails(request):
    trails = TrailArticle.objects.filter(Trail_Difficulty='Beginner')
    return render(request, "NCMTB/home.html", {
        'trails': trails, 
        'page_title': 'Beginner Trails'
    })

def intermediate_trails(request):
    trails = TrailArticle.objects.filter(Trail_Difficulty='Intermediate')
    return render(request, "NCMTB/home.html", {
        'trails': trails, 
        'page_title': 'Intermediate Trails'
    })

def advanced_trails(request):
    trails = TrailArticle.objects.filter(Trail_Difficulty='Advanced')
    return render(request, "NCMTB/home.html", {
        'trails': trails, 
        'page_title': 'Advanced Trails'
    })

def expert_trails(request):
    trails = TrailArticle.objects.filter(Trail_Difficulty='Expert')
    return render(request, "NCMTB/home.html", {
        'trails': trails, 
        'page_title': 'Expert Trails'
    })

# Primary Nav

def reccs(request):
  return render(request, 'NCMTB/reccs.html')
  
def browse(request):
    return render(request, 'NCMTB/browse.html')

def interest(request):
    return render(request, 'NCMTB/destinations.html')

def about(request):
    return render(request, 'NCMTB/about.html')


def trail_maps_view(request):
    trails = TrailArticle.objects.all().order_by('Order_Priority')
    return render(request, 'trailmaps.html', {'trails': trails})





class TrailDetailView(DetailView):
    model = TrailArticle
    template_name = 'trail_detail.html'
    context_object_name = 'trail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filter for Parent comments that HAVE a rating
        comments = self.object.comments.filter(parent__isnull=True).exclude(rating__isnull=True)
        
    
        trail = self.object
        total_count = comments.count()
        avg_rating = comments.aggregate(Avg('rating'))['rating__avg']
        
        context['average_rating'] = round(avg_rating, 1) if avg_rating else 0
        context['total_ratings'] = total_count

        breakdown = []
        for i in range(5, 0, -1):
            count = comments.filter(rating=i).count()
            # Ensure we don't divide by zero and provide a fallback
            percentage = int((count / total_count * 100)) if total_count > 0 else 0
            breakdown.append({
                'stars': i,
                'count': count,
                'percentage': percentage
            })
        
        context['rating_breakdown'] = breakdown
        
        
        # --- Weather API Logic ---
        weather_data = None
        # Use an environment variable for the key
        api_key = settings.OPENWEATHER_API_KEY
        
        if trail.Latitude and trail.Longitude:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={trail.Latitude}&lon={trail.Longitude}&appid={api_key}&units=imperial"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        'temp': round(data['main']['temp']),
                        'description': data['weather'][0]['description'].title(),
                        'icon': data['weather'][0]['icon'],
                        'humidity': data['main']['humidity']
                    }
            except requests.RequestException:
                pass # Fail silently or log error
        
        context['weather'] = weather_data
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context
    
    
    def post(self, request, *args, **kwargs):
        # We need the trail object to associate the comment with it
        trail = self.get_object()
        
        name = request.POST.get('name')
        body = request.POST.get('body')
        rating = request.POST.get('rating')
        parent_id = request.POST.get('parent_id')

        # Logic to create the comment
        if parent_id:
            # It's a reply
            parent_comment = Comment.objects.get(id=parent_id)
            Comment.objects.create(
                post=trail,
                name=name,
                body=body,
                parent=parent_comment,
                rating=None # Replies don't get ratings
            )
        else:
            # It's a top-level comment
            Comment.objects.create(
                post=trail,
                name=name,
                body=body,
                rating=int(rating) if rating else 5
            )

        # Redirect back to the trail page to clear the form and show the comment
        return redirect('trail_detail', slug=trail.slug)
    


