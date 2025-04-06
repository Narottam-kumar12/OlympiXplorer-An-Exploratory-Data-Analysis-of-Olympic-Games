# import streamlit as st
# import pandas as pd
# import preprocessor, helper
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.figure_factory as ff


# df = pd.read_csv('athlete_events.csv')
# region_df = pd.read_csv('noc_regions.csv')

# df = preprocessor.preprocess(df,region_df)  # Load data
# st.sidebar.title("🏅 Olympics Analysis")
# image_url = "https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg"
# st.sidebar.markdown("Analyze Olympics data with various visualizations and insights.")

# # Display image in sidebar
# st.sidebar.image(image_url, caption="Olympics Logo")
# user_menu = st.sidebar.radio(
#     'Select an Option',
#     ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
# )
#   # Display the original DataFrame

# if user_menu == 'Medal Tally':
#     st.sidebar.header("Medal Tally")
#     years,country = helper.country_year_list(df)

#     selected_year = st.sidebar.selectbox("Select Year",years)
#     selected_country = st.sidebar.selectbox("Select Country",country)

#     medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
#     # Call the function correctly
#     if selected_year  == "Overall" and selected_country == "Overall":
#         st.title("🏆 Overall Medal Tally")
#     if selected_year != "Overall" and selected_country == "Overall":
#         st.title("Medal Tally in " + str(selected_year) + " "+" Olympics ")
#     if selected_year == "Overall" and selected_country != "Overall":
#         st.title(selected_country + " Overall performance in Olympics")
#     if selected_year != "Overall" and selected_country != "Overall" :
#         st.title(selected_country + " Performance in " + str(selected_year) +" Olympics ")
#     st.table(medal_tally)  # Display the result properly

# if user_menu == 'Overall Analysis':
#     editions = df['Year'].unique().shape[0]-1
#     cities = df['City'].unique().shape[0]
#     sports = df['Sport'].unique().shape[0]
#     events = df['Event'].unique().shape[0]
#     athletes = df['Name'].unique().shape[0]
#     nations = df['region'].unique().shape[0]

#     st.title("📊 Top Statistics")

#     col1,col2,col3 = st.columns(3)
#     with col1:
#         st.header("Editions")
#         st.title(editions)
#     with col2:
#         st.header("Hosts")
#         st.title(cities)
#     with col3:
#         st.header("Sports")
#         st.title(sports)

#     col1,col2,col3 = st.columns(3)
#     with col1:
#         st.header("Events")
#         st.title(events)
#     with col2:
#         st.header("Nations")
#         st.title(nations)
#     with col3:
#         st.header("Athletes")
#         st.title(athletes)

#     nations_over_time = helper.data_over_time(df, 'region')

#     fig = px.line(nations_over_time, x="Edition", y="region")
#     st.title("Participating Nations Over the Years")
#     st.plotly_chart(fig)

#     events_over_time = helper.data_over_time(df, 'Event')
#     fig = px.line(events_over_time, x="Edition", y="Event")
#     st.title("Events Over the Years")
#     st.plotly_chart(fig)

#     athlete_over_time = helper.data_over_time(df, 'Name')
#     fig = px.line(athlete_over_time, x="Edition", y="Name")
#     st.title("Athletes Over the Years")
#     st.plotly_chart(fig)

#     import streamlit as st
#     import matplotlib.pyplot as plt
#     import seaborn as sns
#     import pandas as pd

#     st.title("No. of Events over time (Every Sport)")

#     # Creating the figure and axis properly
#     fig, ax = plt.subplots(figsize=(20, 20))

#     # Removing duplicates based on Year, Sport, and Event
#     x = df.drop_duplicates(['Year', 'Sport', 'Event'])

#     # Creating the pivot table
#     pivot_table = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)

#     # Creating the heatmap
#     sns.heatmap(pivot_table, annot=True, ax=ax, cmap='YlGnBu', fmt='g')

#     # Displaying the plot in streamlit
#     st.pyplot(fig)

#     st.title("🏅 Most Successful Athletes")
#     sport_list = df['Sport'].unique().tolist()
#     sport_list.sort()
#     sport_list.insert(0,'Overall')

#     selected_sport = st.selectbox('Select a sport',sport_list)
#     x = helper.most_successful(df,selected_sport)
#     st.table(x)

# if user_menu == 'Country-wise Analysis':
#     st.sidebar.title('Country-wise Analysis')

#     country_list = df['region'].dropna().unique().tolist()
#     country_list.sort()

#     selected_country = st.sidebar.selectbox('Select a Country',country_list)

#     country_df =  helper.yearwise_medal_tally(df,selected_country)
#     fig = px.line(country_df,x = "Year",y = "Medal")
#     st.title(selected_country + " Medal Tally over the year ")
#     st.plotly_chart(fig)

#     st.title(selected_country + " excels in the fallowing sports ")
#     heatmap_data = helper.country_event_heatmap(df, selected_country)

