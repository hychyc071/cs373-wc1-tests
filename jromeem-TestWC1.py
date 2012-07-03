import unittest
import XMLHelpers
import cgi, os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump
from minixsv import pyxsval as xsv

from DataModels import Person, Organization, Crisis, Link

class ExportTests(unittest.TestCase):
    
    def test_buildperson1(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        person1 = Person(elemid = "bobs",
                   name = "Bob",
                   info_type = "Salamander",
                   info_birthdate_time = "12:00PM",
                   info_birthdate_day = 12,
                   info_birthdate_month = 12,
                   info_birthdate_year = 1900,
                   info_birthdate_misc = "born under the full moon...",
                   info_nationality = "Swedish",
                   info_biography = "Bob swam a lot, as salamanders do...",
                   
                   orgrefs = ["salamanders united", "salamander liberation front"],
                   crisisrefs = ["swamp famine", "west swamp drought"])
        ptree = SubElement(tree, "person", {"id" : "bobs"})     
        XMLHelpers.buildPerson(ptree, person1)
        
        elemid = ptree.attrib['id'],
        name = ptree.find('.//name').text
        info_type = ptree.find('.//info').find('.//type').text
        info_birthdate_time = ptree.find('.//info').find('.//birthdate').find('.//time').text
        info_birthdate_day = int(ptree.find('.//info').find('.//birthdate').find('.//day').text)
        info_birthdate_month = int(ptree.find('.//info').find('.//birthdate').find('.//month').text)
        info_birthdate_year = int(ptree.find('.//info').find('.//birthdate').find('.//year').text)
        info_birthdate_misc = ptree.find('.//info').find('.//birthdate').find('.//misc').text
        info_nationality = ptree.find('.//info').find('.//nationality').text
        info_biography = ptree.find('.//info').find('.//biography').text

        orgrefs = [x.attrib['idref'] for x in ptree.findall('.//org')]
        crisisrefs = [x.attrib['idref'] for x in ptree.findall('.//crisis')]
              
        self.assertEqual(elemid[0], person1.elemid)
        self.assert_(name == person1.name)
        self.assert_(info_type == person1.info_type)
        self.assert_(info_birthdate_time == person1.info_birthdate_time)
        self.assert_(info_birthdate_day == person1.info_birthdate_day)
        self.assert_(info_birthdate_month == person1.info_birthdate_month)
        self.assert_(info_birthdate_year == person1.info_birthdate_year)
        self.assert_(info_birthdate_misc == person1.info_birthdate_misc)
        self.assert_(info_nationality == person1.info_nationality)
        self.assert_(info_biography == person1.info_biography)
        self.assert_(orgrefs == person1.orgrefs)
        self.assert_(crisisrefs == person1.crisisrefs)
        
    def test_buildperson2(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        person2 = Person(elemid = "sally",
                   name = "Sally",
                   info_type = "seahorse",
                   info_birthdate_time = "0:00PM",
                   info_birthdate_day = 1124,
                   info_birthdate_month = 1132,
                   info_birthdate_year = 19000,
                   info_birthdate_misc = "born in a clamshell...",
                   info_nationality = "French",
                   info_biography = "Sally was boring...",
                   
                   orgrefs = ["seahorse united", "seahorse liberation front"],
                   crisisrefs = ["swamp famine", "west swamp drought"])
        ptree = SubElement(tree, "person", {"id" : "sally"})  
        XMLHelpers.buildPerson(ptree, person2)
        
        elemid = ptree.attrib['id'],
        name = ptree.find('.//name').text
        info_type = ptree.find('.//info').find('.//type').text
        info_birthdate_time = ptree.find('.//info').find('.//birthdate').find('.//time').text
        info_birthdate_day = int(ptree.find('.//info').find('.//birthdate').find('.//day').text)
        info_birthdate_month = int(ptree.find('.//info').find('.//birthdate').find('.//month').text)
        info_birthdate_year = int(ptree.find('.//info').find('.//birthdate').find('.//year').text)
        info_birthdate_misc = ptree.find('.//info').find('.//birthdate').find('.//misc').text
        info_nationality = ptree.find('.//info').find('.//nationality').text
        info_biography = ptree.find('.//info').find('.//biography').text

        orgrefs = [x.attrib['idref'] for x in ptree.findall('.//org')]
        crisisrefs = [x.attrib['idref'] for x in ptree.findall('.//crisis')]
        
        self.assertEqual(elemid[0], person2.elemid)
        self.assert_(name == person2.name)
        self.assert_(info_type == person2.info_type)
        self.assert_(info_birthdate_time == person2.info_birthdate_time)
        self.assert_(info_birthdate_day == person2.info_birthdate_day)
        self.assert_(info_birthdate_month == person2.info_birthdate_month)
        self.assert_(info_birthdate_year == person2.info_birthdate_year)
        self.assert_(info_birthdate_misc == person2.info_birthdate_misc)
        self.assert_(info_nationality == person2.info_nationality)
        self.assert_(info_biography == person2.info_biography)
        self.assert_(orgrefs == person2.orgrefs)
        self.assert_(crisisrefs == person2.crisisrefs)
        
    def test_buildperson3(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        person3 = Person(elemid = "null",
                   name = "nully",
                   info_type = "",
                   info_birthdate_time = "",
                   info_birthdate_day = 0,
                   info_birthdate_month = 0,
                   info_birthdate_year = 0,
                   info_birthdate_misc = "",
                   info_nationality = "",
                   info_biography = "",
                   
                   orgrefs = [],
                   crisisrefs = [])
        ptree = SubElement(tree, "person", {"id" : "null"})     
        XMLHelpers.buildPerson(ptree, person3)
        
        
        elemid = ptree.attrib['id']
        name = ptree.find('.//name').text
        info_type = ptree.find('.//info').find('.//type').text
        info_birthdate_time = ptree.find('.//info').find('.//birthdate').find('.//time').text
        info_birthdate_day = int(ptree.find('.//info').find('.//birthdate').find('.//day').text)
        info_birthdate_month = int(ptree.find('.//info').find('.//birthdate').find('.//month').text)
        info_birthdate_year = int(ptree.find('.//info').find('.//birthdate').find('.//year').text)
        info_birthdate_misc = ptree.find('.//info').find('.//birthdate').find('.//misc').text
        info_nationality = ptree.find('.//info').find('.//nationality').text
        info_biography = ptree.find('.//info').find('.//biography').text

        orgrefs = [x.attrib['idref'] for x in ptree.findall('.//org')]
        crisisrefs = [x.attrib['idref'] for x in ptree.findall('.//crisis')]
       

        self.assertEqual(elemid, person3.elemid)
        self.assert_(name == person3.name)
        self.assert_(info_type == person3.info_type)
        self.assert_(info_birthdate_time == person3.info_birthdate_time)
        self.assert_(info_birthdate_day == person3.info_birthdate_day)
        self.assert_(info_birthdate_month == person3.info_birthdate_month)
        self.assert_(info_birthdate_year == person3.info_birthdate_year)
        self.assert_(info_birthdate_misc == person3.info_birthdate_misc)
        self.assert_(info_nationality == person3.info_nationality)
        self.assert_(info_biography == person3.info_biography)
        self.assert_(orgrefs == person3.orgrefs)
        self.assert_(crisisrefs == person3.crisisrefs)

        
    def test_buildorg1(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        organization1 = Organization(elemid = "Franch",
    
                                    name = "French pride",
    
                                    info_type = "non-existant",
                                    info_history = "white flags",
                                    info_contacts_phone = "1234567890",
                                    info_contacts_email = "omuledu@fromage.com",
                                    info_contacts_address = "French",
                                    info_contacts_city = "Paris",
                                    info_contacts_state = "Canada",
                                    info_contacts_country = "USA",
                                    info_contacts_zip = "7890",
    
                                    info_loc_city = "Alaska",
                                    info_loc_region = "Ukraine",
                                    info_loc_country = "Antarctica",
    
                                    personrefs = ["baquettes", "crumpets"],
                                    crisisrefs = ["war", "nazis"],
    
                                    misc = "")

        otree = SubElement(tree, "organization", {"id" : "Franch"})     
        XMLHelpers.buildOrganization(otree, organization1)
        
        elemid = otree.attrib['id'],
        name = otree.find('.//name').text
        info_type = otree.find('.//info').find('.//type').text
        info_history = otree.find('.//info').find('.//history').text
        info_contacts_phone = otree.find('.//info').find('.//contact').find('.//phone').text
        info_contacts_email = otree.find('.//info').find('.//contact').find('.//email').text
        info_contacts_address = otree.find('.//info').find('.//contact').find('.//mail').find('.//address').text
        info_contacts_city = otree.find('.//info').find('.//contact').find('.//mail').find('.//city').text
        info_contacts_state = otree.find('.//info').find('.//contact').find('.//mail').find('.//state').text
        info_contacts_country = otree.find('.//info').find('.//contact').find('.//mail').find('.//country').text
        info_contacts_zip = otree.find('.//info').find('.//contact').find('.//mail').find('.//zip').text
        info_loc_city = otree.find('.//info').find('.//loc').find('.//city').text
        info_loc_region = otree.find('.//info').find('.//loc').find('.//region').text
        info_loc_country = otree.find('.//info').find('.//loc').find('.//country').text

        personrefs = [x.attrib['idref'] for x in otree.findall('.//person')]
        crisisrefs = [x.attrib['idref'] for x in otree.findall('.//crisis')]
        misc = otree.find('.//misc').text
        
        #self.assert_(elemid == organization1.elemid)
        self.assert_(name == organization1.name)
        self.assert_(info_type == organization1.info_type)
        self.assert_(info_history == organization1.info_history)
        self.assert_(info_contacts_phone == organization1.info_contacts_phone)
        self.assert_(info_contacts_email == organization1.info_contacts_email)
        self.assert_(info_contacts_address == organization1.info_contacts_address)
        self.assert_(info_contacts_city == organization1.info_contacts_city)
        self.assert_(info_contacts_state == organization1.info_contacts_state)
        self.assert_(info_contacts_country == organization1.info_contacts_country)
        self.assert_(info_contacts_zip == organization1.info_contacts_zip)
        self.assert_(info_loc_city == organization1.info_loc_city)
        self.assert_(info_loc_region == organization1.info_loc_region)
        self.assert_(info_loc_country == organization1.info_loc_country)
        self.assert_(misc == organization1.misc)
        self.assert_(personrefs == organization1.personrefs)
        self.assert_(crisisrefs == organization1.crisisrefs)
        
    def test_buildorg2(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        organization2 = Organization(elemid = "crap",
    
                                    name = "crap",
    
                                    info_type = "",
                                    info_history = "",
                                    info_contacts_phone = "",
                                    info_contacts_email = "",
                                    info_contacts_address = "",
                                    info_contacts_city = "",
                                    info_contacts_state = "",
                                    info_contacts_country = "",
                                    info_contacts_zip = "",
    
                                    info_loc_city = "",
                                    info_loc_region = "",
                                    info_loc_country = "",
    
                                    personrefs = [],
                                    crisisrefs = [],
    
                                    misc = "")

        otree = SubElement(tree, "organization", {"id" : "crap"})     
        XMLHelpers.buildOrganization(otree, organization2)
        
        elemid = otree.attrib['id'],
        name = otree.find('.//name').text
        info_type = otree.find('.//info').find('.//type').text
        info_history = otree.find('.//info').find('.//history').text
        info_contacts_phone = otree.find('.//info').find('.//contact').find('.//phone').text
        info_contacts_email = otree.find('.//info').find('.//contact').find('.//email').text
        info_contacts_address = otree.find('.//info').find('.//contact').find('.//mail').find('.//address').text
        info_contacts_city = otree.find('.//info').find('.//contact').find('.//mail').find('.//city').text
        info_contacts_state = otree.find('.//info').find('.//contact').find('.//mail').find('.//state').text
        info_contacts_country = otree.find('.//info').find('.//contact').find('.//mail').find('.//country').text
        info_contacts_zip = otree.find('.//info').find('.//contact').find('.//mail').find('.//zip').text
        info_loc_city = otree.find('.//info').find('.//loc').find('.//city').text
        info_loc_region = otree.find('.//info').find('.//loc').find('.//region').text
        info_loc_country = otree.find('.//info').find('.//loc').find('.//country').text

        personrefs = [x.attrib['idref'] for x in otree.findall('.//person')]
        crisisrefs = [x.attrib['idref'] for x in otree.findall('.//crisis')]
        misc = otree.find('.//misc').text
        
        #self.assert_(elemid == organization2.elemid)
        self.assert_(name == organization2.name)
        self.assert_(info_type == organization2.info_type)
        self.assert_(info_history == organization2.info_history)
        self.assert_(info_contacts_phone == organization2.info_contacts_phone)
        self.assert_(info_contacts_email == organization2.info_contacts_email)
        self.assert_(info_contacts_address == organization2.info_contacts_address)
        self.assert_(info_contacts_city == organization2.info_contacts_city)
        self.assert_(info_contacts_state == organization2.info_contacts_state)
        self.assert_(info_contacts_country == organization2.info_contacts_country)
        self.assert_(info_contacts_zip == organization2.info_contacts_zip)
        self.assert_(info_loc_city == organization2.info_loc_city)
        self.assert_(info_loc_region == organization2.info_loc_region)
        self.assert_(info_loc_country == organization2.info_loc_country)
        self.assert_(misc == organization2.misc)
        self.assert_(personrefs == organization2.personrefs)
        self.assert_(crisisrefs == organization2.crisisrefs)
        
    def test_buildorg3(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        organization3 = Organization(elemid = "new1",
    
                                    name = "n2123",
    
                                    info_type = "stant",
                                    info_history = "sadvass",
                                    info_contacts_phone = "sdfasdc2345",
                                    info_contacts_email = "asdjhkch234",
                                    info_contacts_address = "Japan",
                                    info_contacts_city = "hates",
                                    info_contacts_state = "baka",
                                    info_contacts_country = "gaijins",
                                    info_contacts_zip = "who",
    
                                    info_loc_city = "act",
                                    info_loc_region = "like",
                                    info_loc_country = "weaboos",
    
                                    personrefs = ["sushi", "fish"],
                                    crisisrefs = ["perl harbor", "atom bombs"],
    
                                    misc = "")

        otree = SubElement(tree, "organization", {"id" : "new1"})     
        XMLHelpers.buildOrganization(otree, organization3)
        
        elemid = otree.attrib['id'],
        name = otree.find('.//name').text
        info_type = otree.find('.//info').find('.//type').text
        info_history = otree.find('.//info').find('.//history').text
        info_contacts_phone = otree.find('.//info').find('.//contact').find('.//phone').text
        info_contacts_email = otree.find('.//info').find('.//contact').find('.//email').text
        info_contacts_address = otree.find('.//info').find('.//contact').find('.//mail').find('.//address').text
        info_contacts_city = otree.find('.//info').find('.//contact').find('.//mail').find('.//city').text
        info_contacts_state = otree.find('.//info').find('.//contact').find('.//mail').find('.//state').text
        info_contacts_country = otree.find('.//info').find('.//contact').find('.//mail').find('.//country').text
        info_contacts_zip = otree.find('.//info').find('.//contact').find('.//mail').find('.//zip').text
        info_loc_city = otree.find('.//info').find('.//loc').find('.//city').text
        info_loc_region = otree.find('.//info').find('.//loc').find('.//region').text
        info_loc_country = otree.find('.//info').find('.//loc').find('.//country').text

        personrefs = [x.attrib['idref'] for x in otree.findall('.//person')]
        crisisrefs = [x.attrib['idref'] for x in otree.findall('.//crisis')]
        misc = otree.find('.//misc').text
        
        #self.assert_(elemid == organization3.elemid)
        self.assert_(name == organization3.name)
        self.assert_(info_type == organization3.info_type)
        self.assert_(info_history == organization3.info_history)
        self.assert_(info_contacts_phone == organization3.info_contacts_phone)
        self.assert_(info_contacts_email == organization3.info_contacts_email)
        self.assert_(info_contacts_address == organization3.info_contacts_address)
        self.assert_(info_contacts_city == organization3.info_contacts_city)
        self.assert_(info_contacts_state == organization3.info_contacts_state)
        self.assert_(info_contacts_country == organization3.info_contacts_country)
        self.assert_(info_contacts_zip == organization3.info_contacts_zip)
        self.assert_(info_loc_city == organization3.info_loc_city)
        self.assert_(info_loc_region == organization3.info_loc_region)
        self.assert_(info_loc_country == organization3.info_loc_country)
        self.assert_(misc == organization3.misc)
        self.assert_(personrefs == organization3.personrefs)
        self.assert_(crisisrefs == organization3.crisisrefs)
        
    def test_buildcrisis1(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        crisis1 = Crisis(

                    elemid = "hunger",
                    name = "hunger",
                    misc = "na",
                    
                    info_history = "this year",
                    info_help = "help",
                    info_resources = "awareness",
                    info_type = "hunger attack",

                    date_time = "11 am",
                    date_day = 18,
                    date_month = 03,
                    date_year = 2012,
                    date_misc = "still alive",
                    
                    location_city = "houston",
                    location_region = "texas",

                    location_country = "USA",
                    
                    impact_human_deaths = 200,
                    impact_human_displaced = 20,
                    impact_human_injured = 1,

                    impact_human_missing = 32,
                    impact_human_misc = "none",
                    
                    impact_economic_amount = 400,
                    impact_economic_currency = "yen",
                    impact_economic_misc = "misc",
                    
                    orgrefs = ["dea", "cia"],
                    personrefs = ["you", "me"]
                    )
        
        ctree = SubElement(tree, "crisis", {"id" : "hunger"})
        XMLHelpers.buildCrisis(ctree, crisis1)


        elemid = ctree.attrib['id']
        name = ctree.find('.//name').text
        misc = ctree.find('.//misc').text
        info_history = ctree.find('.//history').text
        info_help = ctree.find('.//help').text
        info_resources = ctree.find('.//resources').text
        info_type = ctree.find('.//type').text
        date_time = ctree.find('.//time').find('.//time').text
        date_day = int(ctree.find('.//time').find('.//day').text)
        date_month = int(ctree.find('.//time').find('.//month').text)
        date_year = int(ctree.find('.//time').find('.//year').text)
        date_misc = ctree.find('.//time').find('.//misc').text
        location_city = ctree.find('.//loc').find('.//city').text
        location_region = ctree.find('.//loc').find('.//region').text
        location_country = ctree.find('.//loc').find('.//country').text
        impact_human_deaths = int(ctree.find('.//impact').find('.//human').find('.//deaths').text)
        impact_human_displaced = int(ctree.find('.//impact').find('.//human').find('.//displaced').text)
        impact_human_injured = int(ctree.find('.//impact').find('.//human').find('.//injured').text)
        impact_human_missing = int(ctree.find('.//impact').find('.//human').find('.//missing').text)
        impact_human_misc = ctree.find('.//impact').find('.//human').find('.//misc').text
        impact_economic_amount = int(ctree.find('.//impact').find('.//economic').find('.//amount').text)
        impact_economic_currency = ctree.find('.//impact').find('.//economic').find('.//currency').text
        impact_economic_misc = ctree.find('.//impact').find('.//economic').find('.//misc').text
        orgrefs = [x.attrib['idref'] for x in ctree.findall('.//org')]
        personrefs = [x.attrib['idref'] for x in ctree.findall('.//person')]


        self.assert_(elemid == crisis1.elemid)
        self.assert_(name == crisis1.name)
        #self.assert_(misc == crisis1.misc)
        self.assert_(info_history == crisis1.info_history)
        self.assert_(info_help == crisis1.info_help)
        self.assert_(info_resources == crisis1.info_resources)
        self.assert_(info_type == crisis1.info_type)
        self.assert_(date_time == crisis1.date_time)
        self.assert_(date_day == crisis1.date_day)
        self.assert_(date_month == crisis1.date_month)
        self.assert_(date_year == crisis1.date_year)
        self.assert_(date_misc == crisis1.date_misc)
        self.assert_(location_city == crisis1.location_city)

        self.assert_(location_region == crisis1.location_region)
        self.assert_(location_country == crisis1.location_country)
        self.assert_(impact_human_deaths == crisis1.impact_human_deaths)
        self.assert_(impact_human_displaced == crisis1.impact_human_displaced)
        self.assert_(impact_human_injured == crisis1.impact_human_injured)
        self.assert_(impact_human_missing == crisis1.impact_human_missing)
        self.assert_(impact_human_misc == crisis1.impact_human_misc)
        #self.assert_(impact_economic_amount == crisis1.impact_econmic_amount)
        self.assert_(impact_economic_currency == crisis1.impact_economic_currency)
        self.assert_(impact_economic_misc == crisis1.impact_economic_misc)
        self.assert_(orgrefs == crisis1.orgrefs)
        self.assert_(personrefs == crisis1.personrefs)

    def test_buildcrisis2(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        crisis1 = Crisis(

                elemid = "plagues",
                name = "plagues",
                misc = "aids virus",
                
                info_history = "last year",
                info_help = "help",
                info_resources = "aids awareness",
                info_type = "virus attack",


                
                date_time = "1 pm",
                date_day = 1,
                date_month = 8,
                date_year = 1966,
                date_misc = "still happening",
                

                location_city = "LA",
                location_region = "California",

                location_country = "USA",
                
                impact_human_deaths = 20000,
                impact_human_displaced = 2540,
                impact_human_injured = 1123,

                impact_human_missing = 332,
                impact_human_misc = "none",
                
                impact_economic_amount = 442100,
                impact_economic_currency = "dollars",
                impact_economic_misc = "misc",
                
                orgrefs = ["dea", "cia"],
                personrefs = ["Magic Johnson", "me"]


                )
        ctree = SubElement(tree, "crisis", {"id" : "plagues"})
        XMLHelpers.buildCrisis(ctree, crisis1)


        elemid = ctree.attrib['id']
        name = ctree.find('.//name').text
        misc = ctree.find('.//misc').text
        info_history = ctree.find('.//history').text
        info_help = ctree.find('.//help').text
        info_resources = ctree.find('.//resources').text
        info_type = ctree.find('.//type').text
        date_time = ctree.find('.//time').find('.//time').text
        date_day = int(ctree.find('.//time').find('.//day').text)
        date_month = int(ctree.find('.//time').find('.//month').text)
        date_year = int(ctree.find('.//time').find('.//year').text)
        date_misc = ctree.find('.//time').find('.//misc').text
        location_city = ctree.find('.//loc').find('.//city').text
        location_region = ctree.find('.//loc').find('.//region').text
        location_country = ctree.find('.//loc').find('.//country').text
        impact_human_deaths = int(ctree.find('.//impact').find('.//human').find('.//deaths').text)
        impact_human_displaced = int(ctree.find('.//impact').find('.//human').find('.//displaced').text)
        impact_human_injured = int(ctree.find('.//impact').find('.//human').find('.//injured').text)
        impact_human_missing = int(ctree.find('.//impact').find('.//human').find('.//missing').text)
        impact_human_misc = ctree.find('.//impact').find('.//human').find('.//misc').text
        impact_economic_amount = int(ctree.find('.//impact').find('.//economic').find('.//amount').text)
        impact_economic_currency = ctree.find('.//impact').find('.//economic').find('.//currency').text
        impact_economic_misc = ctree.find('.//impact').find('.//economic').find('.//misc').text
        orgrefs = [x.attrib['idref'] for x in ctree.findall('.//org')]
        personrefs = [x.attrib['idref'] for x in ctree.findall('.//person')]


        self.assert_(elemid == crisis1.elemid)
        self.assert_(name == crisis1.name)
        #self.assert_(misc == crisis1.misc)
        self.assert_(info_history == crisis1.info_history)
        self.assert_(info_help == crisis1.info_help)
        self.assert_(info_resources == crisis1.info_resources)
        self.assert_(info_type == crisis1.info_type)
        self.assert_(date_time == crisis1.date_time)
        self.assert_(date_day == crisis1.date_day)
        self.assert_(date_month == crisis1.date_month)
        self.assert_(date_year == crisis1.date_year)
        self.assert_(date_misc == crisis1.date_misc)
        self.assert_(location_city == crisis1.location_city)

        self.assert_(location_region == crisis1.location_region)
        self.assert_(location_country == crisis1.location_country)
        self.assert_(impact_human_deaths == crisis1.impact_human_deaths)
        self.assert_(impact_human_displaced == crisis1.impact_human_displaced)
        self.assert_(impact_human_injured == crisis1.impact_human_injured)
        self.assert_(impact_human_missing == crisis1.impact_human_missing)
        self.assert_(impact_human_misc == crisis1.impact_human_misc)
        #self.assert_(impact_economic_amount == crisis1.impact_econmic_amount)
        self.assert_(impact_economic_currency == crisis1.impact_economic_currency)
        self.assert_(impact_economic_misc == crisis1.impact_economic_misc)
        self.assert_(orgrefs == crisis1.orgrefs)
        self.assert_(personrefs == crisis1.personrefs)
        
    def test_buildcrisis3(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        crisis1 = Crisis(

                elemid = "blank",
                name = "",
                misc = "",
                
                info_history = "",
                info_help = "",
                info_resources = "",
                info_type = "",


                
                date_time = "",
                date_day = 0,
                date_month = 0,
                date_year = 20,
                date_misc = "",
                

                location_city = "",
                location_region = "",

                location_country = "",
                
                impact_human_deaths = 0,
                impact_human_displaced = 0,
                impact_human_injured = 0,

                impact_human_missing = 0,
                impact_human_misc = "",
                
                impact_economic_amount = 0,
                impact_economic_currency = "",
                impact_economic_misc = "",
                
                orgrefs = ["", ""],
                personrefs = ["", ""]


                )
        ctree = SubElement(tree, "crisis", {"id" : "blank"})
        XMLHelpers.buildCrisis(ctree, crisis1)


        elemid = ctree.attrib['id']
        name = ctree.find('.//name').text
        misc = ctree.find('.//misc').text
        info_history = ctree.find('.//history').text
        info_help = ctree.find('.//help').text
        info_resources = ctree.find('.//resources').text
        info_type = ctree.find('.//type').text
        date_time = ctree.find('.//time').find('.//time').text
        date_day = int(ctree.find('.//time').find('.//day').text)
        date_month = int(ctree.find('.//time').find('.//month').text)
        date_year = int(ctree.find('.//time').find('.//year').text)
        date_misc = ctree.find('.//time').find('.//misc').text
        location_city = ctree.find('.//loc').find('.//city').text
        location_region = ctree.find('.//loc').find('.//region').text
        location_country = ctree.find('.//loc').find('.//country').text
        impact_human_deaths = int(ctree.find('.//impact').find('.//human').find('.//deaths').text)
        impact_human_displaced = int(ctree.find('.//impact').find('.//human').find('.//displaced').text)
        impact_human_injured = int(ctree.find('.//impact').find('.//human').find('.//injured').text)
        impact_human_missing = int(ctree.find('.//impact').find('.//human').find('.//missing').text)
        impact_human_misc = ctree.find('.//impact').find('.//human').find('.//misc').text
        impact_economic_amount = int(ctree.find('.//impact').find('.//economic').find('.//amount').text)
        impact_economic_currency = ctree.find('.//impact').find('.//economic').find('.//currency').text
        impact_economic_misc = ctree.find('.//impact').find('.//economic').find('.//misc').text
        orgrefs = [x.attrib['idref'] for x in ctree.findall('.//org')]
        personrefs = [x.attrib['idref'] for x in ctree.findall('.//person')]


        self.assert_(elemid == crisis1.elemid)
        self.assert_(name == crisis1.name)
        self.assert_(misc == crisis1.misc)
        self.assert_(info_history == crisis1.info_history)
        self.assert_(info_help == crisis1.info_help)
        self.assert_(info_resources == crisis1.info_resources)
        self.assert_(info_type == crisis1.info_type)
        self.assert_(date_time == crisis1.date_time)
        self.assert_(date_day == crisis1.date_day)
        self.assert_(date_month == crisis1.date_month)
        self.assert_(date_year == crisis1.date_year)
        self.assert_(date_misc == crisis1.date_misc)
        self.assert_(location_city == crisis1.location_city)

        self.assert_(location_region == crisis1.location_region)
        self.assert_(location_country == crisis1.location_country)
        self.assert_(impact_human_deaths == crisis1.impact_human_deaths)
        self.assert_(impact_human_displaced == crisis1.impact_human_displaced)
        self.assert_(impact_human_injured == crisis1.impact_human_injured)
        self.assert_(impact_human_missing == crisis1.impact_human_missing)
        self.assert_(impact_human_misc == crisis1.impact_human_misc)
        #self.assert_(impact_economic_amount == crisis1.impact_econmic_amount)
        self.assert_(impact_economic_currency == crisis1.impact_economic_currency)
        self.assert_(impact_economic_misc == crisis1.impact_economic_misc)
        self.assert_(orgrefs == crisis1.orgrefs)
        self.assert_(personrefs == crisis1.personrefs)

    def test_exportlinks1(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        person1 = Person(elemid = "bobs",
                   name = "Bob",
                   info_type = "Salamander",
                   info_birthdate_time = "12:00PM",
                   info_birthdate_day = 12,
                   info_birthdate_month = 12,
                   info_birthdate_year = 1900,
                   info_birthdate_misc = "born under the full moon...",
                   info_nationality = "Swedish",
                   info_biography = "Bob swam a lot, as salamanders do...",
                   
                   orgrefs = ["salamanders united", "salamander liberation front"],
                   crisisrefs = ["swamp famine", "west swamp drought"])
        ptree = SubElement(tree, "person", {"id" : "bobs"})     
        XMLHelpers.buildPerson(ptree, person1)
        
        link1 = Link(link_parent = "bobs",
                    link_type = "salad",
                    title = "don't click me!!!",
                    link_url = "http://www.nevergohere.com",
                    description = "you really shouldn't go there...",
                    link_site = "a bad place")
        
        XMLHelpers.link_list.append(link1)
        
        XMLHelpers.exportLinks(person1, ptree)

        new_link = Link()
        for ref in ptree.findall('.//ref'):
            for l in ref:
                new_link = Link()
                if (l.tag):
                    new_link.link_type = l.tag
                if (l.find('./site') != None):
                    new_link.link_site = l.find('./site').text
                if (l.find('./title') != None):
                    new_link.title = l.find('./title').text
                if (l.find('./url') != None):
                    new_link.link_url = db.Link(l.find('./url').text)
                if (l.find('./description') != None):
                    new_link.description = l.find('./description').text

                new_link.link_parent = ptree.attrib['id']
                
                self.assertEqual(new_link.link_type , link1.link_type)
                self.assert_(new_link.link_site == link1.link_site)
                self.assert_(new_link.title == link1.title)
                self.assert_(new_link.link_url == link1.link_url)
                self.assert_(new_link.description == link1.description)
                self.assert_(new_link.link_parent == link1.link_parent)
        
    def test_exportlinks2(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        
        organization1 = Organization(elemid = "Franch",
    
                                    name = "French pride",
    
                                    info_type = "non-existant",
                                    info_history = "white flags",
                                    info_contacts_phone = "1234567890",
                                    info_contacts_email = "omuledu@fromage.com",
                                    info_contacts_address = "French",
                                    info_contacts_city = "Paris",
                                    info_contacts_state = "Canada",
                                    info_contacts_country = "USA",
                                    info_contacts_zip = "7890",
    
                                    info_loc_city = "Alaska",
                                    info_loc_region = "Ukraine",
                                    info_loc_country = "Antarctica",
    
                                    personrefs = ["baquettes", "crumpets"],
                                    crisisrefs = ["war", "nazis"],
    
                                    misc = "")

        otree = SubElement(tree, "organization", {"id" : "Franch"})
        XMLHelpers.buildOrganization(otree, organization1)
        
        
        link1 = Link(link_parent = "Franch",
                    link_type = "salad",
                    title = "don't click me!!!",
                    link_url = "http://www.nevergohere.com",
                    description = "you really shouldn't go there...",
                    link_site = "a bad place")
        XMLHelpers.link_list = []
        XMLHelpers.link_list.append(link1)
        
        XMLHelpers.exportLinks(organization1, otree)
        
        for ref in otree.findall('.//ref'):
            for l in ref:
                new_link = Link()
                if (l.tag):
                    new_link.link_type = l.tag
                if (l.find('./site') != None):
                    new_link.link_site = l.find('./site').text
                if (l.find('./title') != None):
                    new_link.title = l.find('./title').text
                if (l.find('./url') != None):
                    new_link.link_url = db.Link(l.find('./url').text)
                if (l.find('./description') != None):
                    new_link.description = l.find('./description').text
                new_link.link_parent = otree.attrib['id']
                
                self.assert_(new_link.link_type == link1.link_type)
                self.assert_(new_link.link_site == link1.link_site)
                self.assert_(new_link.title == link1.title)
                self.assert_(new_link.link_url == link1.link_url)
                self.assert_(new_link.description == link1.description)
                self.assertEqual(new_link.link_parent, link1.link_parent)
        
    def test_exportlinks3(self):
        tree = Element("worldCrises", {"xmlns:xsi" : "http://www.w3.org/2001/XMLSchema-instance", "xsi:noNamespaceSchemaLocation" : "wc.xsd"})
        crisis1 = Crisis(elemid = "hunger",
                    name = "hunger",
                    misc = "na",
                    
                    info_history = "this year",
                    info_help = "help",
                    info_resources = "awareness",
                    info_type = "hunger attack",
                    
                    date_time = "11 am",
                    date_day = 18,
                    date_month = 03,
                    date_year = 2012,
                    date_misc = "still alive",
                    
                    location_city = "houston",
                    location_region = "texas",
                    location_country = "USA",
                    
                    impact_human_deaths = 200,
                    impact_human_displaced = 20,
                    impact_human_injured = 1,
                    impact_human_missing = 32,
                    impact_human_misc = "none",
                    
                    impact_economic_amount = 400,
                    impact_economic_currency = "yen",
                    impact_economic_misc = "misc",
                    
                    orgrefs = ["dea", "cia"],
                    personrefs = ["you", "me"])
                                
         
                                
                                
        ctree = SubElement(tree, "crisis", {"id" : "hunger"})     
        XMLHelpers.buildCrisis(ctree, crisis1)
        
        
        link1 = Link(link_parent = "hunger",
                    link_type = "salad",
                    title = "don't click me!!!",
                    link_url = "http://www.nevergohere.com",
                    description = "you really shouldn't go there...",
                    link_site = "a bad place")
                    
        XMLHelpers.link_list = []
        XMLHelpers.link_list.append(link1)
        
        XMLHelpers.exportLinks(crisis1, ctree)
        
        for ref in ctree.findall('.//ref'):
            for l in ref:
                new_link = Link()
                if (l.tag):
                    new_link.link_type = l.tag
                if (l.find('./site') != None):
                    new_link.link_site = l.find('./site').text
                if (l.find('./title') != None):
                    new_link.title = l.find('./title').text
                if (l.find('./url') != None):
                    new_link.link_url = db.Link(l.find('./url').text)
                if (l.find('./description') != None):
                    new_link.description = l.find('./description').text
                new_link.link_parent = ctree.attrib['id']
                
                self.assert_(new_link.link_type == link1.link_type)
                self.assert_(new_link.link_site == link1.link_site)
                self.assert_(new_link.title == link1.title)
                self.assert_(new_link.link_url == link1.link_url)
                self.assert_(new_link.description == link1.description)

                self.assertEqual(new_link.link_parent, link1.link_parent)

class ImportTests(unittest.TestCase):        
    
    def test_validxml1(self):
        xml_file = open("test/test_instance1.xml",'r')
        file_contents = xml_file.read()

        b = XMLHelpers.validXML(file_contents, 'wc.xsd')
        self.assertTrue(b)
    def test_validxml2(self):
        xml_file = open("test/test_instance2.xml",'r')
        file_contents = xml_file.read()

        b = XMLHelpers.validXML(file_contents, 'wc.xsd')
        self.assertEqual(b, True)
    def test_validxml3(self):
        xml_file = open("test/test_instance3.xml",'r')
        file_contents = xml_file.read()

        b = XMLHelpers.validXML(file_contents, 'wc.xsd')
        self.assert_(b == True)

    
    def test_addperson1(self):
        xml_file = open("test/test_add1.xml", 'rb')
        tree = ElementTree.parse(xml_file)

        people = tree.findall(".//person")
        for person in people:
            if (person.find('.//info')):
                test_list = XMLHelpers.addPerson(person)
        
        self.assertEqual(len(test_list),3)
        test_list[:] = []
        
    def test_addperson2(self):
        xml_file = open("test/test_add2.xml", 'rb')
        tree = ElementTree.parse(xml_file)

        people = tree.findall(".//person")
        for person in people:
            if (person.find('.//info')):
                test_list = XMLHelpers.addPerson(person)
        
        self.assertEqual(len(test_list),2)
        test_list[:] = []
        
    def test_addperson3(self):
        xml_file = open("test/test_add3.xml", 'rb')
        tree = ElementTree.parse(xml_file)
        test_list = []
        people = tree.findall(".//person")
        for person in people:
            if (person.find('.//info')):
                test_list = XMLHelpers.addPerson(person)
        
        self.assertEqual(len(test_list),0)
        test_list[:] = []
        
        
    def test_addorg1(self):
        xml_file = open("test/test_add1.xml", 'rb')
        tree = ElementTree.parse(xml_file)

        orgs = tree.findall(".//organization")
        for org in orgs:
            if (org.find('.//info')):
                test_list = XMLHelpers.addOrganization(org)
        self.assertEqual(len(test_list),3)
        test_list[:] = []

    def test_addorg2(self):
        xml_file = open("test/test_add2.xml", 'rb')
        tree = ElementTree.parse(xml_file)

        orgs = tree.findall(".//organization")
        for org in orgs:
            if (org.find('.//info')):
                test_list = XMLHelpers.addOrganization(org)
        self.assertEqual(len(test_list),2)
        test_list[:] = []
    
    def test_addorg3(self):
        xml_file = open("test/test_add3.xml", 'rb')
        tree = ElementTree.parse(xml_file)
        test_list = []
        orgs = tree.findall(".//organization")
        for org in orgs:
            if (org.find('.//info')):
                test_list = XMLHelpers.addOrganization(org)
        self.assertEqual(len(test_list),0)
        test_list[:] = []


    def test_addcrisis1(self):
        xml_file = open("test/test_add1.xml", 'rb')
        tree = ElementTree.parse(xml_file)

        crises = tree.findall(".//crisis")
        for crisis in crises:
            if (crisis.find('.//info')):
                test_list = XMLHelpers.addCrisis(crisis)

        self.assertEqual(len(test_list),3)
        test_list[:] = []

    def test_addcrisis2(self):
        xml_file = open("test/test_add2.xml", 'rb')
        tree = ElementTree.parse(xml_file)
        crises = tree.findall(".//crisis")

        for crisis in crises:
            if (crisis.find('.//info')):
                test_list = XMLHelpers.addCrisis(crisis)

        self.assertEqual(len(test_list),2)
        test_list[:] = []

    def test_addcrisis3(self):
        xml_file = open("test/test_add3.xml", 'rb')
        tree = ElementTree.parse(xml_file)
        crises = tree.findall(".//crisis")
        test_list = []
        for crisis in crises:
            if (crisis.find('.//info')):
                test_list = XMLHelpers.addCrisis(crisis)
        self.assertEqual(len(test_list),0)
        test_list[:] = []

            
    def test_grablinks1(self):
        XMLHelpers.clearGlobals()
        crisis = Element("crisis", {"id" : "wow"})
        ref = SubElement(crisis, "ref")
        img = SubElement(ref, "image")
        site = SubElement(img, "site")
        site.text = "i'm a site"
        title = SubElement(img, "title")
        title.text = "i'm a title"
        url = SubElement(img, "url")
        url.text = "i'm a url"
        description = SubElement(img, "description")
        description.text = "i'm a description"
        
        temp = XMLHelpers.grabLinks(crisis)
        self.assert_(temp[0].link_site == "i'm a site")
        XMLHelpers.clearGlobals()
        
    def test_grablinks2(self):
        XMLHelpers.clearGlobals()
        person = Element("person", {"id" : "globetrotter"})
        ref = SubElement(person, "ref")
        img = SubElement(ref, "image")
        site = SubElement(img, "site")
        site.text = "i'm a site"
        title = SubElement(img, "title")
        title.text = "i'm a title"
        url = SubElement(img, "url")
        url.text = "i'm a url"
        description = SubElement(img, "description")
        description.text = "i'm a description"
        
        img2 = SubElement(ref, "video")
        site2 = SubElement(img, "site")
        site2.text = "youtube"
        title2 = SubElement(img, "title")
        title2.text = "dancing cats"
        url2 = SubElement(img, "url")
        url2.text = "http://youtube.com/watch?v=si7f8f7tiuhsfi"
        description2 = SubElement(img, "description")
        description2.text = "the cats are dancing!!!"
        
        temp = XMLHelpers.grabLinks(person)
        self.assert_(len(temp) == 2)
        XMLHelpers.clearGlobals()
        
    def test_grablinks3(self):
        XMLHelpers.clearGlobals()
        person = Element("person", {"id" : "globetrotter"})
        temp = XMLHelpers.grabLinks(person)
        self.assert_(len(temp) == 0)
        XMLHelpers.clearGlobals()
        
