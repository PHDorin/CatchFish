# -*- coding: utf-8 -*-
"""
Script to get a user's Facebook public profile information.
"""
import facebook
import urllib.parse
import urllib.request
import requests

APP_SECRET='4b768f8a218db2a17f34710b34d38c8f'
APP_ID='1760577657593271'

# 1. Register to be a Facebook developer here: https://developers.facebook.com/apps (App: CatchFish)
# 2. Get token from Facebook here: https://developers.facebook.com/tools/explorer/
# 3. Paste the token below
user_token="EAACEdEose0cBAOXYpSZB7ZAJNYKZCh84cQLZCFlJynpTZCZBCaWwS7EKoXBu85jMs79ZBTARmZBCotxoOlU4tpyOyPpyUfAkAc78EfgdGinQBEvgAPPcNji4MVg1KeRW9ElAVaZAcPrmI6xUxifb1B4ZBwuzokUiQm1Ih3fADAkV4eSJmag3r0vZAuhZC9t61xa4XWCSXfvMgOXFMgZDZD"

def get_current_user_profile():
    profile = graph.get_object("me")
    #print(profile)
    return profile
    
def get_matching_ids_by_user_name(user_name):
    people_by_name = fb.request('/search?q={}&type=user&fields=name'.format(user_name))
    #print(people_by_name)
    return people_by_name
    
def get_profile_info_for_user(user_id):
    profile = fb.request('/{}'.format(user_id))
    photos = fb.request('/{}/photos'.format(user_id))
    #print(profile)
    return (profile, photos)

def is_name_exact_match(given_first_name, given_last_name, first_name_match, last_name_match):
    return given_first_name == first_name_match and given_last_name == last_name_match

def find_profiles_matching_name(first_name, last_name):
    matching_users = get_matching_ids_by_user_name('{}+{}'.format(first_name, last_name))
    for user in matching_users['data']:        
        (info, photos) = get_profile_info_for_user(user['id'])
        profile_url = info['link']
        # TODO: Need to get public profile link from the app-scoped profile id
        if is_name_exact_match(first_name, last_name, info['first_name'], info['last_name']):
            print(info)

def find_profile_from_url(url):
    last_slash = url.rfind('/')
    user_id = url[last_slash:]
    profile = fb.request('/{}'.format(user_id))
    print(profile)
    
# Initialize FB graph API 
fb = graph = facebook.GraphAPI(user_token)
# Commented: With app-token we cannot get user profile info
#app_token = fb.get_app_access_token(APP_ID, APP_SECRET)

# Display current user's profile info
current_user_profile = get_current_user_profile()
#print(current_user_profile)

# Find profiles matching a given name
find_profiles_matching_name("Catch", "Fisher")

# Get profile info given an FB url
find_profile_from_url('https://www.facebook.com/100015262392106')