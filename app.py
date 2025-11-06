import streamlit as st
import random
import time

# --- Setup and Initialization ---

# Card Back Emojis/Symbols (Used when card is face down)
CARD_BACK_SYMBOL = "🔮" 

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="Mystic's Gate Tarot", 
    page_icon="🔮",
    layout="wide"
)

# --- Helper Function to Create Card Data ---
def create_card_data(name, suit, value, meaning_upright, meaning_reversed):
    """Creates a dictionary for a tarot card with both upright and reversed meanings, using suit/value for rendering."""
    return {
        "name": name,
        "suit": suit,
        "value": value,
        "meaning_upright": meaning_upright,
        "meaning_reversed": meaning_reversed
    }

# --- Full 78-Card Tarot Deck Structure ---
TAROT_DECK = [
    # --- Major Arcana (22 Cards) ---
    create_card_data("The Fool", "Major Arcana", "0", 
        "New beginnings, innocence, spontaneity, a leap of faith.", 
        "Recklessness, being taken advantage of, fear of change, poor judgement."
    ),
    create_card_data("The Magician", "Major Arcana", "I", 
        "Manifestation, resourcefulness, power, inspired action.", 
        "Manipulation, poor planning, dormant talents, deception."
    ),
    create_card_data("The High Priestess", "Major Arcana", "II", 
        "Intuition, sacred knowledge, the subconscious, divine feminine.", 
        "Secrets, repressed intuition, withdrawal, confusion, silence."
    ),
    create_card_data("The Empress", "Major Arcana", "III", 
        "Femininity, beauty, nature, nurturing, abundance.", 
        "Creative block, dependence on others, smothering, barrenness."
    ),
    create_card_data("The Emperor", "Major Arcana", "IV", 
        "Authority, structure, control, fatherhood, leadership.", 
        "Tyranny, rigidity, domination, excessive control, lack of discipline."
    ),
    create_card_data("The Hierophant", "Major Arcana", "V", 
        "Tradition, conformity, morality, ethics, spiritual wisdom.", 
        "Rebellion, non-conformity, new approaches, restriction."
    ),
    create_card_data("The Lovers", "Major Arcana", "VI", 
        "Love, harmony, relationships, choices, union.", 
        "Disharmony, imbalance, misalignment of values, avoidance of commitment."
    ),
    create_card_data("The Chariot", "Major Arcana", "VII", 
        "Control, willpower, assertion, determination, victory.", 
        "Lack of control, opposition, lack of direction, self-defeat."
    ),
    create_card_data("Strength", "Major Arcana", "VIII", 
        "Courage, persuasion, influence, compassion, inner strength.", 
        "Self-doubt, weakness, lack of control, raw emotion."
    ),
    create_card_data("The Hermit", "Major Arcana", "IX", 
        "Introspection, solitude, inner guidance, searching for truth.", 
        "Isolation, loneliness, withdrawal, misguided guidance."
    ),
    create_card_data("Wheel of Fortune", "Major Arcana", "X", 
        "Luck, karma, life cycles, destiny, change.", 
        "Bad luck, disruption, out of control, setbacks."
    ),
    create_card_data("Justice", "Major Arcana", "XI", 
        "Justice, fairness, truth, cause and effect, legal matters.", 
        "Unfairness, lack of accountability, legal complications, bias."
    ),
    create_card_data("The Hanged Man", "Major Arcana", "XII", 
        "Suspension, restriction, letting go, sacrifice, new perspective.", 
        "Stalling, resistance, martyrdom, inability to move on."
    ),
    create_card_data("Death", "Major Arcana", "XIII", 
        "Endings, beginnings, change, transformation, transition.", 
        "Resistance to change, stagnation, fear of the inevitable."
    ),
    create_card_data("Temperance", "Major Arcana", "XIV", 
        "Balance, moderation, patience, purpose, harmony.", 
        "Imbalance, excess, conflicting interests, lack of self-control."
    ),
    create_card_data("The Devil", "Major Arcana", "XV", 
        "Bondage, addiction, materialism, temptation, shadow self.", 
        "Releasing chains, breaking free, overcoming addiction, freedom."
    ),
    create_card_data("The Tower", "Major Arcana", "XVI", 
        "Sudden change, upheaval, chaos, revelation, destruction.", 
        "Fear of disaster, averting disaster, delaying the inevitable."
    ),
    create_card_data("The Star", "Major Arcana", "XVII", 
        "Hope, faith, purpose, rejuvenation, inspiration.", 
        "Hopelessness, despair, lack of inspiration, feeling lost."
    ),
    create_card_data("The Moon", "Major Arcana", "XVIII", 
        "Illusion, fear, anxiety, subconscious, intuition.", 
        "Release of fear, clarity, finding the truth, confusion."
    ),
    create_card_data("The Sun", "Major Arcana", "XIX", 
        "Positivity, warmth, success, vitality, joy.", 
        "Lack of enthusiasm, temporary unhappiness, clouded vision."
    ),
    create_card_data("Judgement", "Major Arcana", "XX", 
        "Rebirth, inner calling, absolution, assessment.", 
        "Self-doubt, refusal to self-evaluate, procrastination, feeling judged."
    ),
    create_card_data("The World", "Major Arcana", "XXI", 
        "Completion, integration, accomplishment, travel, fulfillment.", 
        "Lack of completion, short-cuts, delay, unfulfilled potential."
    ),

    # --- Suit of Wands (14 Cards) ---
    create_card_data("Ace of Wands", "Wands", "Ace", "Inspiration, new opportunities, growth.", "Lack of motivation, feeling burned out, delayed projects."),
    create_card_data("Two of Wands", "Wands", "2", "Future planning, decisions, discovery.", "Fear of the unknown, lack of confidence, lack of planning."),
    create_card_data("Three of Wands", "Wands", "3", "Expansion, foresight, overseas opportunities.", "Obstacles, delays, feeling let down, miscommunication."),
    create_card_data("Four of Wands", "Wands", "4", "Celebration, harmony, home, marriage.", "Instability, transition, lack of support, broken promises."),
    create_card_data("Five of Wands", "Wands", "5", "Conflict, competition, disagreements.", "Avoidance of conflict, tension, finding peace, fear of losing."),
    create_card_data("Six of Wands", "Wands", "6", "Public recognition, victory, success.", "Egotism, public shame, fall from grace, lack of recognition."),
    create_card_data("Seven of Wands", "Wands", "7", "Challenge, protection, perseverance.", "Giving up, feeling overwhelmed, yielding to pressure."),
    create_card_data("Eight of Wands", "Wands", "8", "Speed, action, air travel, movement.", "Delays, resisting change, slow progress, frustration."),
    create_card_data("Nine of Wands", "Wands", "9", "Resilience, courage, persistence.", "Defensiveness, paranoia, burden, walls coming down."),
    create_card_data("Ten of Wands", "Wands", "10", "Burden, extra responsibility, hard work.", "Avoiding responsibility, carrying too much, release of burden."),
    create_card_data("Page of Wands", "Wands", "Page", "Enthusiasm, exploration, creative spark.", "Lack of enthusiasm, poor news, creative block, pessimism."),
    create_card_data("Knight of Wands", "Wands", "Knight", "Energy, passion, adventure, impulsiveness.", "Impetuosity, haste, recklessness, feeling stuck."),
    create_card_data("Queen of Wands", "Wands", "Queen", "Courage, confidence, determination, warmth.", "Selfishness, demanding, temperamental, lack of focus."),
    create_card_data("King of Wands", "Wands", "King", "Natural-born leader, vision, entrepreneurship.", "Ruthlessness, tyrannical, power-hungry, unrealistic expectations."),

    # --- Suit of Cups (14 Cards) ---
    create_card_data("Ace of Cups", "Cups", "Ace", "New love, compassion, creativity, emotion.", "Repressed emotions, emotional turmoil, emptiness, unrequited love."),
    create_card_data("Two of Cups", "Cups", "2", "Unified love, partnership, mutual attraction.", "Break-up, conflict, imbalance in a relationship, separation."),
    create_card_data("Three of Cups", "Cups", "3", "Celebration, friendship, community, joy.", "Gossip, overindulgence, isolation, betrayal of trust."),
    create_card_data("Four of Cups", "Cups", "4", "Apathy, contemplation, disconnectedness.", "Clarity, realization, choosing happiness, new opportunities."),
    create_card_data("Five of Cups", "Cups", "5", "Loss, regret, disappointment, grief.", "Acceptance, moving on, recovery, finding hope."),
    create_card_data("Six of Cups", "Cups", "6", "Nostalgia, childhood memories, reunion.", "Living in the past, stagnation, immaturity, missed opportunity."),
    create_card_data("Seven of Cups", "Cups", "7", "Choices, illusions, fantasy, wishful thinking.", "Clarity of purpose, groundedness, decisive action."),
    create_card_data("Eight of Cups", "Cups", "8", "Walking away, disillusionment, withdrawal.", "Avoidance of necessary departure, fear of change, stagnation."),
    create_card_data("Nine of Cups", "Cups", "9", "Wish fulfillment, comfort, happiness.", "Greed, materialism, dissatisfaction, ill-health."),
    create_card_data("Ten of Cups", "Cups", "10", "Divine love, harmonious relationships, family.", "Broken family, divorce, emotional isolation, lack of inner peace."),
    create_card_data("Page of Cups", "Cups", "Page", "Creative opportunities, intuition, messages of love.", "Emotional immaturity, bad news, creative block, shyness."),
    create_card_data("Knight of Cups", "Cups", "Knight", "Romance, charm, 'knight in shining armor'.", "Moodiness, disappointment, jealousy, coldness, illusion."),
    create_card_data("Queen of Cups", "Cups", "Queen", "Compassion, intuition, emotional stability.", "Emotional martyrdom, insecurity, manipulation, emotional overload."),
    create_card_data("King of Cups", "Cups", "King", "Emotional balance, diplomacy, generosity.", "Emotional manipulation, secrecy, mood swings, dishonesty."),

    # --- Suit of Swords (14 Cards) ---
    create_card_data("Ace of Swords", "Swords", "Ace", "Breakthroughs, mental clarity, success.", "Confusion, lack of focus, destructive force, intellectual poverty."),
    create_card_data("Two of Swords", "Swords", "2", "Stalemate, difficult decisions, avoidance.", "Release, clarity, choosing a side, indecision."),
    create_card_data("Three of Swords", "Swords", "3", "Heartbreak, emotional pain, sorrow, betrayal.", "Forgiveness, recovery, finding hope, moving past the pain."),
    create_card_data("Four of Swords", "Swords", "4", "Rest, contemplation, meditation, recuperation.", "Restlessness, burnout, slow recovery, lack of inner peace."),
    create_card_data("Five of Swords", "Swords", "5", "Conflict, competition, defeat, betrayal.", "Reconciliation, resolution, moving on, loss of face."),
    create_card_data("Six of Swords", "Swords", "6", "Transition, moving on, passage, travel.", "Stuck in the past, resistance to change, emotional baggage."),
    create_card_data("Seven of Swords", "Swords", "7", "Deception, strategy, stealth, betrayal.", "Coming clean, integrity, confession, admitting failure."),
    create_card_data("Eight of Swords", "Swords", "8", "Self-imposed restriction, limitation, feeling trapped.", "Freedom, release, new perspective, finding a way out."),
    create_card_data("Nine of Swords", "Swords", "9", "Anxiety, nightmares, fear, despair.", "Inner peace, release from fear, getting help, finding solutions."),
    create_card_data("Ten of Swords", "Swords", "10", "Painful endings, rock bottom, betrayal.", "Recovery, regeneration, inevitable end, survival."),
    create_card_data("Page of Swords", "Swords", "Page", "Curiosity, thirst for knowledge, new ideas.", "Unforeseen obstacles, idle talk, verbal abuse, intellectual immaturity."),
    create_card_data("Knight of Swords", "Swords", "Knight", "Ambitious, action-oriented, fast-thinking.", "Impatience, poor judgement, hasty action, aggression."),
    create_card_data("Queen of Swords", "Swords", "Queen", "Independent, unbiased judgement, clear boundaries.", "Bitterness, coldness, cruel honesty, emotional distance."),
    create_card_data("King of Swords", "Swords", "King", "Mental clarity, intellectual power, authority.", "Quiet tyranny, abuse of power, manipulation, emotional detachment."),

    # --- Suit of Pentacles (14 Cards) ---
    create_card_data("Ace of Pentacles", "Pentacles", "Ace", "New financial opportunity, manifestation.", "Missed opportunity, financial setback, poor investment."),
    create_card_data("Two of Pentacles", "Pentacles", "2", "Balancing priorities, adaptability, flexibility.", "Imbalance, financial stress, prioritizing incorrectly."),
    create_card_data("Three of Pentacles", "Pentacles", "3", "Teamwork, collaboration, skilled craft, effort.", "Lack of teamwork, mediocrity, poor quality work, disjointed effort."),
    create_card_data("Four of Pentacles", "Pentacles", "4", "Security, conservation, possessiveness, control.", "Releasing control, generosity, financial openness, loss of security."),
    create_card_data("Five of Pentacles", "Pentacles", "5", "Financial loss, poverty, isolation, insecurity.", "Recovery, new job, spiritual poverty, overcoming hardship."),
    create_card_data("Six of Pentacles", "Pentacles", "6", "Generosity, charity, giving and receiving.", "Debt, stinginess, unfairness, conditional giving."),
    create_card_data("Seven of Pentacles", "Pentacles", "7", "Patience, investment, long-term vision, profit.", "Lack of patience, poor investment, sudden loss, failure to persevere."),
    create_card_data("Eight of Pentacles", "Pentacles", "8", "Apprenticeship, skill development, mastery, diligence.", "Perfectionism, monotony, lack of motivation, hasty work."),
    create_card_data("Nine of Pentacles", "Pentacles", "9", "Abundance, luxury, self-sufficiency, security.", "Loss of financial independence, theft, reckless spending."),
    create_card_data("Ten of Pentacles", "Pentacles", "10", "Wealth, family legacy, financial security, stability.", "Family conflict, financial failure, instability, inheritance issues."),
    create_card_data("Page of Pentacles", "Pentacles", "Page", "Manifestation, financial opportunity, skill, focus.", "Lack of follow-through, bad news about money, daydreaming."),
    create_card_data("Knight of Pentacles", "Pentacles", "Knight", "Hard work, routine, diligence, reliability.", "Sloth, laziness, stagnation, perfectionism to the point of delay."),
    create_card_data("Queen of Pentacles", "Pentacles", "Queen", "Nurturing, practical, financially stable, domestic.", "Self-centeredness, insecurity, neglecting home or self."),
    create_card_data("King of Pentacles", "Pentacles", "King", "Wealth, business, leadership, security.", "Greed, corruption, excessive materialism, failure to invest.")
]


