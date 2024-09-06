import streamlit as st
import pandas as pd 
import datetime

# Read the existing journal entries from the CSV file
csv_file = 'entries.csv'
existing_entries = pd.read_csv(csv_file)


# Create an empty DataFrame to store the journal entries
journal_df = pd.DataFrame(columns=['Date', 'Spiritual Practice', 'Meditation Time', 'Reading Minutes', 'Gratitude Entries', 'Mindful Moments', 'Physical Exercise', 'Journaling Thoughts'])
journal_df = pd.concat([journal_df, existing_entries], ignore_index=True)

# Create streamlit app to enter the above data
st.title('Journaling App')
st.write('Enter your journal entries below:')
date = datetime.date.today()

spiritual_practice_options = ['Bible Study', 'Prayer', 'Reflection', 'Devotion']
spiritual_practice = st.selectbox('Spiritual Practice', spiritual_practice_options)

meditation_time = st.number_input('Meditation Time (in minutes)', step=5, min_value=0, max_value=120)
reading_hours = st.number_input('Reading Minutes', step=1, min_value=0, max_value=24)
gratitude_entries = st.number_input('Gratitude Entries', step=1, min_value=0)
mindful_moments = st.number_input('Mindful Moments', step=1, min_value=0)
physical_exercise = st.number_input('Physical Exercise', step=30, min_value=0, max_value=1440)
journaling_thoughts = st.text_area('Journaling Thoughts', height=100)

# Add a submit button
if st.button('Submit'):
    new_entry = pd.DataFrame({'Date': [date],
                          'Spiritual Practice': [spiritual_practice],
                          'Meditation Time': [meditation_time],
                          'Reading Minutes': [reading_hours],
                          'Gratitude Entries': [gratitude_entries],
                          'Mindful Moments': [mindful_moments],
                          'Physical Exercise': [physical_exercise],
                          'Journaling Thoughts': [journaling_thoughts]})
    journal_df = pd.concat([existing_entries, new_entry], ignore_index=True)
    # Save the updated journal entries to the CSV file
    journal_df.to_csv(csv_file, index=False)


if __name__ == '__main__':
    st.write(journal_df)  # Display the journal entries DataFrame