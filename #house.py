# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

filtered = airbnb_search_details[
    (airbnb_search_details['property_type'] == 'House') &
    (airbnb_search_details['amenities'].apply(lambda x: 'TV' in x)) &
    (airbnb_search_details['neighbourhood'] == 'Westlake')
]
filtered = filtered['property_type'].count()

