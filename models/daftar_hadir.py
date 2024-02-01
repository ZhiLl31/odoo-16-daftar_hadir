from odoo import models, fields, api

class DaftarHadir(models.Model):
	_name = 'cep.daftar.hadir'
	_description = 'Daftar Hadir'

	nama = fields.Char(string='Nama')
	user_id = fields.Many2one(comodel_name='res.users', string='User ID')
	check_in = fields.Datetime(string='Tanggal & Jam Masuk')
	check_out = fields.Datetime(string='Tanggal & Jam Keluar')
	location = fields.Selection(string='Lokasi', selection=[('kantor 1', 'Kantor 1'), ('kantor 2', 'Kantor 2'),])
	state = fields.Selection(string='Status', selection=[('draft', 'Masuk'), ('confirm', 'Keluar'),('done', 'Selesai')],default='draft', tracking=True)
	kode_unik = fields.Char(string='Kode Unik')

	@api.constrains('kode_unik')
	def _check_kode_unik(self):
			for record in self:
				if record.kode_unik and not record.kode_unik.isdigit():
					raise models.ValidationError('Kode Unik harus angka')
		
	def action_confirm(self):
			self.state='confirm'
				
	def action_done(self):
			self.state='done'

	def action_draft(self):
			self.state='draft'

