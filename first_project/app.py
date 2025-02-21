import streamlit as st
import pandas as pd
import os
from io import BytesIO
import time

def set_custom_style():
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            color: #1E88E5;
            font-size: 3.5rem !important;
            padding: 20px;
            font-weight: bold;
        }
        .name-highlight {
            background: linear-gradient(120deg, #1E88E5, #00B0FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            font-size: 1.8rem !important;
            padding: 10px;
            text-align: center;
            display: block;
        }
        .welcome-text {
            text-align: center;
            padding: 20px;
            background-color: #f0f2f6;
            border-radius: 10px;
            margin: 2rem 0;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-width: 300px;
            margin: 0 auto;
        }
        .feature-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        .highlight-text {
            color: #1E88E5;
            font-weight: bold;
        }
        .centered-image {
            display: block;
            margin: 0 auto;
            max-width: 150px;
        }
        </style>
    """, unsafe_allow_html=True)

def show_instructions():
    st.markdown("<h1 class='main-title'>📚 How to Use Deep Sweeper</h1>", unsafe_allow_html=True)
    
    # Main steps card
    st.markdown("""
    <div class='feature-card'>
        <h2 style='color: #1E88E5; text-align: center;'>Quick Start Guide</h2>
        <p style='text-align: center; font-size: 1.1rem;'>
            Follow these simple steps to convert and clean your data files
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Step-by-step instructions in cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h3>📤 Step 1: Upload Your File</h3>
            <ul>
                <li>Click on "Upload Files" in the sidebar</li>
                <li>Choose your CSV or Excel file</li>
                <li>Your file preview will appear automatically</li>
            </ul>
        </div>
        
        <div class='feature-card'>
            <h3>🧹 Step 2: Clean Your Data (Optional)</h3>
            <ul>
                <li>Enable "Data Cleaning" in sidebar</li>
                <li>Click "Remove Duplicates" if needed</li>
                <li>Use "Fill Missing Values" for gaps in data</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h3>📊 Step 3: Visualize Data (Optional)</h3>
            <ul>
                <li>Select columns for visualization</li>
                <li>Check "Show Bar Chart" to view</li>
                <li>Analyze your data visually</li>
            </ul>
        </div>
        
        <div class='feature-card'>
            <h3>💾 Step 4: Convert & Download</h3>
            <ul>
                <li>Choose output format (CSV/Excel)</li>
                <li>Click "Convert & Download"</li>
                <li>Save your processed file</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Tips card at the bottom
    st.markdown("""
    <div class='feature-card'>
        <h3 style='text-align: center;'>💡 Helpful Tips</h3>
        <ul>
            <li>Make sure your file is in CSV or Excel format</li>
            <li>Preview your data before processing</li>
            <li>Use the sidebar controls to customize options</li>
            <li>Check the success message before downloading</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def show_about():
    st.markdown("<h1 class='main-title'>🚀 About Deep Sweeper</h1>", unsafe_allow_html=True)
    
    # Project description card
    st.markdown("""
    <div class='feature-card'>
        <h2 style='color: #1E88E5; text-align: center;'>Project Overview</h2>
        <p style='text-align: center; font-size: 1.1rem;'>
            Deep Sweeper represents a journey into data processing and web application development,
            combining passion for data analysis with user-friendly design.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project details in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <h3>🎯 Project Goals</h3>
            <ul>
                <li>Intuitive data conversion interface</li>
                <li>Essential data cleaning features</li>
                <li>Useful visualization capabilities</li>
                <li>User-friendly experience</li>
            </ul>
        </div>
        
        <div class='feature-card'>
            <h3>🛠️ Technologies Used</h3>
            <ul>
                <li>Streamlit - Web Interface</li>
                <li>Pandas - Data Processing</li>
                <li>Python - Backend Logic</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h3>🔮 Future Enhancements</h3>
            <ul>
                <li>Additional file format support</li>
                <li>Advanced data cleaning options</li>
                <li>More visualization types</li>
                <li>Batch processing capabilities</li>
            </ul>
        </div>
        
        <div class='feature-card'>
            <h3>📈 Impact</h3>
            <ul>
                <li>Streamlined data processing</li>
                <li>Enhanced user productivity</li>
                <li>Simplified file conversion</li>
                <li>Improved data quality</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def main_app():
    st.set_page_config(page_title="Deep Sweeper", layout="wide")
    set_custom_style()
    
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Homepage
    if st.session_state.page == 'home':
        # Main title with icon
        st.markdown("<h1 class='main-title'>🌟 Deep Sweeper</h1>", unsafe_allow_html=True)
        st.markdown("<h2 class='name-highlight'>Prepared by Syed Shoaib Sherazi</h2>", unsafe_allow_html=True)
        
        # Welcome message
        st.markdown("""
        <div class='welcome-text'>
            <h3>Welcome to Deep Sweeper! 🎉</h3>
            <p>Transform your data with our powerful file conversion and cleaning tool.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Centered column for buttons
        col1, col2, col3 = st.columns([1,2,1])
        
        with col2:
            st.markdown("<div class='button-container'>", unsafe_allow_html=True)
            if st.button("📖 Instructions", use_container_width=True, key="btn_instructions"):
                st.session_state.page = 'instructions'
                st.rerun()
            
            if st.button("🚀 Open App", use_container_width=True, key="btn_app"):
                st.session_state.page = 'app'
                st.rerun()
            
            if st.button("ℹ️ About", use_container_width=True, key="btn_about"):
                st.session_state.page = 'about'
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature highlights
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(4)
        
        with cols[0]:
            st.markdown("""
            <div class='feature-card' style='text-align: center;'>
                <h3>🔄 Convert</h3>
                <p>CSV ↔️ Excel / Excel ↔️ CSV </p>       
            </div>
            """, unsafe_allow_html=True)
            
        with cols[1]:
            st.markdown("""
            <div class='feature-card' style='text-align: center;'>
                <h3>🧹 Clean</h3>
                <p>Fix Data Issues</p>
            </div>
            """, unsafe_allow_html=True)
            
        with cols[2]:
            st.markdown("""
            <div class='feature-card' style='text-align: center;'>
                <h3>📊 Visualize</h3>
                <p>See Insights</p>
            </div>
            """, unsafe_allow_html=True)
            
        with cols[3]:
            st.markdown("""
            <div class='feature-card' style='text-align: center;'>
                <h3>💾 Save</h3>
                <p>Download Results</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Instructions page
    elif st.session_state.page == 'instructions':
        if st.button("🏠 Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
        show_instructions()
    
    # About page
    elif st.session_state.page == 'about':
        if st.button("🏠 Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
        show_about()
    
    # Main app page
    elif st.session_state.page == 'app':
        if st.button("🏠 Back to Home"):
            st.session_state.page = 'home'
            st.rerun()
            
        st.title(":cd: Deep Sweeper")
        st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

        # Rest of your original app code remains the same
        st.sidebar.header("Upload Files")
        uploaded_files = st.sidebar.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

        if uploaded_files:
            selected_file = st.sidebar.selectbox("Select a file to process", [file.name for file in uploaded_files])

            file = next(f for f in uploaded_files if f.name == selected_file)
            file_ext = os.path.splitext(file.name)[-1].lower()

            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported File Type! {file_ext}")

            st.subheader(f"Preview of {file.name}")
            num_rows = st.sidebar.slider("Number of rows to display:", min_value=1, max_value=len(df), value=5)
            st.dataframe(df.head(num_rows))

            st.sidebar.subheader("Data Cleaning")
            clean_data = st.sidebar.checkbox("Enable Data Cleaning")

            if clean_data:
                if st.sidebar.button("Remove Duplicates"):
                    df.drop_duplicates(inplace=True)
                    st.sidebar.success("✅ Duplicates Removed")

                if st.sidebar.button("Fill Missing Values"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.sidebar.success("✅ Missing values filled")

            st.sidebar.subheader("Column Selection For Showing Bar Chart")
            columns = st.sidebar.multiselect("Choose any 2 columns to show on Bar Chart", df.columns, default=df.columns)
            df = df[columns]

            st.subheader("File Information")
            st.write(f"📂 **File Name**: {file.name}")
            st.write(f"📏 **File Size**: {file.size} bytes")

            st.subheader(":bar_chart: Data Visualization")
            if st.sidebar.checkbox("Show Bar Chart"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

            st.sidebar.subheader("Convert File Format")
            convert_type = st.sidebar.radio("Convert file to:", ["CSV", "Excel"])
            
            if st.sidebar.button("Convert & Download"):
                buffer = BytesIO()
                file_name = file.name.replace(file_ext, f".{convert_type.lower()}")

                if convert_type == "CSV":
                    df.to_csv(buffer, index=False)
                    mime_type = "text/csv"
                elif convert_type == "Excel":
                    df.to_excel(buffer, index=False)
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)
                downloaded = st.download_button(
                    label="📥 Download Processed File",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type,
                )

                if downloaded:
                    progress_bar = st.progress(0)
                    for percent in range(100):
                        time.sleep(0.03)
                        progress_bar.progress(percent + 1)

                    st.success("")
                    st.markdown(
                        """
                        <div style="
                            background-color: #B88E2F; 
                            color: white; 
                            padding: 15px; 
                            border-radius: 10px;
                            text-align: center;
                            font-size: 18px;">
                            ✅ <b>Success!</b> All files have been processed and are ready for download. 🚀
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.balloons()

if __name__ == "__main__":
    main_app()






