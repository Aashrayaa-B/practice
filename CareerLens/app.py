import streamlit as st

# Career skills mapping
career_skills = {
    'Data Analyst': ['Python', 'SQL', 'Excel', 'Tableau', 'Power BI', 'Statistics', 'Data Analysis'],
    'Business Analyst': ['Excel', 'SQL', 'Communication', 'Problem Solving', 'Data Analysis', 'Power BI'],
    'Data Scientist': ['Python', 'Machine Learning', 'Statistics', 'SQL', 'Data Analysis'],
    'ML Engineer': ['Python', 'Machine Learning', 'Deep Learning', 'SQL', 'Statistics'],
    'BI Analyst': ['Tableau', 'Power BI', 'Excel', 'SQL', 'Data Analysis'],
    'Software Engineer': ['Python', 'Java', 'Data Structures', 'Problem Solving', 'Git'],
    'Web Developer': ['HTML', 'CSS', 'JavaScript', 'Problem Solving', 'Git'],
    'Cybersecurity Analyst': ['Networking', 'Problem Solving', 'Communication', 'Linux', 'Python'],
    'Cloud Engineer': ['AWS', 'Python', 'Linux', 'Networking', 'Problem Solving'],
    'AI Research Scientist': ['Python', 'Machine Learning', 'Deep Learning', 'Statistics', 'Research'],
    'Database Administrator': ['SQL', 'Database Design', 'Problem Solving', 'Linux', 'Excel'],
    'Product Analyst': ['SQL', 'Excel', 'Communication', 'Data Analysis', 'Problem Solving'],
    'NLP Engineer': ['Python', 'Machine Learning', 'Deep Learning', 'Research', 'Statistics'],
    'Statistician': ['Statistics', 'Python', 'Excel', 'Data Analysis', 'Research'],
    'IT Consultant': ['Communication', 'Problem Solving', 'Networking', 'Excel', 'SQL'],
}

# Page config
st.set_page_config(page_title="Career Intelligence System", page_icon="🎯", layout="centered")

# Title
st.title("CareerLens")
st.subheader("Discover the career that fits YOU best")
st.markdown("---")

# User inputs
st.header("Tell us about yourself")

education = st.selectbox("Education Level", 
    ["Select", "High School", "Bachelor's", "Master's", "PhD"])

cgpa = st.slider("Your CGPA / Percentage", 0.0, 10.0, 7.0, 0.1)

all_skills = sorted(set(
    skill for skills in career_skills.values() for skill in skills
))

selected_skills = st.multiselect(
    "Select your skills (choose all that apply)",
    options=all_skills
)

# Predict button
if st.button("🔍 Find My Career Matches"):
    if not selected_skills:
        st.warning("Please select at least one skill!")
    else:
        st.markdown("---")
        st.header("🏆 Your Career Matches")

        # Score each career
        results = {}
        for career, required in career_skills.items():
            matched = len(set(selected_skills) & set(required))
            total = len(required)
            score = round((matched / total) * 100)
            results[career] = score

        # Sort by score
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

        # Show top 5
        for i, (career, score) in enumerate(sorted_results[:5]):
            st.subheader(f"{i+1}. {career}")
            st.progress(score / 100)
            st.write(f"**Match: {score}%**")

            # Skills gap
            required = career_skills[career]
            strong = [s for s in selected_skills if s in required]
            missing = [s for s in required if s not in selected_skills]

            col1, col2 = st.columns(2)
            with col1:
                st.success(f"✅ Strong: {', '.join(strong) if strong else 'None'}")
            with col2:
                st.error(f"❌ Missing: {', '.join(missing) if missing else 'None'}")
            st.markdown("---")
            # Skill Roadmap for top career
        top_career = sorted_results[0][0]
        top_missing = [s for s in career_skills[top_career] if s not in selected_skills]

        if top_missing:
            st.header("🗺️ Your Skill Roadmap")
            st.write(f"To become a **{top_career}**, focus on learning these skills next:")

            priority_resources = {
                'Python': 'Kaggle Free Python Course',
                'SQL': 'Mode Analytics SQL Tutorial',
                'Excel': 'GCFGlobal Excel Course (Free)',
                'Tableau': 'Tableau Public Free Training',
                'Power BI': 'Microsoft Learn Power BI (Free)',
                'Machine Learning': 'Andrew Ng ML Course - Coursera',
                'Statistics': 'Khan Academy Statistics (Free)',
                'Data Analysis': 'Google Data Analytics Certificate',
                'Communication': 'Practice presentations and writing daily',
                'Problem Solving': 'LeetCode Easy Problems daily',
                'Deep Learning': 'Fast.ai Deep Learning Course (Free)',
                'Research': 'Read 1 research paper per week',
                'AWS': 'AWS Free Tier + Cloud Practitioner Course',
                'Git': 'GitHub Learning Lab (Free)',
                'Linux': 'Linux Journey (Free)',
                'HTML': 'freeCodeCamp HTML Course (Free)',
                'CSS': 'freeCodeCamp CSS Course (Free)',
                'JavaScript': 'freeCodeCamp JavaScript Course (Free)',
                'Java': 'MOOC.fi Java Programming (Free)',
                'Networking': 'Cisco Networking Academy (Free)',
                'Database Design': 'Stanford DB Course (Free)',
                'Financial Analysis': 'CFI Free Financial Modeling Course',
                'Marketing': 'Google Digital Marketing Certificate',
                'Data Structures': 'GeeksForGeeks DSA Course',
            }

            for i, skill in enumerate(top_missing):
                resource = priority_resources.get(skill, 'Search on YouTube or Coursera')
                st.write(f"**Priority {i+1} → {skill}**")
                st.info(f"📚 Learn from: {resource}")
        else:
            st.header("🗺️ Your Skill Roadmap")
            st.success(f"🎉 You already have all the skills needed for {top_career}! Start applying now.")