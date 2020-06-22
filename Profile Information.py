def get_user_profile(twitter_api, screen_names=None, user_ids=None):

 # Must have either screen_name or user_id (logical xor)
 assert (screen_names != None) != (user_ids != None), \
 "Must have screen_names or user_ids, but not both"

 items_to_info = {}
 items = screen_names or user_ids

 while len(items) > 0:
     items_str = ','.join([str(item) for item in items[:100]])
     items = items[100:]
     if screen_names:
         response = make_twitter_request(twitter_api.users.lookup,
                                         screen_name=items_str)
     else:  # user_ids
         response = make_twitter_request(twitter_api.users.lookup,
                                         user_id=items_str)

     for user_info in response:
         if screen_names:
             items_to_info[user_info['screen_name']] = user_info
     else:  # user_ids
         items_to_info[user_info['id']] = user_info
     return items_to_info
 # Sample usage
 twitter_api = oauth_login()
 print
 get_user_profile(twitter_api, screen_names=["SocialWebMining", "ptwobrussell"])