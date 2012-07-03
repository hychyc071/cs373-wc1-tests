import unittest
from google.appengine.ext import db

class Success(unittest.TestCase):
    def test_success(self):
        self.assertTrue(True)

import unittest
import StringIO
from Import import *
from Models import *

crisis_1 = '''
<crisis id="1">
		<name>World Hunger</name>
		<kind>Global, Biological</kind>
		<location>
			<unspecific>All countries and cities</unspecific>
		</location>
		<image>http://stopworldhunger.webs.com/hunger.jpg</image>
		<image>http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg</image>
		<video>http://www.youtube.com/watch?v=6jSBW0BOPqM</video>
		<video>http://www.youtube.com/watch?v=0W2Ic5hV28w</video>
		<network>http://www.facebook.com/WorldHungerRelief</network>
		<network>https://twitter.com/#!/FAOWFD</network>
		<link>http://www.who.int/en/</link>
		<link>http://www.worldhunger.org/</link>
		<link>http://www.freedomfromhunger.org/</link>
		<date>
			<otherDiscription>Ongoing.</otherDiscription>
		</date>
		<humanImpact>1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.</humanImpact>
		<economicImpact>In the developing world, more than 1.4 billion people live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the world are undernourished. They consume less than the minimum amount of calories for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.</economicImpact>
		<resourcesNeeded>Money donations and food donations.</resourcesNeeded>
		<waysToHelp>Learn and spread awareness about world hunger: <link>http://www.worldhunger.org/learn.htm</link> Donate to the cause. There are many organaztions available, here's one for example: <link>https://www.freedomfromhunger.org/help/online.php?origin=ggHP</link></waysToHelp>
		<organizationId>5</organizationId>
		<personId>9</personId>
	</crisis>
	'''
crisis_2 = """<crisis id="2">
		<name>Fukushima Daiichi Nuclear Disaster</name>
		<kind>Nuclear meltdown and release of radioactive materials</kind>
		<location>
			<city>Okuma</city>
			<state>Fukushima</state>
			<country>Japan</country>
		</location>
		<image>http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg</image>
		<image>http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg</image>
		<video>http://www.youtube.com/watch?v=PqQWpo_AsF8</video>
		<video>http://www.youtube.com/watch?v=44hv-4C2yXI</video>
		<video>http://www.youtube.com/watch?v=1rdWyrtX0cU</video>
		<network>http://www.facebook.com/pages/Japanese-reaction-to-Fukushima-Daiichi-nuclear-disaster/245496545477108</network>
		<link>http://fukushimaupdate.com/</link>
		<date>
			<start>2011-03-11</start>
		</date>
		<humanImpact>~573</humanImpact>
		<economicImpact>unknown</economicImpact>
		<resourcesNeeded>food</resourcesNeeded>
		<waysToHelp></waysToHelp>
		<organizationId>6</organizationId>
		<personId>10</personId>
	</crisis>
	"""
crisis_3 = """<crisis id="3">
		<name>2011 Tohoku Earthquake and Tsunami</name>
		<kind>Natural Disaster</kind>
		<location>
			<country>Japan</country>
		</location>
		<image>http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png</image>
		<image>http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG</image>
		<image>http://www.flickr.com/photos/ifrc/5542584560/</image>
		<image>http://www.flickr.com/photos/ifrc/5587996898/</image>
		<video>http://www.youtube.com/watch?v=6ZJ3-tbkhA4</video>
		<video>http://www.youtube.com/watch?v=oriVz1xE3wQ</video>
		<video>http://www.youtube.com/watch?v=tNgDKyznXkI</video>
		<network></network>
		<link>http://en.wikipedia.org/wiki/2011_Tohoku_earthquake_and_tsunami</link>
		<link>http://www.jrc.or.jp/eq-japan2011/index.html</link>
		<date>
			<start>2011-03-11</start>
			<additional>05:46 UTC</additional>
		</date>
		<humanImpact>15,861 deaths, 6,107 injured, 3,018 missing</humanImpact>
		<economicImpact>Reconstruction needed for over a million buildings
		Reactor Meltdown at the Fukushima Daiichi Nuclear Power Plant
		Costs of damage possibly exceeding 25 trillion Yen ($300 billion)</economicImpact>
		<resourcesNeeded>Food and medical supplies, temporary housing</resourcesNeeded>
		<waysToHelp>Monetary donations directly to the Japanese Red Cross, or through your national Red Cross/Red Crescent society</waysToHelp>
		<organizationId>7</organizationId>
		<personId>10</personId>
	</crisis>
	"""
