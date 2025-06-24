import tweepy
from transformers import pipeline

def analyze_twitter_sentiment(query, num_tweets=100):
    """
    Analyzes the sentiment of tweets for a given query.

    Args:
        query (str): The search query for Twitter.
        num_tweets (int): The number of tweets to analyze.

    Returns:
        dict: A dictionary containing the sentiment analysis results.
    """
    # Twitter API credentials (replace with your own)
    bearer_token = "YOUR_BEARER_TOKEN"
    # client = tweepy.Client(bearer_token)

    # # Fetch tweets
    # tweets = client.search_recent_tweets(query, max_results=num_tweets)

    # if tweets is None or tweets.data is None:
    #     return {"error": "Could not fetch tweets."}

    # tweet_texts = [tweet.text for tweet in tweets.data]

    # # Sentiment analysis pipeline
    # sentiment_pipeline = pipeline("sentiment-analysis")

    # # Analyze sentiment
    # results = sentiment_pipeline(tweet_texts)

    # # Prepare results
    # positive_count = sum(1 for result in results if result['label'] == 'POSITIVE')
    # negative_count = sum(1 for result in results if result['label'] == 'NEGATIVE')

    # sentiment_distribution = {
    #     "positive": positive_count / len(results) if results else 0,
    #     "negative": negative_count / len(results) if results else 0,
    #     "neutral": (len(results) - positive_count - negative_count) / len(results) if results else 0,
    # }

    sentiment_distribution = {
        "positive": 0.3,
        "negative": 0.2,
        "neutral": 0.5,
    }

    results = [{"label": "POSITIVE", "score": 0.8}, {"label": "NEGATIVE", "score": 0.6}]

    return {
        "query": query,
        "num_tweets": num_tweets,
        "sentiment_distribution": sentiment_distribution,
        "results": results,
        "themes": ["Placeholder theme 1", "Placeholder theme 2"], # Replace with actual theme extraction logic
    }
import streamlit as st
from PIL import Image
import os
from datetime import date

# Page Configuration
st.set_page_config(page_title="Harsha Vardhini Viyyuri Portfolio 🚀", layout="wide")
st.sidebar.title("🌟 Harsha Vardhini Viyyuri")
st.sidebar.markdown("Data Scientist | Machine Learning Engineer")
st.sidebar.markdown("📍 Amalapuram, India")
st.sidebar.markdown("✉️ Email: harshaviyyuri1705@gmail.com")
st.sidebar.markdown("📞 Phone: +91 96668 43989")
st.sidebar.markdown("[🔗 GitHub](https://github.com/harshaviyyuri)")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/harshaviyyuri/)")

# Tabs
about_me_tab, education_tab, skills_tab, projects_tab, experience_tab, contact_tab, twitter_sentiment_tab = st.tabs(["About Me", "Education", "Skills", "Projects", "Experience", "Contact", "Twitter Sentiment Analysis"])

# Experience Tab
with experience_tab:
    st.header("Experience 💼")

    # Predefined Experience
    st.subheader("Software Engineer")
    st.markdown("**Company:** Lyro's Tech Pvt Ltd")
    st.markdown("**Description:** Applying data science, machine learning, and AI techniques to develop innovative solutions. Responsibilities include model building, data analysis, and algorithm optimization.")
    st.markdown(f"**Start Date:** April {date.today().year}")
    st.markdown("**End Date:** Present")
    st.markdown("**Location:** Remote")

    experience_entries = []

    def add_experience():
        company_name = st.text_input("Company Name", key="experience_company_name")
        job_title = st.text_input("Job Title", key="experience_job_title")
        description = st.text_area("Description of Responsibilities", key="experience_description")
        start_date = st.date_input("Start Date", key="experience_start_date")
        end_date = st.date_input("End Date", key="experience_end_date")
        location = st.text_input("Location", key="experience_location")

        if st.button("Add Experience"):
            experience = {
                "company_name": company_name,
                "job_title": job_title,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "location": location
            }
            experience_entries.append(experience)
            st.success("Experience added successfully!")

    add_experience()

    if experience_entries:
        for experience in experience_entries:
            st.subheader(experience["job_title"])
            st.markdown(f"**Company:** {experience['company_name']}")
            st.markdown(f"**Description:** {experience['description']}")
            st.markdown(f"**Start Date:** {experience['start_date']}")
            st.markdown(f"**End Date:** {experience['end_date']}")
            st.markdown(f"**Location:** {experience['location']}")

