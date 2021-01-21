WICKET_TYPES = (
    ("C", "CAUGHT"),
    ("BOW", "BOWLED"),
    ("RO", "RUN OUT"),
    ("RETH", "RETIRED HURT"),
    ("RETO", "RETIRED OUT"),
    ("CBOWL", "CAUGHT & BOWLED"),
    ("CBEH", "CAUGHT BEHIND"),
    ("DNB", "DID NOT BAT"),
    ("NO", "NOT OUT"),
    ("HB", "HANDLED BALL"),
    ("HBT", "HIT BALL TWICE"),
    ("HW", "HIT WICKET"),
    ("LBW", "LBW"),
    ("OF", "OBSTRUCTING FIELD"),
    ("S", "STUMPED"),
    ("TO", "TIMED OUT"),
    ("U", "UNKNOWN"),
)

MATCH_TYPE = (
    ("F", "FRIENDLY"),
    ("L", "LEAGUE"),
    ("V", "VPCCL"),
    ("O", "OTHERS"),
    ("T", "TOUR"),
)

HOME_AWAY = (("H", "Home"), ("A", "Away"))

PLAYER_SKILLS = (
    ("BW", "BOWLER"),
    ("BT", "BATSMAN"),
    ("ALL", "ALL_ROUNDER"),
    ("WK", "WICKET_KEEPER"),
)

RESULT = (
    ("W", "Won"),
    ("L", "Lost"),
    ("N", "No Result"),
    ("T", "Drawn"),
    ("A", "Abandoned"),
    ("WO", "Walk Over"),
    ("P", "Postponded"),
    ("R", "Rained Off"),
    ("U", "Unknown"),
)

EVENT_FIRST = (("BAT", "Batted"), ("BOW", "Bowled"))


PLAYING_ROLES = (
    ("bo", "Bowler"),
    ("bat", "Batsman"),
    ("all", "All Rounder"),
    ("WK", "Wicket Keeper"),
)

BATTING_STYLES = (
    ("RHB", "Right-hand bat"),
    ("LHB", "Left-hand bat")
)

BOWLING_STYLES = (
    ("RAF", "Right-arm fast"),
    ("LAF", "Left-arm fast"),
    ("RAFM", "Right-arm fast-medium"),
    ( "LAFM", "Left-arm fast medium"),
    ("RALS", "Right-arm leg spin"),
    ("LALS", "Left-arm leg spin"),
    ( "RAOS", "Right-arm off spin"),
    ( "LAOS", "Left-arm off spin"),
)

APPOINTMENT_TYPES = (
    ("CAP", "Captain"),
    ("VCAP", "Vice Captain"),
    ("MCAP", "MidWeek Captain"),
    ("TRES", "Treasurer"),
    ("WEB", "Webmeister"),
    ("NET", "Netmeister"),
    ("FIX", "Fixturer"),
    ("DTOUR", "Domestic Tour Secretary"),
    ("ITOUR", "International Tour Secretary")
)