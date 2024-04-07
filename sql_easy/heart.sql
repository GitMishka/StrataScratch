select distinct p.* from facebook_reactions r 
inner join facebook_posts p on r.post_id = p.post_id 
and  r.reaction = 'heart' 