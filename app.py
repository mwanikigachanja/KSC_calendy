import streamlit as st
import pandas as pd
from datetime import datetime

# Global variable to store scheduled posts
scheduled_posts_data = []

# Function to display the calendar
def display_calendar():
    st.title('Social Media Calendar App')
    st.sidebar.header('Navigation')

    # Display a simple calendar for the current month
    today = datetime.today()
    current_month = today.strftime('%B %Y')
    st.header(current_month)

    # Create a dataframe with dummy data for demonstration
    data = {'Date': pd.date_range(start=today, periods=30),
            'Posts': [3, 2, 4, 1, 5, 3, 2, 4, 3, 2, 1, 3, 2, 4, 5, 3, 2, 1, 4, 3, 2, 5, 4, 2, 3, 2, 1, 4, 3, 2]}
    df = pd.DataFrame(data)
    
    # Display the calendar
    st.write(df)

# Function to create new posts
def create_post():
    st.title('Create New Post')
    # Add input fields for post content, date/time, etc.
    post_content = st.text_area('Post Content')

    # Date picker for selecting the post date
    post_date = st.date_input('Post Date', datetime.today())

    # Button to schedule the post
    if st.button('Schedule Post'):
        # Save the post to the global list
        scheduled_posts_data.append({
            'content': post_content,
            'date': post_date.strftime('%Y-%m-%d')
        })
        st.success('Post Scheduled Successfully!')

# Function to display the list of scheduled posts
def scheduled_posts():
    st.title('Scheduled Posts')
    if not scheduled_posts_data:
        st.write('No posts scheduled yet.')
    else:
        for idx, post in enumerate(scheduled_posts_data, start=1):
            st.write(f"**Post {idx}**")
            st.write(f"Date: {post['date']}")
            st.write(f"Content: {post['content']}")
            st.write("")

# Main function to run the app
def main():
    # Create a sidebar for navigation
    page = st.sidebar.radio("Go to", ('Calendar View', 'Create New Post', 'Scheduled Posts'))

    # Display the selected page
    if page == 'Calendar View':
        display_calendar()
    elif page == 'Create New Post':
        create_post()
    elif page == 'Scheduled Posts':
        scheduled_posts()

if __name__ == "__main__":
    main()
