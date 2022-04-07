from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from phone_field import PhoneField



OperationType = ((1, "   يعمل"), (2, " لايعمل "), (3,"جار الاستيفاء"  ))

# Create your models here.
class Governerates(models.Model):
    '''
    قائمة بجميع محافظات مصر 
    '''
    
    GovernerateName=models.CharField("المحافظه",max_length=20,unique=True,null=False,blank=False,help_text="اسم المحافظة يجب ان يكون غير مدرج من قبل")
    def __str__(self):
        return self.GovernerateName
    class Meta(object):
        ordering = ['GovernerateName']
        verbose_name_plural="المحافظات"
        verbose_name="المحافظه"
        
        

class Compound(models.Model):
    '''
    قائمة بجميع المجمعات 
    '''
    GoverneratesId=models.ForeignKey(Governerates,verbose_name=("كود المحافظة"), on_delete=models.DO_NOTHING)
    CompoundName=models.CharField("المجمع",max_length=20,unique=True,null=False,blank=False,help_text="اسم المجمع يجب ان يكون غير مدرج من قبل")
    def __str__(self):
        return self.CompoundName
    class Meta(object):
        ordering = ['CompoundName']
        verbose_name_plural="المجمعات"
        verbose_name="المجمع"
        
class LegalEntity(models.Model):
    '''
    قائمة بجميع الكيانات القانونية 
    '''
    LegalEntityName=models.CharField("الكيان القانونى",max_length=70,unique=True,null=False,blank=False,help_text="الكيان القانونى")
    
    def __str__(self):
        return self.LegalEntityName
    class Meta(object):
        ordering = ['LegalEntityName']
        verbose_name_plural="الكيانات القانونية"
        verbose_name="الكيان القانونى"         
class Activities(models.Model):
    '''
    قائمة بجميع الانشطة الصناعية الرئيسيه 
    '''
    ActivityName=models.CharField("النشاط",max_length=40,unique=True,null=False,blank=False,help_text="نشاط صناعي رئيسي")
    
    def __str__(self):
        return self.ActivityName
    class Meta(object):
        ordering = ['ActivityName']
        verbose_name_plural="الانشطه"
        verbose_name="النشاط"       
   
   
        
        
class LandOperatingStatus(models.Model):
    '''
    حالةالوحدة التشغيلية مثل تحت التشغيل التجريبي
    '''

    LandOperatingStatusName=models.CharField(" حاله القطعه التشغيلية" ,max_length=40,unique=True,null=False,blank=False,help_text="حالة القطعه التشغيلية الحالية")
    def __str__(self):
        return self.LandOperatingStatusName
    class Meta(object):
        ordering = ['LandOperatingStatusName']
        verbose_name_plural="حالات القطعه التشغيلية"
        verbose_name="حالة القطعه التشغيلية "       
class SpecificationUnitsData(models.Model):
    #units dept
    GoverneratesId=models.ForeignKey(Governerates,verbose_name=("كود المحافظة"), on_delete=models.DO_NOTHING,null=True,blank=True)
    CompoundId=models.ForeignKey(Compound,verbose_name=("كود المجمع"), on_delete=models.DO_NOTHING,null=True,blank=True)
    UnitNumber=models.PositiveIntegerField(" رقم الوحدة ",default=0 ,blank=False, null=False)
    UnitsCount=models.PositiveIntegerField("عدد الوحدات ",default=0 ,blank=False, null=False)
    UnitArea=models.PositiveIntegerField(" مساحة الوحدة",default=0 ,blank=False, null=False,help_text=" مساحة الوحدة  ")
    TotalArea=models.PositiveIntegerField(" إجمالي المساحة المخصصة",default=0 ,blank=False, null=False,help_text=" إجمالي المساحة المخصصة") 
    Main_Activity=models.ForeignKey( Activities, verbose_name=("كود القطاع الصناعى"),on_delete=models.DO_NOTHING, null=True,blank=False)
    RequestNumber=models.PositiveIntegerField(" رقم الطلب ",default=0 ,blank=False, null=False)
    OwnerUnit=models.CharField("اسم المالك", max_length=300,null=True,blank=True)
    LegalEntity=models.ForeignKey(LegalEntity,verbose_name=("كود الكيان القانونى"), on_delete=models.DO_NOTHING,null=True,blank=True)
    CommitteeNumber=models.PositiveIntegerField(" رقم اللجنة ",default=0 ,blank=False, null=False)
    SpecificationDate=models.DateField("تاريخ تخصيص الوحدة",null=True,blank=True)
    HandedDate=models.DateField("تاريخ استلام الوحدة",null=True,blank=True)
    LandOperatingStatus= models.ForeignKey(LandOperatingStatus ,on_delete=models.DO_NOTHING, null=True, verbose_name="حالة الوحدة التشغيلية" )
    SubActivity=models.CharField(" النشاط على الواقع", max_length=250,null=True,blank=True)
    OperatingLicense=models.BooleanField("رخصة تشغيل",help_text="هل يوجد رخصة تشغيل  ",default=False,null=True,blank=True)
    industrialRegistry=models.BooleanField(" سجل صناعى",help_text="هل يوجد سجل صناعى  ",default=False,null=True,blank=True)
    DeclarationModification=models.BooleanField(" تصريح بالتعديل",help_text="هل يوجد تصريح بالتعديل  ",default=False)
    UnitModification=models.TextField("التعديلات على الوحدة", max_length=1000,blank=True, null=True)
    Has_Electric_Meter=models.BooleanField("هل يوجد عداد الكهرباء  ",help_text="هل يوجد عداد كهرباء",default=False)
    Has_Water_Meter=models.BooleanField("هل يوجد عداد المياه ",help_text="هل يوجد عداد مياه",default=False)
    Has_equipment=models.BooleanField(" هل يوجد معدات ",help_text="هل يوجد معدات",default=False)
    DueServices=models.FloatField("مستحقات الخدمات", null=True,blank=True)
    DuePriceOrrent=models.FloatField("مستحقات الوحدة", help_text='مستحقات الوحدة إيجار او ثمن ',null=True,blank=True)
    Has_Finance=models.BooleanField(" هل يوجد تمويل ",help_text="هل يوجد تمويل",default=False)
    UnitProblems=models.TextField(" المشاكل التى تواجهة المستثمر ", max_length=1500,blank=True, null=True)
    UnitProblemsSolutions=models.TextField("  الاجراءات بخصوص تلك المشكلات", max_length=1500,null=True,blank=True)
    ContactNumber=models.CharField("التليفون",max_length=150,blank=True, null=True,help_text="التليفون و الفاكسات")
    
    # ContactNumber=PhoneField("التليفون",blank=True, null=True,help_text="التليفون و الفاكسات")
    AttendMeeting=models.BooleanField(" هل حضر اجتماعات الهيئة ",help_text="هل حضر اجتماعات الهيئة  ",default=False)
    UnitNotWorkReasons=models.TextField("  اسباب عدم العمل حتى الان", max_length=1500,blank=True, null=True)
    UnitNotes=models.TextField("  ملاحظات", max_length=1500,blank=True, null=True)



    
    
    
    def __str__(self):
        return self.OwnerUnit or ''
    class Meta(object):
        ordering = ['UnitNumber']
        verbose_name_plural="بيانات الوحدة المخصصة"
        verbose_name="بيانات الوحدة المخصصة"
    