org_1 = """<organization id="5">
		<name>World Health Organization</name>
		<kind>Public Health Worldwide</kind>
		<location>
			<unspecific>Headquarters at Geneva, Switzerland, but has offices on all 7 continents in 145 different countries.</unspecific>
		</location>
		<image>http://humanosphere.kplu.org/wp-content/uploads/2012/05/whologo.jpg</image>
		<image>https://encrypted-tbn2.google.com/images?q=tbn:ANd9GcSVoQ8m5nXTZL_62ejj_fLsfDdBtXTiMlx-8o72F9yItj9Cj1bc4Q</image>
		<video>http://www.youtube.com/who</video>
		<video>http://www.youtube.com/watch?v=GWtTQhWwdac</video>
		<network>https://twitter.com/#!/WHO</network>
		<network>http://www.facebook.com/pages/World-Health-Organization-WHO/154163327962392?v=wall</network>
		<link>http://new.paho.org/index.php</link>
		<history>It was established on 7 April 1948, with headquarters in Geneva, Switzerland. Since then, it's played a major role in the eradication of smallpox, yaws, onchocerciasis, SARS and many other infectious diseases.</history>
		<contactInfo><link>http://www.who.int/about/contact_form/en/index.html</link></contactInfo>
		<crisisId>1</crisisId>
		<personId>9</personId>
	</organization>
"""
org_2 = """<organization id="6">
		<name>Groupe INTRA</name>
		<kind>French emergency response organization</kind>
		<location>
			<country>France</country>
		</location>
		<image></image>
		<video></video>
		<network></network>
		<link>http://www.groupe-intra.com/index2.htm</link>
		<history>created by the French CEA and Areva and EDF</history>
		<contactInfo></contactInfo>
		<crisisId>2</crisisId>
	</organization>
"""
org_3 = """<organization id="7">
		<name>Japanese Red Cross</name>
		<kind>Relief Organization</kind>
		<location>
			<city>Tokyo</city>
			<country>Japan</country>
		</location>
		<image>http://en.wikipedia.org/wiki/File:Tsunetami_Sano.jpg</image>
		<image>http://upload.wikimedia.org/wikipedia/commons/a/ac/Japanese_Red_Cross_near_the_Yalu_River_1904.jpg</image>
		<image>http://www.flickr.com/photos/ifrc/5780388293/</image>
		<image>http://www.flickr.com/photos/ifrc/5542584560/</image>
		<video>http://www.youtube.com/watch?v=tNgDKyznXkI</video>
		<network></network>
		<link>http://www.jrc.or.jp/english/index.html</link>
		<history>Founded in 1877 as the Philanthropic Society, by Count Tsunetami Sano, to relieve the injured of the  Satsuma Rebellion.
		In 1887, the organization changed its name to the Japanese Red Cross Society, officialy recognized by the International Committee of the Red Cross on September 2.
		Today, they operate 92 hospitals and 79 blood centers throughout Japan.</history>
		<contactInfo>Address: 1-1-3, Shiba Daimon, Minato-ku, Tokyo 105-8521
		Phone:   +81-3-3438-1311
		Email:   info@jrc.or.jp
		URL:     <link>http://www.jrc.or.jp</link></contactInfo>
		<crisisId>3</crisisId>
		<personId>11</personId>
	</organization>
"""
person_1 = """<person id="9">
		<name>Margaret Chan</name>
		<kind>Director-General of the World Health Organization</kind>
		<location>
			<city>Hong Kong</city>
		</location>
		<image>http://topnews.in/files/margaret-chan1.jpg</image>
		<image>http://static.guim.co.uk/sys-images/Guardian/About/General/2009/7/15/1247677189175/Margaret-Chan-the-World-H-001.jpg</image>
		<video>http://www.youtube.com/watch?v=JE4t9vPX1jA</video>
		<network>https://twitter.com/#!/WHO</network>
		<link>http://www.who.int/en/</link>
		<crisisId>1</crisisId>
		<organizationId>5</organizationId>
	</person>
	"""
