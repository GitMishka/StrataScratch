# Import your libraries
import pandas as pd

# Start writing code
customer_feedback.head()

customer_feedback = customer_feedback[(customer_feedback['comment_category'] != 'short_comments') & (customer_feedback['source_channel'] == 'social_media')]

customer_feedback = customer_feedback[['feedback_id', 'feedback_text', 'source_channel', 'comment_category']]
customer_feedback.drop_duplicates(inplace=True)
customer_feedback
#customer_feedback['comment_category'].unique()
#customer_feedback['source_channel'].unique()