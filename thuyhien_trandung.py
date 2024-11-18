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
# Thiệp
st.image('./Online/baohy1.png')

st.write('')

st.image('./Online/baohy2.png')

#-----------------------------------------------------------------------------------------------
# List of image URLs
image_urls = [
    # "https://app.thesimple.vn/uploads/contact/customer67361aa1b3fcb.png",  # Replace with your image URLs
    # "https://app.thesimple.vn/uploads/contact/customer67361a5dc7982.png",
    # "https://app.thesimple.vn/uploads/contact/customer67361a2ce5345.png",
    # "https://app.thesimple.vn/uploads/contact/customer673619c6be898.png",
    # "https://app.thesimple.vn/uploads/contact/customer67361a77936f0.png",
    "./image/image_1.jpg",
    "./image/image1.jpg",
    "./image/image3.jpg",
    "./image/image4.jpg",
    "./image/image5.jpg"

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
#-----------------------------------------------------------------