person_2 = """
	<person id="10">
		<name>Yukio Edano</name>
		<kind>Minister of Economy, Trade and Industry</kind>
		<location>
			<country>Japan</country>
		</location>
		<image>http://upload.wikimedia.org/wikipedia/commons/8/8f/Yukio_Edano_Sakado_20100910.JPG</image>
		<video>http://www.google.com/</video>
		<network>http://www.google.com/</network>
		<link>http://www.edano.gr.jp/</link>
		<crisisId>2</crisisId>
		<organizationId>6</organizationId>
	</person>
	"""
person_3 = """<person id="11">
		<name>Tadateru Konoe</name>
		<kind>President of the International Federation of Red Cross and Red Crecent Societies</kind>
		<location>
			<country>Japan</country>
		</location>
		<image>http://farm3.staticflickr.com/2620/4117211202_41d8b8e89c_o.jpg</image>
		<video>http://www.youtube.com/watch?v=Ho-GA2Woakk</video>
		<network>http://www.youtube.com/watch?v=Ho-GA2Woakk</network>
		<link>http://www.ifrc.org/en/who-we-are/governance/president/</link>
		<crisisId>3</crisisId>
		<organizationId>7</organizationId>
	</person>
	"""
class TestImport(unittest.TestCase) :
# ------------------
# dictCommonElements
# ------------------
	def test_dictCommonElements_1(self) :
		xml_in = StringIO.StringIO(crisis_1)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '1')
		self.assert_(d['name'] == 'World Hunger')
		self.assert_(d['knd'] == 'Global, Biological')
		self.assert_(d['location'] == 'All countries and cities')
		self.assert_(d['image'] == ['http://stopworldhunger.webs.com/hunger.jpg','http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=6jSBW0BOPqM', 'http://www.youtube.com/watch?v=0W2Ic5hV28w'])
		self.assert_(d['network'] == ['http://www.facebook.com/WorldHungerRelief', 'https://twitter.com/#!/FAOWFD'])
		self.assert_(d['link'] == ['http://www.who.int/en/', 'http://www.worldhunger.org/', 'http://www.freedomfromhunger.org/'])

	def test_dictCommonElements_2 (self) :
		xml_in = StringIO.StringIO(crisis_2)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '2')
		self.assert_(d['name'] == 'Fukushima Daiichi Nuclear Disaster')
		self.assert_(d['knd'] == 'Nuclear meltdown and release of radioactive materials')
		self.assert_(d['location'] == '')
		self.assert_(d['state'] == 'Fukushima')
		self.assert_(d['city'] =='Okuma')
		self.assert_(d['country'] == 'Japan')
		self.assert_(d['image'] == ['http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg', 'http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=PqQWpo_AsF8', 'http://www.youtube.com/watch?v=44hv-4C2yXI', 'http://www.youtube.com/watch?v=1rdWyrtX0cU'])
		self.assert_(d['network'] == ['http://www.facebook.com/pages/Japanese-reaction-to-Fukushima-Daiichi-nuclear-disaster/245496545477108'])
		self.assert_(d['link'] == ['http://fukushimaupdate.com/'])
		
	def test_dictCommonElements_3 (self) :
		xml_in = StringIO.StringIO(crisis_3)
		tree = parse(xml_in)
		d = dictCommonElements(tree.getroot())
		self.assert_(d['ID'] == '3')
		self.assert_(d['name'] == '2011 Tohoku Earthquake and Tsunami')
		self.assert_(d['knd'] == 'Natural Disaster')
		self.assert_(d['location'] == '')
		self.assert_(d['state'] == '')
		self.assert_(d['city'] == '')
		self.assert_(d['country'] == 'Japan')
		self.assert_(d['image'] == ['http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png', 'http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG', 'http://www.flickr.com/photos/ifrc/5542584560/', 'http://www.flickr.com/photos/ifrc/5587996898/'])
		self.assert_(d['video'] == ['http://www.youtube.com/watch?v=6ZJ3-tbkhA4', 'http://www.youtube.com/watch?v=oriVz1xE3wQ', 'http://www.youtube.com/watch?v=tNgDKyznXkI'])
		self.assert_(d['network'] == ['None'])
		self.assert_(d['link'] == ['http://en.wikipedia.org/wiki/2011_Tohoku_earthquake_and_tsunami', 'http://www.jrc.or.jp/eq-japan2011/index.html'])
		