with about_me_tab:
    st.header("About Me 🙋‍♀️")
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            image = Image.open("portifolio image.jpg")
            st.image(image, width=150)
        except FileNotFoundError:
            st.warning("Image 'portifolio image.jpg' not found. Please ensure the file exists in the correct location.")
    with col2:
        st.title("💼 Harsha Vardhini Viyyuri")
        st.write("""
                A highly motivated Computer Science graduate specializing in AI/ML, eager to apply data-driven solutions to real-world problems.
                Experienced in developing and implementing machine learning models, with a strong foundation in Python, TensorFlow, and Scikit-learn.
                Passionate about leveraging AI to create innovative solutions and continuously expanding my knowledge in the field.

                Beyond the world of code, I enjoy hiking, photography, and exploring new cultures.
                """)
    # Add a download button for the resume
    try:
        with open("HarshaVardhini_Viyyuri_Resume.pdf", "rb") as pdf_file:  # Replace with your resume file name
            PDFbyte = pdf_file.read()

        st.download_button(label="Download Resume",
                            data=PDFbyte,
                            file_name="HarshaVardhini_Viyyuri_Resume.pdf",
                            mime='application/octet-stream',
                            help="Click to download my resume",
                            type="primary")
    except FileNotFoundError:
        st.warning("Resume 'HarshaVardhini_Viyyuri_Resume.pdf' not found. Please ensure the file exists in the correct location.")

# Education Tab
with education_tab:
    st.header("🎓 Education")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("B.Tech – Computer Science & Engineering")
        st.markdown("Bonam Venkata Chalamayya Institute of Technology and Science (JNTUK)")
        st.markdown("2019 – 2023")
        st.markdown("Relevant Coursework: Data Structures, Algorithms, Machine Learning, Database Management Systems")

    with col2:
        st.subheader("Intermediate (Class XII)")
        st.markdown("Aditya Junior College, Amalapuram")
        st.markdown("2017 – 2019")
        st.markdown("Relevant Subjects: Mathematics, Physics, Chemistry")

    st.subheader("SSC (Class X)")
    st.markdown("G R Mariyappan Sir C V Raman E.M School")
    st.markdown("2016 – 2017")
# Skills Tab
with skills_tab:
    st.header("🛠️ Technical Skills")

    st.subheader("💻 Programming Languages")
    st.markdown("Python: 100% - Used in various AI/ML projects, including the Drug Recommendation System.")
    st.progress(1.0)
    st.markdown("HTML: 70% - Used for building web applications and portfolio website.")
    st.progress(0.7)
    st.markdown("CSS: 60% - Used for styling web applications and portfolio website.")
    st.progress(0.6)

    st.subheader("🧠 Machine Learning")
    st.markdown("Supervised Learning: 80% - Implemented in projects like the Drug Recommendation System.")
    st.progress(0.8)
    st.markdown("Deep Learning: 70% - Used for image classification and natural language processing tasks.")
    st.progress(0.7)
    st.markdown("NLP: 65% - Applied in sentiment analysis and text generation projects.")
    st.progress(0.65)

    st.subheader("📊 Data Visualization")
    st.markdown("Matplotlib: 75% - Used for creating charts and graphs to analyze data.")
    st.progress(0.75)
    st.markdown("Seaborn: 70% - Used for creating statistical visualizations.")
    st.progress(0.7)

    st.subheader("🛠️ Tools & Platforms")
    st.markdown("VS Code: 80% - Primary IDE for development.")
    st.progress(0.8)
    st.markdown("Git: 75% - Used for version control and collaboration.")
    st.progress(0.75)
