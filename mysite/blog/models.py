from django.db import models
GENDER = (
('male', 'male'),
('female', 'female'),
)

ORGTYPE = (
    ('Правительственная', 'Правительственная'),
    ('Неправительственная', 'Неправительственная'),
    ('Коммерческая','Коммерческая'),
    ('Некоммерческая','некоммерческая'),
    ('Бюджетная','Бюджетная'),
    ('Внебюджетная', 'Внебюджетная'),
    ('Общественные', 'Общественные'),
    ('Хозяйственные', 'Хозяйственные'),
)


class Client(models.Model):
    name = models.CharField(max_length=10, null=True, verbose_name='Имя')
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата обновления")


class DataTable(models.Model):
    firstname = models.CharField(max_length=20, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=20, null=True, verbose_name='Фамилия')
    address = models.TextField(null=True, verbose_name='Адрес')
    phone = models.CharField(max_length=20, null=True, verbose_name='Телефон')
    birthday = models.DateField(null=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=1, null=True, verbose_name='Пол')
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Дата обновления")


class StudyDirection(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='Направление обучения')


class Profession(models.Model):
    name = models.CharField(max_length=30, null=True, verbose_name="Название профессии")
    direction = models.ForeignKey(StudyDirection, on_delete=models.CASCADE)


class Courses(models.Model):
    institution = models.CharField(max_length=40, null=True, verbose_name="Образовательное учреждение")
    address = models.CharField(max_length=60, null=True, verbose_name="Адрес")
    foundation_date = models.DateField()
    image = models.ImageField(upload_to='photos')
    professions = models.ForeignKey(Profession, on_delete=models.CASCADE)


class Student(models.Model):
    lastname = models.CharField(max_length=20, null=True, verbose_name="Фамилия")
    gender = models.CharField(max_length=50, choices=GENDER, verbose_name="Пол", blank=False)
    address = models.CharField(max_length=100, null=True, verbose_name="Адрес участка")
    organization_type = models.CharField(max_length=20, choices=ORGTYPE, verbose_name="Тип организации")
    organization_name = models.CharField(max_length=30, null=True, verbose_name="Имя организации")
    appointment = models.CharField(max_length=30, null=True, verbose_name="Должность")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)