# ------------
# createCrisis
# ------------
	def test_createCrisis_1 (self) :
		xml_in = StringIO.StringIO(crisis_1)
		tree = parse(xml_in)
		c1 = createCrisis(tree.getroot())
		self.assert_(c1.ID == '1')
		self.assert_(c1.name == 'World Hunger')
		self.assert_(c1.knd == 'Global, Biological')
		self.assert_(c1.location == 'All countries and cities')
		self.assert_(c1.image == ['http://stopworldhunger.webs.com/hunger.jpg','http://viroquafood.coop/Portals/62289/images/hunger%20in%20america.jpg'])
		self.assert_(c1.video == ['http://www.youtube.com/watch?v=6jSBW0BOPqM', 'http://www.youtube.com/watch?v=0W2Ic5hV28w'])
		self.assert_(c1.network == ['http://www.facebook.com/WorldHungerRelief', 'https://twitter.com/#!/FAOWFD'])
		self.assert_(c1.link == ['http://www.who.int/en/', 'http://www.worldhunger.org/', 'http://www.freedomfromhunger.org/'])
		self.assert_(c1.date == 'Ongoing.')
		self.assert_(c1.humanImpact == '1 in 7 people go to bed hungry. More than 4.5 million children under the age of 5 will die from hunger related causes this year. Death from malnutirition. 25,000 people die daily. 925 million hungry people in 2010.')
		self.assert_(c1.ecoImpact == 'In the developing world, more than 1.4 billion people live below the international poverty line, earning less than $1.25 per day. Among this group of poor people, many have problems obtaining adequate, nutritious food for themselves and their families. As a result, 1.02 billion people in the world are undernourished. They consume less than the minimum amount of calories for sound health and growth. In 2006, more than 36 million died of hunger or diseases due to deficiencies in micronutrients.')
		self.assert_(c1.resources == 'Money donations and food donations.')
		self.assert_(c1.waysToHelpText == ['Learn and spread awareness about world hunger: ', " Donate to the cause. There are many organaztions available, here's one for example: ", 'None'])
		self.assert_(c1.waysToHelpLinks == ['http://www.worldhunger.org/learn.htm', 'https://www.freedomfromhunger.org/help/online.php?origin=ggHP'])
		self.assert_(c1.orgs == ['5'])
		self.assert_(c1.people == ['9'])
		
	def test_createCrisis_2 (self) :
		xml_in = StringIO.StringIO(crisis_2)
		tree = parse(xml_in)
		c2 = createCrisis(tree.getroot())
		self.assert_(c2.ID == '2')
		self.assert_(c2.name == 'Fukushima Daiichi Nuclear Disaster')
		self.assert_(c2.knd == 'Nuclear meltdown and release of radioactive materials')
		self.assert_(c2.location == '')
		self.assert_(c2.city == 'Okuma')
		self.assert_(c2.state == 'Fukushima')
		self.assert_(c2.country == 'Japan')
		self.assert_(c2.image == ['http://upload.wikimedia.org/wikipedia/commons/d/d7/NIT_Combined_Flights_Ground_Measurements_30Mar_03Apr2011_results.jpg', 'http://upload.wikimedia.org/wikipedia/commons/1/16/Fukushima_I_by_Digital_Globe_crop.jpg'])
		self.assert_(c2.video == ['http://www.youtube.com/watch?v=PqQWpo_AsF8', 'http://www.youtube.com/watch?v=44hv-4C2yXI', 'http://www.youtube.com/watch?v=1rdWyrtX0cU'])
		self.assert_(c2.network == ['http://www.facebook.com/pages/Japanese-reaction-to-Fukushima-Daiichi-nuclear-disaster/245496545477108'])
		self.assert_(c2.link == ['http://fukushimaupdate.com/'])
		self.assert_(c2.date == '')
		self.assert_(c2.startDate == '2011-03-11')
		self.assert_(c2.endDate == '')
		self.assert_(c2.additional == '')
		self.assert_(c2.humanImpact == '~573')
		self.assert_(c2.ecoImpact == 'unknown')
		self.assert_(c2.resources == 'food')
		self.assert_(c2.waysToHelpText == [''] )
		self.assert_(c2.waysToHelpLinks == [] )
		self.assert_(c2.orgs == ['6'])
		self.assert_(c2.people == ['10'])
		
	def test_createCrisis_3 (self) :
		xml_in = StringIO.StringIO(crisis_3)
		tree = parse(xml_in)
		c3 = createCrisis(tree.getroot())
		self.assert_(c3.ID == '3')
		self.assert_(c3.name == '2011 Tohoku Earthquake and Tsunami')
		self.assert_(c3.knd == 'Natural Disaster')
		self.assert_(c3.location == '')
		self.assert_(c3.city == '')
		self.assert_(c3.state == '')
		self.assert_(c3.country == 'Japan')
		self.assert_(c3.image == ['http://upload.wikimedia.org/wikipedia/commons/5/5a/Shindomap_2011-03-11_Tohoku_earthquake.png', 'http://upload.wikimedia.org/wikipedia/commons/b/b9/Carried_train_in_Ishinomaki_Line_.JPG', 'http://www.flickr.com/photos/ifrc/5542584560/', 'http://www.flickr.com/photos/ifrc/5587996898/'])
		self.assert_(c3.video == ['http://www.youtube.com/watch?v=6ZJ3-tbkhA4', 'http://www.youtube.com/watch?v=oriVz1xE3wQ', 'http://www.youtube.com/watch?v=tNgDKyznXkI'])
		self.assert_(c3.network == ['None'])
		self.assert_(c3.link == ['http://en.wikipedia.org/wiki/2011_Tohoku_earthquake_and_tsunami', 'http://www.jrc.or.jp/eq-japan2011/index.html'])
		self.assert_(c3.date == '')
		self.assert_(c3.startDate == '2011-03-11')
		self.assert_(c3.endDate == '')
		self.assert_(c3.additional == '05:46 UTC')
		self.assert_(c3.humanImpact == '15,861 deaths, 6,107 injured, 3,018 missing')
		self.assert_(c3.ecoImpact == """Reconstruction needed for over a million buildings
		Reactor Meltdown at the Fukushima Daiichi Nuclear Power Plant
		Costs of damage possibly exceeding 25 trillion Yen ($300 billion)""")
		self.assert_(c3.resources == 'Food and medical supplies, temporary housing')
		self.assert_(c3.waysToHelpText == ['Monetary donations directly to the Japanese Red Cross, or through your national Red Cross/Red Crescent society'])
		self.assert_(c3.waysToHelpLinks == [])
		self.assert_(c3.orgs == ['7'])
		self.assert_(c3.people == ['10'])
		
