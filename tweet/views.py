from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

def tweet_list(request):
    # Get all tweets ordered by creation date (newest first)
    tweets = Tweet.objects.all().order_by('-created_at')
    
    # Pass the tweets to the template
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    
    return render(request, 'create_tweet.html', {'form': form})

@login_required
def update_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    
    # Check if the logged-in user is the owner of the tweet
    if tweet.user != request.user:
        return HttpResponse("You are not authorized to edit this tweet.", status=403)
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'update_tweet.html', {'form': form, 'tweet': tweet})

@login_required
def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    
    # Check if the logged-in user is the owner of the tweet
    if tweet.user != request.user:
        return HttpResponse("You are not authorized to delete this tweet.", status=403)
    
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'delete_tweet.html', {'tweet': tweet})