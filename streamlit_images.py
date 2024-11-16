import streamlit as st

# List of image URLs
image_urls = [
    "https://app.thesimple.vn/uploads/contact/customer67361aa1b3fcb.png",  # Replace with your image URLs
    "https://app.thesimple.vn/uploads/contact/customer67361a5dc7982.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a2ce5345.png",
    "https://app.thesimple.vn/uploads/contact/customer673619c6be898.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a77936f0.png"

]

st.title("Display Multiple Images")

# Display images
st.image(image_urls, width=300)


#------------------------------------

st.write('################################################################################')

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
st.image(current_image, use_column_width=True)

# Create columns layout: Left (for "Back"), Center (for image), Right (for "Next")
col1, col2 = st.columns([8, 1])  # Adjust column ratios for spacing

# Left column: Back button
with col1:
    st.write("")  # Spacer for vertical alignment
    if st.button("Back"):
        navigate_image("back")


# Right column: Next button
with col2:
    st.write("")  # Spacer for vertical alignment
    if st.button("Next"):
        navigate_image("next")
        