# ------------------
# createOrganization
# ------------------
	def test_createOrganization_1 (self) :
		xml_in = StringIO.StringIO(org_1)
		tree = parse(xml_in)
		o1 = createOrganization(tree.getroot())
		self.assert_(o1.ID == '5')
		self.assert_(o1.name == 'World Health Organization')
		self.assert_(o1.knd == 'Public Health Worldwide')
		self.assert_(o1.location == 'Headquarters at Geneva, Switzerland, but has offices on all 7 continents in 145 different countries.')
		self.assert_(o1.state == None)
		self.assert_(o1.city == None)
		self.assert_(o1.country == None)
		self.assert_(o1.image == ['http://humanosphere.kplu.org/wp-content/uploads/2012/05/whologo.jpg', 'https://encrypted-tbn2.google.com/images?q=tbn:ANd9GcSVoQ8m5nXTZL_62ejj_fLsfDdBtXTiMlx-8o72F9yItj9Cj1bc4Q'])
		self.assert_(o1.video == ['http://www.youtube.com/who', 'http://www.youtube.com/watch?v=GWtTQhWwdac'])
		self.assert_(o1.network == ['https://twitter.com/#!/WHO', 'http://www.facebook.com/pages/World-Health-Organization-WHO/154163327962392?v=wall'])
		self.assert_(o1.link == ['http://new.paho.org/index.php'])
		self.assert_(o1.history == "It was established on 7 April 1948, with headquarters in Geneva, Switzerland. Since then, it's played a major role in the eradication of smallpox, yaws, onchocerciasis, SARS and many other infectious diseases.")
		self.assert_(o1.contactInfoText == ['', 'None'])
		self.assert_(o1.contactInfoLinks == ['http://www.who.int/about/contact_form/en/index.html'])
		self.assert_(o1.crises == ['1'])
		self.assert_(o1.people == ['9'])
	
	def test_createOrganization_2 (self) :
		xml_in = StringIO.StringIO(org_2)
		tree = parse(xml_in)
		o2 = createOrganization(tree.getroot())
		self.assert_(o2.ID == '6')
		self.assert_(o2.name == 'Groupe INTRA')
		self.assert_(o2.knd == 'French emergency response organization')
		self.assert_(o2.location == '')
		self.assert_(o2.state == '')
		self.assert_(o2.city == '')
		self.assert_(o2.country == 'France')
		self.assert_(o2.image == ['None'])
		self.assert_(o2.video == ['None'])
		self.assert_(o2.network == ['None'])
		self.assert_(o2.link == ['http://www.groupe-intra.com/index2.htm'])
		self.assert_(o2.history == 'created by the French CEA and Areva and EDF')
		self.assert_(o2.contactInfoText == [''])
		self.assert_(o2.contactInfoLinks == [])
		self.assert_(o2.crises == ['2'])
		self.assert_(o2.people == [])

	def test_createOrganization_3 (self) :
		xml_in = StringIO.StringIO(org_3)
		tree = parse(xml_in)
		o3 = createOrganization(tree.getroot())
		self.assert_(o3.ID ==  '7')
		self.assert_(o3.name == 'Japanese Red Cross')
		self.assert_(o3.knd == 'Relief Organization')
		self.assert_(o3.location == '')
		self.assert_(o3.state == '')
		self.assert_(o3.city == 'Tokyo')
		self.assert_(o3.country == 'Japan')
		self.assert_(o3.image == ['http://en.wikipedia.org/wiki/File:Tsunetami_Sano.jpg', 'http://upload.wikimedia.org/wikipedia/commons/a/ac/Japanese_Red_Cross_near_the_Yalu_River_1904.jpg', 'http://www.flickr.com/photos/ifrc/5780388293/', 'http://www.flickr.com/photos/ifrc/5542584560/'])
		self.assert_(o3.video == ['http://www.youtube.com/watch?v=tNgDKyznXkI'])
		self.assert_(o3.network == ['None'])
		self.assert_(o3.link == ['http://www.jrc.or.jp/english/index.html'])
		self.assert_(o3.history == """Founded in 1877 as the Philanthropic Society, by Count Tsunetami Sano, to relieve the injured of the  Satsuma Rebellion.
		In 1887, the organization changed its name to the Japanese Red Cross Society, officialy recognized by the International Committee of the Red Cross on September 2.
		Today, they operate 92 hospitals and 79 blood centers throughout Japan.""")
		self.assert_(o3.contactInfoText == ['Address: 1-1-3, Shiba Daimon, Minato-ku, Tokyo 105-8521\n\t\tPhone:   +81-3-3438-1311\n\t\tEmail:   info@jrc.or.jp\n\t\tURL:     ', 'None'])
		self.assert_(o3.contactInfoLinks == ['http://www.jrc.or.jp'])
		self.assert_(o3.crises == ['3'])
		self.assert_(o3.people == ['11'])