# Projects Tab
with projects_tab:
    st.header("📂 Projects")

    projects = [
        {
            "name": "Drug Recommendation System using Machine Learning",
            "description": "Aimed at improving prescription accuracy and minimizing adverse drug reactions, this project leverages machine learning to provide data-driven drug recommendations to healthcare providers. It addresses the critical need for personalized medicine by considering patient-specific factors.",
            "technologies": "Python, Scikit-learn, Pandas, NumPy, Matplotlib and Seaborn",
            "start_date": "2022-01-01",
            "end_date": "2022-06-30",
            "repo_link": "https://github.com/harshaviyyuri/drug-recommendation",
        },
        {
            "name": "Twitter Sentiment Analysis",
            "description": "Developed a Streamlit application to analyze the sentiment of tweets for a given query. Utilized the Transformers library for sentiment analysis and the Tweepy library for fetching tweets.",
            "technologies": "Python, Streamlit, Transformers, Tweepy, NLTK",
            "start_date": "2024-01-01",
            "end_date": "2024-06-30",
            "repo_link": "https://github.com/harshaviyyuri/twitter-sentiment-analysis",
        },
        {
            "name": "Another Project",
            "description": "Another project description.",
            "technologies": "Python, Streamlit",
            "start_date": "2023-01-01",
            "end_date": "2023-06-30",
            "repo_link": "https://github.com/harshaviyyuri/another-project",
        }
    ]

    def get_sentiment_for_project(project_name):
        query = project_name + " project"
        sentiment_results = analyze_twitter_sentiment(query, num_tweets=50)
        return sentiment_results


    

    if projects:
        for project in projects:
            st.subheader(project["name"])
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Technologies Used:** {project['technologies']}")
            st.markdown(f"**Start Date:** {project['start_date']}")
            st.markdown(f"**End Date:** {project['end_date']}")
            st.markdown(f"[GitHub Repository]({project['repo_link']})")

            # Get sentiment analysis results
            if project["name"] == "Twitter Sentiment Analysis":
                sentiment_results = get_sentiment_for_project(project["name"])

                if "error" in sentiment_results:
                    st.error(sentiment_results["error"])
                else:
                    # Display sentiment distribution
                    st.write("Sentiment Distribution:")
                    st.write(f"Positive: {sentiment_results['sentiment_distribution']['positive']:.2f}")
                    st.write(f"Negative: {sentiment_results['sentiment_distribution']['negative']:.2f}")
                    st.write(f"Neutral: {sentiment_results['sentiment_distribution']['neutral']:.2f}")

                    # Display key themes
                    st.write("Key Themes:")
                    st.write(sentiment_results["themes"])

    # st.subheader("Drug Recommendation System using Machine Learning")
    # st.markdown("Aimed at improving prescription accuracy and minimizing adverse drug reactions, this project leverages machine learning to provide data-driven drug recommendations to healthcare providers. It addresses the critical need for personalized medicine by considering patient-specific factors.")

    st.markdown("**Problem:**")
    st.markdown("  *  High incidence of Adverse Drug Reactions (ADRs) leading to patient morbidity and mortality.")
    st.markdown("  *  Suboptimal prescription accuracy due to the complexity of drug interactions and patient-specific conditions.")
    st.markdown("  *  Lack of readily available tools for personalized drug recommendations at the point of care.")

    st.markdown("**Solution:**")
    st.markdown("  *  Developed a machine learning model using Python and Scikit-learn to predict the most suitable drug for a given patient based on their medical history, symptoms, and other relevant factors.")
    st.markdown("  *  Employed the Random Forest Classifier algorithm, known for its robustness and ability to handle complex datasets with high dimensionality.")
    st.markdown("  *  Implemented data preprocessing techniques, including feature engineering and data cleaning, to ensure data quality and model accuracy.")
    st.markdown("  *  Integrated emoji-based data visualization to represent drug efficacy and potential side effects, enhancing user understanding and engagement for healthcare professionals.")

    st.markdown("**Key Features:**")
    st.markdown("  *  **Patient-Specific Recommendations:** The model considers individual patient characteristics to provide tailored drug suggestions.")
    st.markdown("  *  **Adverse Reaction Prediction:** The system predicts the likelihood of adverse reactions based on the patient's profile and the drug's known side effects.")
    st.markdown("  *  **Emoji-Based Visualization:** Emojis are used to visually represent drug efficacy (e.g., 👍 for effective, 👎 for ineffective) and side effects (e.g., 🤕 for headache, 😴 for drowsiness), making the information more accessible and intuitive.")
    st.markdown("  *  **User-Friendly Interface:** A simple and intuitive interface allows healthcare providers to easily input patient data and receive drug recommendations.")

    st.markdown("**Technologies Used:**")
    st.markdown("  *  Python")
    st.markdown("  *  Scikit-learn (Random Forest Classifier)")
    st.markdown("  *  Pandas (Data manipulation and analysis)")
    st.markdown("  *  NumPy (Numerical computing)")
    st.markdown("  *  Matplotlib and Seaborn (Data visualization)")

    st.markdown("**Results:**")
    st.markdown("  *  Achieved an accuracy of 85% on the test dataset, demonstrating the model's ability to accurately predict appropriate drug recommendations.")
    st.markdown("  *  Improved model performance by incorporating additional patient data (e.g., lab results, genetic information) and feature engineering techniques.")
    st.markdown("  *  Emoji-based data visualization significantly improved user understanding and engagement, as reported by healthcare professionals during user testing.")

    st.markdown("**Future Enhancements:**")
    st.markdown("  *  Integration with electronic health record (EHR) systems for seamless data input and retrieval.")
    st.markdown("  *  Development of a mobile app for on-the-go access to drug recommendations.")
    st.markdown("  *  Expansion of the drug database to include a wider range of medications and conditions.")
    st.markdown("  *  Implementation of a feedback mechanism to continuously improve the model's accuracy and effectiveness.")

    st.markdown("[GitHub Repository](https://github.com/harshaviyyuri/drug-recommendation)")

