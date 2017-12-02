#coding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username



class SSD(models.Model):

     name = models.CharField(max_length=128,null=True,blank=True) #姓名
     numble = models.IntegerField(null=True, blank=True)#住院号
     idnumble = models.CharField(max_length=255, null=True, blank=True) #身份证号
     book = models.OneToOneField('Book')
     bookcure = models.OneToOneField('Bookcure')
     bookcheck = models.OneToOneField('Bookcheck')
     bookhealth = models.OneToOneField('Bookhealth')
     bookdange = models.OneToOneField('Bookdange')
     bookchange = models.OneToOneField('Bookchange')
     booksituation = models.OneToOneField('Booksituation')
     bookdiagnose = models.OneToOneField('Bookdiagnose')
     booktime = models.OneToOneField('Booktime')






class Book(models.Model):

    conname =models.CharField(max_length=50,null=True,blank=True) #联系人姓名
    conrelation = models.CharField(max_length=255,null=True,blank=True) #联系人关系
    conphone = models.IntegerField(null=True,blank=True) #联系人电话
    nowprovince =models.CharField(max_length=20,null=True,blank=True) #现地址省
    nowcity = models.CharField(max_length=20,null=True,blank=True) #现地址县/区
    nowcounty =models.CharField(max_length=20,null=True,blank=True) #现地址国家
    nowstreet = models.CharField(max_length=50,null=True,blank=True) #现住址乡/镇/街道
    birthprovince = models.CharField(max_length=20,null=True,blank=True) #出生地省
    birthcity = models.CharField(max_length=20, null=True, blank=True) #出生地县/区
    birtharea = models.CharField(max_length=20, null=True, blank=True) #出生地地区
    birthstreet = models.CharField(max_length=50, null=True, blank=True) #出生地乡/镇/街道
    healthtype = models.CharField(max_length=255,null=True,blank=True) #医保类型
    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Bookcure(models.Model):
    b1 = models.IntegerField(null=True,blank=True) #血管再开通治疗：是否为醒后卒中
    b2 = models.DateTimeField(null=True,blank=True) #血管再开通治疗：发病时间
    b3 = models.CharField(max_length=50,null=True,blank=True) #血管再开通治疗：由何种途径转运至医院
    b4 = models.DateTimeField(null=True,blank=True) #血管再开通治疗：到院时间
    b5 = models.CharField(max_length=50,null=True,blank=True) #血管再开通治疗：入院诊断
    b51 = models.CharField(max_length=50,null=True,blank=True) #确诊依据
    b5a11 = models.IntegerField(null=True, blank=True) #如果是脑梗死，是否行静脉溶栓治疗
    b5a12 = models.DateTimeField(null=True, blank=True, auto_now_add=True) #如果是脑梗死，是否行静脉溶栓治疗:如果“是”，则溶栓开始时间为
    b5a13 = models.IntegerField(null=True, blank=True) #如果是脑梗死:溶栓地点
    b5a14 = models.CharField(max_length=50, null=True, blank=True) #如果是脑梗死:溶栓地点 其他
    b5a15 = models.IntegerField(null=True, blank=True) #如果是脑梗死:所用药物为
    b5a16 = models.FloatField(null=True, blank=True) #如果是脑梗死:rt-PA用量(mg)
    b5a17 = models.FloatField(null=True, blank=True) #如果是脑梗死:尿激酶用量(mg)
    b5a18 = models.IntegerField(null=True, blank=True) #如果是脑梗死:溶栓前NHISS评分
    b5a19 = models.IntegerField(null=True, blank=True) #如果是脑梗死:溶栓后NHISS评分
    b5a110 = models.IntegerField(null=True, blank=True) #是否有并发症
    b5a111 = models.CharField(max_length=50, null=True, blank=True) #是否有并发症：是/否
    b5a112 = models.CharField(max_length=50, null=True, blank=True) #是否有并发症：如果选择"否",则原因为 超过溶栓时间窗/存在禁忌症
    b5a113 = models.CharField(max_length=50, null=True, blank=True) #医生未告知/患者及家属不同意/已在外院行静脉溶栓治疗/不详
    b5a21 = models.IntegerField(null=True,blank=True) #患者是否行动脉溶栓治疗
    b5a22 =models.TimeField(null=True,blank=True,auto_now_add=True) #患者是否行动脉溶栓治疗:如果“是”，则溶栓开始时间为
    b5a23 = models.IntegerField(null=True, blank=True) #患者是否行动脉溶栓治疗:所用药物为
    b5a24 = models.FloatField(null=True, blank=True) #患者是否行动脉溶栓治疗:rt-PA用量(mg)
    b5a25 = models.FloatField(null=True, blank=True) #患者是否行动脉溶栓治疗:尿激酶用量(mg)
    b5a26 = models.IntegerField(null=True, blank=True) #患者是否行动脉溶栓治疗:溶栓前NHISS评分
    b5a27 = models.IntegerField(null=True, blank=True) #患者是否行动脉溶栓治疗:如果“是”，则动脉是否再通？
    b5a28 = models.TimeField(null=True, blank=True,auto_now_add=True) #患者是否行动脉溶栓治疗:若选择“是”，则动脉再通时间为
    b5a31 = models.IntegerField(null=True, blank=True) #患者是否行机械取栓治疗
    b5a32 = models.TimeField(null=True, blank=True,auto_now_add=True) #患者是否行机械取栓治疗:如果“是”，则机械取栓开始时间为
    b5a33 = models.IntegerField(null=True, blank=True) #患者是否行机械取栓治疗:取栓后NHISS评分
    b5a34 = models.IntegerField(null=True, blank=True) #患者是否行机械取栓治疗:如果“是”，则动脉是否再通
    b5a35 = models.TimeField(null=True, blank=True,auto_now_add=True) #患者是否行机械取栓治疗:若选择“是”，则动脉再通时间为
    b5a41 = models.IntegerField(null=True, blank=True) #患者是否行急诊支架治疗
    b5a42 = models.TimeField(null=True, blank=True,auto_now_add=True) #患者是否行急诊支架治疗:如果“是”，则支架开始时间为
    b5a43 = models.IntegerField(null=True, blank=True) #患者是否行急诊支架治疗:急诊支架后NHISS评分




