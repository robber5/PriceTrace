#!/usr/bin/python  
# -*- coding: utf-8 -*-
import os
import time
from models import *
from settings import *


def main():
	cl = [JD(), Gome(), Suning(), Yhd()]
	for x in cl:
		x.fetchAll()


if __name__ == '__main__':
	if not os.path.exists(db_file):
		Base.metadata.create_all(engine)
	main()