# ------------
# createPerson
# ------------
	def test_createPerson_1 (self) :
		xml_in = StringIO.StringIO(person_1)
		tree = parse(xml_in)
		p = createPerson(tree.getroot())
		self.assert_(p.ID == '9')
		self.assert_(p.name == 'Margaret Chan')
		self.assert_(p.knd == 'Director-General of the World Health Organization')
		self.assert_(p.location == '')
		self.assert_(p.state == '')
		self.assert_(p.city == 'Hong Kong')
		self.assert_(p.country == '')
		self.assert_(p.image == ['http://topnews.in/files/margaret-chan1.jpg', 'http://static.guim.co.uk/sys-images/Guardian/About/General/2009/7/15/1247677189175/Margaret-Chan-the-World-H-001.jpg'])
		self.assert_(p.video == ['http://www.youtube.com/watch?v=JE4t9vPX1jA'])
		self.assert_(p.network == ['https://twitter.com/#!/WHO'])
		self.assert_(p.link == ['http://www.who.int/en/'])
		self.assert_(p.crises == ['1'])
		self.assert_(p.orgs == ['5'])
		
	def test_createPerson_2 (self) :
		xml_in = StringIO.StringIO(person_2)
		tree = parse(xml_in)
		p = createPerson(tree.getroot())
		self.assert_(p.ID == '10')
		self.assert_(p.name == 'Yukio Edano')
		self.assert_(p.knd == 'Minister of Economy, Trade and Industry')
		self.assert_(p.location == '')
		self.assert_(p.state == '')
		self.assert_(p.city == '')
		self.assert_(p.country == 'Japan')
		self.assert_(p.image == ['http://upload.wikimedia.org/wikipedia/commons/8/8f/Yukio_Edano_Sakado_20100910.JPG'])
		self.assert_(p.video == ['http://www.google.com/'])
		self.assert_(p.network == ['http://www.google.com/'])
		self.assert_(p.link == ['http://www.edano.gr.jp/'])
		self.assert_(p.crises == ['2'])
		self.assert_(p.orgs == ['6'])
	
	def test_createPerson_3 (self) :
		xml_in = StringIO.StringIO(person_3)
		tree = parse(xml_in)
		p = createPerson(tree.getroot())
		self.assert_(p.ID == '11')
		self.assert_(p.name == 'Tadateru Konoe')
		self.assert_(p.knd == 'President of the International Federation of Red Cross and Red Crecent Societies')
		self.assert_(p.location == '')
		self.assert_(p.state == '')
		self.assert_(p.city == '')
		self.assert_(p.country == 'Japan')
		self.assert_(p.image == ['http://farm3.staticflickr.com/2620/4117211202_41d8b8e89c_o.jpg'])
		self.assert_(p.video == ['http://www.youtube.com/watch?v=Ho-GA2Woakk'])
		self.assert_(p.network == ['http://www.youtube.com/watch?v=Ho-GA2Woakk'])
		self.assert_(p.link == ['http://www.ifrc.org/en/who-we-are/governance/president/'])
		self.assert_(p.crises == ['3'])
		self.assert_(p.orgs == ['7'])

