import streamlit as st
import random
import time

# --- Setup and Initialization ---

# Define the base URL for your images (UPDATE THIS)
# IMPORTANT: Replace 'coder123', 'tarot-app', and 'images' with your actual GitHub path
BASE_URL = "https://raw.githubusercontent.com/coder123/tarot-app/main/images"

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="Mystic's Gate Tarot", 
    page_icon="🔮",
    layout="wide"
)

# --- Full 78-Card Tarot Deck Structure ---
# NOTE: Ensure your image file names (e.g., 'the_fool.jpg') exist in your GitHub 'images' folder.

TAROT_DECK = [
    # Major Arcana
    {"name": "The Fool", "meaning": "New beginnings, innocence, spontaneity.", "image_url": f"{BASE_URL}/the_fool.jpg"},
    {"name": "The Magician", "meaning": "Manifestation, resourcefulness, power.", "image_url": f"{BASE_URL}/the_magician.jpg"},
    {"name": "The High Priestess", "meaning": "Intuition, sacred knowledge, the subconscious.", "image_url": f"{BASE_URL}/the_high_priestess.jpg"},
    {"name": "The Empress", "meaning": "Femininity, beauty, nature, nurturing.", "image_url": f"{BASE_URL}/the_empress.jpg"},
    {"name": "The Emperor", "meaning": "Authority, structure, control, fatherhood.", "image_url": f"{BASE_URL}/the_emperor.jpg"},
    {"name": "The Hierophant", "meaning": "Tradition, conformity, morality, ethics.", "image_url": f"{BASE_URL}/the_hierophant.jpg"},
    {"name": "The Lovers", "meaning": "Love, harmony, relationships, choices.", "image_url": f"{BASE_URL}/the_lovers.jpg"},
    {"name": "The Chariot", "meaning": "Control, willpower, assertion, determination.", "image_url": f"{BASE_URL}/the_chariot.jpg"},
    {"name": "Strength", "meaning": "Courage, persuasion, influence, compassion.", "image_url": f"{BASE_URL}/strength.jpg"},
    {"name": "The Hermit", "meaning": "Introspection, solitude, inner guidance.", "image_url": f"{BASE_URL}/the_hermit.jpg"},
    {"name": "Wheel of Fortune", "meaning": "Luck, karma, life cycles, destiny.", "image_url": f"{BASE_URL}/wheel_of_fortune.jpg"},
    {"name": "Justice", "meaning": "Justice, fairness, truth, cause and effect.", "image_url": f"{BASE_URL}/justice.jpg"},
    {"name": "The Hanged Man", "meaning": "Suspension, restriction, letting go, sacrifice.", "image_url": f"{BASE_URL}/the_hanged_man.jpg"},
    {"name": "Death", "meaning": "Endings, beginnings, change, transformation.", "image_url": f"{BASE_URL}/death.jpg"},
    {"name": "Temperance", "meaning": "Balance, moderation, patience, purpose.", "image_url": f"{BASE_URL}/temperance.jpg"},
    {"name": "The Devil", "meaning": "Bondage, addiction, materialism, temptation.", "image_url": f"{BASE_URL}/the_devil.jpg"},
    {"name": "The Tower", "meaning": "Sudden change, upheaval, chaos, revelation.", "image_url": f"{BASE_URL}/the_tower.jpg"},
    {"name": "The Star", "meaning": "Hope, faith, purpose, rejuvenation.", "image_url": f"{BASE_URL}/the_star.jpg"},
    {"name": "The Moon", "meaning": "Illusion, fear, anxiety, subconscious.", "image_url": f"{BASE_URL}/the_moon.jpg"},
    {"name": "The Sun", "meaning": "Positivity, warmth, success, vitality.", "image_url": f"{BASE_URL}/the_sun.jpg"},
    {"name": "Judgement", "meaning": "Rebirth, inner calling, absolution.", "image_url": f"{BASE_URL}/judgement.jpg"},
    {"name": "The World", "meaning": "Completion, integration, accomplishment.", "image_url": f"{BASE_URL}/the_world.jpg"},
    
    # Suit of Wands
    {"name": "Ace of Wands", "meaning": "Inspiration, new opportunities, growth.", "image_url": f"{BASE_URL}/ace_of_wands.jpg"},
    {"name": "Two of Wands", "meaning": "Future planning, decisions, discovery.", "image_url": f"{BASE_URL}/two_of_wands.jpg"},
    {"name": "Three of Wands", "meaning": "Expansion, foresight, overseas opportunities.", "image_url": f"{BASE_URL}/three_of_wands.jpg"},
    {"name": "Four of Wands", "meaning": "Celebration, harmony, marriage, community.", "image_url": f"{BASE_URL}/four_of_wands.jpg"},
    {"name": "Five of Wands", "meaning": "Conflict, competition, disagreements.", "image_url": f"{BASE_URL}/five_of_wands.jpg"},
    {"name": "Six of Wands", "meaning": "Public recognition, victory, success.", "image_url": f"{BASE_URL}/six_of_wands.jpg"},
    {"name": "Seven of Wands", "meaning": "Challenge, protection, perseverance.", "image_url": f"{BASE_URL}/seven_of_wands.jpg"},
    {"name": "Eight of Wands", "meaning": "Speed, action, air travel, movement.", "image_url": f"{BASE_URL}/eight_of_wands.jpg"},
    {"name": "Nine of Wands", "meaning": "Resilience, courage, persistence, boundaries.", "image_url": f"{BASE_URL}/nine_of_wands.jpg"},
    {"name": "Ten of Wands", "meaning": "Burden, extra responsibility, hard work.", "image_url": f"{BASE_URL}/ten_of_wands.jpg"},
    {"name": "Page of Wands", "meaning": "Enthusiasm, exploration, creative spark.", "image_url": f"{BASE_URL}/page_of_wands.jpg"},
    {"name": "Knight of Wands", "meaning": "Energy, passion, adventure, impulsiveness.", "image_url": f"{BASE_URL}/knight_of_wands.jpg"},
    {"name": "Queen of Wands", "meaning": "Courage, confidence, determination, warmth.", "image_url": f"{BASE_URL}/queen_of_wands.jpg"},
    {"name": "King of Wands", "meaning": "Natural-born leader, vision, entrepreneurship.", "image_url": f"{BASE_URL}/king_of_wands.jpg"},
    
    # Suit of Cups
    {"name": "Ace of Cups", "meaning": "New love, compassion, creativity, emotion.", "image_url": f"{BASE_URL}/ace_of_cups.jpg"},
    {"name": "Two of Cups", "meaning": "Unified love, partnership, mutual attraction.", "image_url": f"{BASE_URL}/two_of_cups.jpg"},
    {"name": "Three of Cups", "meaning": "Celebration, friendship, community.", "image_url": f"{BASE_URL}/three_of_cups.jpg"},
    {"name": "Four of Cups", "meaning": "Apathy, contemplation, disconnectedness.", "image_url": f"{BASE_URL}/four_of_cups.jpg"},
    {"name": "Five of Cups", "meaning": "Loss, regret, disappointment, grief.", "image_url": f"{BASE_URL}/five_of_cups.jpg"},
    {"name": "Six of Cups", "meaning": "Nostalgia, childhood memories, reunion.", "image_url": f"{BASE_URL}/six_of_cups.jpg"},
    {"name": "Seven of Cups", "meaning": "Choices, illusions, fantasy, wishful thinking.", "image_url": f"{BASE_URL}/seven_of_cups.jpg"},
    {"name": "Eight of Cups", "meaning": "Walking away, disillusionment, withdrawal.", "image_url": f"{BASE_URL}/eight_of_cups.jpg"},
    {"name": "Nine of Cups", "meaning": "Wish fulfillment, comfort, happiness.", "image_url": f"{BASE_URL}/nine_of_cups.jpg"},
    {"name": "Ten of Cups", "meaning": "Divine love, harmonious relationships, family.", "image_url": f"{BASE_URL}/ten_of_cups.jpg"},
    {"name": "Page of Cups", "meaning": "Creative opportunities, intuition, messages of love.", "image_url": f"{BASE_URL}/page_of_cups.jpg"},
    {"name": "Knight of Cups", "meaning": "Romance, charm, 'knight in shining armor'.", "image_url": f"{BASE_URL}/knight_of_cups.jpg"},
    {"name": "Queen of Cups", "meaning": "Compassion, intuition, emotional stability.", "image_url": f"{BASE_URL}/queen_of_cups.jpg"},
    {"name": "King of Cups", "meaning": "Emotional balance, diplomacy, generosity.", "image_url": f"{BASE_URL}/king_of_cups.jpg"},
    
    # Suit of Swords
    {"name": "Ace of Swords", "meaning": "Breakthroughs, mental clarity, success.", "image_url": f"{BASE_URL}/ace_of_swords.jpg"},
    {"name": "Two of Swords", "meaning": "Stalemate, difficult decisions, avoidance.", "image_url": f"{BASE_URL}/two_of_swords.jpg"},
    {"name": "Three of Swords", "meaning": "Heartbreak, emotional pain, sorrow.", "image_url": f"{BASE_URL}/three_of_swords.jpg"},
    {"name": "Four of Swords", "meaning": "Rest, contemplation, meditation, recuperation.", "image_url": f"{BASE_URL}/four_of_swords.jpg"},
    {"name": "Five of Swords", "meaning": "Conflict, competition, defeat, betrayal.", "image_url": f"{BASE_URL}/five_of_swords.jpg"},
    {"name": "Six of Swords", "meaning": "Transition, moving on, passage.", "image_url": f"{BASE_URL}/six_of_swords.jpg"},
    {"name": "Seven of Swords", "meaning": "Deception, strategy, stealth, betrayal.", "image_url": f"{BASE_URL}/seven_of_swords.jpg"},
    {"name": "Eight of Swords", "meaning": "Self-imposed restriction, limitation, feeling trapped.", "image_url": f"{BASE_URL}/eight_of_swords.jpg"},
    {"name": "Nine of Swords", "meaning": "Anxiety, nightmares, fear, despair.", "image_url": f"{BASE_URL}/nine_of_swords.jpg"},
    {"name": "Ten of Swords", "meaning": "Painful endings, rock bottom, betrayal.", "image_url": f"{BASE_URL}/ten_of_swords.jpg"},
    {"name": "Page of Swords", "meaning": "Curiosity, thirst for knowledge, new ideas.", "image_url": f"{BASE_URL}/page_of_swords.jpg"},
    {"name": "Knight of Swords", "meaning": "Ambitious, action-oriented, fast-thinking.", "image_url": f"{BASE_URL}/knight_of_swords.jpg"},
    {"name": "Queen of Swords", "meaning": "Independent, unbiased judgement, clear boundaries.", "image_url": f"{BASE_URL}/queen_of_swords.jpg"},
    {"name": "King of Swords", "meaning": "Mental clarity, intellectual power, authority.", "image_url": f"{BASE_URL}/king_of_swords.jpg"},

    # Suit of Pentacles
    {"name": "Ace of Pentacles", "meaning": "New financial opportunity, manifestation.", "image_url": f"{BASE_URL}/ace_of_pentacles.jpg"},
    {"name": "Two of Pentacles", "meaning": "Balancing priorities, adaptability.", "image_url": f"{BASE_URL}/two_of_pentacles.jpg"},
    {"name": "Three of Pentacles", "meaning": "Teamwork, collaboration, skilled craft.", "image_url": f"{BASE_URL}/three_of_pentacles.jpg"},
    {"name": "Four of Pentacles", "meaning": "Security, conservation, possessiveness.", "image_url": f"{BASE_URL}/four_of_pentacles.jpg"},
    {"name": "Five of Pentacles", "meaning": "Financial loss, poverty, isolation.", "image_url": f"{BASE_URL}/five_of_pentacles.jpg"},
    {"name": "Six of Pentacles", "meaning": "Generosity, charity, giving and receiving.", "image_url": f"{BASE_URL}/six_of_pentacles.jpg"},
    {"name": "Seven of Pentacles", "meaning": "Patience, investment, long-term vision.", "image_url": f"{BASE_URL}/seven_of_pentacles.jpg"},
    {"name": "Eight of Pentacles", "meaning": "Apprenticeship, skill development, mastery.", "image_url": f"{BASE_URL}/eight_of_pentacles.jpg"},
    {"name": "Nine of Pentacles", "meaning": "Abundance, luxury, self-sufficiency.", "image_url": f"{BASE_URL}/nine_of_pentacles.jpg"},
    {"name": "Ten of Pentacles", "meaning": "Wealth, family legacy, financial security.", "image_url": f"{BASE_URL}/ten_of_pentacles.jpg"},
    {"name": "Page of Pentacles", "meaning": "Manifestation, financial opportunity, skill.", "image_url": f"{BASE_URL}/page_of_pentacles.jpg"},
    {"name": "Knight of Pentacles", "meaning": "Hard work, routine, diligence, reliability.", "image_url": f"{BASE_URL}/knight_of_pentacles.jpg"},
    {"name": "Queen of Pentacles", "meaning": "Nurturing, practical, financially stable.", "image_url": f"{BASE_URL}/queen_of_pentacles.jpg"},
    {"name": "King of Pentacles", "meaning": "Wealth, business, leadership, security.", "image_url": f"{BASE_URL}/king_of_pentacles.jpg"}
]


