import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from story_generator import generate_story
from database import init_db, log_submission, DB_FILE

def test_story_generation():
    print("--- Testing Story Generation ---")
    user = "Alice"
    crush = "Bob"
    answers = {
        "meet_place": "Coffee shop",
        "vibe": "Instant sparks",
        "first_conv": "Talked for hours",
        "realization": "You made them laugh",
        "first_date": "Karaoke night singing horribly out-of-tune duets",
        "challenge": "Surviving an escape room under extreme pressure"
    }
    
    # Generate story
    story = generate_story(user, crush, answers)
    
    assert len(story) == 5, f"Expected 5 stages, got {len(story)}"
    print("Stages generated successfully:")
    for stage, text in story.items():
        print(f"\n[{stage}]")
        print(text)
        assert user in text or user.lower() in text.lower(), f"User name missing from stage {stage}"
        assert crush in text or crush.lower() in text.lower(), f"Crush name missing from stage {stage}"
        
    print("\nStory generation validation: PASSED")

def test_database():
    print("\n--- Testing Database Logging ---")
    # Reset test db file if exists
    if os.path.exists(DB_FILE):
        try:
            os.remove(DB_FILE)
            print("Reset existing database for clean test.")
        except Exception as e:
            print(f"Could not remove DB file: {e}")
            
    init_db()
    assert os.path.exists(DB_FILE), "Database file was not created!"
    
    answers = {
        "meet_place": "Online",
        "vibe": "Awkward but cute",
        "first_conv": "Nervous small talk",
        "realization": "Love at first sight",
        "first_date": "Stargazing on a roof but it started pouring rain",
        "challenge": "Assembling Swedish flat-pack furniture"
    }
    
    success = log_submission("Juliet", "Romeo", answers, 98)
    assert success, "Database logging failed!"
    print("Database logging validation: PASSED")

if __name__ == "__main__":
    test_story_generation()
    test_database()
    print("\nAll tests completed successfully!")
