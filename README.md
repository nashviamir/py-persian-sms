## py-persian-sms

<p dir="rtl">
پکیج پایتون برای کار با ای پی آی sms.ir .در این پکیج تنها قابلیت **ارسال پیامک** به وسیله ای پی آی فعال است.
</p>
<p dir="rtl">
توسعه توسط امیرحسین نشوی
</p>

## how to use
installation

    pip install py-persian-sms

usage

    from pars_sms import Sms
	
	api_key = "YOUR-API-KEY"
	secret_key = "YOUR-SECRET-KEY"
	line_number = "YOUR-LINE-NUMBER" #only required for bulk sms and sms without template
	
	manager = Sms(api_key, secret_key, line_number)
	manager.send("0912XXXXXXX",  text="سلام")
	