#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from StringIO import StringIO
from google.appengine.ext.webapp import Request
from google.appengine.ext.webapp import Response
from google.appengine.ext.webapp import RequestHandler
from main import Export
from main import Schema
from main import Import
from main import ImportSchema
from Models import *

class Test(unittest.TestCase):
    
    def testExternal1(self):
	d = External(dummy = 'peep')
	self.assert_(d.dummy == 'peep')
    
    def testExternal2(self):
	d = External(dummy = 'peeps')
	self.assert_(d.dummy == 'peeps')
    
    def testExternal3(self):
	d = External(dummy = 'peept')
	self.assert_(d.dummy == 'peept')
    
    def testImage1(self):
	d = Image(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', caption = 'chris boy')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(d.caption == 'chris boy')
    
    def testImage2(self):
	d = Image(link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX', caption = 'steve jobs')
	self.assert_(d.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(d.caption == 'steve jobs')
    
    def testImage3(self):
	d = Image(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw', caption = 'Scarlet jo')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(d.caption == 'Scarlet jo')
	
    def testVideo1(self):
	d = Video(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', caption = 'chris boy')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(d.caption == 'chris boy')
	
    def testVideo2(self):
	d = Video(link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX', caption = 'steve jobs')
	self.assert_(d.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(d.caption == 'steve jobs')
	
    def testVideo3(self):
	d = Video(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw', caption = 'Scarlet jo')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(d.caption == 'Scarlet jo')
	
    def testSocial1(self):
	d = Social(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', title = 'chris boy')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(d.title == 'chris boy')
	
    def testSocial2(self):
	d = Social(link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX', title = 'steve jobs')
	self.assert_(d.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(d.title == 'steve jobs')
	
    def testSocial3(self):
	d = Social(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw', title = 'Scarlet jo')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(d.title == 'Scarlet jo')
	
    def testExtLink1(self):
	d = ExtLink(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', title = 'chris boy')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(d.title == 'chris boy')
	
    def testExtLink2(self):
	d = ExtLink(link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX', title = 'steve jobs')
	self.assert_(d.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(d.title == 'steve jobs')
	
    def testExtLink3(self):
	d = ExtLink(link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw', title = 'Scarlet jo')
	self.assert_(d.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(d.title == 'Scarlet jo')
	
	
    def testPerson1(self) :
        e = Person(name = 'whatever', kind_ = 'politician', location = 'bobwai', description = 'tapeworm', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['lovelybones', 'bottle-neck', 'shooe-box'], relatedCrises = ['alfred', 'john', 'jacob'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'whatever')
	self.assert_(e.kind_ == 'politician')
	self.assert_(e.location == 'bobwai')
	self.assert_(e.description == 'tapeworm')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['lovelybones', 'bottle-neck', 'shooe-box'])
	self.assert_(e.relatedCrises == ['alfred', 'john', 'jacob'])
	
	
    def testPerson2(self) :
        e = Person(name = 'jacob', kind_ = 'werewolf', location = 'quillete', description = 'muscular', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['swaddle', 'pillow', 'shooed-box'], relatedCrises = ['nerd', 'geek', 'dope'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'jacob')
	self.assert_(e.kind_ == 'werewolf')
	self.assert_(e.location == 'quillete')
	self.assert_(e.description == 'muscular')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['swaddle', 'pillow', 'shooed-box'])
	self.assert_(e.relatedCrises == ['nerd', 'geek', 'dope'])
	
	
    def testPerson3(self) :
        e = Person(name = 'edward', kind_ = 'vampire', location = 'forks', description = 'skinny', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['lovelybones2', 'bottle-neck2', 'shooe-box2'], relatedCrises = ['mobi', 'mafi', 'feefee'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'edward')
	self.assert_(e.kind_ == 'vampire')
	self.assert_(e.location == 'forks')
	self.assert_(e.description == 'skinny')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['lovelybones2', 'bottle-neck2', 'shooe-box2'])
	self.assert_(e.relatedCrises == ['mobi', 'mafi', 'feefee'])

    def testCrisis1(self) :
	e = Crisis(name = 'whatever', kind_ = 'politician', location = 'bobwai', description = 'tapeworm', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['lovelybones', 'bottle-neck', 'shooe-box'], relatedPeople = ['alfred', 'john', 'jacob'])
	self.assert_(e.name == 'whatever')
	self.assert_(e.kind_ == 'politician')
	self.assert_(e.location == 'bobwai')
	self.assert_(e.description == 'tapeworm')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['lovelybones', 'bottle-neck', 'shooe-box'])
	self.assert_(e.relatedPeople == ['alfred', 'john', 'jacob'])
	
	
    def testCrisis2(self) :
        e = Crisis(name = 'jacob', kind_ = 'werewolf', location = 'quillete', description = 'muscular', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['swaddle', 'pillow', 'shooed-box'], relatedPeople = ['nerd', 'geek', 'dope'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'jacob')
	self.assert_(e.kind_ == 'werewolf')
	self.assert_(e.location == 'quillete')
	self.assert_(e.description == 'muscular')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['swaddle', 'pillow', 'shooed-box'])
	self.assert_(e.relatedPeople == ['nerd', 'geek', 'dope'])
	
	
    def testCrisis3(self) :
        e = Crisis(name = 'edward', kind_ = 'vampire', location = 'forks', description = 'skinny', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', relatedOrganizations = ['lovelybones2', 'bottle-neck2', 'shooe-box2'], relatedPeople = ['mobi', 'mafi', 'feefee'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'edward')
	self.assert_(e.kind_ == 'vampire')
	self.assert_(e.location == 'forks')
	self.assert_(e.description == 'skinny')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.relatedOrganizations == ['lovelybones2', 'bottle-neck2', 'shooe-box2'])
	self.assert_(e.relatedPeople == ['mobi', 'mafi', 'feefee'])
    
    def testWayToHelp1(self):
	w = WayToHelp(way = 'bobble', link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(w.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(w.way == 'bobble')
    
    def testWayToHelp2(self):
	w = WayToHelp(way = 'bobble2', link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(w.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(w.way == 'bobble2')
    
    def testWayToHelp3(self):
	w = WayToHelp(way = 'bobble3', link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(w.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(w.way == 'bobble3')
	
    def testResourceNeeded1(self):
	w = ResourceNeeded(resource = 'bobble', link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(w.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(w.resource == 'bobble')
	
    def testResourceNeeded2(self):
	w = ResourceNeeded(resource = 'bobble2', link = 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(w.link == 'https://www.google.com/imgres?imgurl=http://thiwaratri-resort.com/uploads/posts/2011-12/1322751142_steve-jobs11.jpg&imgrefurl=http://praxiscoaching.com/?tag%3Dsteve-jobs&h=162&w=243&sz=4&tbnid=tPq9WYO88Q16EM&tbnh=0&tbnw=0&zoom=1&usg=__LsYC4t9aVaHVl2ahx4zAKmDCeCI=&docid=YDAPKMnvKfWOAM&sa=X&ei=TkzxT8n8MOnC2wXJzMGxCg&ved=0CKMBENUX')
	self.assert_(w.resource == 'bobble2')
	
    def testResourceNeeded3(self):
	w = ResourceNeeded(resource = 'bobble3', link = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(w.link == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS9-hUng68q1qyaBn5NqKZCoCaJInaqNhEbSL4JcREloEHS2zLGPw')
	self.assert_(w.resource == 'bobble3')
	
    def testHumanImpact1(self):
	w = HumanImpact(amount = 98, kind_ = 'badness')
	self.assert_(w.amount == 98)
	self.assert_(w.kind_ == 'badness')
	
    def testHumanImpact2(self):
	w = HumanImpact(amount = 444444, kind_ = 'cesarian')
	self.assert_(w.amount == 444444)
	self.assert_(w.kind_ == 'cesarian')
	
    def testHumanImpact3(self):
	w = HumanImpact(amount = 12340987, kind_ = 'tabletop')
	self.assert_(w.amount == 12340987)
	self.assert_(w.kind_ == 'tabletop')
	
    def testEconomicImpact(self):
	w = EconomicImpact(amount = 98.55, kind_ = 'badness')
	self.assert_(w.amount == 98.55)
	self.assert_(w.kind_ == 'badness')
	
    def testEconomicImpact2(self):
	w = EconomicImpact(amount = 101.3333, kind_ = 'dribble')
	self.assert_(w.amount == 101.3333)
	self.assert_(w.kind_ == 'dribble')
	
    def testEconomicImpact3(self):
	w = EconomicImpact(amount = 42424.21, kind_ = 'frontloader')
	self.assert_(w.amount == 42424.21)
	self.assert_(w.kind_ == 'frontloader')
    
    def testOrganization1(self):
	e = Organization(name = 'whatever', kind_ = 'politician', location = 'bobwai', description = 'tapeworm', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'chris hemsworth', contactInfo = 'callMe', relatedCrises = ['lovelybones', 'bottle-neck', 'shooe-box'], relatedPeople = ['alfred', 'john', 'jacob'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'whatever')
	self.assert_(e.kind_ == 'politician')
	self.assert_(e.location == 'bobwai')
	self.assert_(e.description == 'tapeworm')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.primaryCaption == 'chris hemsworth')
	self.assert_(e.contactInfo == 'callMe')
	self.assert_(e.relatedCrises == ['lovelybones', 'bottle-neck', 'shooe-box'])
	self.assert_(e.relatedPeople == ['alfred', 'john', 'jacob'])
    
    def testOrganization2(self):
	e = Organization(name = 'redhatorg', kind_ = 'fashion', location = 'zimbabwe', description = 'apple red hats dance in a water fall', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'jacobo', contactInfo = '2121212 deacon Lodge, el Paso, tx', relatedCrises = ['swaddle', 'pillow', 'shooed-box'], relatedPeople = ['nerd', 'geek', 'dope'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'redhatorg')
	self.assert_(e.kind_ == 'fashion')
	self.assert_(e.location == 'zimbabwe')
	self.assert_(e.description == 'apple red hats dance in a water fall')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.primaryCaption == 'jacobo')
	self.assert_(e.contactInfo == '2121212 deacon Lodge, el Paso, tx')
	self.assert_(e.relatedCrises == ['swaddle', 'pillow', 'shooed-box'])
	self.assert_(e.relatedPeople == ['nerd', 'geek', 'dope'])
    
    def testOrganization3(self):
	e = Organization(name = 'alderonFront', kind_ = 'jango-bosc', location = 'rankoor', description = 'chubby-sand-worm', primaryImage = 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg', primaryCaption = 'lieber', contactInfo = '555 melrose , compton, LA', relatedCrises = ['lovelybones2', 'bottle-neck2', 'shooe-box2'], relatedPeople = ['mobi', 'mafi', 'feefee'])
	#e.relatedCrises = ['katrina', '9/11']
	self.assert_(e.name == 'alderonFront')
	self.assert_(e.kind_ == 'jango-bosc')
	self.assert_(e.location == 'rankoor')
	self.assert_(e.description == 'chubby-sand-worm')
	self.assert_(e.primaryImage == 'https://encrypted-tbn1.google.com/images?q=tbn:ANd9GcS733X56RY6_7s3quyooRGMbma2M01QF7q_MWbGJDG37YCPEKBMpg')
	self.assert_(e.primaryCaption == 'lieber')
	self.assert_(e.contactInfo == '555 melrose , compton, LA')
	self.assert_(e.relatedCrises == ['lovelybones2', 'bottle-neck2', 'shooe-box2'])
	self.assert_(e.relatedPeople == ['mobi', 'mafi', 'feefee'])
	
    def test_Schema1(self):
        j = Schema(schema = 'why the hell-o')
        self.assert_(j.schema == 'why the hell-o')
       
    def test_Schema2(self):
        j = Schema(schema = 'fleece the sheep')
        self.assert_(j.schema == 'fleece the sheep')
       
    def test_Schema3(self):
        j = Schema(schema = 'the rabbits in the hat')
        self.assert_(j.schema == 'the rabbits in the hat')
       
    def test_Import_post(self):
        handler = Import()
        self.assert_(issubclass(type(handler), RequestHandler))
