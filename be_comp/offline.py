from sentiment import sentiment, sentiment_score
from model import predict
from trial import finBert

# url = "https://www.washingtonpost.com/world/2023/10/13/white-phosphorus-chemical-what-is/"
# url = "https://www.nst.com.my/business/economy/2023/10/966852/real-estate-developers-wary-mixed-bag-2024-budget" 
# "https://www.thestar.com.my/business/business-news/2023/03/27/bonds-are-back"
# "https://themalaysianreserve.com/2023/08/09/malaysias-export-decline-sparks-bond-market-volatility-fears/"

text, score, dummy = sentiment("https://www.thestar.com.my/business/business-news/2023/03/27/bonds-are-back")
print(text)
print(score)
# print(score)
# print(dummy)

# data = """
# KUALA LUMPUR: Foreign demand for Malaysian bonds may remain pressured in November ahead of the general elections (GE15), which could be exacerbated by a hung parliament situation.
# Kenanga Investment Bank Bhd, however, the local debt market may find some relief should there be a swift government formation and from the potential return of global risk-on sentiment following easing US inflationary pressures.
# The yields of Malaysian Government Securities (MGS) and Government Investment Issues (GII) increased this week, moving between 3.4 bps to 18.7 bps overall.
# The 10-year MGS yield rose by 14.2 bps to 4.48 per cent, whilst the 3-year MGS increased by 14.3 bps to 3.93 per cent.
# "Demand for govvies was mainly pressured this week, as investors digested Bank Negara Malaysia's recent rate hike and higher global bond yields and remained broadly cautious ahead of the GE15.
# "Meanwhile, foreign selling of Malaysian bonds intensified in October, down to RM6.3 billion, the largest foreign outflow since March 2020," the research firm said in a note.
# Kenanga said the domestic yields might trend lower next week, following a potentially strong third quarter (Q3) 2022 gross domestic product (GDP) released last week,  taking cues from falling US Treasury yields after the US mid-term elections and cooler inflation data.
# "Nonetheless, domestic market sentiment will likely remain cautious ahead of the GE15, which is on November 19," Kenanga noted.
# On the ringgit, Kenanga said the local note strengthened by almost 1.0 per cent against the US Dollar after trading above the 4.70 psychological threshold for 18 consecutive trading days, partly due to tightening domestic labour market conditions and sharp appreciation of the yuan.
# Kenanga said the local note might extend its gains due to potential double-digit growth in Malaysia's Q3 2022 GDP reading and further weakening of the USD index (DXY) amid cooler-than-expected US core inflation reading.
# "Despite a sharp correction in the DXY due to rising market expectations of a more dovish Fed, the ringgit may continue to rollercoaster between gains and losses and trade around the 4.64 – 4.72 zone amid heightened political risk ahead of the general election.
# "The direction of the volatile yuan may also influence the local note due to the uncertainty over China's zero-Covid-19 policy and the movement of the EUR, which hinges on the European Central Bank's stance on its monetary policy," Kenanga said.
# """

# score = finBert(data)
# print(score)
# print(predict(data))