# Whisp 📞

**Whisp** هي أداة تفاعلية تعمل في بيئة الطرفية (Terminal)، مصممة لمحاكاة واجهة رسومية بسيطة وجذابة، وتستخدم مكتبات مثل `colorama`، `pyfiglet`، و `simple-term-menu` لتوفير تجربة استخدام ممتعة، بالإضافة إلى `phonenumbers` و `twilio` لمعالجة واستعمال أرقام الهواتف.

---

## 📌 ميزات الأداة

- واجهة طرفية ملونة وسهلة الاستخدام
- تحليل أرقام الهواتف باستخدام مكتبة `phonenumbers`
- دعم خدمة الرسائل عبر Twilio
- قائمة تفاعلية بواسطة `simple-term-menu`
- متوافقة مع Termux (على أندرويد) وبيئات Linux الأخرى

---

## ⚙️ المتطلبات

لتشغيل الأداة بدون مشاكل، يجب توفر المتطلبات التالية:

### 🖥️ نظام التشغيل:
- Android (عبر Termux)
- Linux (أي توزيعة تدعم Python 3)

### 📦 مكتبات Python المطلوبة:

- colorama
- pyfiglet
- simple-term-menu
- phonenumbers
- twilio

---

## 🚀 خطوات التثبيت (على Termux)

افتح Termux ونفّذ الأوامر التالية بالترتيب:

```bash
# تحديث الحزم
pkg update -y && pkg upgrade -y

# تثبيت Python و pip
pkg install python -y

# تثبيت git
pkg install git -y

# نسخ مستودع Whisp من GitHub
git clone https://github.com/MOHAMED-MOKTAR-BAKAY/whisp_x

# الدخول إلى مجلد الأداة
cd whisp_x

# تثبيت جميع المكتبات المطلوبة دفعة واحدة
pip install colorama pyfiglet simple-term-menu phonenumbers twilio

▶️ طريقة التشغيل

بعد التثبيت، لتشغيل الأداة:

python backends.py

📌 ملاحظة: الملف التنفيذي الحالي هو backends.py، وليس whisp_x.py.


---

🔍 استكشاف الأخطاء

إذا ظهرت رسالة مثل:

ModuleNotFoundError: No module named 'xxxxx'

فالحل هو تثبيت المكتبة الناقصة يدويًا، مثل:

pip install xxxxx

مثال:

pip install pyfiglet

