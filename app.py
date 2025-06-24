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
about_me_tab, education_tab, skills_tab, projects_tab, experience_tab, contact_tab = st.tabs(["About Me", "Education", "Skills", "Projects", "Experience", "Contact"])

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

    # --- Project 1: Drug Recommendation System ---
    st.subheader("Drug Recommendation System using Machine Learning")
    st.markdown("**Description:** Aimed at improving prescription accuracy and minimizing adverse drug reactions, this project leverages machine learning to provide data-driven drug recommendations to healthcare providers. It addresses the critical need for personalized medicine by considering patient-specific factors.")

    st.markdown("**Problem:**")
    st.markdown("""
    * High incidence of Adverse Drug Reactions (ADRs) leading to patient morbidity and mortality.
    * Suboptimal prescription accuracy due to the complexity of drug interactions and patient-specific conditions.
    * Lack of readily available tools for personalized drug recommendations at the point of care.
    """)

    st.markdown("**Solution:**")
    st.markdown("""
    * Developed a machine learning model using Python and Scikit-learn to predict the most suitable drug for a given patient based on their medical history and symptoms.
    * Used Random Forest Classifier for robustness in handling complex, high-dimensional datasets.
    * Performed data cleaning and feature engineering for accuracy.
    * Introduced emoji-based visualizations to represent drug efficacy and side effects.
    """)

    st.markdown("**Key Features:**")
    st.markdown("""
    * **Patient-Specific Recommendations:** Tailored drug suggestions using patient data.
    * **Adverse Reaction Prediction:** Predicts likelihood of side effects based on known reactions.
    * **Emoji-Based Visualization:** Uses emojis like 👍, 👎, 🤕, 😴 for intuitive visual feedback.
    * **User-Friendly Interface:** Simple UI for healthcare providers to input data and receive suggestions.
    """)

    st.markdown("**Technologies Used:**")
    st.markdown("""
    * Python  
    * Scikit-learn (Random Forest Classifier)  
    * Pandas, NumPy  
    * Matplotlib, Seaborn
    """)

    st.markdown("**Results:**")
    st.markdown("""
    * 85% model accuracy on test data.
    * Improved performance through feature engineering and data enrichment.
    * Emoji visualization improved user comprehension.
    """)

    st.markdown("**Future Enhancements:**")
    st.markdown("""
    * EHR integration  
    * Mobile app development  
    * Broader drug and condition coverage  
    * Feedback-based model improvement
    """)

    st.markdown("[GitHub Repository](https://github.com/harshaviyyuri/drug-recommendation)")

    st.markdown("---")

    # --- Project 2: Twitter Sentiment Analysis ---
    st.subheader("Twitter Sentiment Analysis 🐦")
    st.markdown("**Description:** A Streamlit app to analyze the sentiment of tweets based on user-defined queries using Hugging Face Transformers and Tweepy.")

    query = st.text_input("Enter a Twitter search query:", "Python")
    num_tweets = st.slider("Number of tweets to analyze:", 10, 200, 100)

    if st.button("Analyze"):
        sentiment_results = analyze_twitter_sentiment(query, num_tweets)

        if "error" in sentiment_results:
            st.error(sentiment_results["error"])
        else:
            st.write(f"**Number of tweets analyzed:** {sentiment_results['num_tweets']}")
            sentiment_distribution = sentiment_results['sentiment_distribution']

            st.markdown("**Sentiment Distribution:**")
            st.write(f"😊 Positive: {sentiment_distribution['positive']:.2f}")
            st.write(f"😞 Negative: {sentiment_distribution['negative']:.2f}")
            st.write(f"😐 Neutral: {sentiment_distribution['neutral']:.2f}")

            st.markdown("**Key Themes Identified:**")
            st.write(sentiment_results["themes"])

    st.markdown("**Technologies Used:** Python, Streamlit, Transformers, Tweepy, NLTK")
    st.markdown("[GitHub Repository](https://github.com/harshaviyyuri/twitter-sentiment-analysis)")


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
