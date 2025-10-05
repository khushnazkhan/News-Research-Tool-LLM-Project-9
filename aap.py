import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
from langchain_config import get_news_articles, summarize_articles, get_enhanced_summary

# Premium Page Configuration
st.set_page_config(
    page_title="🚀 NewsMatrix Pro - GROQ ACTIVE",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra Premium CSS with Animated Gradient
st.markdown("""
<style>
    /* Main Background with Animated Gradient */
    .stApp {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Fixed Sidebar Background */
    .css-1d391kg, .css-1lcbmhc {
        background: rgba(0, 0, 0, 0.7) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    /* Sidebar Text Color */
    .css-1d391kg p, .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, 
    .css-1d391kg h4, .css-1d391kg label, .css-1d391kg div {
        color: white !important;
    }
    
    /* Glass Morphism with Neon Glow */
    .neo-glass {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .neo-glass::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: 0.5s;
    }
    
    .neo-glass:hover::before {
        left: 100%;
    }
    
    .neo-glass:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    /* API Status Cards */
    .api-status-active {
        background: rgba(76, 175, 80, 0.3);
        border: 2px solid #4CAF50;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    .api-status-inactive {
        background: rgba(244, 67, 54, 0.3);
        border: 2px solid #F44336;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    /* Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating {
        animation: float 6s ease-in-out infinite;
    }
    
    /* Premium Cards */
    .premium-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.4s ease;
    }
    
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    /* Advanced Button Designs */
    .stButton button {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 300% 300%;
        border: none;
        border-radius: 50px;
        color: white;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.5s ease;
        animation: gradientShift 3s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    
    /* Text Colors */
    .white-text {
        color: white !important;
    }
    
    .gradient-text {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
</style>
""", unsafe_allow_html=True)

def create_hero_section():
    """Create stunning hero section with API status"""
    st.markdown(f"""
    <div class="neo-glass" style="text-align: center; padding: 3rem 2rem;">
        <h1 class="floating" style="font-size: 4rem; margin-bottom: 1rem; background: linear-gradient(45deg, #667eea, #764ba2, #f093fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🚀 NewsMatrix Pro</h1>
        <p style="font-size: 1.3rem; color: rgba(255,255,255,0.9); margin-bottom: 2rem;">
            GROQ API ACTIVE • Real-time Intelligence • Lightning Fast
        </p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <div class="api-status-active">
                <strong>🚀 GROQ API</strong>
                <div style="color: #4CAF50; font-size: 1.1rem;">✅ ACTIVE & RUNNING</div>
                <div style="font-size: 0.8rem;">Llama3 - Ultra Fast</div>
            </div>
            <div class="api-status-active">
                <strong>📰 NewsAPI</strong>
                <div style="color: #4CAF50; font-size: 1.1rem;">✅ ACTIVE & RUNNING</div>
                <div style="font-size: 0.8rem;">Real-time News</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_search_interface():
    """Create premium search interface"""
    st.markdown("""
    <div class="neo-glass">
        <h2 style="color: white; text-align: center; margin-bottom: 2rem;">🔮 Ask Anything - GROQ Powered</h2>
    """, unsafe_allow_html=True)
    
    # Search input with icon
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_input(
            " ",
            placeholder="🔍 Ask anything: Cricket, Stock market, Technology, Politics...",
            label_visibility="collapsed"
        )
    
    with col2:
        search_clicked = st.button("🚀 Launch Analysis", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    return query, search_clicked

def display_premium_results(articles_data, query):
    """Display results in premium format"""
    st.markdown(f"""
    <div class="neo-glass">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
            <h2 style="color: white; margin: 0;">📡 Live Intelligence: {query}</h2>
            <span style="background: rgba(255,255,255,0.2); color: white; padding: 0.5rem 1.5rem; border-radius: 20px;">
                {len(articles_data)} Sources • GROQ ACTIVE
            </span>
        </div>
    """, unsafe_allow_html=True)
    
    # Display articles in grid
    cols = st.columns(2)
    for i, article in enumerate(articles_data):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="premium-card">
                <div style="display: flex; align-items: start; gap: 1rem;">
                    <img src="{article['image']}" style="width: 120px; height: 80px; border-radius: 8px; object-fit: cover;">
                    <div style="flex: 1;">
                        <h4 style="color: white; margin-bottom: 0.5rem;">{article['title']}</h4>
                        <p style="color: rgba(255,255,255,0.8); margin-bottom: 0.5rem; font-size: 0.9rem;">
                            <strong>Source:</strong> {article['source']} | 
                            <strong>Date:</strong> {article['published_at']}
                        </p>
                        <p style="color: rgba(255,255,255,0.9); margin-bottom: 1rem; line-height: 1.4;">
                            {article['description']}
                        </p>
                        <a href="{article['url']}" target="_blank" style="color: #f093fb; text-decoration: none; font-weight: 600;">
                            🔗 Read Full Article
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def display_ai_intelligence(analysis, query):
    """Display AI analysis in premium format"""
    st.markdown("""
    <div class="neo-glass">
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">
            <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 15px;">
                <span style="font-size: 2rem;">🧠</span>
            </div>
            <div>
                <h2 style="color: white; margin: 0;">Neural Network Analysis</h2>
                <p style="color: rgba(255,255,255,0.8); margin: 0;">Powered by GROQ Llama3 - Ultra Fast</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="premium-card">
        <h4 style="color: white; margin-bottom: 1rem;">🚀 GROQ AI Executive Brief</h4>
        <div style="color: rgba(255,255,255,0.9); line-height: 1.6; background: rgba(0,0,0,0.3); padding: 1.5rem; border-radius: 10px;">
            {analysis}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def create_sidebar_intelligence():
    """Create intelligent sidebar with API status and Quick Intelligence"""
    with st.sidebar:
        st.markdown("""
        <div class="premium-card">
            <h3 style="color: white; text-align: center;">🔭 Control Center</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # API Status in Sidebar
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: white; margin-bottom: 1rem;">🚀 API Status</h4>
            <div style="color: rgba(255,255,255,0.9);">
                <div style="background: rgba(102, 126, 234, 0.3); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border: 1px solid #667eea;">
                    <strong>🚀 GROQ AI</strong>
                    <div style="color: #667eea; font-size: 1rem;">✅ ACTIVE & RUNNING</div>
                    <div style="font-size: 0.8rem;">Llama3 - Ultra Fast</div>
                </div>
                <div style="background: rgba(118, 75, 162, 0.3); padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border: 1px solid #764ba2;">
                    <strong>📰 NewsAPI</strong>
                    <div style="color: #764ba2; font-size: 1rem;">✅ ACTIVE & RUNNING</div>
                    <div style="font-size: 0.8rem;">Real-time News</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Intelligence - All 6 categories moved here
        st.markdown("""
        <div class="premium-card">
            <h4 style="color: white; margin-bottom: 1rem;">🎯 Quick Intelligence</h4>
            <div style="color: rgba(255,255,255,0.9);">
        """, unsafe_allow_html=True)
        
        # Quick categories in sidebar
        categories = [
            ("🏏 Cricket Updates", "cricket"),
            ("💼 Stock Market", "stock market"), 
            ("🤖 AI Technology", "artificial intelligence"),
            ("🇮🇳 Politics", "india politics"),
            ("🌍 World News", "world news"),
            ("🔬 Science", "science news")
        ]
        
        selected_category = None
        for display_name, search_query in categories:
            if st.button(display_name, key=f"sidebar_{search_query}", use_container_width=True):
                selected_category = search_query
        
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        return selected_category

def main():
    """Main application function"""
    # Initialize session state
    if 'current_query' not in st.session_state:
        st.session_state.current_query = ""
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False
    
    # Hero Section with API Status
    create_hero_section()
    
    # Search Interface at TOP
    query, search_clicked = create_search_interface()
    
    # Sidebar Intelligence with Quick Categories
    selected_category = create_sidebar_intelligence()
    
    # Handle search - IMMEDIATE RESULTS
    if selected_category:
        # If category selected from sidebar, set as current query and show results immediately
        st.session_state.current_query = selected_category
        st.session_state.show_results = True
        # Use st.rerun() to immediately refresh and show results
        st.rerun()
    
    if search_clicked and query:
        # If search button clicked, set as current query and show results immediately  
        st.session_state.current_query = query
        st.session_state.show_results = True
        # Use st.rerun() to immediately refresh and show results
        st.rerun()
    
    # Display results immediately when show_results is True
    if st.session_state.show_results and st.session_state.current_query:
        current_query = st.session_state.current_query
        
        with st.spinner("🧠 Activating GROQ Neural Network..."):
            try:
                # Get intelligence data from APIs
                articles = get_news_articles(current_query)
                articles_data = summarize_articles(articles)
                
                if articles_data:
                    # Display intelligence feed
                    display_premium_results(articles_data, current_query)
                    
                    # GROQ AI Intelligence
                    analysis = get_enhanced_summary(current_query, articles_data)
                    display_ai_intelligence(analysis, current_query)
                
                else:
                    st.error("🚫 No intelligence signals detected. Please refine your query.")
                    
            except Exception as e:
                st.error(f"⚠️ System anomaly: {str(e)}")

if __name__ == "__main__":
    main()