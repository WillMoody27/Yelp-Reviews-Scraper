from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
This is a simple python project that was designed to scrape reviews from a specific Yelp business page and generate a CSV report containing the extracted data. The script fetches the content from the page, parses the HTML to extract review information, and saves it into a structured CSV file, that can be furthur used with data visualization tools like Tableau, PowerBI, etc.
'''


# NOTE: Replace <BUSINESS NAME> with the name of the business you want to scrape reviews from.
url = "https://www.yelp.com/biz/<BUSINESS NAME>"

# Requests page to obtain the document content parsed as HTML

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


# Review Div
review_div = soup.find_all('li', class_='y-css-1jp2syp')

dic = {}
name_list, review_list, rating_list = [], [], []

# # Account for reviews from the user should match the len of names_span.
# # NOTE this does not count the replies from the business owner etc.
def findReviews(reviews_p, review_list):
    review_content = reviews_p.find_all('span', class_='raw__09f24__T4Ezm')
    for review in review_content:
        review_list.append(review.text)


def findNames(review, name_list): 
    usernames = review.find_all('a', class_='y-css-12ly5yx')[0]
    for name in usernames:
        name_list.append(name.text)

# NOTE: The aria-label attribute is used to define a string that labels the current rating.
def findRatingCount(review, rating_list):
    rating = review.find_all('div', class_='y-css-9tnml4')
    for rate in rating:
        # get the first char of the aria-label attribute to get the rating per user.
        rating_list.append(rate['aria-label'][0:1]) 

for review in review_div: 
    findNames(review, name_list)
    findReviews(review, review_list)
    findRatingCount(review, rating_list)

# Create a dictionary to store the data for each review
for i in range(len(name_list)):
    dic[i] = {'Name': name_list[i], 'Review': review_list[i], 'Rating': rating_list[i]}

# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(dic, orient='index')

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('yelp_reviews.csv', index=False)

print('File saved as yelp_reviews.csv')