#     # Increase figure size
#     fig, ax = plt.subplots(figsize=(20, 20))


#     # Plot heatmap
#     ax = sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='g')

#     # Show the plot
#     st.pyplot(fig)

#     st.title("Top 10 athletes of " + selected_country)

#     top10_df = helper.most_succesful_countrywise(df,selected_country)
#     st.table(top10_df)

# if user_menu == 'Athlete-wise Analysis':
#     # Drop duplicates based on 'Name' and 'region' to get unique athletes
#     st.title('👩‍🎓 Athlete-wise Analysis')
#     athlete_df = df.drop_duplicates(subset=['Name', 'region'])

#     # Prepare age data for distribution plots
#     x1 = athlete_df['Age'].dropna()
#     x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
#     x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
#     x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

#     # Create the distribution plot
#     fig = ff.create_distplot(
#         [x1.tolist(), x2.tolist(), x3.tolist(), x4.tolist()],
#         ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
#         show_hist=False,
#         show_rug=False
#     )

#     # Optimize layout
#     fig.update_layout(
#         autosize=False,
#         width=1000,
#         height=600
#     )

#     # Add title and display the plot
#     st.title('Distribution of Age')
#     st.plotly_chart(fig)

#     x = []  # Store age lists
#     name = []  # Store sport names

#     # List of famous sports
#     famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming', 'Badminton', 'Sailing',
#                      'Gymnastics', 'Art Competitions', 'Handball', 'Weightlifting', 'Water Polo', 'Hockey', 'Rowing',
#                      'Fencing', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Golf',
#                      'Softball', 'Archery', 'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
#                      'Rhythmic Gymnastics', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo',
#                      'Ice Hockey']

#     # Iterate through each sport and get age data for gold medalists
#     for sport in famous_sports:
#         temp_df = athlete_df[athlete_df['Sport'] == sport]
#         gold_ages = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna().tolist()

#         # Only add non-empty lists to avoid errors
#         if len(gold_ages) > 0:
#             x.append(gold_ages)
#             name.append(sport)

#     # Create the distribution plot if data exists
#     if len(x) > 0:
#         fig = ff.create_distplot(
#             x,
#             name,
#             show_hist=False,
#             show_rug=False
#         )

#         # Customize layout
#         fig.update_layout(
#             autosize=False,
#             width=1000,
#             height=600
#         )

#         # Add title and plot
#         st.title("Distribution of Age with Respect to Sport")
#         st.plotly_chart(fig)
#     else:
#         st.warning("No data available for the selected sports.")

#     sport_list = df['Sport'].unique().tolist()
#     sport_list.sort()
#     sport_list.insert(0, 'Overall')

#     # Select sport from dropdown
#     selected_sport = st.selectbox('Select a Sport', sport_list)

#     # Get the filtered data for weight vs height based on the selected sport
#     temp_df = helper.weight_v_height(df, selected_sport)

#     # Check if the returned DataFrame is not empty
#     if temp_df is not None and not temp_df.empty:
#         # Create the scatter plot
#         fig, ax = plt.subplots(figsize=(8, 6))
#         ax = sns.scatterplot(
#             data=temp_df,
#             x='Weight',
#             y='Height',
#             hue='Medal',
#             style='Sex',
#             s=100
#         )

#         # Add plot title and labels
#         ax.set_title(f'Weight vs Height Analysis for {selected_sport}')
#         ax.set_xlabel('Weight (kg)')
#         ax.set_ylabel('Height (cm)')

#         # Display the plot
#         st.pyplot(fig)

#     else:
#         st.warning(f"No data available for {selected_sport}")

#     st.title("Men vs Women Participation Over The Years")
#     final = helper.men_vs_women(df)
#     fig = px.line(final,x = 'Year',y = ["Male","Female"])
#     fig.update_layout(autosize = False,width = 1000,height = 600)
#     st.plotly_chart(fig)

# st.sidebar.markdown("---")
# st.sidebar.markdown("Developed by Narottam Kumar")


import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# Page config for responsiveness
st.set_page_config(page_title="Olympics Analysis", layout="wide")

# Load data
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
df = preprocessor.preprocess(df, region_df)

# Sidebar UI
st.sidebar.title("🏅 Olympics Analysis")
image_url = "https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg"
st.sidebar.image(image_url, caption="Olympics Logo")
st.sidebar.markdown("Analyze Olympics data with various visualizations and insights.")

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

# ---------------------- Medal Tally ----------------------

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == "Overall" and selected_country == "Overall":
        st.title("🏆 Overall Medal Tally")
    elif selected_year != "Overall" and selected_country == "Overall":
        st.title(f"Medal Tally in {selected_year} Olympics")
    elif selected_year == "Overall" and selected_country != "Overall":
        st.title(f"{selected_country} Overall Performance in Olympics")
    else:
        st.title(f"{selected_country} Performance in {selected_year} Olympics")

    st.table(medal_tally)

