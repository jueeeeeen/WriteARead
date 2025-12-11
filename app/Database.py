from app.models.Book import Book
from app.models.Chapter import Chapter
from app.models.Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from app.models.Promotion import CoinPromotion
from app.models.Reader import Reader, Writer
from app.Controller import Controller
from app.models.CoinTransaction import CoinTransaction
from app.models.ChapterTransaction import ChapterTransaction

from datetime import datetime, date, timedelta

write_a_read = Controller()

#user
Mo = Writer("Mozaza", "12345678", "12/05/2000")
Jin = Writer("Jinzaza", "12345678", "01/01/2005")
Pint = Reader("Pintzaza", "12345678", "01/01/2005")
Pang = Reader("Pangzaza", "12345678", "01/01/2004")

#add user
write_a_read.add_writer(Mo)
write_a_read.add_writer(Jin)
write_a_read.add_reader(Pint)
write_a_read.add_reader(Pang)

#prologue
shin_chan_prologue = "Shin Chan is a 50-year-old boy"
doraemon_prologue = "Doraemon, Noby, and their three friends are sucked into a portal during a heavy storm and transported to the village of Natura. It becomes apparent that the gadgets Doraemon usually carries, that could potentially save them and return them to the present, are all missing."
sailor_moon_prologue = "A 14-year-old underachieving young schoolgirl named Usagi Tsukino meets a magical talking cat named Luna. Luna gives Usagi the ability to transform into a magical alter ego — Sailor Moon — tasked with locating the moon princess and battling the evil forces of the Dark Kingdom."
orv_prologue = "A novel called Three Ways to Survive in a Ruined World (written by the anonymous author tls123) has been written and published over the course of a decade, and Kim Dokja is the sole reader who has followed it to its ending. When the real world is plunged into the premise of Ways of Survival, Kim Dokja's unique knowledge of the novel becomes vital to his survival."
naruto_prologue = "A powerful fox known as the Nine-Tails attacks Konoha, the hidden leaf village in the Land of Fire, one of the Five Great Shinobi Countries in the Ninja World. In response, the leader of Konoha and the Fourth Hokage, Minato Namikaze, at the cost of his life, seals the fox inside the body of his newborn son, Naruto Uzumaki, making him a host of the beast."

#book
write_a_read.create_book("Shin chan", "Mola", "Mozaza", "adventure", "publishing", False, shin_chan_prologue) #1
write_a_read.create_book("Shinnosuke", "Mola", "Mozaza", "comedy", "publishing", True, shin_chan_prologue) #2
write_a_read.create_book("Doraemon", "Jina", "Jinzaza", "comedy", "publishing", False, doraemon_prologue) #3
write_a_read.create_book("Doraemon Special", "Jina", "Jinzaza", "adventure", "publishing", False, doraemon_prologue) #4
write_a_read.create_book("Sailor moon", "Jinny", "Jinzaza", "fantasy", "publishing", True, sailor_moon_prologue) #5
write_a_read.create_book("Sailor moon Special", "Jinny", "Jinzaza", "fantasy", "publishing", False, sailor_moon_prologue) #6
write_a_read.create_book("Omniscient readers viewpoint", "MolaMola", "Mozaza", "sci-fi", "publishing", True, orv_prologue) #7
write_a_read.create_book("Omniscient readers viewpoint Special", "MolaMola", "Mozaza", "sci-fi", "publishing", False, orv_prologue) #8
write_a_read.create_book("Naruto", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #9
write_a_read.create_book("Naruto Special", "Moeiei", "Mozaza", "adventure", "publishing", False, naruto_prologue) #10

shin_chan_chapter_1 = "While playing at the local park, Shinnosuke & his 4 friends Kazama, Nene, Masao & Bo encounter an woman named Tamiko, who claims to be Shinnosuke's would-be-wife from future. She states that in 20 years into the future Shinnosuke had been converted into a stone statue by Tamiko's father, but before being converted into stone, Shinnosuke asked Tamiko to bring his 5 year old self. Tamiko takes the five 5-year old children into the future via a time machine in order to save the adult Shinnosuke. After reaching the future, Tamiko is ambushed by the men employed by his father Masuzo Kaneari, who took her back to her house. The children seek refuge at the Shinnosuke's house. Here they meet Shinnosuke's parents Hiroshi & Misae.\n To Be continue...\n please buy next chapter"

# chapter
write_a_read.create_chapter("Shin chan", "1", "Shin chan first ch", shin_chan_chapter_1, 184)
write_a_read.create_chapter("Shin chan", "2", "Shin chan second ch", "this is the second chapter of shincha", 200)
write_a_read.create_chapter("Shin chan", "3", "Shin chan third ch", "this is the third chapter of shincha", 300)
write_a_read.create_chapter("Shinnosuke", "1", "Shinnosuke first ch", "this is the first chapter of shincha", 184)
write_a_read.create_chapter("Doraemon", "1", "Doraemon first ch", "this is the first chapter of Doraemon", 0)
write_a_read.create_chapter("Doraemon Special", "1", "Doraemon Special first ch", "this is the first chapter of Doraemon Special", 500)
write_a_read.create_chapter("Doraemon Special", "2", "Doraemon Special second ch", "this is the second chapter of Doraemon Special", 500)
write_a_read.create_chapter("Sailor moon", "1", "Sailor moon first ch", "this is the first chapter of Sailor moon", 0)
write_a_read.create_chapter("Sailor moon Special", "1", "Sailor moon Special first ch", "this is the first chapter of Sailor moon Special", 40)
write_a_read.create_chapter("Omniscient readers viewpoint", "1", "Omniscient readers first ch", "this is the first chapter of Omniscient readers", 0)
write_a_read.create_chapter("Omniscient readers viewpoint Special", "1", "Omniscient readers Special first ch", "this is the first chapter of Omniscient readers Special", 750)
write_a_read.create_chapter("Naruto", "1", "Naruto first ch", "this is the first chapter of Naruto", 0)
write_a_read.create_chapter("Naruto Special", "1", "Naruto Special first ch", "this is the first chapter of Naruto Special", 800)

#comment
write_a_read.create_comment("Shin_chan-1", "Pangzaza", "wow very fun! I love your writing.")
write_a_read.create_comment("Shin_chan-1", "Pintzaza", "I love your writing. Saranghae Mola!!!")
write_a_read.create_comment("Shinosuke-1", "Pangzaza", "why so expensive. :(")

#buy coin
write_a_read.buy_coin("Mozaza","OnlineBanking","1",None, 1000)

#promotion
promotion_11_11 = CoinPromotion("15/03/2024", 10, "November")
promotion_12_12 = CoinPromotion("15/03/2024", 20, "December")
write_a_read.add_promotion(promotion_11_11)
write_a_read.add_promotion(promotion_12_12)

#add coin transac
Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", "20/02/2024, 15:23:10"))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0989899889"), 500, "+500", "+50", "20/02/2024, 15:23:10"))