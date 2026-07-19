import random

def generate_story(user_name, crush_name, answers):
    """
    Generates a funny, sweet, randomized romantic comedy story in 5 stages.
    Returns a dictionary of stages: {stage_title: paragraph_text}
    """
    # Clean up name strings, capitalize them
    user = user_name.strip().title()
    crush = crush_name.strip().title()

    # 1. THE MEETING
    meet_place = answers.get("meet_place", "Coffee shop")
    meeting_templates = {
        "Coffee shop": [
            f"It was a crisp morning at the local coffee shop. {user} was trying to order a decaf oat milk latte when they noticed {crush} reading a book nearby, looking effortlessly cool.",
            f"At the crowded coffee shop, {user} grabbed a cup of hot chocolate, only to nearly collide with {crush}, who was holding three croissants like a professional juggler.",
            f"Inside the warm aroma of freshly ground coffee, {user} sat at the only empty table, unaware that {crush} was about to ask if the adjacent chair was taken with a dazzling smile."
        ],
        "College campus": [
            f"{user} was wandering around the campus, hopelessly lost on the way to a lecture, when {crush} kindly pointed them in the right direction—which was actually the opposite way, but it was the thought that counted.",
            f"Between lectures on a sunny campus afternoon, {user} was sitting on the grass when {crush} sat nearby, accidentally playing a loud meme video on their phone and laughing sheepishly.",
            f"It was finals week, and {user} was buried under a mountain of textbooks in the library. {crush} walked by, quietly sliding a pack of gummy bears onto {user}'s desk as a silent gesture of solidarity."
        ],
        "Through friends": [
            f"At a mutual friend's chaotic birthday party, {user} and {crush} were the only two people who preferred eating the snack platter in the quiet kitchen over dancing.",
            f"Introduced by well-meaning but meddlesome friends, {user} and {crush} found themselves standing awkwardly in a group circle, trying to make polite conversation before finding common ground in their shared hatred of pineapple on pizza.",
            f"It was a weekend barbecue when a mutual friend shouted, 'You two need to meet!' {user} and {crush} were pushed together, holding half-eaten paper plates of potato salad and exchanging amused glances."
        ],
        "Online": [
            f"In the vast wilderness of the internet, {user}'s funny post caught the attention of {crush}. One witty comment led to a direct message, and soon they were texting as if they had known each other for years.",
            f"A random algorithm-powered match brought {user} and {crush} together online. Their first chat was a debate about whether soup is a drink, setting the perfect chaotic tone for their future.",
            f"Scroll, scroll, match! {user} and {crush} connected online. What started as simple emojis escalated into late-night paragraph messages about their favorite childhood cartoons."
        ],
        "Random accident like bumping into them": [
            f"As if straight out of a movie script, {user} took a sharp turn around a street corner and literally bumped into {crush}, sending a shower of loose papers (and dignity) flying into the air.",
            f"It was a rainy afternoon when {user} tried to open an umbrella, only to accidentally poke {crush}'s backpack. In the ensuing flurry of apologies, a connection was born.",
            f"At the local grocery store, both reached for the very last box of double-chocolate cookies. Their fingers touched, and {user} let out an awkward squeak while {crush} chuckled."
        ]
    }
    
    # 2. THE EYE CONTACT
    vibe = answers.get("vibe", "Slow motion movie moment")
    eye_contact_templates = {
        "Slow motion movie moment": [
            f"As their eyes locked, the world around them slowed down. A non-existent violin track seemed to play in the background, and {user} forgot how to blink for a solid five seconds while staring at {crush}.",
            f"Their gaze met, and for a brief second, it felt like a romantic movie trailer. {crush} smiled, and {user} felt an inexplicable urge to flip their hair dramatically.",
            f"Time ground to a halt. The ambient noise faded, and {user} was convinced they could hear cinematic orchestra swells as {crush}'s eyes locked onto theirs."
        ],
        "Awkward but cute": [
            f"When their eyes met, {user} tried to give a cool nod, but it ended up looking like a sudden neck spasm. Thankfully, {crush} just giggled and waved back.",
            f"They locked eyes, and both immediately looked down, then looked up again at the exact same time, realizing they were both caught staring. It was peak awkwardness between {user} and {crush}, and it was absolutely adorable.",
            f"{user} attempted a sophisticated wink, but closed both eyes instead. {crush} laughed, finding {user}'s pure dorkiness incredibly endearing."
        ],
        "Instant sparks": [
            f"The moment they looked at each other, a bolt of electricity shot through the room. {user} felt a sudden rush of butterflies doing acrobatics in their stomach as {crush} held their gaze.",
            f"There was an instant, unmistakable spark. {crush}'s eyes shone with a mischievous glint that told {user} their life was about to get a lot more interesting.",
            f"It was an electric connection. When their eyes met, {user}'s heart did a mini-backflip, and {crush}'s face flushed with a subtle, warm blush."
        ],
        "Total coincidence": [
            f"They happened to look up at the exact same moment. It was a total coincidence, but the prolonged eye contact made {user} wonder if the universe was dropping a massive hint about them and {crush}.",
            f"By pure chance, their eyes aligned across the room. {crush} offered a polite smile, while {user} tried to look very busy examining a nearby fire extinguisher.",
            f"It was a complete accident that their paths of sight crossed. Yet, the split-second of eye contact with {crush} lingered just long enough to make {user}'s pulse quicken."
        ]
    }

    # 3. THE FIRST CONVERSATION
    first_conv = answers.get("first_conv", "Talked for hours")
    first_conv_templates = {
        "Talked for hours": [
            f"What was supposed to be a quick hello turned into an epic marathon of words. {user} and {crush} talked for hours, covering everything from childhood dreams to their hyper-specific conspiracy theories about pigeons.",
            f"Time seemed to lose all meaning for the two of them. {user} and {crush} chatted endlessly about favorite movies, music, and food. Before they knew it, the staff were putting chairs on tables, but neither wanted the conversation to end.",
            f"They clicked instantly. The conversation flowed like a river, drifting from light banter to deep secrets, leaving both {user} and {crush} completely captivated."
        ],
        "Nervous small talk": [
            f"The conversation began with exceptionally nervous small talk. {user} commented on the high quality of oxygen in the room, which {crush} surprisingly agreed with, laughing off the tension.",
            f"{user} cleared their throat and asked {crush} about the weather, to which {crush} replied with a nervous stutter. They both laughed, realizing they were both equally terrified of saying the wrong thing.",
            f"There were lots of 'ums' and 'uhs,' but the nervous energy was charming. {user} stumbled over their words, and {crush} kept twisting their sleeves, building a sweet, tentative bridge of connection between them."
        ],
        "One of you spilled coffee": [
            f"In a display of classic clumsy romance, {user} gestured a bit too enthusiastically and sent their coffee splashing right toward {crush}. As they both rushed to clean it up, their hands brushed, turning a mess into a memory.",
            f"{crush} took a sip and, in a moment of pure shock at a funny joke {user} made, did a minor spit-take with their drink. They were both red-faced but laughing hysterically.",
            f"A stray elbow sent a beverage tumbling down. The frantic grab for napkins resulted in {user} and {crush} bumping heads, making them laugh so hard they forgot about the stain."
        ],
        "Exchanged numbers immediately": [
            f"There was no time to waste. Within three minutes of talking, {user} boldly suggested they swap numbers, and {crush} happily agreed, saving the contact info with a heart emoji.",
            f"After sharing just a few words, {crush} pulled out their phone and said, 'Let's skip the small talk—give me your number.' {user}'s heart skipped a beat.",
            f"Recognizing an instant connection, {user} handed over their phone. {crush} typed in their number and immediately sent a silly selfie to establish contact."
        ]
    }

    # 4. FALLING FOR EACH OTHER
    realization = answers.get("realization", "You made them laugh")
    first_date = answers.get("first_date", "Fancy dinner where a dog ate your steak")
    challenge = answers.get("challenge", "Assembling Swedish flat-pack furniture")

    realization_phrases = {
        "You made them laugh": [
            f"{crush} truly fell for {user} during a moment when {user} made a terrible pun, and instead of groaning, {crush} laughed so hard they snorted.",
            f"It was {user}'s quirky sense of humor that did it. {crush} realized they were hooked when they couldn't stop smiling at {user}'s jokes long after they parted."
        ],
        "A grand gesture": [
            f"The turning point came when {user} performed a grand gesture—which was actually just holding an umbrella over {crush} in a storm while getting completely soaked themselves.",
            f"{crush} realized their feelings when {user} drove across town at midnight just to deliver a specific type of ice cream that {crush} had offhandedly mentioned craving."
        ],
        "Slowly over time": [
            f"It wasn't a single moment, but rather a slow realization. {crush} noticed how {user} remembered their favorite snacks and always knew how to brighten their day.",
            f"Like a slow-burn romance, feelings deepened over weeks. {crush} woke up one day and realized {user} had become the very first person they wanted to share all their news with."
        ],
        "Love at first sight": [
            f"It was love at first sight for {crush}, who later confessed that they were completely smitten from the very first second they saw {user}.",
            f"There was no doubt from day one. {crush} knew right away that {user} was someone incredibly special, a feeling that only grew stronger with time."
        ]
    }

    first_date_phrases = {
        "Fancy dinner where a dog ate your steak": [
            f"This bond was cemented on their first date: a fancy dinner that went awry when a stray golden retriever wandered into the patio and ate {user}'s steak right off the plate.",
            f"Their first date was a high-end restaurant where they tried to look sophisticated, until a sneaky dog stole {user}'s gourmet steak, forcing them to finish the night sharing a single plate of fries."
        ],
        "Amusement park where one of you got stuck on a ride": [
            f"Their bond was tested on their first date at the amusement park, where they got stuck on the Ferris wheel for two hours, sharing secrets (and a single bag of cotton candy) at the very top.",
            f"A first date at the amusement park took a turn when the roller coaster halted midway. Being suspended in the air for an hour allowed {user} and {crush} to talk about everything, conquering their fears together."
        ],
        "Stargazing on a roof but it started pouring rain": [
            f"Their first date was a romantic rooftop stargazing attempt, which quickly turned into a wet t-shirt contest when a sudden rainstorm drenched them. They ended up eating damp sandwiches in a stairwell.",
            f"Hoping for a magical night of stargazing, they were caught in a torrential downpour. Dripping wet and shivering, they ran for cover and realized that even in a storm, they were having the time of their lives."
        ],
        "Karaoke night singing horribly out-of-tune duets": [
            f"Their first date was a wild karaoke night where they sang horribly out-of-tune duets of 80s love ballads, earning cheers from the bartender and laughs from each other.",
            f"They braved a crowded karaoke bar for their first date. Singing a duet of 'Total Eclipse of the Heart' completely off-key, {user} and {crush} became the stars of the pub."
        ]
    }

    challenge_phrases = {
        "Assembling Swedish flat-pack furniture": [
            f"They proved their ultimate compatibility by successfully assembling a complex Swedish flat-pack bookshelf together, surviving the trial with only three leftover screws and their relationship intact.",
            f"Nothing says true love like flat-pack furniture. They spent an afternoon wrestling with Allen keys and confusing diagrams, laughing at the upside-down shelf and proving they make a perfect team."
        ],
        "Surviving an escape room under extreme pressure": [
            f"They conquered a major milestone: escaping a high-pressure escape room with only 12 seconds left on the clock, thanks to {user}'s quick thinking and {crush}'s puzzle-solving skills.",
            f"Locked in a room with a fake bomb ticking, their teamwork shone. {crush} solved the riddles while {user} kept their cool, escaping just in time and celebrating with high-fives."
        ],
        "Cooking a complex recipe that ended in ordering pizza": [
            f"They faced the kitchen challenge of cooking a five-course meal from scratch, which ended in a smoky kitchen, a minor fire alarm incident, and happily ordering a large pepperoni pizza instead.",
            f"Attempting a gourmet French recipe, they accidentally set off the smoke detector. As the kitchen cleared, {user} and {crush} sat on the floor eating delivery pizza, feeling closer than ever."
        ],
        "Meeting the quirky in-laws for the first time": [
            f"They braved the daunting challenge of meeting each other's eccentric families, standing united in the face of embarrassing childhood photo albums and strange family traditions.",
            f"Surviving the first family dinner was a true triumph. From dealing with quirky uncles to answering rapid-fire questions, {user} and {crush} held hands under the table, knowing they could face anything."
        ]
    }

    # Pick a random template and format
    realization_text = random.choice(realization_phrases[realization])
    date_text = random.choice(first_date_phrases[first_date])
    challenge_text = random.choice(challenge_phrases[challenge])

    falling_text = f"{realization_text} {date_text} Soon after, they faced a true test of their partnership: {challenge_text}"

    # 5. HAPPILY EVER AFTER
    happily_templates = [
        f"Today, {user} and {crush} are inseparable. They still argue about who loves whom more (and who is the better driver), but one thing is certain: their love story is one for the ages—or at least, one that will make a great romantic comedy someday. And they lived happily ever after!",
        f"From that chaotic start to this very day, {user} and {crush} have been writing their own rules. With a love built on laughter, shared inside jokes, and an occasional spilled drink, they are ready for whatever adventure comes next. The end is just the beginning of their happily ever after!",
        f"Looking back, it's clear the universe knew exactly what it was doing. {user} and {crush} continue to make each other laugh, support one another through thick and thin, and prove that sometimes, the cheesiest love stories are the best ones of all. Here's to their beautiful journey ahead!"
    ]
    happily_text = random.choice(happily_templates)

    return {
        "The Meeting": random.choice(meeting_templates[meet_place]),
        "The Eye Contact": random.choice(eye_contact_templates[vibe]),
        "The First Conversation": random.choice(first_conv_templates[first_conv]),
        "Falling for Each Other": falling_text,
        "Happily Ever After": happily_text
    }
