import streamlit as st

# List of image URLs
image_urls = [
    "https://app.thesimple.vn/uploads/contact/customer67361aa1b3fcb.png",  # Replace with your image URLs
    "https://app.thesimple.vn/uploads/contact/customer67361a5dc7982.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a2ce5345.png",
    "https://app.thesimple.vn/uploads/contact/customer673619c6be898.png",
    "https://app.thesimple.vn/uploads/contact/customer67361a77936f0.png"

]

# st.title("Display Multiple Images")

# # Display images
# st.image(image_urls, width=300)


#------------------------------------

# st.write('################################################################################')

columns = """
<style>
    div.container {
        display: flex;
        flex-flow: row wrap;
        gap: 2em;
        align-items: flex-start;
        align-content: flex-start;
        justify-content: flex-start;
    }
    div.item {
        flex: 1 1 auto;
    }
</style>
<div class="container">
    <div class="item">
        <table>
        <tr><th>alpha beta</th><th>gamma delta</th><th>epsilon zeta</th></tr>
        <tr><td>123</td><td>456</td><td>789</td></tr>
        </table>
    </div>
    <div class="item">
        <table>
        <tr><th>eta theta</th><th>iota kappa</th><th>lambda mu</th></tr>
        <tr><td>123</td><td>456</td><td>789</td></tr>
        </table>
    </div>
</div>
"""

st.markdown(columns, unsafe_allow_html=True)

def fix_mobile_columns():    
    st.write('''<style>
    [data-testid="column"] {
        width: calc(16.6666% - 1rem) !important;
        flex: 1 1 calc(16.6666% - 1rem) !important;
        min-width: calc(16.6666% - 1rem) !important;
    }
    </style>''', unsafe_allow_html=True)

fix_mobile_columns()

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
col6, col7= st.columns([1,1])  # Adjust column ratios for spacing

# Left column: Back button
with col6:
    st.write("")  # Spacer for vertical alignment
    if st.button("Back"):
        navigate_image("back")


# Right column: Next button
with col7:
    st.write("")  # Spacer for vertical alignment
    if st.button("Next"):
        navigate_image("next")



