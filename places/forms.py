from django.forms import (
	ModelForm, HiddenInput, ValidationError
)

from places.models import Place

class PlaceCreationForm(ModelForm):
	class Meta:
		model = Place
		fields = (
			'name',
			'coordinates',
			'category',
			'has_wifi',
			'telephone',
			'description',
		)
		widgets = {
			'coordinates': HiddenInput
		}

	def clean_coordinates(self):
		coords = self.cleaned_data['coordinates']

		try:
			lat, lng = coords.split(',')
			lat = float(lat)
			lng = float(lng)

			if (
				lat < -90 or lat > 90 or
				lng < -180 or lng > 180
			):
				raise ValidationError('Geçerli bir koordinat girin.')

		except ValueError:
			raise ValidationError('Koordinat girin.')

		return self.cleaned_data
