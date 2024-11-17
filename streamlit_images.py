import streamlit as st

# List of image URLs
image_urls = [
    "https://app.thesimple.vn/uploads/contact/customer67361aa1b3fcb.png",  # Replace with your image URLs
    "https://app.thesimple.vn/uploads/contact/customer67361a5dc7982.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a2ce5345.png",
    "https://app.thesimple.vn/uploads/contact/customer673619c6be898.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a77936f0.png",
    "./image/image_1.jpg"

]

st.header("Ảnh cưới")

st.title("Display Multiple Images")

# Display images
st.image(image_urls, width=300)


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
st.image(current_image, use_column_width=True)

# # Create columns layout: Left (for "Back"), Center (for image), Right (for "Next")
# col1, col2, col3, col4 = st.columns([3,2,2,3])  # Adjust column ratios for spacing

# # Left column: Back button
# with col2:
#     st.write("")  # Spacer for vertical alignment
#     if st.button("Back"):
#         navigate_image("back")


# # Right column: Next button
# with col3:
#     st.write("")  # Spacer for vertical alignment
#     if st.button("Next"):
#         navigate_image("next")

# Create columns layout: Left (for "Back"), Center (for image), Right (for "Next")
col1, col2= st.columns([1,1])  # Adjust column ratios for spacing


st.write('''<style>
[data-testid="column"] {
    width: calc(25% - 1rem) !important;
    flex: 1 1 calc(25% - 1rem) !important;
    min-width: calc(20% - 1rem) !important;
}
.css-1l269bu {max-width:20% !important;}
</style>''', unsafe_allow_html=True)

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



with col8:
    st.button("Button 4")

