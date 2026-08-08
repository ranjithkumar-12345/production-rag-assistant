from pathlib import Path
from typing import Dict, List, Any

def chunk_text(text:str,chunk_size:int,overlap:int):
    text : str
    chunk_size : int
    overlap : int
    chunks = []
    start = 0
    while  start < len(text):
        end = start+chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end -overlap
    return chunks


if __name__ == "__main__":

    chunk_size = 50
    over_lap = 5
    test =chunk_text("""   Task 1 
1. High-Fidelity Wireframes 
Frame Setup
Create a desktop frame: 1440 × 1024.
Background color: light gray (#F6F8FB) to match RecruitCRM.
Header Section
Left side:
Add a square logo placeholder (56×56, rounded corners).
Next to it, add Company Name (18px, bold).
Below name, add Company Meta Info (13px, muted gray).
Right side:
Place Quick Action Buttons:
“Log Call” (secondary style)
“Add Job” (primary blue button)
“Add Contact” (secondary style)
Keep them aligned horizontally with equal spacing.
Navigation Tabs (Sticky)
Directly below header, add horizontal tabs:
Overview | Jobs | Contacts | Candidates | Activities | Notes
Use RecruitCRM’s existing tab style: active tab = bold + underline (blue).
""",50,5)

print(test)