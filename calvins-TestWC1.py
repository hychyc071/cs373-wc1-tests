import unittest
from helloworld import *
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree



class TestWC1(unittest.TestCase):


    def testName(self):
        self.assertTrue(True)

    def test_feature_one(self):
	cris = Crisis()
	cris.name = "Deepwater Horizon Oil Spill"
	self.assertTrue(cris.name == "Deepwater Horizon Oil Spill")
    def test_feature_two(self):
	cris = Crisis()
	cris.misc = ""
	self.assertTrue(cris.misc == "")
    def test_feature_third(self):
	org = Organization()
	self.assertTrue(org.name != "")
    def test_feature_fourth(self):
	org = Organization()
	self.assertTrue(org.name is None) 
    def test_feature_fifth(self):
	peps = Person()
	peps.name = "Connor Bowman"
	self.assertTrue(peps.name is "Connor Bowman")
    def test_feature_six(self):
	t = Time()
    	t.month = "4" 
	self.assertTrue(t.month == "4")
    def test_feature_seven(self):
	t = Time()
	t.day = "30"
	self.assertTrue(t.day == "30")
    def test_feature_twenty(self):
	t = Time()
	t.year = "1970"
	self.assertTrue(t.year == "1970")
    def test_feature_eight(self):
	t = Time()
	t.time = "11:30"
	self.assertTrue(t.time == "11:30")
    def test_feature_nine(self):
	m = Mail()
	m.address = "1 Main St."
	self.assertTrue(m.address == "1 Main St.")
    def test_feature_ten(self):
	m = Mail()
	m.city = "Austin"
	self.assertTrue(m.city == "Austin")
    def test_feature_eleven(self):
	m = Mail()	
	m.state = "TX"
	self.assertTrue(m.state == "TX")
    def test_feature_twelve(self):
	m = Mail()
	m.country = "USA"
	self.assertTrue(m.country == "USA")
    def test_feature_thirteen(self):
	m = Mail()
	m.mail_zip = "78705"
	self.assertTrue(m.mail_zip == "78705")
    def fourteen(self):
	l = Location()
	l.city = "Austin"
	self.assertTrue(l.city == "Austin")
    def test_feature_eight(self):
	p = xml.etree.ElementTree.fromstring("""	<crisis id = "deepwater">
<name>Deepwater Horizon Oil Spill</name>
<info>
<history></history>
<help> Volunteering along the gulf to help clean</help>
<resources> Help cleaning spill and wildlife</resources>
<type>Wellhead Blowout and Oil Spill</type>
<time>
<time></time>
<day>20</day>
<month>4</month>
<year>2010</year>
<misc></misc>
</time>
<loc>
<city></city>
<region>Gulf of Mexico</region>
<country></country>
</loc>
<impact>
<human>
<deaths>11</deaths>
<displaced>0</displaced>
<injured>0</injured>
<missing>0</missing>
<misc></misc>
</human>
<economic>
<amount>30000000000</amount>
<currency>dollars</currency>
<misc></misc>
</economic>
</impact>
</info>
<ref>
            <primaryImage>
                <site></site>
<title></title>
<url></url>
<description></description>
            </primaryImage>
<image>
                <site></site>
<title>Deepwater Horizon</title>
<url>http://www.thebuzzmedia.com/wp-content/uploads/2010/06/bp-oil-spill-bird-covered-in-oil.jpg</url>
<description></description>
</image>
<video>
<site>Youtube</site>
<title></title>
<url>http://www.youtube.com/watch?v=lY-PikuXTYY</url>
<description></description>
</video>
<social>
                <site></site>
<title>Facebook</title>
<url>http://www.facebook.com/BPOilCrisisInTheGulf?ref=ts</url>
                <description></description>
</social>
<ext>
                <site></site>
<title>Wikipedia</title>
<url>http://en.wikipedia.org/wiki/Deepwater_Horizon_oil_spill#Consequences</url>
<description></description>
</ext>
</ref>
<misc></misc>
<org idref = "bp"/>
<person idref = "feinberg"/>
</crisis>""")
	d = p.find("name")
	
	self.assertTrue(d.text == "Deepwater Horizon Oil Spill")
	



	
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestWC1.testName']
    unittest.main()