# -----------
# buildModels
# -----------
	def test_buildModels_1 (self) :
		mock_xml = """
		<data>
			<crises> 
				%s
			</crises>
			<organizations>
				%s
			</organizations>
			<people>
				%s
			</people>
		</data>""" % (crisis_1, org_1, person_1)
		
		mock_file = StringIO.StringIO(mock_xml)
		tree = parse(mock_file)
		cList, oList, pList = buildModels(tree)
		for c in cList :
			self.assert_(c.kind() == 'Crisis')
	
		for o in oList :
			self.assert_(o.kind() == 'Organization')

		for p in pList :
			self.assert_(p.kind() == 'Person')
			
	def test_buildModels_3 (self) :
		mock_xml = """
		<data>
			<crises> 
				%s
			</crises>
			<organizations>
				%s
			</organizations>
			<people>
				%s
			</people>
		</data>""" % (crisis_1 + crisis_2 + crisis_3, 
		org_1 + org_2 + org_3, 
		person_1 + person_2 + person_3)
		
		mock_file = StringIO.StringIO(mock_xml)
		tree = parse(mock_file)
		cList, oList, pList = buildModels(tree)
		for c in cList :
			self.assert_(c.kind() == 'Crisis')
	
		for o in oList :
			self.assert_(o.kind() == 'Organization')

		for p in pList :
			self.assert_(p.kind() == 'Person')
	def test_buildModels_2 (self) :
		mock_xml = """
		<data>
			<crises> 
				%s
			</crises>
			<organizations>
				%s
			</organizations>
			<people>
				%s
			</people>
		</data>""" % (crisis_1+crisis_2, org_1+org_2, person_1+person_2)
		
		mock_file = StringIO.StringIO(mock_xml)
		tree = parse(mock_file)
		cList, oList, pList = buildModels(tree)
		for c in cList :
			self.assert_(c.kind() == 'Crisis')
	
		for o in oList :
			self.assert_(o.kind() == 'Organization')

		for p in pList :
			self.assert_(p.kind() == 'Person')
	