class Bookcheck(models.Model):
    c1 = models.IntegerField(null=True, blank=True)#意识 选择
    c1a1 = models.IntegerField(null=True, blank=True)#意识Glasgow评分
    c2 = models.CharField(max_length=225, null=True, blank=True)#体征 多选
    c2a1 = models.CharField(max_length=50, null=True, blank=True)#体征 失语 单选
    c2a2 = models.IntegerField(null=True, blank=True)#体征nihss评分
    c3 = models.FloatField(null=True, blank=True)#血糖
    c4a1 = models.IntegerField(null=True, blank=True)#入院后首次血压高压
    c4a2 = models.IntegerField(null=True, blank=True)#入院后首次血压低压
    c5a1 = models.FloatField(null=True, blank=True)#血小板
    c5a2 = models.FloatField(null=True, blank=True)#白细胞
    c5a3 = models.FloatField(null=True, blank=True)#红细胞
    c5a4 = models.FloatField(null=True, blank=True)#血红蛋白
    c6a1 = models.FloatField(null=True, blank=True)#血脂TG
    c6a2 = models.FloatField(null=True, blank=True)  # TC
    c6a3 = models.FloatField(null=True, blank=True)  # LDL-C
    c6a4 = models.FloatField(null=True, blank=True)	#  HDL-C
    c7a1 = models.FloatField(null=True, blank=True)#谷丙转氨酶
    c7a2 = models.FloatField(null=True, blank=True)#谷草转氨酶
    c7a3 = models.FloatField(null=True, blank=True)#尿素氮
    c7a4 = models.FloatField(null=True, blank=True)#血肌酐
    c8 = models.FloatField(null=True, blank=True)#同型半胱氨酸
    c9 = models.FloatField(null=True, blank=True)#超敏-c反应蛋白
    c10 = models.FloatField(null=True, blank=True)#CK
    c11 = models.CharField(max_length=225, null=True, blank=True)#CT多选
    c12a1 = models.IntegerField(null=True, blank=True)#MRI急性期改变 单选有无
    c12a2 = models.CharField(max_length=225, null=True, blank=True)#MRI急性期改变 部位多选
    c12a3 = models.CharField(max_length=50, null=True, blank=True)#MRI急性期改变 范围单选
    # c13a1 = models.CharField(max_length=50, null=True, blank=True)
    # c13a2 = models.CharField(max_length=225, null=True, blank=True)
    # c13a3 = models.CharField(max_length=225, null=True, blank=True)
    c14a1 = models.IntegerField(null=True, blank=True)#心电监护 有无单选
    c14a2 = models.CharField(max_length=50, null=True, blank=True)#心电监护 有则为单选
    c15 = models.FloatField(null=True, blank=True)#Lp-PLA





