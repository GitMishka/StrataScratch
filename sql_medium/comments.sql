select distinct * from customer_feedback where comment_category not in ('short_comments') and source_channel in ('social_media')