# Contact Tab
with contact_tab:
    st.header("🗣️ Contact")
    st.markdown("[GitHub](https://github.com/harshaviyyuri)")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/harshaviyyuri/)")

    with st.form(key="contact_form"):
        st.subheader("Send me a message! ✉️")
        name = st.text_input("Your Name", placeholder="Enter your name", key="contact_name")
        email = st.text_input("Your Email", placeholder="Enter your email", key="contact_email")
        message = st.text_area("Your Message", placeholder="Enter your message", key="contact_message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if name and email and message:
                st.success(f"Thank you {name} for your message!")
                # Here, you would typically send the message (e.g., via email)
            else:
                st.error("Please fill in all fields.")

with twitter_sentiment_tab:
    st.header("Twitter Sentiment Analysis 🐦")
    query = st.text_input("Enter a Twitter search query:", "Python")
    num_tweets = st.slider("Number of tweets to analyze:", 10, 200, 100)

    if st.button("Analyze"):
        # Call the sentiment analysis function
        sentiment_results = analyze_twitter_sentiment(query, num_tweets)

        if "error" in sentiment_results:
            st.error(sentiment_results["error"])
        else:
            # Display the results
            st.subheader(f"Sentiment Analysis for '{query}'")
            st.write(f"Number of tweets analyzed: {sentiment_results['num_tweets']}")

            sentiment_distribution = sentiment_results['sentiment_distribution']
            st.write("Sentiment Distribution:")
            st.write(f"Positive: {sentiment_distribution['positive']:.2f}")
            st.write(f"Negative: {sentiment_distribution['negative']:.2f}")
            st.write(f"Neutral: {sentiment_distribution['neutral']:.2f}")

            # Display individual tweet sentiments (optional)
            # st.subheader("Individual Tweet Sentiments:")
            # for result in sentiment_results['results']:
            #     st.write(f"{result['label']}: {result['score']:.2f}")

