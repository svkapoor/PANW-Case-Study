from journal.sentiment import analyze_sentiment

def test_analyze_sentiment_neutral_steadying():
    result = analyze_sentiment("This situation is steadying my senses")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_high_stress_collapsing():
    result = analyze_sentiment("I feel like I am collapsing under pressure")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_positive_high_energy_climbing():
    result = analyze_sentiment("I feel like I am climbing under pressure")
    assert result in ["positive_high_energy", "optimism"]

def test_analyze_sentiment_intense_too_much():
    result = analyze_sentiment("Everything feels too intense")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_intense_appropriate():
    result = analyze_sentiment("Everything feels appropriately intense")
    assert result in ["neutral", "positive_high_energy"]

def test_analyze_sentiment_fears_louder():
    result = analyze_sentiment("My fears keep getting louder")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_analyze_sentiment_positive_low_energy_fears_quieter():
    result = analyze_sentiment("My fears keep getting quieter")
    assert result in ["positive_low_energy", "neutral"]

def test_analyze_sentiment_world_closing():
    result = analyze_sentiment("I feel like the world is closing in on me")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_positive_low_energy_world_opening():
    result = analyze_sentiment("I feel like the world is opening up for me")
    assert result in ["positive_low_energy", "optimism"]

def test_analyze_sentiment_negative_high_stress_stress_worse():
    result = analyze_sentiment("My stress is getting worse")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_stress_easing():
    result = analyze_sentiment("My stress is easing off")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_uneasy_cannot_stop():
    result = analyze_sentiment("I cannot stop feeling uneasy")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_analyze_sentiment_neutral_no_longer_uneasy():
    result = analyze_sentiment("I no longer feel uneasy")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_high_stress_too_much_handle():
    result = analyze_sentiment("This moment feels too much to handle")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_analyze_sentiment_neutral_simple_handle():
    result = analyze_sentiment("This moment feels simple to handle")
    assert result in ["neutral", "positive_low_energy"]

def test_analyze_sentiment_negative_low_energy_drained():
    result = analyze_sentiment("I feel drained mentally")
    assert result in ["negative_low_energy", "negative_high_stress"]
from journal.sentiment import analyze_sentiment

def test_sentiment_overwhelmed_brain_fog():
    result = analyze_sentiment("My mind feels foggy and overwhelmed")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_centered_and_balanced():
    result = analyze_sentiment("I feel centered and balanced right now")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_energy_rising_today():
    result = analyze_sentiment("I feel my energy rising today")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_pressure_building():
    result = analyze_sentiment("I can feel the pressure building inside me")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_senses_relaxing():
    result = analyze_sentiment("My senses feel relaxed and slow today")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_tension_in_chest():
    result = analyze_sentiment("I feel tension tightening in my chest")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_soft_motivation():
    result = analyze_sentiment("I feel a soft sense of motivation")
    assert result in ["positive_low_energy", "positive_high_energy"]

def test_sentiment_nothing_feels_wrong():
    result = analyze_sentiment("Nothing feels wrong at the moment")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_nothing_feels_right():
    result = analyze_sentiment("Nothing feels right at the moment")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_building_confidence():
    result = analyze_sentiment("I feel confidence building inside me")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_energy_fading():
    result = analyze_sentiment("My energy is fading fast")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_grounded_clear():
    result = analyze_sentiment("I feel grounded and clear-headed")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_feeling_distant():
    result = analyze_sentiment("I feel distant from everything")
    assert result in ["negative_low_energy", "neutral"]

def test_sentiment_rush_of_focus():
    result = analyze_sentiment("I feel a rush of focus right now")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_pressure_spiking():
    result = analyze_sentiment("The pressure inside me is spiking")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_warmth_in_body():
    result = analyze_sentiment("I feel warmth spreading through my body")
    assert result in ["positive_low_energy", "positive_high_energy"]

def test_sentiment_slow_steady_day():
    result = analyze_sentiment("Today feels slow and steady")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_day_heavy():
    result = analyze_sentiment("Today feels heavy and exhausting")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_alert_and_ready():
    result = analyze_sentiment("I feel alert and ready to move")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_weight_on_shoulders():
    result = analyze_sentiment("It feels like there's weight on my shoulders")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_mind_quieting_down():
    result = analyze_sentiment("My mind is quieting down")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_mind_speeding_up():
    result = analyze_sentiment("My mind is speeding up too fast")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_clear_and_productive():
    result = analyze_sentiment("I feel clear and productive")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_sluggish_today():
    result = analyze_sentiment("I feel sluggish today")
    assert result in ["negative_low_energy", "neutral"]