# -*- coding: utf-8 -*-

# -------------
# TestExport.py
# -------------

# -------
# imports
# -------

import unittest
from xml.etree.ElementTree import Element, SubElement
from Models import Crisis, Organization, Person
from Export import *
from BuildTesterTree import build_tester_tree


class TestExport (unittest.TestCase) :
	# ----
	# test build tree
	# ----
	def test_build_tree1(self):
		try:
			cmods = []
			omods = []
			pmods = []
			cmods.append(Crisis(ID = 1))
			self.assert_ (False)
		except Exception:
			self.assert_ (True)

	def test_build_tree2(self):
		try:
			cmods, omods, pmods = build_tester_tree()
			root = buildTree(cmods, omods, pmods)
		except Exception:
			self.assert_ (False)

	def test_build_tree3(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)
		self.assert_ (len(root[0]) == 5)
		self.assert_ (len(root[1]) == 5)
		self.assert_ (len(root[2]) == 5)
	  
	# ----
	# test build pages of type
	# ----
	def test_buildPagesofType1(self):
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[0]
		root2 = buildTree(cmods, omods, pmods)[0]
		buildPagesofType(root1, "crisis", cmods, buildCrisisPage)

		for x in range(len(cmods)) :
			SubElement(root2, "crisis")
			elements = buildCrisisPage(root2[x], cmods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		self.assert_ (root1 == root2)

	def test_buildPagesofType2(self):
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[0]
		root2 = buildTree(cmods, omods, pmods)[0]
		buildPagesofType(root1, "crisis", cmods, buildCrisisPage)

		self.assert_ (root1 != root2)

	def test_buildPagesofType3(self):
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[1]
		root2 = buildTree(cmods, omods, pmods)[1]
		buildPagesofType(root1, "organization", omods, buildOrgPage)

		for x in range(len(omods)) :
			SubElement(root2, "organization")
			elements = buildOrgPage(root2[x], omods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		self.assert_ (root1 == root2)

	def test_buildPagesofType4(self):
		cmods, omods, pmods = build_tester_tree()
		root1 = buildTree(cmods, omods, pmods)[2]
		root2 = buildTree(cmods, omods, pmods)[2]
		buildPagesofType(root1, "person", pmods, buildPersonPage)

		for x in range(len(pmods)) :
			SubElement(root2, "person")
			elements = buildPersonPage(root2[x], pmods[x])		

			# add sub elements		
			for element in elements :
				root2[x].append(element)	

		self.assert_ (root1 == root2)

	def test_buildCrisisPage1(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (len(root[0]) == 20)

	def test_buildCrisisPage2(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][0] == 'n')

	def test_buildCrisisPage3(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCrisisPage(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][len(root[0])-1] == 'p1')

	def test_buildOrganizationPage1(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (len(root[0]) == 16)

	def test_buildOrganizationPage2(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][0] == 'n')

	def test_buildOrganizationPage3(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'Organization')
		elements = buildOrgPage(root[0], omods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][len(root[0])-1][0] == 'p1')

	def test_buildPersonPage1(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_(len(root[0]) == 13)

	def test_buildPersonPage2(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][0] == 'n')

	def test_buildPersonPage3(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'Person')
		elements = buildPersonPage(root[0], pmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (root[0][len(root[0])-1][0] == 'p1')

	def test_buildCommonData(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[0]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_( len(root[0]) == 11)
		self.assert_ (root[0][0] == 'n')

	def test_buildCommonData(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[1]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)

		self.assert_ (len(root[0]) == 11)
		self.assert_ (root[0][0] == 'n')

	def test_buildCommonData(self):
		cmods, omods, pmods = build_tester_tree()
		root = buildTree(cmods, omods, pmods)[2]
		SubElement(root, 'crisis')
		elements = buildCommonData(root[0], cmods[0])
		for element in elements:
			root[0].append(element)
		self.assert_ (len(root[0]) == 11)
		self.assert_ (root[0][0] == 'n')


# ----
# main
# ----

#unittest.main()