# --- Spread Definitions ---
SPREAD_DEFINITIONS = {
    "Three-Card Spread (Past, Present, Future)": {
        "count": 3,
        "labels": ["Your Past (Card 1)", "Your Present (Card 2)", "Your Future (Card 3)"]
    },
    # Celtic Cross spread definition will be added in the next step
}

# --- Helper Functions ---
def load_css(file_name):
    """Loads a CSS file for styling."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"{file_name} file not found. App will run with default styling.")

def draw_card_with_orientation():
    """Picks a card and randomly assigns an upright or reversed orientation."""
    if st.session_state.deck_remaining:
        card_data = st.session_state.deck_remaining.pop(0) 
        
        is_reversed = random.choice([True, False]) 
        
        # Combine data for the drawn card
        drawn_card = {
            "name": card_data["name"],
            "suit": card_data["suit"],
            "value": card_data["value"],
            "is_reversed": is_reversed,
            "meaning": card_data["meaning_reversed"] if is_reversed else card_data["meaning_upright"],
            "orientation": "Reversed" if is_reversed else "Upright"
        }
        return drawn_card
    return None

def render_card_face(card, width_px="200px", height_px="350px"):
    """Generates the CSS/HTML to display the stylized card face."""
    
    # Map suits to emojis and CSS class for color/border
    suit_map = {
        "Major Arcana": ("⭐", "major"),
        "Wands": ("🔥", "wands"),
        "Cups": ("💧", "cups"),
        "Swords": ("⚔️", "swords"),
        "Pentacles": ("💰", "pentacles")
    }
    
    emoji, css_class = suit_map.get(card["suit"], ("?", "default"))
    
    # Apply rotation class if reversed
    rotation_class = "card-reversed" if card["is_reversed"] else ""
    
    html = f"""
    <div class='generated-card-face {css_class} {rotation_class}' 
         style='width: {width_px}; height: {height_px};'>
        <div class='card-title-top'>{card["value"]}</div>
        <div class='card-name'>{card["name"]}</div>
        <div class='card-suit-center'>{emoji}</div>
        <div class='card-title-bottom'>{card["value"]}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