# --- Helper Function to Load Custom CSS ---
def load_css(file_name):
    """Loads a CSS file for styling."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"{file_name} file not found. App will run with default styling.")

# --- Session State Management Initialization ---
if 'reading_active' not in st.session_state:
    st.session_state.reading_active = False
if 'drawn_cards' not in st.session_state:
    st.session_state.drawn_cards = []
if 'deck_remaining' not in st.session_state:
    # Shuffle and store the deck once per session
    shuffled_deck = list(TAROT_DECK)
    random.shuffle(shuffled_deck)
    st.session_state.deck_remaining = shuffled_deck
if 'pick_count' not in st.session_state:
    st.session_state.pick_count = 0

# --- State Functions ---

def start_reading():
    """Initializes a new reading session."""
    if st.session_state.name and st.session_state.question:
        st.session_state.reading_active = True
        st.session_state.drawn_cards = []
        st.session_state.pick_count = 0
        # Re-shuffle the deck for a fresh start
        shuffled_deck = list(TAROT_DECK)
        random.shuffle(shuffled_deck)
        st.session_state.deck_remaining = shuffled_deck
    else:
        st.warning("Please enter your name and question to begin.")

def pick_card():
    """Picks the next card from the top of the remaining deck."""
    if st.session_state.deck_remaining:
        # Get the next card from the top of the shuffled deck
        card = st.session_state.deck_remaining.pop(0) 
        st.session_state.drawn_cards.append(card)
        st.session_state.pick_count += 1
    else:
        st.error("The deck is empty!")

def reset_reading():
    """Resets the entire application state."""
    st.session_state.reading_active = False
    st.session_state.drawn_cards = []
    st.session_state.deck_remaining = []
    st.session_state.pick_count = 0
    # Force a full Rerun to clear input fields (FIXED: using st.rerun())
    st.rerun() 


# --- Main App Logic ---
def run_tarot_app():
    st.title("🌙 Your Personal Tarot Reading 🔮")
    st.markdown("---")
    
    # 1. Input Section
    # Check if inputs are initialized before accessing
    if 'name' not in st.session_state: st.session_state.name = ""
    if 'question' not in st.session_state: st.session_state.question = ""

    st.session_state.name = st.text_input("What is your name?", value=st.session_state.name, key="name_input")
    st.session_state.question = st.text_input("What question do you ask of the cards?", value=st.session_state.question, key="question_input")
    
    # 2. Start Button
    if st.button("Shuffle and Start Reading", disabled=st.session_state.reading_active, key="start_btn"):
        start_reading()

    # --- Interactive Reading Flow ---
    if st.session_state.reading_active:
        st.markdown(f"---")
        st.subheader(f"{st.session_state.name}, let your intuition guide you...")
        st.markdown(f"**Question:** *{st.session_state.question}*")
        
        # Check if the reading is complete
        if st.session_state.pick_count < 3:
            st.markdown(f"Click the card below to select **Card {st.session_state.pick_count + 1} of 3**.")
        
        # Card Selection Display (The interactive part)
        card_labels = ["Your Past (Card 1)", "Your Present (Card 2)", "Your Future (Card 3)"]
        
        # Display the slots for the three cards
        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                st.markdown(f"<div class='card-slot'>", unsafe_allow_html=True)
                
                if i < st.session_state.pick_count:
                    # Card has been picked - Show the result
                    card = st.session_state.drawn_cards[i]
                    st.markdown(f"<p style='color:#ffd700; font-weight:bold;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                    st.markdown(f'<div class="card-container">', unsafe_allow_html=True)
                    # We use a slight delay for visual drama on reveal
                    time.sleep(0.05) 
                    st.image(card["image_url"], caption=card["name"], use_column_width=True)
                    st.markdown(f"**Meaning:** {card['meaning']}")
                    st.markdown('</div>', unsafe_allow_html=True)
                
                elif i == st.session_state.pick_count and st.session_state.pick_count < 3:
                    # Current card to be picked - Show interactive card back
                    st.markdown(f"<p style='color:#ffd700; font-weight:bold;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                    
                    # You MUST have a 'card_back.jpg' image in your GitHub 'images' folder
                    card_back_url = f"{BASE_URL}/card_back.jpg" 
                    
                    # Streamlit trick: Use a button to handle the click action
                    if st.button(f"Pick Card {i+1}", key="pick-btn-action", use_container_width=True):
                        pick_card()
                        st.rerun() # FIXED: using st.rerun() to update the display
                        
                    st.image(card_back_url, caption="Click button to reveal", use_column_width=True)

                else:
                    # Card slot is empty - show placeholder
                    st.markdown(f"<p style='color:#888;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                    st.markdown('<div style="height: 350px; border: 1px dashed #444; border-radius: 8px;"></div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")

        # 3. Reading Complete Section
        if st.session_state.pick_count == 3:
            st.success("✨ Your **3-Card Reading** is Complete! ✨")
            st.markdown("Meditate on the meanings revealed above.")
            if st.button("Start New Reading", key="reset"):
                reset_reading()
    
# --- Execution ---
load_css("style.css")
run_tarot_app()
