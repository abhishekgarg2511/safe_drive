import tempfile
import streamlit as st
import cv2
import numpy as np


def main():
    st.title("Traffic Video Analysis")

    # uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])
    st.sidebar.title("settings")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width : 400px;}
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{width : 400px; margin-left: -400px}
        </style>
        """,
        unsafe_allow_html=True,    
    )
    st.sidebar.markdown('----')
    confidence =st.sidebar.slider('Confidence',min_value=0.0, max_value=1.0 ,value=0.25)
    st.sidebar.markdown('----')

    #checkboxes
    save_img =st.sidebar.checkbox('Save Video')
    enable_GPU=st.sidebar.checkbox('Enable GPU')

    # uploading output video
    video_file_buffer = st.sidebar.file_uploader("Upload a video file", type=[" mp4 " , " mov " , " avi " , " m4v ", " asf "])
    DEMO_VIDEO= "traffic.mp4"
    tfflie = tempfile.NamedTemporaryFile(suffix='.mp4',delete=False)

    #Get input image
    if not video_file_buffer:
        print("Video not uploaded")
    
    else:
        tfflie.write(video_file_buffer.read())
        dem_vid = open(tfflie.name , 'rb')
        demo_bytes=dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(demo_bytes)
        
        



    # if uploaded_file is not None:
    #     video = cv2.VideoCapture(uploaded_file)
    #     video.release()

if __name__ == "__main__":
    main()