# --- Session State Management Initialization ---
if 'reading_active' not in st.session_state:
    st.session_state.reading_active = False
if 'drawn_cards' not in st.session_state:
    st.session_state.drawn_cards = []
if 'deck_remaining' not in st.session_state:
    shuffled_deck = list(TAROT_DECK)
    random.shuffle(shuffled_deck)
    st.session_state.deck_remaining = shuffled_deck
if 'pick_count' not in st.session_state:
    st.session_state.pick_count = 0
if 'selected_spread' not in st.session_state:
    st.session_state.selected_spread = "Three-Card Spread (Past, Present, Future)"

# --- State Functions ---

def start_reading():
    """Initializes a new reading session."""
    spread_info = SPREAD_DEFINITIONS[st.session_state.selected_spread]
    
    if st.session_state.name_input and st.session_state.question_input:
        st.session_state.reading_active = True
        st.session_state.drawn_cards = []
        st.session_state.pick_count = 0
        shuffled_deck = list(TAROT_DECK)
        random.shuffle(shuffled_deck)
        st.session_state.deck_remaining = shuffled_deck
        st.session_state.total_cards = spread_info["count"] 
    else:
        st.warning("Please enter your name and question to begin.")

def pick_card():
    """Picks the next card using the new drawing logic."""
    card = draw_card_with_orientation()
    if card:
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
    st.rerun() 

