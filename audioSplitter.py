import pydub
import os

def minutesToMilliseconds(minutes, seconds):
    return ((minutes * 60) + seconds) * 1000

def main():
    fullSetPath = "C:\\Users\\kamil\\OneDrive\\Music\\Martin Garrix - Ultra 2024 (Full Set)\\MARTIN GARRIX LIVE @ ULTRA MUSIC FESTIVAL MIAMI 2024.wav"
    fullSet = pydub.AudioSegment.from_wav(fullSetPath)

    trimTimings = [
        {"start": (0, 0), "end": (2, 19), "title": "Martin Garrix & DubVision feat. Jaimes - Empty (Intro Edit)"},
        {"start": (2, 20), "end": (3, 49), "title": "ID - ID"},
        {"start": (3, 50), "end": (5, 19), "title": "Martin Garrix & Matisse & Sadko - Good Morning"},
        {"start": (5, 20), "end": (8, 46), "title": "Martin Garrix & MOTI - Virus"},
        {"start": (8, 47), "end": (11, 38), "title": "Eleganto - Express Yourself (ID)"},
        {"start": (11, 39), "end": (12, 53), "title": "070 Shakes - Cocoon (Martin Garrix & Space Ducks Remix)"},
        {"start": (12, 54), "end": (14, 44), "title": "Martin Garrix & Third Party - Lions In The Wild"},
        {"start": (14, 45), "end": (16, 29), "title": "Martin Garrix & Sentinal feat. Bonn vs Avicii - Hurricane vs Fade Into Darkness (Martin Garrix Mashup)"},
        {"start": (16, 30), "end": (18, 6), "title": "Martin Garrix & Third Party - Something To Believe In (ID)"},
        {"start": (18, 7), "end": (21, 45), "title": "Lewis Capaldi - Someone You Loved (Martin Garrix Remix)"},
        {"start": (21, 46), "end": (24, 36), "title": "Martin Garrix & Mesto feat. WILHELM - Breakaway"},
        {"start": (24, 37), "end": (26, 21), "title": "Martin Garrix & Zedd - Follow"},
        {"start": (26, 22), "end": (28, 59), "title": "AREA21 - Drinks Up (ID)"},
        {"start": (29, 0), "end": (31, 25), "title": "ALOK & The Chainsmokers ft. Mae Stephens vs Martin Garrix & Dua Lipa - Jungle (Arcando Remix) vs Scared To Be Lonely (Martin Garrix Mashup)"},
        {"start": (31, 26), "end": (32, 35), "title": "Martin Garrix & Mesto - Limitless"},
        {"start": (32, 36), "end": (34, 56), "title": "Avicii - Waiting For Love"},
        {"start": (34, 57), "end": (36, 33), "title": "Martin Garrix & DubVision feat. Shaun Farrugia - Starlight (Keep Me Afloat)"},
        {"start": (36, 34), "end": (40, 27), "title": "Martin Garrix feat. Bonn - High On Life"},
        {"start": (40, 28), "end": (42, 41), "title": "Dimitri Vegas, Martin Garrix, Like Mike - Tremor"},
        {"start": (42, 42), "end": (44, 55), "title": "Martin Garrix & Sem Vox - Gravity"},
        {"start": (44, 56), "end": (46, 17), "title": "Martin Garrix - Animals"},
        {"start": (46, 18), "end": (48, 50), "title": "Martin Garrix & Blinders vs Martin Garrix ft. Macklemore & Patrick Stump of Fall Out Boy - Breach vs Summer Days (Martin Garrix Mashup)"},
        {"start": (48, 51), "end": (50, 4), "title": "Julian Jordan - ID"},
        {"start": (50, 5), "end": (51, 48), "title": "Matisse & Sadko - ID"},
        {"start": (51, 49), "end": (54, 16), "title": "Alesso & Sentinel vs. Sander van Doorn & Martin Garrix & DVBBS & Aleesia - Interstellar vs. Gold Skies (Martin Garrix Mashup)"},
        {"start": (54, 17), "end": (57, 29), "title": "Martin Garrix & JVKE vs Kx5 & Hayla & John Summit -- Hero (DubVision Remix) vs Escape (Martin Garrix Mashup)"},
        {"start": (57, 30), "end": (60, 35), "title": "Martin Garrix & Bebe Rexha vs Martin Garrix & Blinders - In The Name Of Love vs Aurora (Martin Garrix Mashup)"},
        {"start": (60, 36), "end": (62, 21), "title": "Martin Garrix & DubVision feat. Jordan Grace - Oxygen"},
        {"start": (62, 22), "end": (65, 9), "title": "Martin Garrix & Third Party feat. Oaks & Declan J Donovan - Carry You"},
        {"start": (65, 10), "end": (69, 41), "title": "Martin Garrix & DubVision feat. Shaun Farrugia - Wherever You Are (ID) (Outro Edit)"}
        
    #     {"start": (0, 0), "end": (2, 15), "title": "Martin Garrix & DubVision ft. Jaimes - Empty (Intro Edit)"},
    #     {"start": (2, 16), "end": (4, 46), "title": "Matisse & Sadko & Sentinel - Once Again w/"},
    #     {"start": (4, 46), "end": (7, 11), "title": "Martin Garrix & Tiësto - The Only Way Is Up"},
    #     {"start": (5, 10), "end": (8, 45), "title": "Sebastian Ingrosso & Alesso & Ryan Tedder vs. Martin Garrix & Dua Lipa - Calling vs. Scared To Be Lonely (Martin Garrix Mashup) w/"},
    #     {"start": (8, 46), "end": (11, 37), "title": "ALOK & The Chainsmokers & Arcando vs. Martin Garrix & Dua Lipa - Jungle vs. Scared To Be Lonely (Martin Garrix Mashup)"},
    #     {"start": (11, 38), "end": (12, 52), "title": "Martin Garrix & Mesto - Limitless"},
    #     {"start": (12, 53), "end": (14, 42), "title": "070 Shake - Cocoon (Martin Garrix & Space Ducks Remix)"},
    #     {"start": (14, 43), "end": (16, 28), "title": "DubVision & Martin Garrix & Matisse & Sadko - Turn It Around vs. Break Through The Silence (Martin Garrix Mashup) w/"},
    #     {"start": (16, 29), "end": (18, 4), "title": "Tove Lo - Habits (Stay High) (Acapella)"},
    #     {"start": (18, 5), "end": (19, 23), "title": "Lewis Capaldi - Someone You Loved (Martin Garrix Remix)"},
    #     {"start": (19, 24), "end": (20, 59), "title": "Martin Garrix & Mesto ft. WILHELM - Breakaway"},
    #     {"start": (21, 0), "end": (24, 34), "title": "Martin Garrix - Animals w/"},
    #     {"start": (24, 35), "end": (25, 59), "title": "Martin Garrix & Vluarr & NEADU - New ID"},
    #     {"start": (26, 0), "end": (28, 58), "title": "Martin Garrix & Zedd ft. Emily Warren - Follow"},
    #     {"start": (28, 59), "end": (31, 25), "title": "Martin Garrix & Brooks & Icona Pop & Charli XCX - Quantum vs. I Love It (Martin Garrix Mashup)"},
    #     {"start": (31, 26), "end": (32, 28), "title": "Martin Garrix ft. Bonn - High on Life"},
    #     {"start": (32, 29), "end": (34, 25), "title": "Martin Garrix ft. Simon Aldred - Waiting For Love (Co-Prod. by Martin Garrix) w/"},
    #     {"start": (34, 26), "end": (40, 25), "title": "Martin Garrix vs. Dimitri Vegas & Like Mike vs. Avicii ft. Simon Aldred - Tremor vs. Waiting For Love (Martin Garrix Mashup)"},
    #     {"start": (40, 26), "end": (42, 46), "title": "Martin Garrix ft. Baby - BABYABADAM w/ Julian Jordan & Nova Blue Remix"},
    #     {"start": (42, 47), "end": (44, 52), "title": "Martin Garrix & MOTT ft. Jenny Wahlström - Virus (How About Now) w/"},
    #     {"start": (44, 53), "end": (46, 56), "title": "Martin Garrix & MOTT ft. Jenny Wahlström - Yottabyte vs. Virus (Martin Garrix Mashup)"},
    #     {"start": (46, 57), "end": (50, 9), "title": "Julian Jordan - ID"},
    #     {"start": (50, 10), "end": (51, 53), "title": "Martin Garrix & Sem Vox ft. Jaimes - Gravity"},
    #     {"start": (51, 54), "end": (54, 25), "title": "Martin Garrix & Third ≠ Party & Matt Joe - Something To Believe In (ID)"},
    #     {"start": (54, 26), "end": (57, 28), "title": "Martin Garrix & Blinders vs. Macklemore & Patrick Stump of Fall Out Boy - Summer Days w/"},
    #     {"start": (57, 29), "end": (60, 4), "title": "Third ≠ Party & Three ≠ Blanco - ID"},
    #     {"start": (60, 5), "end": (62, 18), "title": "Avicii ft. Zac Brown Band - Broken Arrows"},
    #     {"start": (62, 19), "end": (65, 9), "title": "Martin Garrix & Blinders vs. Martin Garrix ft. Shaun Farrugia - Starlight (Keep Me Afloat) w/"},
    #     {"start": (65, 10), "end": (69, 40), "title": "Martin Garrix ft. Bonn - High On Life (Acoustic) (PLEASE RELEASE MARTY<3)"}
    ]
    
    outputDirectory = "E:\\Music"
    os.makedirs(outputDirectory, exist_ok=True)

    for trim in trimTimings:
        startTime = minutesToMilliseconds(*trim["start"])
        endTime = minutesToMilliseconds(*trim["end"])
        title = trim["title"]

        audio = fullSet[startTime:endTime]

        tempAudioFile = f"{title}.wav"
        audio.export(tempAudioFile, format="wav")

main()