import streamlit as st
import random
import time

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="Mystic's Gate Tarot", 
    page_icon="🔮",
    layout="wide"
)

# --- Full 78-Card Tarot Deck (with Placeholder Images) ---
# IMPORTANT: Replace these 'https://picsum.photos' links with the raw links 
# to your own images hosted on GitHub for a professional look.

TAROT_DECK = [
    # Major Arcana
    {"name": "The Fool", "meaning": "New beginnings, innocence, spontaneity.", "image_url": "https://picsum.photos/seed/the_fool/400/600"},
    {"name": "The Magician", "meaning": "Manifestation, resourcefulness, power.", "image_url": "https://picsum.photos/seed/the_magician/400/600"},
    {"name": "The High Priestess", "meaning": "Intuition, sacred knowledge, the subconscious.", "image_url": "https://picsum.photos/seed/the_high_priestess/400/600"},
    {"name": "The Empress", "meaning": "Femininity, beauty, nature, nurturing.", "image_url": "https://picsum.photos/seed/the_empress/400/600"},
    {"name": "The Emperor", "meaning": "Authority, structure, control, fatherhood.", "image_url": "https://picsum.photos/seed/the_emperor/400/600"},
    {"name": "The Hierophant", "meaning": "Tradition, conformity, morality, ethics.", "image_url": "https://picsum.photos/seed/the_hierophant/400/600"},
    {"name": "The Lovers", "meaning": "Love, harmony, relationships, choices.", "image_url": "https://picsum.photos/seed/the_lovers/400/600"},
    {"name": "The Chariot", "meaning": "Control, willpower, assertion, determination.", "image_url": "https://picsum.photos/seed/the_chariot/400/600"},
    {"name": "Strength", "meaning": "Courage, persuasion, influence, compassion.", "image_url": "https://picsum.photos/seed/strength/400/600"},
    {"name": "The Hermit", "meaning": "Introspection, solitude, inner guidance.", "image_url": "https://picsum.photos/seed/the_hermit/400/600"},
    {"name": "Wheel of Fortune", "meaning": "Luck, karma, life cycles, destiny.", "image_url": "https://picsum.photos/seed/wheel_of_fortune/400/600"},
    {"name": "Justice", "meaning": "Justice, fairness, truth, cause and effect.", "image_url": "https://picsum.photos/seed/justice/400/600"},
    {"name": "The Hanged Man", "meaning": "Suspension, restriction, letting go, sacrifice.", "image_url": "https://picsum.photos/seed/the_hanged_man/400/600"},
    {"name": "Death", "meaning": "Endings, beginnings, change, transformation.", "image_url": "https://picsum.photos/seed/death/400/600"},
    {"name": "Temperance", "meaning": "Balance, moderation, patience, purpose.", "image_url": "https://picsum.photos/seed/temperance/400/600"},
    {"name": "The Devil", "meaning": "Bondage, addiction, materialism, temptation.", "image_url": "https://picsum.photos/seed/the_devil/400/600"},
    {"name": "The Tower", "meaning": "Sudden change, upheaval, chaos, revelation.", "image_url": "https://picsum.photos/seed/the_tower/400/600"},
    {"name": "The Star", "meaning": "Hope, faith, purpose, rejuvenation.", "image_url": "https://picsum.photos/seed/the_star/400/600"},
    {"name": "The Moon", "meaning": "Illusion, fear, anxiety, subconscious.", "image_url": "https://picsum.photos/seed/the_moon/400/600"},
    {"name": "The Sun", "meaning": "Positivity, warmth, success, vitality.", "image_url": "https://picsum.photos/seed/the_sun/400/600"},
    {"name": "Judgement", "meaning": "Rebirth, inner calling, absolution.", "image_url": "https://picsum.photos/seed/judgement/400/600"},
    {"name": "The World", "meaning": "Completion, integration, accomplishment.", "image_url": "https://picsum.photos/seed/the_world/400/600"},
    
    # Suit of Wands
    {"name": "Ace of Wands", "meaning": "Inspiration, new opportunities, growth.", "image_url": "https://picsum.photos/seed/ace_of_wands/400/600"},
    {"name": "Two of Wands", "meaning": "Future planning, decisions, discovery.", "image_url": "https://picsum.photos/seed/two_of_wands/400/600"},
    {"name": "Three of Wands", "meaning": "Expansion, foresight, overseas opportunities.", "image_url": "https://picsum.photos/seed/three_of_wands/400/600"},
    {"name": "Four of Wands", "meaning": "Celebration, harmony, marriage, community.", "image_url": "https://picsum.photos/seed/four_of_wands/400/600"},
    {"name": "Five of Wands", "meaning": "Conflict, competition, disagreements.", "image_url": "https://picsum.photos/seed/five_of_wands/400/600"},
    {"name": "Six of Wands", "meaning": "Public recognition, victory, success.", "image_url": "https://picsum.photos/seed/six_of_wands/400/600"},
    {"name": "Seven of Wands", "meaning": "Challenge, protection, perseverance.", "image_url": "https://picsum.photos/seed/seven_of_wands/400/600"},
    {"name": "Eight of Wands", "meaning": "Speed, action, air travel, movement.", "image_url": "https://picsum.photos/seed/eight_of_wands/400/600"},
    {"name": "Nine of Wands", "meaning": "Resilience, courage, persistence, boundaries.", "image_url": "https://picsum.photos/seed/nine_of_wands/400/600"},
    {"name": "Ten of Wands", "meaning": "Burden, extra responsibility, hard work.", "image_url": "https://picsum.photos/seed/ten_of_wands/400/600"},
    {"name": "Page of Wands", "meaning": "Enthusiasm, exploration, creative spark.", "image_url": "https://picsum.photos/seed/page_of_wands/400/600"},
    {"name": "Knight of Wands", "meaning": "Energy, passion, adventure, impulsiveness.", "image_url": "https://picsum.photos/seed/knight_of_wands/400/600"},
    {"name": "Queen of Wands", "meaning": "Courage, confidence, determination, warmth.", "image_url": "https://picsum.photos/seed/queen_of_wands/400/600"},
    {"name": "King of Wands", "meaning": "Natural-born leader, vision, entrepreneurship.", "image_url": "https://picsum.photos/seed/king_of_wands/400/600"},
    
    # Suit of Cups
    {"name": "Ace of Cups", "meaning": "New love, compassion, creativity, emotion.", "image_url": "https://picsum.photos/seed/ace_of_cups/400/600"},
    {"name": "Two of Cups", "meaning": "Unified love, partnership, mutual attraction.", "image_url": "https://picsum.photos/seed/two_of_cups/400/600"},
    {"name": "Three of Cups", "meaning": "Celebration, friendship, community.", "image_url": "https://picsum.photos/seed/three_of_cups/400/600"},
    {"name": "Four of Cups", "meaning": "Apathy, contemplation, disconnectedness.", "image_url": "https://picsum.photos/seed/four_of_cups/400/600"},
    {"name": "Five of Cups", "meaning": "Loss, regret, disappointment, grief.", "image_url": "https://picsum.photos/seed/five_of_cups/400/600"},
    {"name": "Six of Cups", "meaning": "Nostalgia, childhood memories, reunion.", "image_url": "https://picsum.photos/seed/six_of_cups/400/600"},
    {"name": "Seven of Cups", "meaning": "Choices, illusions, fantasy, wishful thinking.", "image_url": "https://picsum.photos/seed/seven_of_cups/400/600"},
    {"name": "Eight of Cups", "meaning": "Walking away, disillusionment, withdrawal.", "image_url": "https://picsum.photos/seed/eight_of_cups/400/600"},
    {"name": "Nine of Cups", "meaning": "Wish fulfillment, comfort, happiness.", "image_url": "https://picsum.photos/seed/nine_of_cups/400/600"},
    {"name": "Ten of Cups", "meaning": "Divine love, harmonious relationships, family.", "image_url": "https://picsum.photos/seed/ten_of_cups/400/600"},
    {"name": "Page of Cups", "meaning": "Creative opportunities, intuition, messages of love.", "image_url": "https://picsum.photos/seed/page_of_cups/400/600"},
    {"name": "Knight of Cups", "meaning": "Romance, charm, 'knight in shining armor'.", "image_url": "https://picsum.photos/seed/knight_of_cups/400/600"},
    {"name": "Queen of Cups", "meaning": "Compassion, intuition, emotional stability.", "image_url": "https://picsum.photos/seed/queen_of_cups/400/600"},
    {"name": "King of Cups", "meaning": "Emotional balance, diplomacy, generosity.", "image_url": "https://picsum.photos/seed/king_of_cups/400/600"},
    
    # Suit of Swords
    {"name": "Ace of Swords", "meaning": "Breakthroughs, mental clarity, success.", "image_url": "https://picsum.photos/seed/ace_of_swords/400/600"},
    {"name": "Two of Swords", "meaning": "Stalemate, difficult decisions, avoidance.", "image_url": "https://picsum.photos/seed/two_of_swords/400/600"},
    {"name": "Three of Swords", "meaning": "Heartbreak, emotional pain, sorrow.", "image_url": "https://picsum.photos/seed/three_of_swords/400/600"},
    {"name": "Four of Swords", "meaning": "Rest, contemplation, meditation, recuperation.", "image_url": "https://picsum.photos/seed/four_of_swords/400/600"},
    {"name": "Five of Swords", "meaning": "Conflict, competition, defeat, betrayal.", "image_url": "https://picsum.photos/seed/five_of_swords/400/600"},
    {"name": "Six of Swords", "meaning": "Transition, moving on, passage.", "image_url": "https://picsum.photos/seed/six_of_swords/400/600"},
    {"name": "Seven of Swords", "meaning": "Deception, strategy, stealth, betrayal.", "image_url": "https://picsum.photos/seed/seven_of_swords/400/600"},
    {"name": "Eight of Swords", "meaning": "Self-imposed restriction, limitation, feeling trapped.", "image_url": "https://picsum.photos/seed/eight_of_swords/400/600"},
    {"name": "Nine of Swords", "meaning": "Anxiety, nightmares, fear, despair.", "image_url": "https://picsum.photos/seed/nine_of_swords/400/600"},
    {"name": "Ten of Swords", "meaning": "Painful endings, rock bottom, betrayal.", "image_url": "https://picsum.photos/seed/ten_of_swords/400/600"},
    {"name": "Page of Swords", "meaning": "Curiosity, thirst for knowledge, new ideas.", "image_url": "https://picsum.photos/seed/page_of_swords/400/600"},
    {"name": "Knight of Swords", "meaning": "Ambitious, action-oriented, fast-thinking.", "image_url": "https://picsum.photos/seed/knight_of_swords/400/600"},
    {"name": "Queen of Swords", "meaning": "Independent, unbiased judgement, clear boundaries.", "image_url": "https://picsum.photos/seed/queen_of_swords/400/600"},
    {"name": "King of Swords", "meaning": "Mental clarity, intellectual power, authority.", "image_url": "https://picsum.photos/seed/king_of_swords/400/600"},

    # Suit of Pentacles
    {"name": "Ace of Pentacles", "meaning": "New financial opportunity, manifestation.", "image_url": "https://picsum.photos/seed/ace_of_pentacles/400/600"},
    {"name": "Two of Pentacles", "meaning": "Balancing priorities, adaptability.", "image_url": "https://picsum.photos/seed/two_of_pentacles/400/600"},
    {"name": "Three of Pentacles", "meaning": "Teamwork, collaboration, skilled craft.", "image_url": "https://picsum.photos/seed/three_of_pentacles/400/600"},
    {"name": "Four of Pentacles", "meaning": "Security, conservation, possessiveness.", "image_url": "https://picsum.photos/seed/four_of_pentacles/400/600"},
    {"name": "Five of Pentacles", "meaning": "Financial loss, poverty, isolation.", "image_url": "https://picsum.photos/seed/five_of_pentacles/400/600"},
    {"name": "Six of Pentacles", "meaning": "Generosity, charity, giving and receiving.", "image": "https://picsum.photos/seed/six_of_pentacles/400/600"},
    {"name": "Seven of Pentacles", "meaning": "Patience, investment, long-term vision.", "image_url": "https://picsum.photos/seed/seven_of_pentacles/400/600"},
    {"name": "Eight of Pentacles", "meaning": "Apprenticeship, skill development, mastery.", "image_url": "https://picsum.photos/seed/eight_of_pentacles/400/600"},
    {"name": "Nine of Pentacles", "meaning": "Abundance, luxury, self-sufficiency.", "image_url": "https://picsum.photos/seed/nine_of_pentacles/400/600"},
    {"name": "Ten of Pentacles", "meaning": "Wealth, family legacy, financial security.", "image_url": "https://picsum.photos/seed/ten_of_pentacles/400/600"},
    {"name": "Page of Pentacles", "meaning": "Manifestation, financial opportunity, skill.", "image_url": "https://picsum.photos/seed/page_of_pentacles/400/600"},
    {"name": "Knight of Pentacles", "meaning": "Hard work, routine, diligence, reliability.", "image_url": "https://picsum.photos/seed/knight_of_pentacles/400/600"},
    {"name": "Queen of Pentacles", "meaning": "Nurturing, practical, financially stable.", "image_url": "https://picsum.photos/seed/queen_of_pentacles/400/600"},
    {"name": "King of Pentacles", "meaning": "Wealth, business, leadership, security.", "image_url": "https://picsum.photos/seed/king_of_pentacles/400/600"}
]


