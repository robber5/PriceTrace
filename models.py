#!/usr/bin/python  
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
#from sqlalchemy import create_engine
#from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, DECIMAL, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from datetime import *

db_file = 'price.db'
engine = create_engine('sqlite:///' + db_file)
engine.echo = False  # Try changing this to True and see what happens
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
	__tablename__ = 'item'
	id			= Column(Integer, primary_key=True, autoincrement=True)
	name 		= Column(String(200))
	thumb 		= Column(String(200))
	description	= Column(String(512))
	pub_date	= Column(DateTime, default=datetime.utcnow)
	vendorid	= Column(Integer, ForeignKey('vendor.id'))
	propertyid	= Column(Integer, ForeignKey('attribute.id'))

	def new(self):
		session.add(self)
		session.commit()
		return self

	def update(self):
		session.commit()
		return self

	def remove(self):
		session.delete(self)
		session.commit()
		return self


class Attribute(Base):
	__tablename__ = 'attribute'
	id			= Column(Integer, primary_key=True, autoincrement=True)
	name 		= Column(String(200))
	value 		= Column(String(200))
	pub_date	= Column(DateTime, default=datetime.utcnow)
	itemid		= Column(Integer, ForeignKey('item.id'))

	def new(self):
		session.add(self)
		session.commit()
		return self

	def update(self):
		session.commit()
		return self

	def remove(self):
		session.delete(self)
		session.commit()
		return self

class Vendor(Base):
	__tablename__ = 'vendor'
	id			= Column(Integer, primary_key=True, autoincrement=True)
	name 		= Column(String(20))
	tag 		= Column(String(200))
	url 		= Column(String(1024))
	description	= Column(String(1024))

	pub_date= Column(DateTime, default=datetime.utcnow)

	def new(self):
		session.add(self)
		session.commit()
		return self

	def update(self):
		session.commit()
		return self

	def remove(self):
		session.delete(self)
		session.commit()
		return self


class Price(Base):
	__tablename__ = 'price'
	id		= Column(Integer, primary_key=True, autoincrement=True)
	price	= Column(String(20))
	pub_date= Column(DateTime, default=datetime.utcnow)
	vendorid= Column(Integer, ForeignKey('iphone.id'))

	def new(self):
		session.add(self)
		session.commit()
		return self

	def update(self):
		session.commit()
		return self

	def remove(self):
		session.delete(self)
		session.commit()
		return self


class Iphone(Base):
	__tablename__ = 'iphone'
	id		= Column(Integer, primary_key=True, autoincrement=True)
	age 	= Column(Integer)
	model	= Column(String(20))
	memory	= Column(String(20))
	color	= Column(String(20))
	pub_date= Column(DateTime, default=datetime.utcnow)
	vendorid= Column(Integer, ForeignKey('vendor.id'))
	#vendor		= relationship('Vendor')


	def new(self):
		session.add(self)
		session.commit()
		return self

	def update(self):
		session.commit()
		return self

	def remove(self):
		session.delete(self)
		session.commit()
		return self




		