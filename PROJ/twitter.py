import snscrape.modules.twitter as sntwitter
from cleantext import clean
import re

istenen = ["IRL", "JK", "LMAO", "LOL", "OMG", "ROFL", "SMH", "TBH", "YOLO", "YW", "TGIF", "Q&A", "FWIW", "HTH", "IMO", "FTW", "BRB", "BFF", "BTW", "FOMO", "TTYL", "IMHO", "ICYMI", "TMI", "NP", "AFK", "J/K", "YMMV", "ROTFL", "OOTD", "FTFY", "AFAIK", "OTOH", "IIRC", "TIL", "WTH", "WTF", "JD", "WYSIWYG", "GTG", "HBD", "IDC", "FAQ", "Totes Adorbs", "STFU", "TL;DR", "LMK", "NVM", "BYOB", "BOGO", "JW", "TBF", "RN", "FUBAR", "ISO", "BRT", "GG", "BFD", "DAE", "NGL", "BS", "IKR", "HMU", "WYD", "IDK", "IDGAF", "NBD", "TBA", "TBD", "ABT", "IYKYK", "B4", "BC", "JIC", "SNAFU", "G2G", "H8", "IYKWIM", "MYOB", "POV", "TLC", "W/E", "FWIF", "TW", "DM", "FB", "IG", "LI", "YT", "FF", "IM", "PM", "OP", "QOTD", "OOTD", "RT", "TBT", "TIL", "AMA", "ELI5", "FBF", "MFW", "HMU", "OOTD", "DM", "RT", "AMA", "CTA", "DYK", "FBF", "TBT", "BF", "GF", "BAE", "LYSM", "PDA", "LTR", "DTR", "LDR", "XOXO", "OTP", "LOML", "LMFAO", "R", "U", "ASAP", "IMY", "Lit", "Yeah", "Hows", "its", "hes", "nah", "Cmon", "Gonna", "Alr", "Hey", "Dude", "Bro", "Yo", "Sup", "Chill", "Sick", "Epic", "Bored", "Bae", "Swag", "Dope", "Flex", "Clout", "Squad", "Savage", "Salty", "Fam", "Shady", "Low-key", "High-key", "Janky", "Slay", "Hype", "Thirsty", "Fave"]

istenmeyen = ["Individual", "policy", "definition", "established", "approach", "significant", "resident", "construction", "elements", "conclusion", "consequences", "hence", "despite", "parameters", "undertaken", "precise", "whereas", "furthermore", "cited", "explicit", "aggregate", "underlying", "intervention", "quotation", "thereby", "clarity", "contemporary", "contradiction", "complement", "accompany", "via", "behalf", "diminished", "coherence", "whereby", "encountered", "forthcoming", "likewise", "nonetheless"]
all_tweets=[]
limit=1000

istenmeyen_kelime=""
for a in istenmeyen:
    istenmeyen_kelime = istenmeyen_kelime + " -" + a
for a in istenen:
    query = a + istenmeyen_kelime + " lang:en"
    #query = a + " lang:en"
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == limit:
            all_tweets.append(tweets)
            break
        else:
            tweets.append([tweet.content])

d = 1
with open('readme.txt', 'w') as f:
    for a in all_tweets:
        for e in a:
            for b in e:
                c = clean(b, no_emoji=True)

                c = re.sub('http://\S+|https://\S+', '',c)
                c = re.sub('@\S+', '', c)
                c = re.sub('\n', '', c)

                f.write(c)   
                f.write('\n')
                d = d + 1

