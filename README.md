Whisp 📞

Whisp هي أداة تفاعلية تعمل في بيئة الطرفية (Terminal) مصممة لمحاكاة واجهة رسومية جميلة، وتستخدم واجهات مثل `colorama` و `pyfiglet` و `TerminalMenu` وغيرها، بهدف تنفيذ مهام تتعلق بأرقام الهواتف باستخدام مكتبة `phonenumbers` وخدمة `Twilio`.
📦 المتطلبات

لضمان تشغيل الأداة دون مشاكل، تأكد من تثبيت التالي:

✅ نظام التشغيل المدعوم:
- Android (عبر [Termux](https://f-droid.org/en/packages/com.termux/))
- Linux
✅ بايثون والمكتبات:
- Python 3.10 أو أحدث
- المكتبات التالية:

colorama
pyfiglet
simple-term-menu
phonenumbers
twilio

🛠️ التثبيت (خطوة بخطوة على Termux)

# تحديث النظام
pkg update -y && pkg upgrade -y

# تثبيت Python و pip
pkg install python -y

# تثبيت git
pkg install git -y

# نسخ المستودع
git clone https://github.com/MOHAMED-MOKTAR-BAKAY/whisp_x

# الدخول إلى مجلد الأداة
cd whisp_x

# تثبيت جميع المكتبات المطلوبة
pip install colorama pyfiglet simple-term-menu phonenumbers twilio 

▶️ طريقة التشغيل

python backends.py

💪ملاحظة: الملف التنفيذي الرئيسي حاليًا هو backends.py وليس whisp_x.py


❗ ملاحظات

تأكد من أنك تملك اتصال إنترنت لتثبيت الحزم بنجاح

خدمة Twilio تحتاج إلى حساب ومفاتيح API خاصة لتعمل بشكل صحيح

إذا ظهرت لك أي أخطاء أخرى تحقق من وجود الملف المطلوب عبر:


ls

وتأكد من كتابة الاسم الصحيح عند التنفيذ

📧 المطور

الاسم: محمد مختار بكاي

GitHub: @MOHAMED-MOKTAR-BAKAY
