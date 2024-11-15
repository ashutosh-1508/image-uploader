from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myapp/home.html', {'img':img, 'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form}) 

# View function to display the image
def view_image(request, id):
    # Use get_object_or_404 to fetch the image or return 404
    image = get_object_or_404(Image, id=id)
    return render(request, 'myapp/view_image.html', {'image': image})

# View function to delete an image
from django.shortcuts import get_object_or_404, redirect
from .models import Image  # Replace with your model name if different

def delete_image(request, id):
    # Fetch the image instance
    image = get_object_or_404(Image, id=id)

    # Delete the image
    try:
        image.delete()
        # Redirect back to the home page or gallery
        return redirect('home')  # Replace 'home' with the name of your gallery view
    except Exception as e:
        # Log the error and provide feedback
        print(f"Error deleting image: {e}")
        return redirect('myapp/home.html')  # Provide user-friendly fallback
