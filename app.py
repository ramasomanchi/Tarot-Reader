import streamlit as st
import random
import time

# --- Tarot Card Data (Simplified) ---
# In a real app, you'd have 78 cards. We'll use a small set for this example.
# You would also host your images online (e.g., on GitHub or Imgur)
TAROT_DECK = [
    {
        "name": "The Fool",
        "meaning": "New beginnings, innocence, spontaneity, faith, the unknown.",
        "image_url": "https-link-to-your-image-of-the-fool.jpg"
    },
    {
        "name": "The Magician",
        "meaning": "Manifestation, resourcefulness, power, inspired action.",
        "image_url": "https-link-to-your-image-of-the-magician.jpg"
    },
    {
        "name": "The High Priestess",
        "meaning": "Intuition, sacred knowledge, divine feminine, the subconscious mind.",
        "image_url": "https-link-to-your-image-of-the-high-priestess.jpg"
    },
    {
        "name": "The Lovers",
        "meaning": "Love, harmony, relationships, values alignment, choices.",
        "image_url": "https-link-to-your-image-of-the-lovers.jpg"
    },
    {
        "name": "Strength",
        "meaning": "Strength, courage, persuasion, influence, compassion.",
        "image_url": "https-link-to-your-image-of-strength.jpg"
    },
    {
        "name": "The Hermit",
        "meaning": "Introspection, soul-searching, inner guidance, solitude.",
        "image_url": "https-link-to-your-image-of-the-hermit.jpg"
    }
]

# --- Helper Function to Load Custom CSS ---
def load_css(file_name):
    """Loads a CSS file for styling."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- Main App Function ---
def run_tarot_app():
    """The main logic for the Tarot Reader app."""
    
    st.title("🌙 Your Personal Tarot Reading 🔮")
    
    # --- Individualization Inputs ---
    name = st.text_input("What is your name?")
    question = st.text_input("What question do you ask of the cards?")

    # --- The "Draw" Button ---
    if st.button("Reveal My Destiny"):
        if name and question:
            # Simple validation
            st.markdown(f"---")
            st.subheader(f"{name}, you asked: \"{question}\"")
            st.write("The cards have revealed this for you...")

            # --- Card Drawing Logic ---
            # A simple 3-card (Past, Present, Future) spread
            try:
                drawn_cards = random.sample(TAROT_DECK, 3)
            except ValueError:
                st.error("Error: Not enough cards in the deck for this reading.")
                return

            labels = ["Your Past", "Your Present", "Your Future"]
            
            # Display cards with animation
            cols = st.columns(3)
            for i, card in enumerate(drawn_cards):
                with cols[i]:
                    # Add a slight delay for dramatic effect
                    time.sleep(0.5) 
                    
                    # Apply CSS class for fade-in effect
                    st.markdown(f'<div class="card-container">', unsafe_allow_html=True)
                    st.image(card["image_url"], caption=card["name"], use_column_width=True)
                    st.markdown(f"**{labels[i]}: {card['name']}**")
                    st.write(card["meaning"])
                    st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.warning("Please provide your name and your question to draw the cards.")

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(page_title="Mystic's Gate", layout="wide")

# --- Load the Custom CSS ---
# This assumes you have a 'style.css' file in the same directory
try:
    load_css("style.css")
except FileNotFoundError:
    st.warning("style.css file not found. App will run with default styling.")

# --- Main Execution ---
# Now we call the main app function directly, no password check!
run_tarot_app()