def test_sentiment_intense_drive():
    result = analyze_sentiment("I feel an intense drive to get things done")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_small_glimmer_strength():
    result = analyze_sentiment("I feel a small glimmer of strength coming back")
    assert result in ["positive_low_energy", "positive_high_energy"]

def test_sentiment_spiraling_feelings():
    result = analyze_sentiment("My feelings feel like they're spiraling")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_stable_evening():
    result = analyze_sentiment("My mood feels stable this evening")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_rushed_and_uneasy():
    result = analyze_sentiment("I feel rushed and uneasy right now")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_soft_relief():
    result = analyze_sentiment("I feel a soft wave of relief")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_energized_for_day():
    result = analyze_sentiment("I feel energized for the day ahead")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_worn_down():
    result = analyze_sentiment("I feel worn down by everything")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_lighthearted():
    result = analyze_sentiment("I feel lighthearted today")
    assert result in ["positive_low_energy", "positive_high_energy"]

def test_sentiment_empty_inside():
    result = analyze_sentiment("I feel empty inside")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_strong_forward_momentum():
    result = analyze_sentiment("I feel strong forward momentum")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_dull_but_okay():
    result = analyze_sentiment("I feel dull today but it's okay")
    assert result in ["neutral", "negative_low_energy"]

def test_sentiment_caught_in_pressure():
    result = analyze_sentiment("I feel caught in a wave of pressure")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_in_tune_with_myself():
    result = analyze_sentiment("I feel in tune with myself")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_spike_of_energy():
    result = analyze_sentiment("I felt a spike of energy just now")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_fading_motivation():
    result = analyze_sentiment("My motivation is fading")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_high_focus_mode():
    result = analyze_sentiment("I feel like I'm in high focus mode")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_stuck_in_place():
    result = analyze_sentiment("I feel stuck in place")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_relaxed_and_unbothered():
    result = analyze_sentiment("I feel relaxed and unbothered")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_charged_up():
    result = analyze_sentiment("I feel completely charged up")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_close_to_burnout():
    result = analyze_sentiment("I feel close to burnout")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_soft_appreciation():
    result = analyze_sentiment("I feel a soft appreciation for everything today")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_happy_soft_emoji():
    result = analyze_sentiment("Feeling calm today 😊")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_happy_hype_emoji():
    result = analyze_sentiment("Let's go!! 🔥🔥")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_exhausted_emoji():
    result = analyze_sentiment("I'm so tired... 😩")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_overwhelmed_emoji():
    result = analyze_sentiment("Everything is too much rn 😣")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_peaceful_emoji():
    result = analyze_sentiment("Feeling peaceful 🌿")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_rising_energy_emoji():
    result = analyze_sentiment("Energy coming back ⚡")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_low_key_good_emoji():
    result = analyze_sentiment("lowkey feeling good 😌")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_brain_fried_emoji():
    result = analyze_sentiment("My brain is fried 😵‍💫")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_strong_drive_emoji():
    result = analyze_sentiment("Motivated as hell today 💪")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_unmotivated_emoji():
    result = analyze_sentiment("Zero motivation today 😔")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_anxious_but_you_removed_it():
    result = analyze_sentiment("Nervous but pushing through 😬")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_okay_emoji():
    result = analyze_sentiment("I'm okay 🙂")
    assert result in ["neutral", "positive_low_energy"]

def test_sentiment_dead_tired_emoji():
    result = analyze_sentiment("I feel dead tired 😪")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_on_edge_emoji():
    result = analyze_sentiment("I'm on edge rn 😖")
    assert result in ["negative_high_stress", "negative_low_energy"]

def test_sentiment_hyped_up_emoji():
    result = analyze_sentiment("I'M SO READY FOR TODAY 🚀")
    assert result in ["positive_high_energy", "positive_low_energy"]

def test_sentiment_soft_relief_emoji():
    result = analyze_sentiment("Ahh finally some relief 😮‍💨")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_neutral_blank_emoji():
    result = analyze_sentiment("meh 😐")
    assert result in ["neutral", "negative_low_energy"]

def test_sentiment_shutting_down_emoji():
    result = analyze_sentiment("My body is shutting down 😵")
    assert result in ["negative_low_energy", "negative_high_stress"]

def test_sentiment_slightly_better_emoji():
    result = analyze_sentiment("Feeling a tiny bit better 🙂‍↕️")
    assert result in ["positive_low_energy", "neutral"]

def test_sentiment_focus_mode_emoji():
    result = analyze_sentiment("Entering focus mode 🎯")
    assert result in ["positive_high_energy", "positive_low_energy"]