class Bookhealth(models.Model):
    d1a10 = models.IntegerField(null=True, blank=True) #抗血小板聚集药物
    d1a11 = models.IntegerField(null=True, blank=True) #抗血小板聚集药物:如果“是”，则为
    d1a12 = models.FloatField(null=True, blank=True) #抗血小板聚集药物:单抗  阿司匹林剂量(mg/天)
    d1a13 = models.FloatField(null=True, blank=True) #抗血小板聚集药物:单抗  氯吡格雷剂量(mg/天)
    d1a14 = models.FloatField(null=True, blank=True) #抗血小板聚集药物:双抗  阿司匹林剂量(mg/天)
    d1a15 = models.FloatField(null=True, blank=True) #抗血小板聚集药物:双抗  氯吡格雷剂量(mg/天)
    d1a20 = models.IntegerField(null=True, blank=True) #1.2.抗凝药物
    d1a21 = models.IntegerField(null=True, blank=True) #1.2.抗凝药物：如果“是”，则为：药物
    d1a22 = models.FloatField(null=True, blank=True) #1.2.抗凝药物：剂量(mg/天或iu)
    d1a23 = models.CharField(max_length=128, null=True, blank=True) #1.2.抗凝药物：如果“是”，则为：其他
    d1a30 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物
    d1a31 = models.CharField(max_length=225, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物
    d1a32 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物 他汀类
    d1a33 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：他汀类 其他
    d1a34 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：他汀类 剂量(mg/天)
    d1a35 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物 贝特类
    d1a36 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：贝特类 其他
    d1a37 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：贝特类 剂量(mg/天)
    d1a38 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物 脂质抗氧化剂
    d1a39 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：脂质抗氧化剂 其他
    d1a310 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：脂质抗氧化剂 剂量(mg/天)
    d1a311 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物 烟酸类
    d1a312 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：烟酸类 其他
    d1a313 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：烟酸类 剂量(mg/天)
    d1a314 = models.IntegerField(null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：药物 胆酸螯合剂
    d1a315 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：如果“是”，则为：胆酸螯合剂 其他
    d1a316 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：胆酸螯合剂 剂量(mg/天)
    d1a317 = models.CharField(max_length=128, null=True, blank=True) #1.3.调节血脂药物：其他
    d1a318 = models.FloatField(null=True, blank=True) #1.3.调节血脂药物：其他 剂量(mg/天)
    d1a40 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物
    d1a41 = models.CharField(max_length=225, null=True, blank=True) #1.4.控制血压药物：如果“是”，则为：药物
    d1a42 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：钙离子拮抗剂CCB 剂量(mg/天)
    d1a43 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：血管紧张素转换酶抑制剂ACEI 剂量(mg/天)
    d1a44 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：血管紧张素Ⅱ受体拮抗剂ARB 剂量(mg/天)
    d1a45 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：利尿剂 剂量(mg/天)
    d1a46 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：β受体阻滞剂 剂量(mg/天)
    d1a47 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：α受体阻滞剂 剂量(mg/天)
    d1a48 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：其他
    d1a49 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：其他 剂量(mg/天)
    d1a51 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：中药 药物1
    d1a52 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：中药 药物2
    d1a53 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：中药 药物3
    d1a54 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：中药 药物4
    d1a55 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：中药 药物5
    d1a56 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：中药 药物1 剂量(mg/天)
    d1a57 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：中药 药物2 剂量(mg/天)
    d1a58 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：中药 药物3 剂量(mg/天)
    d1a59 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：中药 药物4 剂量(mg/天)
    d1a510 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：中药 药物5 剂量(mg/天)
    d1a511 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脑保护：药物1
    d1a512 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脑保护：药物2
    d1a570 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脑保护：药物3
    d1a571 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脑保护：药物4
    d1a572 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脑保护：药物5
    d1a513 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脑保护：药物1 剂量(mg/天)
    d1a514 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脑保护：药物2 剂量(mg/天)
    d1a573 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脑保护：药物3 剂量(mg/天)
    d1a574 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脑保护：药物4 剂量(mg/天)
    d1a575 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脑保护：药物5 剂量(mg/天)
    d1a515 = models.CharField(max_length=225, null=True, blank=True) #1.4.控制血压药物：脱水：药物
    d1a516 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脱水：药物1 甘露醇 剂量(mg/天)
    d1a517 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脱水：药物2 甘油果糖 剂量(mg/天)
    d1a518 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脱水：药物3 白蛋白 剂量(mg/天)
    d1a519 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脱水：药物4 七叶皂苷钠 剂量(mg/天)
    d1a520 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：脱水：药物 其他
    d1a521 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：脱水：药物 其他 剂量(g或mg或u/天)
    d1a522 = models.CharField(max_length=225, null=True, blank=True) #1.4.控制血压药物：扩容：药物
    d1a523 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 羟乙基淀粉注射液 剂量(u/天)
    d1a524 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 低分子右旋糖苷 剂量(u/天)
    d1a525 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 白蛋白 剂量(u/天)
    d1a526 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 血浆 剂量(u/天)
    d1a527 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 多种氨基酸 剂量(u/天)
    d1a528 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物1 琥珀酸凝胶 剂量(u/天)
    d1a529 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：扩容：药物 其他
    d1a530 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：扩容：药物 其他 剂量(g或mg或u/天)
    d1a531 = models.CharField(max_length=225, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物
    d1a532 = models.CharField(max_length=225, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素
    d1a533 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 超长效：甘精 剂量(u/天)
    d1a534 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 超长效：地特 剂量(u/天)
    d1a535 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 长效：精蛋白 剂量(u/天)
    d1a536 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 中效：低精蛋白锌胰岛素 剂量(u/天)
    d1a537 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 短效：普通胰岛素 剂量(u/天)
    d1a538 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 短效：正规胰岛素 剂量(u/天)
    d1a539 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 超短效：门冬胰岛素 剂量(u/天)
    d1a540 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 超短效：赖脯胰岛素 剂量(u/天)
    d1a541 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 预混：30R 剂量(u/天)
    d1a542 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 预混：50R 剂量(u/天)
    d1a543 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 其他
    d1a544 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰岛素 其他 剂量(u/天)
    d1a545 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 双胍类 二甲双胍/其他
    d1a546 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 双胍类 其他
    d1a547 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 双胍类 剂量(mg/天)
    d1a548 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 磺酰脲类 格列本脲/格列吡嗪/格列喹酮/格列齐特/格列美脲/其他
    d1a549 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 磺酰脲类 其他
    d1a550 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 磺酰脲类 剂量(mg/天)
    d1a551 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 α葡萄糖苷酶抑制剂 阿卡波糖/伏格列波糖/其他
    d1a552 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 α葡萄糖苷酶抑制剂 其他
    d1a553 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 α葡萄糖苷酶抑制剂 剂量(mg/天)
    d1a554 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 噻唑烷二酮类 罗格列酮/吡格列酮/其他
    d1a555 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 噻唑烷二酮类 其他
    d1a556 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 噻唑烷二酮类 剂量(mg/天)
    d1a557 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 格列奈类 瑞格列奈/那格列奈/其他
    d1a558 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 格列奈类 其他
    d1a559 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 格列奈类 剂量(mg/天)
    d1a560 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰高糖素样多肽-1受体激动剂 艾塞那肽/利拉鲁肽/其他
    d1a561 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰高糖素样多肽-1受体激动剂 其他
    d1a562 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 胰高糖素样多肽-1受体激动剂 剂量(mg/天)
    d1a563 = models.IntegerField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 二肽基肽酶-4抑制剂 西格列汀/维格列汀/沙格列汀/其他
    d1a564 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 二肽基肽酶-4抑制剂 其他
    d1a565 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 二肽基肽酶-4抑制剂 剂量(mg/天)
    d1a566 = models.CharField(max_length=128, null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 其他
    d1a567 = models.FloatField(null=True, blank=True) #1.4.控制血压药物：控制血糖：药物 其他 剂量(mg/天)
    d1a6 = models.CharField(max_length=225, null=True, blank=True) #1.6外科治疗
    d1a7 = models.CharField(max_length=225, null=True, blank=True) #1.7介入治疗
    d2a10 = models.IntegerField(null=True, blank=True) #2.1脱水药物
    d2a11 = models.CharField(max_length=225, null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物
    d2a12 = models.FloatField(null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 甘露醇 剂量(g或mg/天)
    d2a13 = models.FloatField(null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 甘油果糖 剂量(g或mg/天)
    d2a14 = models.FloatField(null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 白蛋白 剂量(g或mg/天)
    d2a15 = models.FloatField(null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 七叶皂苷钠 剂量(g或mg/天)
    d2a16 = models.CharField(max_length=128, null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 其他
    d2a17 = models.FloatField(null=True, blank=True) #2.1脱水药物 如果“是”，则为：药物 其他 剂量(g或mg或u/天)
    d2a20 = models.IntegerField(null=True, blank=True) #2.2控制血压药物
    d2a21 = models.CharField(max_length=225, null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物
    d2a22 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 钙离子拮抗剂CCB 剂量(mg/天)
    d2a23 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 血管紧张素转换酶抑制剂ACEI 剂量(mg/天)
    d2a24 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 血管紧张素Ⅱ受体拮抗剂ARB 剂量(mg/天)
    d2a25 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 利尿剂 剂量(mg/天)
    d2a26 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 β受体阻滞剂 剂量(mg/天)
    d2a27 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 α受体阻滞剂 剂量(mg/天)
    d2a28 = models.CharField(max_length=128, null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 其他
    d2a29 = models.FloatField(null=True, blank=True) #2.2控制血压药物 如果“是”，则为：药物 其他 剂量(g或mg或u/天)
    d2a31 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 中药：药物1
    d2a32 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 中药：药物2
    d2a33 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 中药：药物3
    d2a34 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 中药：药物4
    d2a35 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 中药：药物5
    d2a36 = models.FloatField(null=True, blank=True) #2.3其他 中药：药物1 剂量(g或mg/天)
    d2a37 = models.FloatField(null=True, blank=True) #2.3其他 中药：药物2 剂量(g或mg/天)
    d2a38 = models.FloatField(null=True, blank=True) #2.3其他 中药：药物3 剂量(g或mg/天)
    d2a39 = models.FloatField(null=True, blank=True) #2.3其他 中药：药物4 剂量(g或mg/天)
    d2a310 = models.FloatField(null=True, blank=True) #2.3其他 中药：药物5 剂量(g或mg/天)
    d2a311 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 脑保护：药物1
    d2a312 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 脑保护：药物2
    d2a315 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 脑保护：药物3
    d2a316 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 脑保护：药物4
    d2a317 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 脑保护：药物5

    d2a313 = models.FloatField(null=True, blank=True) #2.3其他 脑保护：药物1 剂量(mg/天)
    d2a314 = models.FloatField(null=True, blank=True) #2.3其他 脑保护：药物2 剂量(mg/天)
    d2a318 = models.FloatField(null=True, blank=True) #2.3其他 脑保护：药物3 剂量(mg/天)
    d2a319 = models.FloatField(null=True, blank=True) #2.3其他 脑保护：药物4 剂量(mg/天)
    d2a3110 = models.FloatField(null=True, blank=True) #2.3其他 脑保护：药物5 剂量(mg/天)

    d2a331 = models.CharField(max_length=225, null=True, blank=True) #2.3其他 控制血糖：药物
    d2a332 = models.CharField(max_length=225, null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素
    d2a333 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 超长效：甘精 剂量(u/天)
    d2a334 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 超长效：地特 剂量(u/天)
    d2a335 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 长效：精蛋白 剂量(u/天)
    d2a336 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 中效：低精蛋白锌胰岛素 剂量(u/天)
    d2a337 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 短效：普通胰岛素 剂量(u/天)
    d2a338 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 短效：正规胰岛素 剂量(u/天)
    d2a339 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 超短效：门冬胰岛素 剂量(u/天)
    d2a340 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 超短效：赖脯胰岛素 剂量(u/天)
    d2a341 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 预混：30R 剂量(u/天)
    d2a342 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 预混：50R 剂量(u/天)
    d2a343 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 其他
    d2a344 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰岛素 其他 剂量(u/天)
    d2a345 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 双胍类 二甲双胍/其他
    d2a346 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 双胍类 其他
    d2a347 = models.FloatField(null=True, blank=True) #2.3其他 双胍类 剂量(mg/天)
    d2a348 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 磺酰脲类 格列本脲/格列吡嗪/格列喹酮/格列齐特/格列美脲/其他
    d2a349 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 磺酰脲类 其他
    d2a350 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 磺酰脲类 剂量(mg/天)
    d2a351 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 α葡萄糖苷酶抑制剂 阿卡波糖/伏格列波糖/其他
    d2a352 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 α葡萄糖苷酶抑制剂 其他
    d2a353 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 α葡萄糖苷酶抑制剂 剂量(mg/天)
    d2a354 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 噻唑烷二酮类 罗格列酮/吡格列酮/其他
    d2a355 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 噻唑烷二酮类 其他
    d2a356 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 噻唑烷二酮类 剂量(mg/天)
    d2a357 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 格列奈类 瑞格列奈/那格列奈/其他
    d2a358 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 格列奈类 其他
    d2a359 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 格列奈类 剂量(mg/天)
    d2a360 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 胰高糖素样多肽-1受体激动剂 艾塞那肽/利拉鲁肽/其他
    d2a361 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 胰高糖素样多肽-1受体激动剂 其他
    d2a362 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 胰高糖素样多肽-1受体激动剂 剂量(mg/天)
    d2a363 = models.IntegerField(null=True, blank=True) #2.3其他 控制血糖：药物 二肽基肽酶-4抑制剂 西格列汀/维格列汀/沙格列汀/其他
    d2a364 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 二肽基肽酶-4抑制剂 其他
    d2a365 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 二肽基肽酶-4抑制剂 剂量(mg/天)
    d2a366 = models.CharField(max_length=128, null=True, blank=True) #2.3其他 控制血糖：药物 其他
    d2a367 = models.FloatField(null=True, blank=True) #2.3其他 控制血糖：药物 其他 剂量(u/天)
    d2a4 = models.CharField(max_length=225, null=True, blank=True) #2.4外科治疗
    d2a5 = models.CharField(max_length=225, null=True, blank=True) #2.5介入治疗

class Bookdange(models.Model):
    e1 = models.CharField(max_length=225, null=True, blank=True)#危险因素 多选


class Bookchange(models.Model):
    f1 = models.CharField(max_length=225, null=True, blank=True)#住院一周内病情变化 单选

class  Booksituation(models.Model):
    g1 = models.CharField(max_length=225, null=True, blank=True)#出院情况 单选
    g2 = models.IntegerField(null=True, blank=True)#出院情况 nhiss评分


class Bookdiagnose(models.Model):
    h1 = models.CharField(max_length=225, null=True, blank=True)#出院诊断 多选
    h2 = models.CharField(max_length=225, null=True, blank=True)#出院诊断 脑梗死 多选
    h3 = models.CharField(max_length=225, null=True, blank=True)#出院诊断 脑梗死 部位
    h4 = models.CharField(max_length=225, null=True, blank=True)#出院诊断 脑出血 部位

class Booktime(models.Model):
    i1 = models.IntegerField(null=True, blank=True)#住院时间
    i2 = models.IntegerField(null=True, blank=True)#住院期间总费用
    i3 = models.IntegerField(null=True, blank=True)#其中药物花费
    i4 = models.IntegerField(null=True, blank=True)#辅助检查花费


















class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name