def generate_deep_dive(reading_name, question, cards):
    """Generates a cohesive interpretation based on the drawn cards."""
    
    # Simple, hard-coded synthesis for the 3-card spread (Past, Present, Future)
    if len(cards) < 3:
        return 

    past_card = cards[0]
    present_card = cards[1]
    future_card = cards[2]

    st.subheader("💡 Deep Dive Reading Insight")
    st.markdown(f"***{reading_name}, regarding your question: '{question}'***")

    interpretation = (
        f"Your reading begins with the **{past_card['name']} ({past_card['orientation']})** in the Past position. "
        f"This suggests a foundation built on: *{past_card['meaning']}*. "
        f"In your present situation, the **{present_card['name']} ({present_card['orientation']})** indicates a focus on: *{present_card['meaning']}*. "
        f"This combination of past influences and present energy directs the current flow towards the future, "
        f"where the **{future_card['name']} ({future_card['orientation']})** suggests a likely outcome of: *{future_card['meaning']}*. "
        "Focus on the balance of the past card, present card, and future card energies to find your path forward."
    )
    st.info(interpretation)


# --- Main App Logic ---
def run_tarot_app():
    st.title("🌙 Your Personal Tarot Reading 🔮")
    st.markdown("---")
    
    # 1. Input Section
    col_spread, col_name, col_question = st.columns([1, 1.5, 2])

    with col_spread:
        st.session_state.selected_spread = st.selectbox(
            "Select Your Spread",
            list(SPREAD_DEFINITIONS.keys()),
            key="spread_select",
            disabled=st.session_state.reading_active
        )
    
    with col_name:
        st.text_input("What is your name?", key="name_input")
    
    with col_question:
        st.text_input("What question do you ask of the cards?", key="question_input")
    
    current_spread = SPREAD_DEFINITIONS[st.session_state.selected_spread]
    
    # 2. Start Button
    if st.button("Shuffle and Start Reading", disabled=st.session_state.reading_active, key="start_btn", use_container_width=True):
        start_reading()

    # --- Interactive Reading Flow ---
    if st.session_state.reading_active:
        st.markdown(f"---")
        st.subheader(f"{st.session_state.name_input}, let your intuition guide you...")
        st.markdown(f"**Question:** *{st.session_state.question_input}*")
        
        total_cards = current_spread["count"]
        card_labels = current_spread["labels"]
        
        if st.session_state.pick_count < total_cards:
            st.markdown(f"Click the card below to select **Card {st.session_state.pick_count + 1} of {total_cards}**.")
        
        cols = st.columns(3)
        for i in range(total_cards):
            
            if i < 3: # Logic for 3-card layout
                with cols[i]:
                    st.markdown(f"<div class='card-slot'>", unsafe_allow_html=True)
                    
                    if i < st.session_state.pick_count:
                        # Card has been picked - Show the result
                        card = st.session_state.drawn_cards[i]
                        
                        st.markdown(f"<p style='color:#ffd700; font-weight:bold;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                        st.markdown(f'<div class="card-container">', unsafe_allow_html=True)
                        
                        render_card_face(card)
                        
                        st.markdown(f"**Orientation:** {card['orientation']}")
                        st.markdown(f"**Meaning:** {card['meaning']}")
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    elif i == st.session_state.pick_count:
                        # Current card to be picked - Show interactive card back
                        st.markdown(f"<p style='color:#ffd700; font-weight:bold;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                        
                        if st.button(f"Pick Card {i+1}", key=f"pick-btn-{i}", use_container_width=True):
                            pick_card()
                            st.rerun() 
                            
                        # RENDER CARD BACK
                        st.markdown(f"""
                        <div class='card-back-placeholder'>
                            {CARD_BACK_SYMBOL}
                        </div>
                        """, unsafe_allow_html=True)

                    else:
                        # Card slot is empty - show placeholder
                        st.markdown(f"<p style='color:#888;'>{card_labels[i]}</p>", unsafe_allow_html=True)
                        st.markdown('<div class="empty-card-slot" style="height: 350px; border: 1px dashed #444; border-radius: 8px;"></div>', unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")

        # 3. Reading Complete Section
        if st.session_state.pick_count == total_cards:
            st.success(f"✨ Your **{st.session_state.selected_spread}** is Complete! ✨")
            generate_deep_dive(
                st.session_state.name_input, 
                st.session_state.question_input, 
                st.session_state.drawn_cards
            )
            st.markdown("Meditate on the meanings revealed above.")
            if st.button("Start New Reading", key="reset"):
                reset_reading()
    
# --- Execution ---
load_css("style.css")
run_tarot_app()
