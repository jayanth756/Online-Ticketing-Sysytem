class Audience(models.Model):
	name=models.CharField(max_length=50,null=True)
	age=models.IntegerField()
	gender=models.CharField(max_length=6,null=True)
	phoneno=models.CharField(max_length=10,null=True)
	email=models.EmailField(max_length=200,null=True)
	address=models.TextField()
	date_registed=models.DateTimeField(auto_now_add=True)
	updated_date=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.phoneno


class Tags(models.Model):
	name=models.CharField(max_length=100)

	def __str__ (self):
		return self.name



class Genre(models.Model):
	name=models.CharField(max_length=100,null=True)

   	def __str__(self):
   		return self.name


class Artists(models.Model):
	name=models.CharField(max_length=100,null=True)
	genre_name=models.ForeignKey(Genre,null=True,on_delete=models.CASCADE)


	def __str__(self):
		return self.name


class Venue(models.Model):
	location=models.PointField()
	address=models.TextField()
	city=models.CharField(max_length=100)

	def __str__(self):
		return self.city



class Concert(models.Model):
	CATEGORY=(
			('Indoor', 'Indoor'),
			('Outdoor',	'Outdoor'),
			)
	name=models.CharField(max_length=10)
	price=models.FloatField()
	category=models.CharField(max_length=100,choices=CATEGORY)
	description=models.CharField(max_length=200,blank=True)
	date_event=models.DateTimeField(auto_now_add=True)
	updated_date=models.DateTimeField(auto_now_add=True)
	tags=models.ManyToManyField(Tag)
	artist_name=models.ForeignKey(Artists,null=True,on_delete=models.CASCADE)
	genre_name=models.ForeignKey(Genre,null=True,on_delete=models.CASCADE)
	venue_name=models.ManyToManyField(Venue)

	def __str__(self):
		return self.name


class Tickets(models.Model):
	STATUS=(
		('Pending','Pending')
		('Confirmed','Confirmed')
		)
	audience=models.ForeignKey(Audience,null=true,on_delete=models.CASCADE)
	concert=models.ForeignKey(Concert,null=true,on_delete=models.CASCADE)
	status=models.CharField(max_length=100,null=True,choices=STATUS)