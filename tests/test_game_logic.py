from logic_utils import check_guess

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