# ---------------------- Overall Analysis ----------------------

if user_menu == 'Overall Analysis':
    st.title("📊 Top Statistics")

    editions = df['Year'].nunique() - 1
    cities = df['City'].nunique()
    sports = df['Sport'].nunique()
    events = df['Event'].nunique()
    athletes = df['Name'].nunique()
    nations = df['region'].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Editions", editions)
    col2.metric("Hosts", cities)
    col3.metric("Sports", sports)

    col1, col2, col3 = st.columns(3)
    col1.metric("Events", events)
    col2.metric("Nations", nations)
    col3.metric("Athletes", athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    st.title("🌍 Participating Nations Over the Years")
    st.plotly_chart(px.line(nations_over_time, x="Edition", y="region"))

    events_over_time = helper.data_over_time(df, 'Event')
    st.title("🏟️ Events Over the Years")
    st.plotly_chart(px.line(events_over_time, x="Edition", y="Event"))

    athlete_over_time = helper.data_over_time(df, 'Name')
    st.title("👤 Athletes Over the Years")
    st.plotly_chart(px.line(athlete_over_time, x="Edition", y="Name"))

    st.title("📅 No. of Events Over Time (Every Sport)")
    fig, ax = plt.subplots(figsize=(12, 0.5 * df['Sport'].nunique()))
    heatmap_data = df.drop_duplicates(['Year', 'Sport', 'Event']).pivot_table(
        index='Sport', columns='Year', values='Event', aggfunc='count'
    ).fillna(0).astype(int)
    sns.heatmap(heatmap_data, annot=True, fmt='g', cmap='YlGnBu', ax=ax)
    st.pyplot(fig)

    st.title("🏅 Most Successful Athletes")
    sport_list = sorted(df['Sport'].unique().tolist())
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox("Select a Sport", sport_list)
    top_athletes = helper.most_successful(df, selected_sport)
    st.table(top_athletes)

# ---------------------- Country-wise Analysis ----------------------

if user_menu == 'Country-wise Analysis':
    st.sidebar.header("Country-wise Analysis")
    country_list = sorted(df['region'].dropna().unique().tolist())
    selected_country = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    st.title(f"{selected_country} Medal Tally Over the Years")
    st.plotly_chart(px.line(country_df, x="Year", y="Medal"))

    st.title(f"{selected_country} Excels in the Following Sports")
    heatmap_data = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(12, 0.5 * heatmap_data.shape[0]))
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='g', ax=ax)
    st.pyplot(fig)

    st.title(f"Top 10 Athletes of {selected_country}")
    top10_df = helper.most_succesful_countrywise(df, selected_country)
    st.table(top10_df)

# ---------------------- Athlete-wise Analysis ----------------------

if user_menu == 'Athlete-wise Analysis':
    st.title("👩‍🎓 Athlete-wise Analysis")
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    # Age Distribution
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot(
        [x1.tolist(), x2.tolist(), x3.tolist(), x4.tolist()],
        ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
        show_hist=False, show_rug=False
    )
    fig.update_layout(autosize=True, height=500)
    st.title("📈 Distribution of Age")
    st.plotly_chart(fig)

    # Age Distribution by Sport
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming',
                     'Badminton', 'Sailing', 'Gymnastics', 'Handball', 'Weightlifting', 'Water Polo',
                     'Hockey', 'Rowing', 'Fencing', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling',
                     'Diving', 'Canoeing', 'Tennis', 'Golf', 'Softball', 'Archery', 'Volleyball',
                     'Table Tennis', 'Baseball', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon']

    x, name = [], []
    for sport in famous_sports:
        temp = athlete_df[athlete_df['Sport'] == sport]
        gold_ages = temp[temp['Medal'] == 'Gold']['Age'].dropna().tolist()
        if gold_ages:
            x.append(gold_ages)
            name.append(sport)

    if x:
        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=True, height=600)
        st.title("🏅 Age Distribution by Sport (Gold Medalists)")
        st.plotly_chart(fig)
    else:
        st.warning("No data available for selected sports.")

    # Weight vs Height Analysis
    sport_list = sorted(df['Sport'].unique().tolist())
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport for Height vs Weight', sport_list)

    temp_df = helper.weight_v_height(df, selected_sport)
    if temp_df is not None and not temp_df.empty:
        fig, ax = plt.subplots()
        sns.scatterplot(data=temp_df, x='Weight', y='Height', hue='Medal', style='Sex', s=100, ax=ax)
        ax.set_title(f'Weight vs Height Analysis for {selected_sport}')
        ax.set_xlabel('Weight (kg)')
        ax.set_ylabel('Height (cm)')
        st.pyplot(fig)
    else:
        st.warning(f"No data available for {selected_sport}")

    # Men vs Women Participation
    st.title("👨‍🦰 Men vs 👩‍🦱 Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=True, height=500)
    st.plotly_chart(fig)

# ---------------------- Footer ----------------------

st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Narottam Kumar**")
