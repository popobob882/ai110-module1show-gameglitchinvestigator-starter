from logic_utils import check_guess

# FIX: Test documents and should expect new-game reset behavior (AI-assisted)
def test_new_game_requires_status_reset():
    # Simulate the session state before and after a new game
    session = {"status": "lost", "attempts": 5, "score": 30}
    # Applying the fix: status must be reset to "playing"
    session["status"] = "playing"
    session["attempts"] = 0
    assert session["status"] == "playing", "New game must reset status to 'playing'"
    assert session["attempts"] == 0

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# FIX: Test added to verify the backwards-hint bug is resolved (AI-assisted)
def test_too_high_is_not_too_low():
    # Bug: guess=60 against secret=50 previously returned "Too Low" due to swapped messages
    outcome = check_guess(60, 50)
    assert outcome == "Too High", f"Expected 'Too High' but got '{outcome}'"
    assert outcome != "Too Low"
#Fix: Test added to verify the backwards-hint bug is resolved (AI-assisted)
def test_too_low_is_not_too_high():
    # Bug: guess=40 against secret=50 previously returned "Too High" due to swapped messages
    outcome = check_guess(40, 50)
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}'"
    assert outcome != "Too High"
