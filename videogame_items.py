from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///videogamecatalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for PS4
category1 = Category(name="Playstation 4", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Horizon Zero Dawn", user_id=1, description="The plot revolves around Aloy, a hunter and archer living in a world overrun by robots. Having been an outcast her whole life, she sets out to discover the dangers that kept her sheltered. The character uses ranged weapons and a spear and stealth tactics to combat the mechanised creatures, whose remains can be looted for resources. A skill tree provides the player with new abilities and passive bonuses. The game features an open world environment for Aloy to explore, divided into tribes that hold side quests to undertake, while the main story guides her across the entire map.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Witcher 3: Wild Hunt", user_id=1,  description="With the Empire attacking the Kingdoms of the North and the Wild Hunt, a cavalcade of ghastly riders, breathing down your neck, the only way to survive is to fight back. As Geralt of Rivia, a master swordsman and monster hunter, leave none of your enemies standing. Explore a gigantic open world, slay beasts and decide the fates of whole communities with your actions, all in a genuine next generation format.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Uncharted 4: A Thief's End", user_id=1, description="Following Uncharted 3: Drake's Deception, it is the final Uncharted game to feature protagonist Nathan Drake (portrayed by Nolan North). Drake, now retired from fortune hunting with his wife Elena, reunites with his estranged older brother Sam and longtime partner Sully to search for Captain Henry Avery's lost treasure.", category=category1)

session.add(item3)
session.commit()

# Items for PS3
category2 = Category(name="Playstation 3", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="The Last of Us", user_id=1, description="Twenty years after a pandemic radically transformed known civilization, infected humans run amuck and survivors kill one another for sustenance and weapons - literally whatever they can get their hands on. Joel, a salty survivor, is hired to smuggle a fourteen-year-old girl, Ellie, out of a rough military quarantine, but what begins as a simple job quickly turns into a brutal journey across the country.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Grand Theft Auto V", user_id=1,  description="Los Santos is a vast, sun-soaked metropolis full of self-help gurus, starlets and once-important, formerly-known-as celebrities. The city was once the envy of the Western world, but is now struggling to stay afloat in an era of economic uncertainty and reality TV. Amidst the chaos, three unique criminals plot their own chances of survival and success: Franklin, a former street gangster in search of real opportunities and serious cheddar; Michael, a professional ex-con whose retirement is a lot less rosy than he hoped it would be; and Trevor, a violent maniac driven by the chance of a cheap high and the next big score. Quickly running out of options, the crew risks it all in a sequence of daring and dangerous heists that could set them up for life.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Batman: Arkham City", user_id=1, description="Batman: Arkham City builds upon the intense, atmospheric foundation of Batman: Arkham Asylum, sending players soaring into Arkham City, the new maximum security home for all of Gotham City's thugs, gangsters and insane criminal masterminds. Set inside the heavily fortified walls of a sprawling district in the heart of Gotham City, this highly anticipated sequel introduces a brand-new story that draws together a new all-star cast of classic characters and murderous villains from the Batman universe, as well as a vast range of new and enhanced gameplay features to deliver the ultimate experience as the Dark Knight.", category=category2)

session.add(item3)
session.commit()

# Items for XBox360
category3 = Category(name="XBox 360", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Bioshock", user_id=1, description="After your plane crashes into icy uncharted waters, you discover a rusted bathysphere and descend into Rapture, a city hidden beneath the sea. Constructed as an idealistic society for a hand picked group of scientists, artists and industrialists, the idealism is no more. Now the city is littered with corpses, wildly powerful guardians roam the corridors as little girls loot the dead, and genetically mutated citizens ambush you at every turn. Take control of your world by hacking mechanical devices, commandeering security turrets and crafting unique items critical to your very survival. Upgrade your weapons with ionic gels, explosives and toxins to customize them to the enemy and environment. Genetically modify your body through dozens of Plasmid Stations scattered throughout the city, empowering you with fantastic and often grotesque abilities. Explore a living world powered by Ecological A.I., where the inhabitants have interesting and consequential relationships with one another that impact your gameplay experience. Experience truly next generation graphics that vividly illustrate the forlorn art deco city, highlighted by the most detailed and realistic water effects ever developed in a video game. Make meaningful choices and mature decisions, ultimately culminating in the grand question: do you exploit the innocent survivors of Rapture...or save them?", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Mass Effect 2", user_id=1, description="Mass Effect 2 is the second installment of the Mass Effect series and a sequel to the original Mass Effect. The game takes place within the Milky Way galaxy during the 22nd century, where humanity is threatened by an insectoid species known as the Collectors. The player assumes the role of Commander Shepard, an elite human soldier who must construct and gain the loyalty of a diverse team and stop the enemy in a suicide mission. With the use of a completed saved game of its predecessor, the player can impact the story of the game in numerous ways.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Halo 3", user_id=1, description="Halo 3 is the third game in the Halo Trilogy and provides the thrilling conclusion to the events begun in Halo: Combat Evolved. Halo 3 picks up where Halo 2 left off. The Master Chief is returning to Earth to finish the fight. The Covenant occupation of Earth has uncovered a massive and ancient object beneath the African sands - an object who's secrets have yet to be revealed. Earth's forces are battered and beaten. The Master Chief's AI companion Cortana is still trapped in the clutches of the Gravemind - a horrifying Flood intelligence, and a civil war is raging in the heart of the Covenant. This is how the world ends...", category=category3)

session.add(item3)
session.commit()

# Items for Wii
category4 = Category(name="Wii", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Super Mario Galaxy", user_id=1, description="The ultimate Nintendo hero is taking the ultimate step ... out into space. Join Mario as he ushers in a new era of video games, defying gravity across all the planets in the galaxy. When some creature escapes into space with Princess Peach, Mario gives chase, exploring bizarre planets all across the galaxy. Mario, Peach and enemies new and old are here. Players run, jump and battle enemies as they explore all the planets in the galaxy. Since this game makes full use of all the features of the Wii Remote, players have to do all kinds of things to succeed: pressing buttons, swinging the Wii Remote and the Nunchuk, and even pointing at and dragging things with the pointer. Since he's in space, Mario can perform mind-bending jumps unlike anything he's done before. He'll also have a wealth of new moves that are all based around tilting, pointing and shaking the Wii Remote. Shake, tilt and point! Mario takes advantage of all the unique aspects of the Wii Remote and Nunchuk controller, unleashing new moves as players shake the controller and even point at and drag items with the pointer.", category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="The Legend of Zelda: Twilight Princess", user_id=1, description="When an evil darkness enshrouds the land of Hyrule, a young farm boy named Link must awaken the hero - and the animal - within. When Link travels to the Twilight Realm, he transforms into a wolf and must scour the land with the help of a mysterious girl named Midna. Using the power and unique control of the Wii console, The Legend of Zelda: Twilight Princess features precise aiming control using the Wii Remote. The Wii Remote and the Nunchuk controller are used for a variety of game activities, including fishing and special sword attacks. Players ride into battle against troops of foul creatures using an amazing horseback combat system, then take on massive bosses that must be seen to be believed.", category=category4)

session.add(item2)
session.commit()

item3 = CategoryItem(name="New Super Mario Bros. Wii", user_id=1, description="New Super Mario Bros. Wii's plot is similar to those of other side-scrolling Super Mario games. New Super Mario Bros. Wii follows Mario as he fights his way through Bowser's henchmen to rescue Princess Peach. Mario has access to several power-ups that help him complete his quest, including the Ice Flower, the Fire Flower, and the Starman, each giving him unique abilities. While traveling through up to nine worlds with a total of 80 levels, Mario must defeat Bowser's children (the Koopalings and Bowser Jr.), Kamek, and Bowser himself before finally saving Princess Peach.", category=category4)

session.add(item3)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name