# --- Helper Function to Load Custom CSS ---
def load_css(file_name):
    """Loads a CSS file for styling."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"{file_name} file not found. App will run with default styling.")

# --- Main App Function ---
def run_tarot_app():
    """The main logic for the Tarot Reader app."""
    
    st.title("🌙 Your Personal Tarot Reading 🔮")
    st.markdown("---")
    
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
            if len(TAROT_DECK) < 3:
                st.error("Error: Not enough cards in the deck for this reading.")
                return

            # Use random.sample to pick 3 *unique* cards
            drawn_cards = random.sample(TAROT_DECK, 3)
            
            labels = ["Your Past", "Your Present", "Your Future"]
            
            # Display cards with animation
            cols = st.columns(3)
            for i, card in enumerate(drawn_cards):
                with cols[i]:
                    # Add a slight delay for dramatic effect
                    time.sleep(0.5) 
                    
                    # Apply CSS class for fade-in effect (defined in style.css)
                    st.markdown(f'<div class="card-container">', unsafe_allow_html=True)
                    st.image(card["image_url"], caption=card["name"], use_column_width=True)
                    st.markdown(f"**{labels[i]}: {card['name']}**")
                    st.write(card["meaning"])
                    st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.warning("Please provide your name and your question to draw the cards.")

# --- Execution ---
load_css("style.css")
run_tarot_app()
