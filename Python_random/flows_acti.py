import matplotlib.pyplot as plt

# Data
areas_of_interest = [
    "Reading", "Watching kdrama", "Listening to music", "Organizing",
    "Socializing in Discord", "Eating at festi/landmark", "Coming to school event",
    "Sleeping at grass field/library", "Playing video games", "Playing guitar",
    "Creating videos", "Cooking", "Exercise", "Programming",
    "Rewatching favorite series", "Commuting", "Going outdoors", "Eating spicy food"
]

# Count of YES responses for each area
yes_counts = [2, 1, 4, 4, 2, 1, 0, 2, 1, 2, 2, 2, 1, 3, 2, 0, 2, 2]

# Bar chart
plt.figure(figsize=(10, 6))
plt.barh(areas_of_interest, yes_counts, color='skyblue')
plt.xlabel('Count of YES responses')
plt.ylabel('Areas of Interest')
plt.title('Count of YES Responses for Each Area of Interest')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(yes_counts, labels=areas_of_interest, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of YES Responses Across Areas of Interest')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
