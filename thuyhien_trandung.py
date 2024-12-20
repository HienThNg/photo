import streamlit as st
import base64

st.set_page_config(
    page_title="Thúy Hiền & Trần Dũng",
    page_icon="🌟",
    layout="centered",  # Options: "centered" or "wide"
    initial_sidebar_state="expanded")
#-----------------------------------------------------------------------------------------------------------
### gif from local file
# file_ = open("/Online/673427199f66a-330618_GIF.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
#     unsafe_allow_html=True,
# )

#-----------------------------------------------------------------------------------------------
# Bìa

st.image('./Online/bia.png')

#-----------------------------------------------------------------------------------------------
# Nhạc
# st.write('A Thousand Years - Christina Perri')
# st.audio("music.mp3", format="audio/mpeg", loop=True)

#-----------------------------------------------------------------------------------------------
# Thông tin

st.image('./Online/about1.png')

st.write('')

st.image('./Online/about2.png')
#-----------------------------------------------------------------------------------------------

st.header("Thiệp mời")

#-----------------------------------------------------------------------------------------------
# Thiệp
st.image('./Online/baohy1.png')

st.write('')

st.image('./Online/baohy3.png')

#-----------------------------------------------------------------------------------------------
# List of image URLs
image_urls = [
    "https://app.thesimple.vn/uploads/contact/customer67361aa1b3fcb.png", 
    "https://app.thesimple.vn/uploads/contact/customer67361a5dc7982.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a2ce5345.png",
    "https://app.thesimple.vn/uploads/contact/customer673619c6be898.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a77936f0.png"
    # "./image/image_1.jpg",
    # "./image/image1.png",
    # "./image/image3.png",
    # "./image/image4.png",
    # "./image/image5.png"

]

st.header("Ảnh cưới")


#------------------------------------

# st.write('################################################################################')


# Initialize session state for the current image index
if "current_image" not in st.session_state:
    st.session_state.current_image = 0

# Function to navigate images
def navigate_image(direction):
    if direction == "next":
        st.session_state.current_image = (st.session_state.current_image + 1) % len(image_urls)
    elif direction == "back":
        st.session_state.current_image = (st.session_state.current_image - 1) % len(image_urls)

current_image = image_urls[st.session_state.current_image]
st.image(current_image, use_container_width=True)

# Create columns layout: Left (for "Back"), Center (for image), Right (for "Next")
col1, col2, col3, col4 = st.columns([3,2,2,3])  # Adjust column ratios for spacing

# Left column: Back button
with col2:
    if st.button("Ảnh trước"):
        navigate_image("back")


# Right column: Next button
with col3:
    if st.button("Ảnh tiếp theo"):
        navigate_image("next")
#-----------------------------------------------------------------------------------------------
# Map
st.header('Bản đồ')
st.image('./Online/map-bao-hy1.png')

#-----------------------------------------------------------------------------------------------
# Lời cảm ơn
# mystyle = '''
#     <style>
#         p {
#             text-align: center;
#             font-size: 25px; /* Adjust size as needed, e.g., 20px, 50px */
#         }
#     </style>
#     '''
# st.markdown(mystyle, unsafe_allow_html=True)

# st.divider()

# st.markdown('''
# Kính gửi Quý Khách, chúng tôi xin chân thành cảm ơn Quý Khách đã dành thời gian đến tham dự đám cưới của chúng tôi. Sự có mặt của Quý Khách đã làm cho ngày trọng đại của chúng tôi thêm ý nghĩa và vui vẻ. Chúng tôi xin gửi lời chúc sức khỏe và hạnh phúc đến Quý Khách và Gia đình.
# ''')

# st.divider()

st.divider()
st.markdown('''
    <style>
        p {
            text-align: center;
        }
    </style>
    <p>
        Kính gửi Quý Khách, chúng tôi xin chân thành cảm ơn Quý Khách đã dành thời gian đến tham dự đám cưới của chúng tôi. 
        Sự có mặt của Quý Khách đã làm cho ngày trọng đại của chúng tôi thêm ý nghĩa và vui vẻ. 
        Chúng tôi xin gửi lời chúc sức khỏe và hạnh phúc đến Quý Khách và Gia đình.
    </p>
''', unsafe_allow_html=True)
st.divider()


#-----------------------------------------------------------------------------------------------
# Kết
st.image('./Online/6734271a2abeb-FOOTER202.png')

#-----------------------------------------------------------------------------------------------

# Path to your audio file
audio_file_path = "music.mp3"  # Replace with the path to your file

# Read the audio file
with open(audio_file_path, "rb") as audio_file:
    audio_bytes = audio_file.read()

# Convert audio to base64 for embedding
audio_base64 = base64.b64encode(audio_bytes).decode()

# Generate HTML for autoplay and loop audio
audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
"""

# Render the HTML
st.markdown(audio_html, unsafe_allow_html=True)




