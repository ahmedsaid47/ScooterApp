# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arkafren(models.Model):
    arkafrenid = models.AutoField(db_column='ArkaFrenID', primary_key=True)  # Field name made lowercase.
    arkafren = models.CharField(db_column='ArkaFren', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArkaFren'

    def __str__(self):
        return self.arkafren


class Favoriler(models.Model):
    favorilerid = models.AutoField(db_column='FavorilerID', primary_key=True)  # Field name made lowercase.
    kullaniciid = models.ForeignKey('Kullanici', models.DO_NOTHING, db_column='KullaniciID', blank=True, null=True)  # Field name made lowercase.
    olusturmatarihi = models.DateTimeField(db_column='OlusturmaTarihi', blank=True, null=True)  # Field name made lowercase.
    sonduzenleme = models.DateTimeField(db_column='SonDuzenleme', blank=True, null=True)  # Field name made lowercase.
    urunsayisi = models.IntegerField(db_column='UrunSayisi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Favoriler'


class Favorilerdetay(models.Model):
    favorilerdetayid = models.AutoField(db_column='FavorilerDetayID', primary_key=True)  # Field name made lowercase.
    favorilerid = models.ForeignKey(Favoriler, models.DO_NOTHING, db_column='FavorilerID', blank=True, null=True)  # Field name made lowercase.
    urunid = models.ForeignKey('Urun', models.DO_NOTHING, db_column='UrunID', blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateTimeField(db_column='Tarih', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FavorilerDetay'


class Fiyat(models.Model):
    fiyatid = models.AutoField(db_column='FiyatID', primary_key=True)  # Field name made lowercase.
    fiyatlarid = models.ForeignKey('Fiyatlar', models.DO_NOTHING, db_column='FiyatlarID', blank=True, null=True)  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    saticiid = models.ForeignKey('Satici', models.DO_NOTHING, db_column='SaticiID', blank=True, null=True)  # Field name made lowercase.
    fiyatlink = models.CharField(db_column='FiyatLink', max_length=500, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='Fiyat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fiyat'
        
    def __str__(self):
        return self.fiyatid


class Fiyatlar(models.Model):
    fiyatlarid = models.AutoField(db_column='FiyatlarID', primary_key=True)  # Field name made lowercase.
    scooterid = models.ForeignKey('Scooter', models.DO_NOTHING, db_column='ScooterID', blank=True, null=True)  # Field name made lowercase.
    fiyatsayisi = models.IntegerField(db_column='FiyatSayisi', blank=True, null=True)  # Field name made lowercase.
    sitesayisi = models.IntegerField(db_column='SiteSayisi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fiyatlar'
    


class Frenteknolojisi(models.Model):
    frenteknolojisiid = models.AutoField(db_column='FrenTeknolojisiID', primary_key=True)  # Field name made lowercase.
    frenteknolojisi = models.CharField(db_column='FrenTeknolojisi', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrenTeknolojisi'
    
    def __str__(self):
        return self.Frenteknolojisi
    
    


class Genelozellik(models.Model):
    genelozellikid = models.AutoField(db_column='GenelOzellikID', primary_key=True)  # Field name made lowercase.
    scooterid = models.ForeignKey('Scooter', models.DO_NOTHING, db_column='ScooterID', blank=True, null=True)  # Field name made lowercase.
    motorgucumax = models.IntegerField(db_column='MotorGucumax', blank=True, null=True)  # Field name made lowercase.
    menzilmax = models.IntegerField(db_column='Menzilmax', blank=True, null=True)  # Field name made lowercase.
    hizmax = models.IntegerField(db_column='Hizmax', blank=True, null=True)  # Field name made lowercase.
    tasimakapasitesi = models.IntegerField(db_column='TasimaKapasitesi', blank=True, null=True)  # Field name made lowercase.
    tekerlektipiid = models.ForeignKey('Tekerlektipi', models.DO_NOTHING, db_column='TekerlekTipiID', blank=True, null=True)  # Field name made lowercase.
    tekerleksayisi = models.IntegerField(db_column='TekerlekSayisi', blank=True, null=True)  # Field name made lowercase.
    lastikebati = models.IntegerField(db_column='LastikEbati', blank=True, null=True)  # Field name made lowercase.
    katlanabilme = models.CharField(db_column='Katlanabilme', max_length=5, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GenelOzellik'


class Korumasertifikasyonu(models.Model):
    korumasertifikasyonuid = models.AutoField(db_column='KorumaSertifikasyonuID', primary_key=True)  # Field name made lowercase.
    korumasertifikasyonu = models.CharField(db_column='KorumaSertifikasyonu', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KorumaSertifikasyonu'

    def __str__(self):
        return self.korumasertifikasyonu


class Kullanici(models.Model):
    kullaniciid = models.AutoField(db_column='KullaniciID', primary_key=True)  # Field name made lowercase.
    kullaniciadi = models.CharField(db_column='KullaniciAdi', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sifre = models.CharField(db_column='Sifre', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isimsoyisim = models.CharField(db_column='IsimSoyisim', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cinsiyet = models.CharField(db_column='Cinsiyet', max_length=1, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    olusturmatarihi = models.DateTimeField(db_column='OlusturmaTarihi', blank=True, null=True)  # Field name made lowercase.
    dogumgunu = models.DateField(db_column='Dogumgunu', blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=15, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kullanici'
    


class Marka(models.Model):
    markaid = models.AutoField(db_column='MarkaID', primary_key=True)  # Field name made lowercase.
    marka = models.CharField(db_column='Marka', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    markalink = models.CharField(db_column='MarkaLink', max_length=500, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marka'

    def __str__(self):
        return self.marka


class Model(models.Model):
    modelid = models.AutoField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    markaid = models.ForeignKey(Marka, models.DO_NOTHING, db_column='MarkaID', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Model'

    def __str__(self):
        return self.model


class Onfren(models.Model):
    onfrenid = models.AutoField(db_column='OnFrenID', primary_key=True)  # Field name made lowercase.
    onfren = models.CharField(db_column='Onfren', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnFren'


class Renk(models.Model):
    renkid = models.AutoField(db_column='RenkID', primary_key=True)  # Field name made lowercase.
    renk = models.CharField(db_column='Renk', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Renk'


class Satici(models.Model):
    saticiid = models.AutoField(db_column='SaticiID', primary_key=True)  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    satici = models.CharField(db_column='Satici', max_length=100, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Satici'

    def __str__(self):
        return self.satici


class Scooter(models.Model):
    scooterid = models.AutoField(db_column='ScooterID', primary_key=True)  # Field name made lowercase.
    markaid = models.ForeignKey(Marka, models.DO_NOTHING, db_column='MarkaID', blank=True, null=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Model, models.DO_NOTHING, db_column='ModelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scooter'


class Site(models.Model):
    siteid = models.AutoField(db_column='SiteID', primary_key=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sitelink = models.CharField(db_column='SiteLink', max_length=500, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'


class Tekerlektipi(models.Model):
    tekerlektipiid = models.AutoField(db_column='TekerlekTipiID', primary_key=True)  # Field name made lowercase.
    tekerlektipi = models.CharField(db_column='TekerlekTipi', max_length=50, db_collation='Turkish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TekerlekTipi'


class Teknikozellik(models.Model):
    teknikozellikid = models.AutoField(db_column='TeknikOzellikID', primary_key=True)  # Field name made lowercase.
    scooterid = models.ForeignKey(Scooter, models.DO_NOTHING, db_column='ScooterID', blank=True, null=True)  # Field name made lowercase.
    frenteknolojisiid = models.ForeignKey(Frenteknolojisi, models.DO_NOTHING, db_column='FrenTeknolojisiID', blank=True, null=True)  # Field name made lowercase.
    onfrenid = models.ForeignKey(Onfren, models.DO_NOTHING, db_column='ÍnFrenID', blank=True, null=True)  # Field name made lowercase.
    arkafrenid = models.ForeignKey(Arkafren, models.DO_NOTHING, db_column='ArkaFrenID', blank=True, null=True)  # Field name made lowercase.
    bataryavoltaji = models.IntegerField(db_column='BataryaVoltaji', blank=True, null=True)  # Field name made lowercase.
    bataryaakimi = models.IntegerField(db_column='BataryaAkimi', blank=True, null=True)  # Field name made lowercase.
    tirmanmaacisi = models.IntegerField(db_column='TirmanmaAcisi', blank=True, null=True)  # Field name made lowercase.
    korumasertifikasyonuid = models.ForeignKey(Korumasertifikasyonu, models.DO_NOTHING, db_column='KorumaSertifikasyonuID', blank=True, null=True)  # Field name made lowercase.
    renkid = models.ForeignKey(Renk, models.DO_NOTHING, db_column='RenkID', blank=True, null=True)  # Field name made lowercase.
    agirlik = models.FloatField(db_column='Agirlik', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeknikOzellik'


class Urun(models.Model):
    urunid = models.AutoField(db_column='UrunID', primary_key=True)  # Field name made lowercase.
    scooterid = models.ForeignKey(Scooter, models.DO_NOTHING, db_column='ScooterID', blank=True, null=True)  # Field name made lowercase.
    genelozellikid = models.ForeignKey(Genelozellik, models.DO_NOTHING, db_column='GenelOzellikID', blank=True, null=True)  # Field name made lowercase.
    teknikozellikid = models.ForeignKey(Teknikozellik, models.DO_NOTHING, db_column='TeknikOzellikID', blank=True, null=True)  # Field name made lowercase.
    fiyatlarid = models.ForeignKey(Fiyatlar, models.DO_NOTHING, db_column='FiyatlarID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Urun'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Turkish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Turkish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Turkish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Turkish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Turkish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Turkish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Turkish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Turkish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Turkish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Turkish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Turkish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Turkish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Turkish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Turkish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Turkish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Turkish_CI_AS')
    session_data = models.TextField(db_collation='Turkish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Turkish_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
