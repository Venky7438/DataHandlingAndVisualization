# Data Source Link : https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization/data
#Github Link :

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('netflix1.csv')

# Convert the 'date_added' column to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract the release year from the 'date_added' column
df['release_year_added'] = df['date_added'].dt.year

# Count the number of contents added each year
contents_added_by_year = df['release_year_added'].value_counts().sort_index()

# Count the occurrences of each director
director_counts = df['director'].value_counts()

# Filter out entries where director names are not given
filtered_director_counts = director_counts[director_counts.index != 'Not Given']

# Take the top N directors (e.g., top 5 for this example)
top_directors = filtered_director_counts.head(5)

# Split the 'listed_in' column into individual genres
genres = df['listed_in'].str.split(', ', expand = True).stack()

# Count the occurrences of each genre
genre_counts = genres.value_counts()

# Take the top N genres (e.g., top 5 for this example)
top_genres = genre_counts.head(5)

# Count the occurrences of each rating
rating_counts = df['rating'].value_counts()

# Set up a 2x2 grid layout for the dashboard
fig , axs = plt.subplots(3 , 2 , figsize = (12 , 15))

# Set the background color of the entire dashboard to black
fig.patch.set_facecolor('black')

# Plot 1: Line graph for contents added through the years
axs[0 , 0].plot(contents_added_by_year.index , contents_added_by_year.values ,
                marker = 'o' , linestyle = '-' , color = 'red')
axs[0 , 0].set_title('Number of Contents Added Through the Years' ,
                     color = 'white' , fontsize = 16)
axs[0 , 0].set_xlabel('Year' , color = 'white')
axs[0 , 0].set_ylabel('Number of Contents Added' , color = 'white')
axs[0 , 0].tick_params(axis = 'x' , colors = 'white')
axs[0 , 0].tick_params(axis = 'y' , colors = 'white')
axs[0 , 0].grid(True , color = 'white' , linestyle = '--' , alpha = 0.5)

# Plot 2: Bar graph for top directors
top_directors.plot(kind = 'bar' , ax = axs[0 , 1] , color = 'red')
axs[0 , 1].set_title('Top Directors' , color = 'white' , fontsize = 16)
axs[0 , 1].set_xlabel('Director' , color = 'white')
axs[0 , 1].set_ylabel('Number of Works' , color = 'white')
axs[0 , 1].tick_params(axis = 'x' , colors = 'white')
axs[0 , 1].tick_params(axis = 'y' , colors = 'white')
axs[0 , 1].grid(axis = 'y' , linestyle = '--' , alpha = 0.5)

# Plot 3: Bar graph for top genres
top_genres.plot(kind = 'bar' , ax = axs[1 , 0] , color = 'red')
axs[1 , 0].set_title('Top Genres' , color = 'white' , fontsize = 16)
axs[1 , 0].set_xlabel('Genre' , color = 'white')
axs[1 , 0].set_ylabel('Number of Works' , color = 'white')
axs[1 , 0].tick_params(axis = 'x' , colors = 'white' , rotation = 45)
axs[1 , 0].tick_params(axis = 'y' , colors = 'white')
axs[1 , 0].grid(axis = 'y' , linestyle = '--' , alpha = 0.5)

# Plot 4: Bar graph for top ratings
rating_counts.plot(kind = 'bar' , ax = axs[2 , 0] , color = 'red')
axs[2 , 0].set_title('Top Ratings' , color = 'white' , fontsize = 16)
axs[2 , 0].set_xlabel('Rating' , color = 'white')
axs[2 , 0].set_ylabel('Number of Works' , color = 'white')
axs[2 , 0].tick_params(axis = 'x' , colors = 'white')
axs[2 , 0].tick_params(axis = 'y' , colors = 'white')
axs[2 , 0].grid(axis = 'y' , linestyle = '--' , alpha = 0.5)

# Text space grid (additional space for text annotations)
text = "The following analysis is displayed on the dashboard.\n" \
       "   1. Up until 2016, Netflix's content additions were growing;\n" \
       "      after 2020, they started to fall.\n" \
       "   2. The top director on Netflix with the most works is \n" \
       "      Rajiv Chilaka.\n" \
       "   3. The most popular genre on Netflix with the most works \n" \
       "      is international movies.\n" \
       "   4. We can note that most contents on Netflix are rated TV-MA.\n" \
       "      TV-MA in the United States by the TV Parental Guidelines \n" \
       "      signifies content for mature audiences."
axs[1 , 1].text(0.5 , 0.5 , text , ha = 'center' , va = 'center' ,
                color = 'white' , fontsize = 14 , multialignment = 'left')
axs[1 , 1].axis('off')  # Turn off axis for this subplot
axs[1 , 1].axis('off')
# Adjust layout for better spacing
plt.tight_layout(rect=[0 , 0.03 , 1 , 0.95])

# Text space grid (additional space for text annotations)
text = "Student Id : 22074132\n" \
       "Student Name : Venkatesh Chattu"
axs[2 , 1].text(0.5 , 0.5 , text , ha = 'center' , va = 'center' ,
                color = 'white' , fontsize = 14 , multialignment = 'left')
axs[2 , 1].axis('off')  # Turn off axis for this subplot
# Adjust layout for better spacing
plt.tight_layout(rect = [0 , 0.03 , 1 , 0.95])

# Add a main title to the entire dashboard
fig.suptitle('Netflix Dashboard' , fontsize = 20 , color = 'white')
plt.savefig('22074132.png' , dpi=300)
# Show the dashboard
# plt.show()
