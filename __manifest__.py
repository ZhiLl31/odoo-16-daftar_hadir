# -*- coding: utf-8 -*-
{
	'name': "daftar_hadir",

	'summary': """
		Daftar Hadir""",

	'description': """
		Membuat aplikasi sederhana untuk Daftar Hadir
	""",

	'author': "My Company",
	'website': "https://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '16.0.1',

	# any module necessary for this one to work correctly
	'depends': ['base'],

	# always loaded
	'data': [
		'security/groups.xml',
		'security/ir.model.access.csv',
		# 'views/views.xml',
		# 'views/templates.xml',
		'views/daftar_hadir.xml',
		'views/menu_daftar_hadir.xml',
	],
	# only loaded in demonstration mode
	'demo': [
		# 'demo/demo.xml',
	],
}