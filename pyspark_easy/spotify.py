# Import your libraries
from pyspark.sql import functions as F



listening_habits = listening_habits.fillna(0, subset=['listen_duration'])

grouped_data = listening_habits.groupby('user_id').agg(
    F.sum('listen_duration').alias('total_listen_duration'),
    F.countDistinct('song_id').alias('unique_song_count')
)
grouped_data = grouped_data.withColumn('total_listen_duration', (F.col('total_listen_duration') / 60).cast('integer'))
grouped_data = grouped_data.orderBy('user_id')

grouped_data_pd = grouped_data.toPandas()