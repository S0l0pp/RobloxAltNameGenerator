يقوم بإنشاء 30 اسمًا بديلًا ويفحص ما إذا كانت مأخوذة أم لا (إذا كانت الأسماء محظورة مثل الشتائم، فإن النتيجة تكون مأخوذة) ويحفظ الأسماء المتاحة في ملف
تذكر أنه في قسم التصدير في الكود تحتاج إلى تغيير الدليل الذي يوجد فيه ملف available_usernames.exe (يجب عليك إنشاؤه)

if EXPORT:
if available:
with open("YOUR available_usernames.exe DIRECTORY", "w", encoding="utf-8") as f:
f.write("\n".join(available))
print("📁 تم الحفظ في available_usernames.txt")
else:
print("⚠️ لا توجد أسماء مستخدمين متاحة للحفظ.")
